import requests

requests.packages.urllib3.disable_warnings()

# https://docs.binaryedge.io/api-v2/
class BinaryEdge:
    def __init__(self):
        self.url = 'https://api.binaryedge.io/v2/'
        self.headers = {'X-Key': 'your API key'}