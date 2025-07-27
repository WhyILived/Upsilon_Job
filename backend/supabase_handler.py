import os
import supabase
from pathlib import Path
from dotenv import load_dotenv
import numpy as np 

project_root = Path(__file__).parent.parent
load_dotenv(project_root / '.env')

url = os.environ.get("SUPABASE_URL")
api_key = os.environ.get("SUPABASE_KEY")

supabase_client = supabase.create_client(url, api_key)

def store_vector_embeddings(embeddings):
    response = (
        supabase_client.table("vectorembeddings")
        .insert([{"embedding":embeddings[i]} for i in range(len(embeddings))])
        .execute()
    ).data
    return [response[i]['id'] for i in range(len(response))] 