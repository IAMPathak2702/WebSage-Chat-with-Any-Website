# main.py
import os 
from fastapi import FastAPI, Form , WebSocket, Request
from typing import Annotated , List
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from openai import OpenAI
from components.data_retrival import retrieve_content
import uvicorn
from components.chatlog import chat_bot , document_loader
from dotenv import load_dotenv
import asyncio
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()
# Retrieve sensitive information from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # OpenAI API Key
USERNAME = os.getenv("WORDPRESS_USERNAME")  # WordPress Username
PASSWORD = os.getenv("WORDPRESS_PASSWORD")  # WordPress Password
APIURL ="https://iampathak2702.github.io/Resume/"  # API URL for WordPress


# Initialize FastAPI application
app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Specify directory for Jinja2 templates
templates = Jinja2Templates(directory="src/templates")

@app.get("/", response_class=HTMLResponse)
def homepage_url(request: Request):
    """
    Renders the URL input page.

    Parameters:
    - request (Request): The incoming request object.

    Returns:
    - HTMLResponse: The rendered HTML template response.
    """
    return templates.TemplateResponse("url.html", {'request': request})

@app.post("/", response_class=RedirectResponse)
async def receive_url(request: Request, url: Annotated[str, Form()]):
    """
    Handles the URL submission and redirects to the chat page.

    Parameters:
    - request (Request): The incoming request object.
    - url (str): The URL submitted by the user.

    Returns:
    - RedirectResponse: A redirect response to the chat page.
    """
    global APIURL  # Reference the global variable
    url_received = url

    # Check if the URL starts with http:// or https://
    if url_received.startswith("http://") or url_received.startswith("https://"):
        APIURL = url_received  # Assign the received URL to the global variable
        print(APIURL)
        response = RedirectResponse(url="/index", status_code=302)
        return response
    else:
        error_message = f"Invalid URL format. Please provide a URL starting with 'http://' or 'https://' you got, {url}"
        return templates.TemplateResponse('url.html', {"request": request, "api_url": error_message})
      

          
            
# Route to render the chat page using an HTML template
@app.get('/index', response_class=HTMLResponse)
async def chat_page(request: Request):
    """
    Renders the chat page using an HTML template.

    Parameters:
    - request: The incoming request object.

    Returns:
    - HTMLResponse: The rendered HTML template response.
    """
    return templates.TemplateResponse("index.html", {'request': request, 'api_url': APIURL})


 # Stores the history of chat messages
chat_responses: List[str] = []  # Stores user input messages only

# Define a WebSocket route for handling chat
@app.websocket('/ws')
async def chat(websocket: WebSocket):
    """
    WebSocket route for handling chat communication between the client and the server.

    Parameters:
    - websocket (WebSocket): WebSocket connection object for bidirectional communication.

    Returns:
    - None

    Side Effects:
    - Sends and receives messages over the WebSocket connection.
    - Updates `chat_log` and `chat_responses` lists with user input and bot responses.
    """
    # Accept the WebSocket connection
    await websocket.accept()

    # Continuously listen for user input
    while True:
        global APIURL
        # Receive user input from the WebSocket connection
        user_input = await websocket.receive_text()
        retriever = document_loader(url=APIURL) #retrives the vectordatabase
       
        try:
            # Generate a response from the chat model using the chat bot
            response = chat_bot(api_key=OPENAI_API_KEY, retriever=retriever, user_input=user_input)
            # Split the response into words
            words = response.split()
            # Send each word with a delay to create a typing effect
            for word in words:
                await websocket.send_text(word)
                await asyncio.sleep(0.1)
            
            chat_responses.append(response)
              # Send the current state of the response

        except Exception as e:
            # Handle any exceptions that occur during response generation
            await websocket.send_text(f"Error: {str(e)}")
            break  # Exit the loop in case of an error  

@app.post("/index", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):
    """
    Handles chat interactions.

    Parameters:
    - request: The incoming request object.
    - user_input: The user's input obtained from the HTML form.

    Returns:
    - HTMLResponse: The rendered HTML template response.
    """
    # Append user's input to the chat log
    global APIURL
    user_query = user_input
    response = chat_bot(api_key=OPENAI_API_KEY, url=APIURL, user_input=user_query)

    # Render HTML template with updated chat responses
    return templates.TemplateResponse('index.html', {"request": request, "chat_responses": [response], "api_url":APIURL})


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)