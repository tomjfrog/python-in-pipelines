#!/usr/bin/env python3

### IMPORTS ###
# import base64
# import json
import logging
import os
import requests


# import sys

def main():
    logging.basicConfig(
        format="%(asctime)s:%(levelname)s:%(name)s:%(funcName)s: %(message)s",
        level=logging.DEBUG
    )
    basic_auth_string = os.environ['int_webhook_basic_auth_b64_encoded_basic_auth_string']
    logging.info("Starting Python Script...")
    # test_curl = subprocess.run('curl -X POST https://tomjfrog-pipelines-api.jfrog.io/v1/projectIntegrations/127/hook --header Authorization: Basic foo'.split(' '),
    url = "https://tomjfrog-pipelines-api.jfrog.io/v1/projectIntegrations/127/hook"
    payload = ""
    auth_header_value = f'Basic {basic_auth_string}'
    headers = {"Authorization": auth_header_value}
    response = requests.request("POST", url, data=payload, headers=headers)
    logging.debug("tmp_mvn_output: %s", response)
    logging.info("Finishing Python Script...")

if __name__ == "__main__":
    main()
