from __future__ import print_function

from pprint import pprint
from unicodedata import name

import pandas as pd
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

creds = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=creds)
project = 'seahsteel-erp-prod'

def create_machine_image():

    request_body = {
        "name": "test-image",
        "sourceInstance": "projects/seahsteel-erp-prod/zones/asia-northeast3-a/instances/ldy-test-vm-1"
    }

    request = service.machineImages().insert(project=project, body=request_body)
    response = request.execute()

    print(response)

    
create_machine_image()
