Here is a `README.md` file for your RAG-based OpenAI chatbot project using Langchain and FAISS:

```markdown
# WebSage: Chat with Any Website

Welcome to WebSage, a RAG (Retrieval-Augmented Generation) based chatbot designed to chat with any website. This project utilizes OpenAI's GPT, Langchain, and FAISS as the vector database for efficient retrieval and interaction with web content.

## Features

- **Web Content Interaction**: Uses BeautifulSoup4 for web scraping and content extraction.
- **FastAPI Integration**: Provides a seamless API endpoint for chatbot interaction.
- **Langchain for LLM**: Utilizes Langchain for managing and interacting with language models.
- **FAISS Vector Database**: Employs FAISS for fast and efficient similarity search and retrieval.
- **Environment Variables**: Configurable via `.env` file for API keys and other settings.

## Installation

### Prerequisites

Ensure you have Python 3.10 or higher installed. Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```
## Project Snapshots

### URL Input Page
![URL Input Page](https://github.com/IAMPathak2702/WebSage-Chat-with-Any-Website/blob/main/snapshots/urlPage.png)

### Chatbot Interaction Page
![Chatbot Interaction Page](https://github.com/IAMPathak2702/WebSage-Chat-with-Any-Website/blob/main/snapshots/chatbotPage.png)

### Demo Video
[![Websage Video](https://github.com/IAMPathak2702/WebSage-Chat-with-Any-Website/blob/main/snapshots/Websage-Video.mp4)](https://github.com/IAMPathak2702/WebSage-Chat-with-Any-Website/blob/main/snapshots/Websage-Video.mp4)

### Animated Workflow
![WebSage GIF](https://github.com/IAMPathak2702/WebSage-Chat-with-Any-Website/blob/main/snapshots/WebSage.gif)

### Libraries Used

- beautifulsoup4==4.12.3
- fastapi==0.111.0
- langchain==0.1.20
- langchain_community==0.0.38
- langchain_core==0.1.52
- langchain_openai==0.1.7
- openai==1.30.1
- pinecone==4.0.0
- pydantic==2.7.1
- python-dotenv==1.0.1
- Requests==2.31.0
- setuptools==69.5.1
- uvicorn==0.29.0

## Project Structure

```plaintext
|-- .env
|-- .gitignore
|-- main.py
|-- README.md
|-- requirements.txt
|-- __init__.py
|
|-- .idea
|   |-- .gitignore
|   |-- misc.xml
|   |-- modules.xml
|   |-- vcs.xml
|   |-- ved-prakash-pathak-wasserstoff-AiTask.iml
|   |-- workspace.xml
|   |
|   |-- inspectionProfiles
|       |-- profiles_settings.xml
|       |-- Project_Default.xml
|
|-- components
|   |-- chatlog.py
|   |-- data_retrival.py
|   |-- llmresponse.py
|   |-- __init__.py
|   |
|   |-- __pycache__
|       |-- chatlog.cpython-312.pyc
|       |-- data_retrival.cpython-311.pyc
|       |-- data_retrival.cpython-312.pyc
|       |-- llmresponse.cpython-311.pyc
|       |-- __init__.cpython-312.pyc
|
|-- static
|   |-- index.js
|   |-- style.css
|   |
|   |-- images
|       |-- send.png
|
|-- templates
|   |-- index.html
|   |-- url.html
|   |-- __init__.py
|
|-- __pycache__
    |-- main.cpython-311.pyc
    |-- main.cpython-312.pyc
```

## Getting Started

### Running the Application

1. Clone the repository:

```bash
git clone https://github.com/IAMPathak2702/WebSage-Chat-with-Any-Website.git
cd WebSage-Chat-with-Any-Website
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Configure your `.env` file with the necessary API keys and settings.

4. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

5. Open your browser and navigate to `http://localhost:8000` to access the chatbot interface.

### Usage

- Enter the URL of the website you want to interact with in the input field.
- The chatbot will retrieve and process the content from the specified URL and respond to your queries based on the extracted information.

## Author

Ved Prakash Pathak

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the open-source community for the libraries and tools used in this project.
- Inspired by the advancements in AI and NLP technologies.

For more details, visit the [GitHub repository](https://github.com/IAMPathak2702/WebSage-Chat-with-Any-Website).

