import time
import requests

requests.packages.urllib3.disable_warnings()

class GoWitness:
    def __init__(self):
        self.url = 'http://10.147.20.106:7776/api/'

    # get list
    def get_list(self):
        """
        Get the list of screenshots.
        :return: List with the response.
        """
        url = self.url + 'list'
        try:
            response = requests.get(url, verify=False)
            return response.json()
        except Exception as e:
            print(f'get_list: {e}')
            return None
        
    def get_detail(self, id) -> dict:
        """
        Get the detail of a screenshot.
        :param id: ID of the screenshot.
        :return: Dictionary with the response.
        """
        url = self.url + 'detail/' + id
        try:
            response = requests.get(url, verify=False)
            return response.json()
        except Exception as e:
            print(f'get_detail: {e}')
            return None
        
    def get_screenshot(self, id) -> dict:
        """
        Get the screenshot of a screenshot.
        :param id: ID of the screenshot.
        :return: Dictionary with the response.
        """
        url = self.url + 'detail/' + id + '/screenshot'
        try:
            response = requests.get(url, verify=False)
            return response.json()
        except Exception as e:
            print(f'get_screenshot: {e}')
            return None
    
    def search(self, query) -> list:
        """
        Search for a screenshot.
        :param query: Query to search.
        :return: List with the response.
        """
        url = self.url + 'search?q=' + query
        try:
            response = requests.get(url, verify=False)
            return response.json()
        except Exception as e:
            print(e)
            return None
        
    def take_screenshot(self, url) -> dict:
        """
        Take a screenshot.
        :param url: URL to take the screenshot.
        :return: Dictionary with the response.
        """
        query_url = self.url + 'screenshot'
        json = {"url": url, "oneshot": "false"}

        try:
            response = requests.post(query_url, verify=False, json=json)
            return response.json()
        except Exception as e:
            print(f'take_screenshot: {e}')
            return None
        
gowitness = GoWitness()
print(gowitness.get_list())
# print(gowitness.get_detail('1'))
# print(gowitness.get_screenshot('1'))
# print(gowitness.search('https://example.com'))
# print(gowitness.take_screenshot('https://example.com'))

# try:
#     with open('test.txt', 'r') as file:
#         urls = file.readlines()
#         for url in urls:
#             url = url.strip()
#             print(f'Take screenshot for {url}', gowitness.take_screenshot(url))
#             time.sleep(1)
#     print('Done')
# except Exception as e:
#     print(e)

'''
GET /list detail
GET /detail/:id detail
GET /detail/:id/screenshot detail
GET /search detail
POST /screenshot detail
'''