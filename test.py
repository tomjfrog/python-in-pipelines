#!/usr/bin/env python3

### IMPORTS ###
import base64
import json
import logging
import os
import requests


# import sys
def fetchRepos(authString):
    logging.info("Fetching all repos....")
    basic_auth_string = os.environ['int_webhook_basic_auth_b64_encoded_basic_auth_string']
    url = "https://tomjfrog.jfrog.io/artifactory/api/repositories/"
    payload = ""
    auth_header_value = f'Basic {basic_auth_string}'
    headers = {"Authorization": auth_header_value}
    response = requests.request("GET", url, data=payload, headers=headers)
    logging.debug("Fetch Repos Response: %s", response)
    logging.info("Response payload JSON: %s", response.json())
    response_json = response.json()
    # Remove everything except Docker repos
    docker_repos = [element for element in response_json if element.get('packageType') == 'Docker']
    return docker_repos

def triggerChildPipeline(authString, repo_name):
    logging.info("Triggering Child Pipeline...")
    url = "https://tomjfrog-pipelines-api.jfrog.io/v1/projectIntegrations/127/hook"
    payload = {
        "repo": repo_name
    }
    auth_header_value = f'Basic {authString}'
    headers = {"Authorization": auth_header_value}
    response = requests.request("POST", url, json=payload, headers=headers)
    logging.debug("response: %s", response)


def main():
    logging.basicConfig(
        format="%(asctime)s:%(levelname)s:%(name)s:%(funcName)s: %(message)s",
        level=logging.DEBUG
    )
    logging.info("Starting Python Script...")
    basic_auth_string = os.environ['int_webhook_basic_auth_b64_encoded_basic_auth_string']
    repos = fetchRepos(basic_auth_string)
    for repo in repos:
        triggerChildPipeline(basic_auth_string, repo)
    logging.info("Finishing Python Script...")


if __name__ == "__main__":
    main()
