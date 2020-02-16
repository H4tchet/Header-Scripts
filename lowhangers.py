import requests
import sys
import webbrowser
from colorama import Fore

headers = sys.argv[1]
url = sys.argv[1]
response = requests.get(headers)

def verboseHeaders():
    print(Fore.GREEN + "Verbose Headers:")

if "Server" in response.headers:
	print(Fore.GREEN + "Server: " + response.headers['Server'])
else:
    print(Fore.RED + "No Server Header")
if "X-Powered-By" in response.headers:
	print(Fore.GREEN + "X-Powered-By:" + response.headers['X-Powered-By'])
if "X-AspNet-Version" in response.headers:
    print(Fore.GREEN + "X-AspNet-Version" + response.headers['X-AspNet-Version'])
if "X-AspNetMvc-Version" in response.headers:
    print(Fore.GREEN + "X-AspNetMvc-Version" + response.headers['X-AspNetMvc-Version'])
else:
    pass

def securityHeaders():
    if "X-XSS-Protection" in response.headers:
        print(Fore.GREEN + "[+]	XSS header is present")
    else:
        print(Fore.RED + "[-]	XSS header is not present")

    if "x-frame-options" in response.headers:
        print(Fore.GREEN + "[+]	X-Frame header is present")
    else:
        print(Fore.RED + "[-]	X-Frame header is not present")

    if "x-content-type" in response.headers:
        print(Fore.GREEN + "[+]	X-Content-Type header is present")
    else:
        print(Fore.RED + "[-]	C-Content-Type header is not present")

    if "Public-Key-Pins" in response.headers:
        print(Fore.GREEN + "[+]	Public-Key-Pins is present")
    else:
        print(Fore.RED + "[-]	Public-Key-Pins header is not present")

    if "X-Content-Type-Options" in response.headers:
        print(Fore.GREEN + "[+]	X-Content-Type-Options is present")
    else:
        print(Fore.RED + "[-]	X-Content-Type-Options header is not present")

    if "X-Permitted-Cross-Domain-Policies" in response.headers:
        print(Fore.GREEN + "[+]	X-Permitted-Cross-Domain-Policies is present")
    else:
        print(Fore.RED + "[-]	X-Permitted-Cross-Domain-Policies header is not present")

    if "Content-Security-Policy" in response.headers:
        print(Fore.GREEN + "[+]	Referrer-Policy is present")
    else:
        print(Fore.RED + "[-]	Referrer-Policy header is not present")

    if "Content-Security-Policy" and "X-Content-Type-Options" not in response.headers:
	    print(Fore.RED + "\n[!] Site may be vulnerable to Clickjacking")
    if "X-XSS-Protection" not in response.headers:
	    print(Fore.RED + "\n[!] Check site with XSS payloads")
    print(Fore.GREEN + "\nCompleted")


def headerCheck():
#    webbrowser.open_new(url)
    webbrowser.open_new("https://securityheaders.com/?q=" + url + "&hide=on")

def sslChecks():
    webbrowser.open_new_tab("https://www.ssllabs.com/ssltest/analyze.html?d=" + url + "&hideResults=on")

headerCheck()
verboseHeaders()
securityHeaders()
sslChecks()
