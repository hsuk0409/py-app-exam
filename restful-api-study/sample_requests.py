import requests


class SampleRequests:
    def call_url(self):
        apiUrl = "https://jsonplaceholder.typicode.com/todos/1"
        response = requests.get(apiUrl)

        return response


def call_url():
    return None