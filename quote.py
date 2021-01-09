#!/usr/bin/env python3

from datetime import datetime as dt
from pprint import pprint
from string import Template

import requests

QUOTE_URL = "https://favqs.com/api/qotd"

def get_quote():
    resp = requests.get(QUOTE_URL).json()["quote"]
    qdct = {"quote": resp["body"], "author": resp["author"]}
    with open("template.html", "r") as f:
        tmpl = Template(f.read())
    text = f'{resp["body"]}\n - {resp["author"]}'
    html = tmpl.substitute(qdct)
    qdct |= {"html": html, 
             "text": text, 
             "email": {"subj": "you've got a quote!", "plain": text, "html": html}
            }
    return qdct

if __name__ == "__main__":  # Local testing
    pprint(get_quote())
