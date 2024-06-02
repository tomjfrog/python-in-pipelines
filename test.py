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
    test_curl = subprocess.run('curl https://www.google.com/'.split(' '),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == "__main__":
    main()
