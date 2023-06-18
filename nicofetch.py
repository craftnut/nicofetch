# -*- coding: utf-8 -*-

import os
import sys
import psutil
from argparse import ArgumentParser

import platform_fetches
import shutil

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
    
    disk_space = int((shutil.disk_usage('/')[0])*(9.313225*(10**-10)))
    disk_usage = round((shutil.disk_usage('/')[1])*(9.313225*(10**-10)), 2)
    
    disk_percent = (round(((int(disk_usage)/disk_space)*100), 2))

    print(f"{colors.blue}Disk (/):{colors.end} {disk_usage}GiB / {disk_space}GiB ({disk_percent}%)")
    print(f"{colors.blue}Memory:{colors.end} {mem_used}MiB / {mem}MiB ({mem_usage}%)")
    print(f"{colors.blue}Terminal Size:{colors.end} {res}")

print("----------------------")