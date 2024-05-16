import os
from dotenv import load_dotenv
from langchain_openai import OpenAI , ChatOpenAI , OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain , create_history_aware_retriever
from langchain_core.messages import HumanMessage , AIMessage


def document_loader(url: str):
    """
    Load documents from the given URL, generate embeddings, and return a retriever.

    Args:
        url (str): URL for accessing relevant documents.

    Returns:
        Retriever: A retriever object for accessing and retrieving documents.
    """

    # Load documents from the web
    web_loader = WebBaseLoader(url)
    documents = web_loader.load()

    # Generate embeddings for the documents
    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter()
    split_documents = text_splitter.split_documents(documents)
    vector_store = FAISS.from_documents(documents=split_documents, embedding=embeddings)
    retriever = vector_store.as_retriever()
    
    return retriever


def chat_bot(api_key: str, retriever, user_input: str) -> str:
    """
    Generates a response based on the user input using a combination of history-aware retrieval and document analysis.

    Args:
        api_key (str): The API key for accessing OpenAI services.
        url (str): URL for accessing relevant documents.
        user_input (str): User's input to generate a response.

    Returns:
        str: Response generated based on the user input and context.
    """

    # Initialize ChatOpenAI instance
    chat_ai = ChatOpenAI(api_key=api_key) 
    
    # Define prompt for history-aware retrieval
    prompt_retrieval = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
        ("user", "Based on the conversation above, generate a search query to retrieve relevant information.")
    ])
    
    # Create history-aware retriever
    history_aware_retriever = create_history_aware_retriever(chat_ai, retriever=retriever, prompt=prompt_retrieval)
    
    # Initialize chat history
    chat_history = [
        HumanMessage(content="Who are we talking about?"),
        AIMessage(content="Yes")
    ]
    
    # Define prompt for document analysis
    prompt_analysis = ChatPromptTemplate.from_messages([
        ("system", "Answer the user's content based on the context below:\n\n{context}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}")
    ])
    
    # Create document analysis chain
    document_analysis_chain = create_stuff_documents_chain(chat_ai, prompt_analysis)
    
    # Create retrieval chain
    retrieval_chain = create_retrieval_chain(history_aware_retriever, document_analysis_chain)
    
    # Invoke retrieval chain to generate response
    response = retrieval_chain.invoke({
        'chat_history': chat_history,
        'input': f"{user_input}"
    })
    
    return response['answer']



    