import requests

requests.packages.urllib3.disable_warnings()

class InternetDB:
    def __init__(self):
        self.url = 'https://internetdb.shodan.io/'

    def lookup(self, ip) -> dict:
        """
        Lookup an IP address in the InternetDB.
        :param ip: IP address to lookup.
        :return: Dictionary with the response.
        """
        url = self.url + ip
        try:
            response = requests.get(url, verify=False)
            return response.json()
        except Exception as e:
            print(e)
            return None
        
# internetdb = InternetDB()
# print(internetdb.lookup('1.1.1.1'))
# {'cpes': [], 'hostnames': ['one.one.one.one'], 'ip': '1.1.1.1', 'ports': [53, 80, 443, 2083, 2086, 2087, 8080, 8443, 8880], 'tags': [], 'vulns': []}