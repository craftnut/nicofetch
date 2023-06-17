# -*- coding: utf-8 -*-
# Nicofetch: The Universal Fetch Script

import os
import sys
import psutil
from argparse import ArgumentParser

import platform_fetches

import math

parser = ArgumentParser()
parser.add_argument("--skip-platform", action="store_true")
parser.add_argument("--platform-only", action="store_true")
args = parser.parse_args()

user = os.getlogin()

class colors:
    blue = "\033[94m"
    red = "\033[91m"
    end = "\033[0m"
    
# if the user is on linux print related system details first
if not args.skip_platform:
    if sys.platform == "linux":
        platform_fetches.fetch_linux()
    elif sys.platform == "win32":
        platform_fetches.fetch_windows()
    elif sys.platform == "freebsdN":
        platform_fetches.fetch_freebsd()
    else:
        print("Currently unsupported platform.")

# universal  details, should work for every platform
if not args.platform_only:
    res = f"{os.get_terminal_size().columns}x{os.get_terminal_size().lines}"
    mem = math.ceil((psutil.virtual_memory()[0])/(1024**3))
    mem_usage = psutil.virtual_memory()[2]

    print(f"{colors.blue}Terminal Size:{colors.end}", res)
    print(f"{colors.blue}RAM:{colors.end}", str(mem) + "gb")
    print(f"{colors.blue}RAM Usage:{colors.end}", str(mem_usage) + "%")