import base64
import requests
from bs4 import BeautifulSoup

def get_posts(USERNAME, PASSWORD, website_link):
    # Combine username and password
    credentials = USERNAME + PASSWORD

    # Encode credentials
    token = base64.b64encode(credentials.encode())

    # Set authorization header
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}

    # Make request to API
    response = requests.get(website_link, headers=header)

    # Check if request was successful
    if response.status_code == 200:
        # Parse the response JSON
        posts = response.json()
        return posts
    else:
        return None

def strip_html_and_split_into_paragraphs(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract text
    text = soup.get_text(separator="\n", strip=True)
    
    # Define a translation table to remove special characters
    special_chars = ",;:.!?()[]{}<>`~@#$%^&*_-=+|\\/"

    # Remove special characters from the text
    translation_table = str.maketrans("", "", special_chars)
    text = text.translate(translation_table)

    # Split the text into paragraphs using "\n\n"
    paragraphs = text.split("\n\n")

    # Split each paragraph into lines
    stripped_paragraphs = [p.split("\n") for p in paragraphs]

    # Strip leading and trailing whitespace from each line
    stripped_paragraphs = [[line.strip() for line in p] for p in stripped_paragraphs]

    return stripped_paragraphs


def retrieve_content(username, password, website_link):
    """
    Retrieves content from a WordPress API endpoint, processes it, and returns paragraphs.

    Args:
    - username (str): The username for authentication.
    - password (str): The password for authentication.
    - website_link (str): The URL of the API endpoint.

    Returns:
    - list: A list of paragraphs extracted from the content.
    """
    # Fetch posts from the API
    posts = get_posts(USERNAME=username, PASSWORD=password, website_link=website_link)

    # Initialize lists to store paragraphs and titles
    paragraphs = []
    titles = []

    # If posts are fetched successfully
    if posts:
        # Iterate over each post
        for post in posts:
            # Extract the title and content of the post
            title = post["title"]['rendered']
            content = post['content']['rendered']
            
            # Strip HTML tags and split content into paragraphs
            paragraphs.extend(strip_html_and_split_into_paragraphs(content))
            titles.extend(strip_html_and_split_into_paragraphs(title))
    
    return {"title": titles, "paragraph": paragraphs}



