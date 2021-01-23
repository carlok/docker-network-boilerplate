# pylint: disable=C0111, E0401
""" API Entry Point """

import json

import hug
import urllib3

http = urllib3.PoolManager()

@hug.get("/", output=hug.output_format.html)
def base():
    return "<h1>hello from ck_kis_companies</h1>"


@hug.get("/add", examples="num=1")
def add(num: hug.types.number = 1):
    return {"res" : num + 1}