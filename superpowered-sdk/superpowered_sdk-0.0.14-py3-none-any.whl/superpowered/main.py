# TODO: make this more performant by using asyncio and aiohttp
# TODO: use deque for chat history since the order is reversed in time

# import aiohttp
# import asyncio
import requests

# declare global variables
global HEADERS
global models
global incantations

HEADERS = None
models = {}
incantations = {}


BASE_URL = 'https://58shnvgnlf.execute-api.us-east-1.amazonaws.com/sandbox/'


def get_models():
    url = BASE_URL + 'models'
    resp = requests.get(url, headers=HEADERS)
    resp = _format_http_response(resp)
    for model in resp['body']:
        m = Model(
            model_id=model['id'],
            model_spec=model['model_spec'],
            supp_id = model['supp_id'],
            description=model['description']
        )
        models[model['id']] = m


def get_incantations():
    url = BASE_URL + 'incantations'
    resp = requests.get(url, headers=HEADERS)
    resp = _format_http_response(resp)
    for incantation in resp['body']:
        inc = Incantation(
            incantation_id=incantation['id'],
            title=incantation['title'],
            text=incantation['text'],
            supp_id=incantation['supp_id'],
            description=incantation['description']
        )
        incantations[incantation['id']] = inc


def init(api_key: str):
    global HEADERS
    global models
    global incantations
    HEADERS = {'x-api-key': api_key}

    # get the current state with models and incantations
    models = get_models()
    incantations = get_incantations()

    print(models)
    print(incantations)


# exceptions
class NoApiKeyError(Exception):
    def __init__(self):
        super().__init__('No API key has been set. Please run check that your API key is correct and then run `superpowered.init(api_key)` before continuing')


def _format_http_response(resp: requests.Response):
    if resp.status_code != 200:
        raise Exception(resp.json())
    return {
        'http_code': resp.status_code,
        'body': resp.json()
    }


class Incantation:
    def __init__(self, title: str, text: str, supp_id: str = None, description: str = None, incantation_id: str = None):
        self.incantation_id = incantation_id
        self.title = title
        self.text = text
        self.supp_id = supp_id
        self.description = description
        self.is_deployed = self.incantation_id is not None

    def create(self):
        if self.is_deployed:
            raise Exception('This incantation has already been deployed: ' + self.incantation_id)
        url = BASE_URL + 'incantations'
        payload = {
            'title': self.title,
            'text': self.text,
            'supp_id': self.supp_id,
            'description': self.description
        }
        resp = _format_http_response(requests.post(url, headers=HEADERS, json=payload))
        self.incantation_id = self.get_incantation_id()
        self.is_deployed = True
        incantations[resp['body']['id']]
        return resp['body']

    def update(self):
        if not self.is_deployed:
            raise Exception('This incantation has not been deployed yet. Please run `incantation.create()` before running `incantation.update()')
        url = BASE_URL + f'incantations/{self.incantation_id}'
        payload = {}
        if self.title is not None:
            payload['title'] = self.title
        if self.text is not None:
            payload['text'] = self.text
        if self.supp_id is not None:
            payload['supp_id'] = self.supp_id
        if self.description is not None:
            payload['description'] = self.description
        resp = _format_http_response(requests.put(url, headers=HEADERS, json=payload))
        return resp['body']

    def delete(self, incantation_id: str):
        url = BASE_URL + f'incantations/{incantation_id}'
        _format_http_response(requests.delete(url, headers=HEADERS))
        del incantations[incantation_id]


