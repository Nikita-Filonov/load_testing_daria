import json
from functools import lru_cache

from locust import SequentialTaskSet
from locust.clients import LocustResponse
from locust.contrib.fasthttp import FastHttpSession
from settings import TEST_USER


class BaseTaskSet(SequentialTaskSet):

    @lru_cache(maxsize=None)
    def get_token(self, user=None):
        if isinstance(user, str):
            user = json.loads(user)

        response = self.client.post('/api/v1/token', data=user or TEST_USER)
        json_response = response.json()
        return json_response.get('token')

    def request(self, method: str, url: str, user: dict = None, **kwargs) -> LocustResponse:
        client: FastHttpSession = self.client

        token = self.get_token(user)
        headers = {
            'Content-type': 'application/json',
            'Authorization': f'Token {token}'
        }

        return client.request(method=method, url=url, headers=headers, **kwargs)

    def get(self, url, params=None, user=None, **kwargs):
        return self.request(method='GET', url=url, user=user, params=params, **kwargs)

    def post(self, url, json=None, user=None, **kwargs):
        return self.request(method='POST', url=url, user=user, json=json, **kwargs)
    
    def patch(self, url, json=None, user=None, **kwargs):
        return self.request(method='PATCH', url=url, user=user, json=json, **kwargs)
