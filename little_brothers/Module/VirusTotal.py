import requests

requests.packages.urllib3.disable_warnings()

class VirusTotal:
    def __init__(self):
        self.url = 'https://www.virustotal.com/api/v3/'
        self.headers = {'x-apikey': 'your API key'}