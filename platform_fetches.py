# -*- coding: utf-8 -*-

import os
import platform
from time import strftime
from time import gmtime

# ANSI escape codes:
class colors:
    blue = "\033[94m"
    red = "\033[91m"
    end = "\033[0m"
    
user = os.getlogin()

system = platform.uname()[0]
machine = platform.uname()[4]

# linux-specific fetch:
def fetch_linux():
    import subprocess
    import distro
    
    linux_distro = distro.id().capitalize()
    linux_version = distro.version()
    
    desktop = os.environ['XDG_CURRENT_DESKTOP']
    home = os.environ['HOME']
    shell = os.environ['SHELL']
    session = os.environ['XDG_SESSION_TYPE']
    
    if not "Budgie" in desktop:
        cur = os.environ['XCURSOR_THEME']
        cur_size = os.environ['XCURSOR_SIZE']
        desktop_session = os.environ.get('DESKTOP_SESSION')
        
        if 'wayland' in desktop_session:
            de = f"{desktop} {(desktop_session.replace('wayland', '').capitalize())}"
        else:
            de = f"{desktop} {desktop_session.capitalize()}"   
    
    hostname = platform.uname()[1]
    kernel = platform.uname()[2]

    # gets uptime by checking /proc/uptime file on linux
    with open('/proc/uptime', 'r') as f:
        uptime = int(float(f.readline().split()[0]))
        up_hours = int(strftime("%H", gmtime(uptime)))
        up_minutes = int(strftime("%M", gmtime(uptime)))
        
    print(f"{colors.red}{user}{colors.end}@{colors.red}{hostname}{colors.end}")
    
    print("----------------------")
    
    print(f"{colors.blue}OS:{colors.end} {linux_distro} {system} {machine}")
    
    if linux_version:
        print(f"{colors.blue}Version:{colors.end} {linux_version}")

    print(f"{colors.blue}Kernel:{colors.end} {kernel}")
    print(f"{colors.blue}Uptime:{colors.end} {up_hours} Hours, {up_minutes} Minutes")
    print(f"{colors.blue}Shell:{colors.end} {shell}")
    
    if not 'Budige' in desktop:
        print(f"{colors.blue}DE:{colors.end} {desktop}")
    else:
        print(f"{colors.blue}DE:{colors.end} {de}")
    
    if 'cur' in locals():
        print(f"{colors.blue}Cursor:{colors.end} {cur} ({cur_size}px)")
    
    print(f"{colors.blue}Session:{colors.end} {session}")
    
    # get cpu model and vendor
    cpu_info = subprocess.check_output("cat /proc/cpuinfo", shell=True).decode().strip()
    for line in cpu_info.split("\n"):
        if "model name" in line:
            cpu_model = line,1
        if "vendor_id" in line:
            cpu_vendor = line,1  

    print(f"{colors.blue}CPU:{colors.end}", str(cpu_model).strip(repr("('model name\t: ")).strip("', 1)"))
    print(f"{colors.blue}CPU Vendor:{colors.end}", str(cpu_vendor).strip(repr("('vendor_id\t: ")).strip("', 1)"))
    print(f"{colors.blue}Home Directory:{colors.end} {home}")
    
# win32-specific fetch:
def fetch_windows():
    
    import ctypes
    
    # gets uptime using windll.kernel32
    lib = ctypes.windll.kernel32
    uptime = lib.GetTickCount64()
    up_hours = int(strftime("%H", gmtime(int(str(uptime)[:-3]))))
    up_minutes = int(strftime("%M", gmtime(int(str(uptime)[:-3]))))
    
    release = platform.uname()[2]
    version = platform.uname()[3]
    cpu = platform.processor()
    
    userdomain = os.environ['USERDOMAIN']
    
    print(f"{colors.red}{user}{colors.end}@{colors.red}{userdomain}{colors.end}")
    
    print("----------------------")
    
    print(f"{colors.blue}OS:{colors.end} {system} {release} {machine}")
    print(f"{colors.blue}Version:{colors.end} {version}")
    print(f"{colors.blue}Uptime:{colors.end} {up_hours} Hours, {up_minutes} Minutes")
    print(f"{colors.blue}CPU:{colors.end} {cpu}") # should replace with way to get CPU model name

# freebsd-specific fetch:
def fetch_freebsd():
    
    import subprocess
    
    release = platform.uname()[2]
    version = platform.uname()[3]
    
    cpu = platform.processor()
    
    print(f"{colors.blue}OS:{colors.end} {system} {release} {machine}")
    print(f"{colors.blue}Version:{colors.end} {version}")
    print("Uptime:", subprocess.check_output("uptime")) # prints result of uptime command, doesn't look very good, should be replaced
    print(f"{colors.blue}CPU:{colors.end} {cpu}")