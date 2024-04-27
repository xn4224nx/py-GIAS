#!/usr/bin/python3

import pytest

from .. import scrape


def test_api_get():
    """
    Enusure that the API class can connect to a non-API website successfully.
    """
    endpt = scrape.API()
    result = endpt.get("https://www.bbc.com/")

    assert result.status_code == 200
    assert type(result.content == str)
    assert result.content is not None
