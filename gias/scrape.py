#!/usr/bin/python3

import requests
import os


class API:
    """
    A class to handle requests to the DFE API endpoint.
    """

    def __init__(self):
        self.proxy = {
            "http": None,
            "https": None,
            "ftp": None,
        }

        self.credentials = {
            "GOV_APP_NAME": None,
            "GOV_CLIENT_ID": None,
            "GOV_PRI_SEC": None,
            "GOV_SEC_SEC": None,
        }

        self.gov_url = "https://oat-api-customerengagement.platform.education.gov.uk"
        self.endpt = "dfe/open-info"

    def get(self, url: str):
        """
        Make a get request.
        """

        api_req = requests.get(url, proxies=self.proxy)

        return api_req

    def populate_credentials(self):
        """
        Access the users environmental variables to get the credentials to
        access the DFE API.
        """
        users_env_var = os.environ

        for cred_name in self.credentials:
            if cred_name not in users_env_var:
                raise Exception(
                    f"The credential '{cred_name}' has not been set in your environment!"
                )
            else:
                self.credentials[cred_name] = users_env_var[cred_name]
