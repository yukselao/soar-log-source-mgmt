#!/usr/bin/env python

import requests
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient import SimpleHTTPException
import logging

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




filter = {
                "filters": [
                    {
                        "conditions": [
                            {
                            "field_name": "create_date",
                            "method": "gte",
                            "value": 1645603140
                            }
                        ]
                    }
                ],
                "sorts":[],
                "start":10,
                "length":100
}

url="https://10.10.2.50"
querystr = "/incidents/query_paged?return_level=normal"


def main():
	print("app started")
	s=FunctionComponent("test")

if __name__ == '__main__':
	main()
