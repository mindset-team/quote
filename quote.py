#!/usr/bin/env python3

# dev branch

from datetime import datetime as dt
from pprint import pprint
from string import Template

import requests

QUOTE_URL = "https://api.quotable.io/random"


def get_quote():
    resp = requests.get(QUOTE_URL).json()
    qdct = {"quote": resp["content"], "author": resp["author"], "utc_time": f"{dt.utcnow().isoformat()[:-7]}Z"}
    with open("template.html", "r") as f:
        tmpl = Template(f.read())
    text = f'{qdct["quote"]}\n - {qdct["author"]}'
    html = tmpl.substitute(qdct)
    qdct |= {
        "html": html,
        "text": text,
        "email": {
            "subject": "you've got a quote!",
            "plain": text,
            "html": html,
        },
    }
    return qdct

def dev_branch_demo():
    return "demo"

if __name__ == "__main__":  # Local testing
    pprint(get_quote())
