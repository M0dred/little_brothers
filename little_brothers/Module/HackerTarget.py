import requests

requests.packages.urllib3.disable_warnings()

# https://hackertarget.com/ip-tools/
class HackerTarget():
    def __init__(self):
        self.url = 'https://api.hackertarget.com/'
    
    # Access to the MTR Traceroute API
    def mtr(self, ip) -> str:
        """
        Perform a traceroute to a host.
        :param ip: IP address to traceroute.
        :return: String with the response.
        """
        url = self.url + 'mtr/?q=' + ip
        try:
            response = requests.get(url, verify=False)
            return response.text
        except Exception as e:
            print(e)
            return None
        
# hackertarget = HackerTarget()
# print(hackertarget.mtr('1.1.1.1'))