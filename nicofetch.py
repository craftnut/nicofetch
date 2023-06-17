# -*- coding: utf-8 -*-

import os
import sys
import psutil
from argparse import ArgumentParser

import platform_fetches

# launch args
parser = ArgumentParser()
parser.add_argument("--skip-platform", action="store_true")
parser.add_argument("--platform-only", action="store_true")
args = parser.parse_args()

# ANSI escape codes:
class colors:
    blue = "\033[94m"
    red = "\033[91m"
    end = "\033[0m"
    
print("----------------------")
    
# first, fetch platform-specific details:
if not args.skip_platform:
    if sys.platform == "linux":
        platform_fetches.fetch_linux()
    elif sys.platform == "win32":
        platform_fetches.fetch_windows()
    elif "freebsd" in sys.platform:
        platform_fetches.fetch_freebsd()
    else:
        print("Currently unsupported platform.")

# then, fetch universal non-specific details:
if not args.platform_only:
    res = f"{os.get_terminal_size().columns}x{os.get_terminal_size().lines}"
    mem = int((psutil.virtual_memory()[0])*(1/1048576))
    mem_used = int((psutil.virtual_memory()[3])*(1/1048576))
    mem_usage = psutil.virtual_memory()[2]

    print(f"{colors.blue}Terminal Size:{colors.end}", res)
    print(f"{colors.blue}Memory:{colors.end}", str(mem_used) + "MiB /", str(mem) + "MiB", "(" + str(mem_usage) + "%)")

print("----------------------")