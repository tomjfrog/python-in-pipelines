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
    test_curl = subprocess.run('curl https://www.google.com/'.split(' '),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logging.debug("tmp_mvn_output: %s", test_curl)
    tmp_mvn_str = test_curl.stdout.decode()
    logging.info("Finishing Python Script...")


if __name__ == "__main__":
    main()
