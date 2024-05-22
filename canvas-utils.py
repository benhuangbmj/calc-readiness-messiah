import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
headers={"Authorization": "Bearer " + os.getenv('API_TOKEN_PRODUCTION'), "Accept": "application/json+canvas-string-ids"}
baseURL='https://canvas.instructure.com/api/v1/'

def listAssignments(courseId, params={}):
    res = requests.get(baseURL + f'courses/{courseId}/assignments', headers=headers, params=params)
    output = res.json()
    return output

def listSubmission(courseId, assignmentId, params={}):
    res = requests.get(baseURL + f'courses/{courseId}/assignments/{assignmentId}/submissions', headers=headers, params=params)
    output = res.json()
    return output

