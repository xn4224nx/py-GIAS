#!/usr/bin/python3

import requests


class API:
    """
    A class to handle requests to the DFE API endpoint.
    """

    def __init__(self):
        proxy = {
            "http": None,
            "https": None,
            "ftp": None,
        }

    def get(self, url: str):
        """
        Make a get request.
        """

        api_req = requests.get(url)

        return api_req
