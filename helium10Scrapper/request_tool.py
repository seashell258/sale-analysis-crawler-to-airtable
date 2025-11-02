import json
from .path import *
from .setting import H10_ACCOUNT_ID


BLACK_BOX_SEARCH_ID_REQ_ENDPOINT = (
    f"https://research-tools.helium10.com/api/blackbox/v1/search/products?"
)

ACC_ID_TO_AUTH_HEADER = {1546375935: "header01", 1546378525: "header02"}


def add_header(header_name, header_str):
    switch = 0
    header = {}
    last_key = ""
    for line in header_str.split("\n")[1:-1]:
        if switch == 0:
            header[line[:-1]] = ""
            last_key = line[:-1]
            switch = 1
        else:
            header[last_key] = line
            switch = 0

    f = open(HEADERS_DIR.joinpath(f"{header_name}.json"), "w")
    json.dump(header, f, indent=4)
    f.close()


def get_header(header_name="header01"):
    try:
        with open(HEADERS_DIR.joinpath(f"./{header_name}.json"), "r") as f:
            header = json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError("no such header")

    return header
