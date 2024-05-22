import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
headers={"Authorization": "Bearer " + os.getenv('API_TOKEN_PRODUCTION'), "Accept": "application/json+canvas-string-ids"}
response = requests.get("https://canvas.instructure.com/api/v1/courses", headers=headers)
response = response.json()
print(json.dumps(response, indent=2))