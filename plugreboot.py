#!/usr/bin/env python3

import json
import requests

##########################################################################
# A Python3 program to manipulate the plugs on a WTI Power type of Device
# For more information on the RESTful API please refer to this location
# https://www.wti.com/t-wti-restful-api-download.aspx
##########################################################################

# supress Unverified HTTPS request, only do this is a verified environment
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Address of the WTI device
URI = "https://"
SITE_NAME = "rest.wti.com"
BASE_PATH = "/api/v2/config/powerplug"

# username and password to your WTI device
USERNAME = "restpowerpublic"
PASSWORD = "restfulpassword"

# plugs to change, to enter more than one comma seperate i.e. 1,2,3,4
PLUGS = "1"

# valid ACTION: boot, on, off
ACTION = "boot"

print("\n\nWTI Plug Reboot Test program")
print("----------------------------\n")

tempdata = input("Enter URI [default: %s ]: " % (URI))
if (len(tempdata) > 0):
	URI = tempdata

tempdata = input("Enter SITE_NAME [default: %s ]: " % (SITE_NAME))
if (len(tempdata) > 0):
    SITE_NAME = tempdata

tempdata = input("Enter USERNAME [default: %s ]: " % (USERNAME))
if (len(tempdata) > 0):
    USERNAME = tempdata

tempdata = input("Enter PASSWORD [default: %s ]: " % (PASSWORD))
if (len(tempdata) > 0):
    PASSWORD = tempdata

tempdata = input("Enter Plugs to control [default: %s ]: " % (PLUGS))
if (len(tempdata) > 0):
    PLUGS = tempdata

tempdata = input("Enter ACTION [default: %s ]: " % (ACTION))
if ((len(tempdata) > 0) and ((tempdata == "boot") or (tempdata == "on") or (tempdata == "off"))):
    ACTION = tempdata

allplugsarray = PLUGS.split(",")

payloadtext = ""
for SinglePlug in allplugsarray:
    if (len(payloadtext) > 0):
        payloadtext = ("%s, " % (payloadtext))
    payloadtext = ("%s{\"plug\": \"%s\", \"state\": \"%s\"}" % (payloadtext, SinglePlug, ACTION))

print("Username: %s" % (USERNAME))
print("Password: %s" % (PASSWORD))
print("Payload: %s" % (payloadtext))

try:
    print("Contacting: %s%s%s" % (URI, SITE_NAME, BASE_PATH))
    headersJSON = {'content-type': 'application/json'}

    r = requests.post(URI+SITE_NAME+BASE_PATH, auth=(USERNAME, PASSWORD), data=payloadtext, verify=False, headers=headersJSON)

    if (r.status_code == 200):
        parsed_json = r.json()

        print ("JSON return: %s" % (parsed_json))

        statuscode = parsed_json["status"]["code"][0]

        if (int(statuscode) != 0):
            exit(1)

        # how many plug data sets where returned in the JSON
        datapoints = int(parsed_json['plugdatacount'])

        tempdatapoints = 0

        while (tempdatapoints < datapoints):
            tempdata = parsed_json["powerplugs"][tempdatapoints]["plug"]
            print ("Plug Number: %s" % (tempdata))

            tempdata = parsed_json["powerplugs"][tempdatapoints]["plugname"]
            print ("Plug Name: %s" % (tempdata))

            tempdata = parsed_json["powerplugs"][tempdatapoints]["busy"]
            if (len(tempdata) > 0):
                if (int(tempdata) > 0):
                    print ("Busy: Yes [In the process of changing state]")
                else:
                    print ("Busy: No")

            statuscode = parsed_json["powerplugs"][tempdatapoints]["state"]
            print ("State: %s\n" % (statuscode))

            tempdatapoints += 1

    else:
        print(r.status_code)
        print(r.reason)

except requests.exceptions.RequestException as e:
    print (e)
