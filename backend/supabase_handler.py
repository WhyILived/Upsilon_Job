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

def store_accomplishments(e_id, embeddings, raw_sentence, key_terms, impact):
    response = (
        supabase_client.table("accomplishments")
        .insert([{"embedding":embeddings[i], "impact": impact[i], "key_terms": key_terms[i], "e_id" : e_id[i], "raw_sentence" : raw_sentence[i]} for i in range(len(embeddings))])
        .execute()
    ).data
    return [response[i]['a_id'] for i in range(len(response))]

def store_experience(u_id, name, type):
    response = (
        supabase_client.table("experience")
        .insert([{"u_id" : u_id, "name": name[i], "type": type[i]} for i in range(len(name))])
        .execute()
    ).data
    return [response[i]['e_id'] for i in range(len(response))]