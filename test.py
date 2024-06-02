#!/usr/bin/env python3

### IMPORTS ###
# import base64
# import json
import logging
# import os
import subprocess
# import sys

def main():
    logging.basicConfig(
        format="%(asctime)s:%(levelname)s:%(name)s:%(funcName)s: %(message)s",
        level=logging.DEBUG
    )
    logging.info("Starting Python Script...")
    test_curl = subprocess.run('curl -X POST https://tomjfrog-pipelines-api.jfrog.io/v1/projectIntegrations/127/hook'.split(' '),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logging.debug("tmp_mvn_output: %s", test_curl)
    logging.info("Finishing Python Script...")


if __name__ == "__main__":
    main()
