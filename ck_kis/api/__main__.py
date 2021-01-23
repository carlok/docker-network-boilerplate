# pylint: disable=C0111, E0401
""" API Entry Point """

import json

import hug
import urllib3

http = urllib3.PoolManager()

@hug.get("/", output=hug.output_format.html)
def base():
    return "<h1>hello from ck_kis</h1>"


@hug.get("/remote")
def remote():
    r = http.request(
        'GET',
        'http://ck_kis_companies_nginx/add',
        fields={'num': 2}
    )

    if r.status == 200:
        return json.loads(r.data.decode('utf-8'))
    else:
        return json.loads({})
