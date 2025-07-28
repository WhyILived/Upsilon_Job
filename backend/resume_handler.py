from google import genai
from google.genai import types
import os
from pathlib import Path
from dotenv import load_dotenv
import numpy as np
import supabase_handler 
import vellum_handler

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


test_id = "1af120f7-2322-43fa-86da-7b09b90588ab"
def store_resume(resume_dict, u_id):
    resume_dict = vellum_handler.parse_resume(resume_dict)
    experience_array = resume_dict["Experiences"]
    name = []
    exp_type = []

    for i in range(len(experience_array)):
        name.append(experience_array[i]["Name"])
        exp_type.append(experience_array[i]["Type"])

    e_id = supabase_handler.store_experience(u_id, name, exp_type)

    exp_id = []
    impact = []
    key_terms = []
    raw = []
    weighted_sentence = []

    for i in range(len(experience_array)):
        accomplishments = experience_array[i]["Accomplishments"]
        for j in range(len(accomplishments)):

            exp_id.append(e_id[i])
            impact.append(accomplishments[j]["Impact"])
            joined_terms = ", ".join(accomplishments[j]["Key Terms"])
            key_terms.append(joined_terms)
            raw.append(accomplishments[j]["Sentence"])
            weighted_sentence.append(accomplishments[j]["Sentence"] + ". " +  joined_terms)
    embeddings = get_sentence_embeddings(weighted_sentence)

    supabase_handler.store_accomplishments(exp_id, embeddings, raw, key_terms, impact)

store_resume(test_dict, test_id)