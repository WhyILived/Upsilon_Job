import os
from vellum.client import Vellum
import vellum.types as types
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).parent.parent
load_dotenv(project_root / '.env')
# create your API key here: https://app.vellum.ai/api-keys#keys
client = Vellum(
  api_key=os.environ.get("VELLUM_API_KEY")
)
def parse_resume(resume_JSON : dict):    
    result = client.execute_workflow(
        workflow_deployment_name="bullet-point-terms",
        release_tag="LATEST",
        inputs=[
            types.WorkflowRequestJsonInputRequest(
                name="BuildingBlocks",
                type="JSON",
                value=resume_JSON,
            ),
        ],
    )
    return result.model_dump()['data']['outputs'][0]['value']