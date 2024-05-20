from setuptools import setup, find_packages

setup(
    name='WebSage',
    version='0.0.1',
    author="Ved Prakash Pathak",
    description="WebSage: A RAG-based chatbot that interacts with any website using OpenAI's GPT, Langchain, and FAISS.",
    long_description="""Welcome to WebSage, a RAG (Retrieval-Augmented Generation) based chatbot designed to chat with any website. This project leverages cutting-edge technologies such as OpenAI's GPT, Langchain, and FAISS to provide efficient retrieval and interaction with web content.
Web Content Interaction: Utilizes BeautifulSoup4 for web scraping and content extraction, enabling the chatbot to interact with live web pages and retrieve relevant information.
FastAPI Integration: Offers a seamless API endpoint for easy interaction with the chatbot, facilitating integration with other applications and services.
Langchain for LLM: Manages and interacts with language models using Langchain, ensuring robust and scalable conversational AI capabilities.
FAISS Vector Database: Employs FAISS for fast and efficient similarity search and retrieval, enhancing the chatbot's ability to find and provide accurate information from large datasets.
Environment Variables: Configurable via a .env file, allowing easy setup and management of API keys and other critical settings.
WebSage combines the power of advanced AI technologies to deliver a versatile and efficient chatbot capable of interacting with any website, making it an invaluable tool for various applications.""",
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.12.3',
        'fastapi==0.111.0',
        'langchain==0.1.20',
        'langchain_community==0.0.38',
        'langchain_core==0.1.52',
        'langchain_openai==0.1.7',
        'openai==1.30.1',
        'pinecone==4.0.0',
        'pydantic==2.7.1',
        'python-dotenv==1.0.1',
        'requests==2.31.0',
        'setuptools==69.5.1',
        'uvicorn==0.29.0',
    ],
)
