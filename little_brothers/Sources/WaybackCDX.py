import requests

requests.packages.urllib3.disable_warnings()

# https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server
class Wayback:
    def __init__(self):
        self.url = 'https://web.archive.org/cdx/search/cdx'

    # ["urlkey","timestamp","original","mimetype","statuscode","digest","length"]
    def example(self):
        # Basic Usage
        url = self.url + '?url=archive.org&limit=100'
        response = requests.get(url, verify=False)
        print(response.text)

# wayback = Wayback()
# wayback.example()