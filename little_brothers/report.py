import os
import json
from pprint import pprint

# read json from a json file
def read_json(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f'read_json: {e}')
        return []
    
# dict_keys(['cpes', 'hostnames', 'ip', 'ports', 'tags', 'vulns'])
def main():
    vulns = read_json('vulns.json')
    # for vuln in vulns:
    #     if len(vuln['vulns']) > 0:
    #         print(vuln['ip'], f'has {len(vuln["vulns"])} vulnerabilities')
    
    # Found top 10 most vulnerable IPs
    # Sort the list of IPs based on the number of vulnerabilities
    # sorted_vulns = sorted(vulns, key=lambda x: len(x['vulns']), reverse=True)
    # for vuln in sorted_vulns[:10]:
    #     print(vuln['ip'], f'has {len(vuln["vulns"])} vulnerabilities')

    # Found top 10 most vulnerable CVEs
    cves = {}
    for vuln in vulns:
        for cve in vuln['vulns']:
            if cve not in cves:
                cves[cve] = 1
            else:
                cves[cve] += 1
    sorted_cves = sorted(cves.items(), key=lambda x: x[1], reverse=True)
    for cve in sorted_cves[:10]:
        print(cve)

if __name__ == "__main__":
    main()