class Model:
    def __init__(self, model_spec: dict, supp_id: str = None, description: str = None, model_id: str = None):
        self.model_id = model_id
        self.model_spec = model_spec
        self.supp_id = supp_id
        self.description = description
        self.is_deployed = self.model_id is not None
        self.model_instances = self.get_instances()
        print(locals())

    def create(self):
        if self.is_deployed:
            raise Exception('This model has already been deployed: ' + self.model_id)
        url = BASE_URL + 'models'
        payload = {
            'model_spec': self.model_spec,
            'supp_id': self.supp_id,
            'description': self.description
        }
        resp = _format_http_response(requests.post(url, headers=HEADERS, json=payload))
        self.model_id = self.get_model_id()
        self.is_deployed = True
        models[resp['body']['id']]
        return resp['body']

    def update(self):
        if not self.is_deployed:
            raise Exception('This model has not been deployed yet. Please run `model.create()` before running `model.update()')
        url = BASE_URL + f'models/{self.model_id}'
        payload = {}
        if self.model_spec is not None:
            payload['model_spec'] = self.model_spec
        if self.supp_id is not None:
            payload['supp_id'] = self.supp_id
        if self.description is not None:
            payload['description'] = self.description
        resp = _format_http_response(requests.put(url, headers=HEADERS, json=payload))
        return resp['body']

    def delete(self):
        url = BASE_URL + f'models/{self.model_id}'
        _format_http_response(requests.delete(url, headers=HEADERS))
        del models[self.model_id]
        return True

    def get_instances(self):
        url = BASE_URL + f'models/{self.model_id}/instances'
        resp = _format_http_response(requests.get(url, headers=HEADERS))
        instances = {}
        for instance in resp['body']:
            inst = ModelInstance(
                model_id=instance['model_id'],
                supp_id=instance['supp_id'],
                description=instance['description'],
                instance_id=instance['id']
            )
            instances[instance['id']] = inst
        return instances


class ModelInstance:
    def __init__(self, model_id: str = None, supp_id: str = None, description: str = None, instance_id = None):
        self.supp_id = supp_id
        self.description = description
        self.instance_id = instance_id
        self.model_id = model_id
        self.chat_history = []
        self.chat_history = self.get_chat_history()
        self.is_deployed = self.instance_id is not None

    def get_chat_history(self):
        # get chat history interactions with pagination
        url = BASE_URL + f'models/{self.model_id}/instances/{self.instance_id}/chat_history'
        response = _format_http_response(requests.get(url, headers=HEADERS))
        print('get_chat_history debugging')
        print(url)
        print(response)
        self.chat_history.extend(response['body']['interactions'])
        while 'next_page_token' in response:
            response = _format_http_response(requests.get(url, headers=HEADERS, params={'next_page_token': response['next_page_token']}))
            self.chat_history.extend(response['body']['interactions'])

    def create(self):
        if self.is_deployed:
            raise Exception('This model instance has already been deployed: ' + self.instance_id)
        url = BASE_URL + f'models/{self.model_id}/instances'
        payload = {
            'supp_id': self.supp_id,
            'description': self.description
        }
        resp = _format_http_response(requests.post(url, headers=HEADERS, json=payload))
        self.instance_id = self.get_instance_id()
        self.is_deployed = True
        models[self.model_id].model_instances[self.instance_id] = self
        return resp['body']

    def update(self):
        if not self.is_deployed:
            raise Exception('This model instance has not been deployed yet. Please run `model_instance.create()` before running `model_instance.update()')
        url = BASE_URL + f'models/{self.model_id}/instances/{self.instance_id}'
        payload = {}
        if self.supp_id is not None:
            payload['supp_id'] = self.supp_id
        if self.description is not None:
            payload['description'] = self.description
        resp = _format_http_response(requests.put(url, headers=HEADERS, json=payload))
        return resp['body']

    def delete(self):
        url = BASE_URL + f'models/{self.model_id}/instances/{self.instance_id}'
        resp = _format_http_response(requests.delete(url, headers=HEADERS))
        del models[self.instance_id]
        return resp['body']

    def get_response(self, human_input: list):
        url = BASE_URL + f'models/{self.model_id}/instances/{self.instance_id}/get_response'
        payload = {
            'human_input': human_input
        }
        resp = _format_http_response(requests.post(url, headers=HEADERS, json=payload))
        self.chat_history.insert(0, resp.body['interaction'])
        return resp['body']
