#!/usr/bin/env python

import os
import json
import logging as log
from utils.common import LogManager
from some_utility import tech_util

if __name__ == '__main__':
    log_manager = LogManager()
    log_manager.init_logging()
    log.info("Creating Jira project...")

    log.info("Environment: %s", os.environ)

    result = {'result': {
        'projectKey': 'TSTPRJ',
        'projectName': os.environ.get('PROJECT_NAME', 'ProjectName'),
        'boardType': os.environ.get('BOARD_TYPE', 'scrum'),
        'url': 'http://jira.yourcompany.example.com',
        'someValue': tech_util.sum_n_multiply(2)
    }}

    with open(os.environ['RESULT_FILE'], 'w', encoding="utf8") as target_file:
        target_file.write(json.dumps(result))

    log.info("...DONE")
