import requests
from requests.exceptions import HTTPError
from django.conf import settings
from .tasks import populatedb
from celery.result import AsyncResult
import json

class StackExchange:
    endpoint = 'https://api.stackexchange.com/2.2/{}'  # endpoint for Stackexchange API

    def get_all_questions(self, page=1,order="desc", sort="activity", site="stackoverflow"):
        param={
            "page":page,
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.endpoint.format('questions'), params=param)
            json_response = response.json()
            return response.json()
            response.raise_for_status()
        except Exception as err:
            print(f'Error occurred: {err}')

    def get_by_query(self, query, page=1, order="desc", sort="activity", site="stackoverflow"):
        param={
            "page":page,
            "intitle" : query,
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.endpoint.format('search'), params=param)
            json_response = response.json()
            populatedb.delay(query,json_response)
            return response.json()
            response.raise_for_status()
        except Exception as err:
            print(f'Error occurred: {err}')
    

    

