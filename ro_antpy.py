## AntenaPlay - RO
## Problem shown : Token isn't site specific.
## Issue replica

# CASE 1 = Basic usage
# Import Flask, BS and request (from urllib)
# re is for case 2
import urllib
from bs4 import BeautifulSoup
import urllib.request as rq
from flask import Flask, request, redirect
import re

app = Flask(__name__)

# Flask encapsulation
@app.route("/ro_antpy", methods=['GET'])
def home():
    # Making a realistic request (not using urllib useragent)
    req = urllib.request.Request(
        "https://radiozu.ro/live",
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    # Get Radio Zu page, one of the only websites that got a public livestream
    page = rq.urlopen(req)

    # Invoke BS4 and parse page
    soup = BeautifulSoup(page, 'html.parser')

    # Get source
    data = soup.find_all("source")
    print(data)

    # Extract link and test
    link = data[0]['src']

    # This should work
    return redirect(link)


# CASE 2 = Changing host via query parameters and regular expression (out of normal usage)

@app.route("/ro_antpy_case2", methods=['GET'])
def antena_issue():
    # Making a realistic request (not using urllib useragent)
    req = urllib.request.Request(
        "https://radiozu.ro/live",
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    if not request.args:
        return "No argument recieved"
    else:
        args = request.args

        # Get Radio Zu page, one of the only websites that got a public livestream
        page = rq.urlopen(req)

        # Invoke BS4 and parse page
        soup = BeautifulSoup(page, 'html.parser')

        # Get source
        data = soup.find_all("source")
        print(data)

        # Extract link and test
        link = data[0]['src']

        # Replace channel with another one from the AntenaPlay list
        replaced = re.sub('zurtv', args.get('channel'), link)

        # This should work
        return redirect(replaced)


# Launching flask app
if __name__ == '__main__':
    app.run(threaded=False, port=5000)