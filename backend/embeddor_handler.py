from google import genai
from google.genai import types
import os
from pathlib import Path
from dotenv import load_dotenv
import numpy as np
import supabase_handler 

project_root = Path(__file__).parent.parent
load_dotenv(project_root / '.env')

client = genai.Client(api_key = os.environ.get("GOOGLE_API_KEY"))

def get_sentence_embeddings(sentence_list):
    return [
        e.values for e in client.models.embed_content(
            model="gemini-embedding-001",
            contents = sentence_list,
            config = types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")).embeddings
        ]

def add_embeddings(experience_dict):
    experience_array = experience_dict["Experiences"]
    term_weighted_arr = []

    for experience in experience_array:

        for accomplishment in experience["Accomplishments"]:

            term_weighted_sentence = accomplishment["Sentence"] + ". Key Terms: " + ", ".join(accomplishment["Key Terms"]) + "."

            term_weighted_arr.append(term_weighted_sentence)

    embeddings = get_sentence_embeddings(term_weighted_arr)
    embed_ids = supabase_handler.store_vector_embeddings(embeddings)

    idx = 0
    for i in range(len(experience_array)):
        for j in range(len(experience_array[i]["Accomplishments"])):
            experience_dict["Experiences"][i]["Accomplishments"][j]["Term Weighted"] = term_weighted_arr[idx]
            experience_dict["Experiences"][i]["Accomplishments"][j]["Embedding Index"] = embed_ids[idx]
            idx += 1
    return experience_dict