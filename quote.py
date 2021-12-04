#!/usr/bin/env python3

from datetime import datetime as dt
from pathlib import Path
from string import Template

import requests

QUOTE_URL = "https://api.quotable.io/random"


def get_quote():
    resp = requests.get(QUOTE_URL).json()
    qdct = {
        "quote": resp["content"],
        "author": resp["author"],
        "text": f'{resp["content"]}\n - {resp["author"]}',
        "utc_time": f"{dt.utcnow().isoformat()[:-7]}Z",
    }
    tmpl = Template(Path("template.html").read_text())
    qdct['html'] = tmpl.substitute(qdct)
    return qdct


if __name__ == "__main__":  # Local testing
    from pprint import pprint
    pprint(get_quote())
