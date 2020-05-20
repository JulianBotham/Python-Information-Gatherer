"""
INFO GATHERER
This program reaches out to ipinfo.io with a specified web address, requests information,
and then displays it to the user.
It provides the following info about the website to the user:
City
Region
Country
Location
Postal/Zip

"""

import sys
import requests
import socket
import json


if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)

req = requests.get("https://" + sys.argv[1])
print("\n" + str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])

print("\nThe IP address of " + sys.argv[1] + " is: " + gethostby_ + "\n")

#IPinfo.io API

req_two = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
resp_ = json.loads(req_two.text)

print("City: " + resp_["city"])
print("Region: " + resp_["region"])
print("Country: " + resp_["country"])
print("Location: " + resp_["loc"])
print("Postal: "+ resp_["postal"])



