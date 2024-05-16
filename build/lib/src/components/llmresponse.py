import os
from openai import OpenAI
from typing import List , Dict


import os
from typing import List
from pinecone import Pinecone, ServerlessSpec
import openai
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from components.data_retrival import retrieve_content

def Rag(username: str, password: str, wordpress_link: str):
    # Get API keys and other environment variables
    pinecone_key = os.getenv("PINECONE_KEY")
    pinecone_host = os.getenv("PINECONE_HOST")
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Initialize Pinecone client
    pc = Pinecone(api_key=pinecone_key, host=pinecone_host)

    # Create a new index if it doesn't exist, or get the existing one
    try:
        index = pc.Index("chatbot")
    except:
        pc.create_index(
            name="chatbot",
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
        index = pc.Index("chatbot")

    # Initialize OpenAI embedding model
    embed_model = OpenAIEmbeddings(api_key=openai_api_key)

    # Retrieve content from WordPress using provided credentials
    content = retrieve_content(username=username, password=password, website_link=wordpress_link)

    # Embed and store the documents in the Pinecone index
    title_texts = [{"text": title} for title in content["title"]]
    paragraph_texts = [{"text": paragraph} for paragraph in content["paragraph"]]

    # Embed title documents
    title_embeds = embed_model.embed_documents(title_texts)
    title_to_upsert = list(zip(title_embeds, title_texts))
    index.upsert(vectors=title_to_upsert)

    # Embed paragraph documents
    paragraph_embeds = embed_model.embed_documents(paragraph_texts)
    paragraph_to_upsert = list(zip(paragraph_embeds, paragraph_texts))
    index.upsert(vectors=paragraph_to_upsert)

    # Prepare training data
    training_data = []
    for title, paragraph in zip(content["title"], content["paragraph"]):
        training_data.append({"prompt": title, "completion": paragraph})

    # Fine-tune the model
    openai.api_key = openai_api_key
    fine_tune_response = openai.FineTune.create(
        train_data=training_data,
        model="ada",  # or any other base model you prefer
        suffix="my-custom-model"
    )

    # Wait for the fine-tuning to complete
    fine_tune_response = openai.FineTune.retrieve(fine_tune_response["id"])
    while fine_tune_response.status != "succeeded":
        fine_tune_response = openai.FineTune.retrieve(fine_tune_response["id"])

    # Get the fine-tuned model name
    fine_tuned_model = fine_tune_response.fine_tuned_model

    return fine_tuned_model


def generate_response(query, settings, chat_log):
    # Check if the fine-tuned model is enabled in settings
    if settings.get("use_fine_tuned_model", False):
        # Use the fine-tuned model
        fine_tuned_model = settings.get("fine_tuned_model_name")
        rag = Rag(fine_tuned_model)
        result = rag(query)
        response = result['result']  # Extract the response from the result
    else:
        # Use the base model
        client = openai.OpenAIClient()
        # Generate response using the base model
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_log,
            temperature=0.6
        )
        response = response.choices[0].message.content  # Extract the content of the response

    return response
