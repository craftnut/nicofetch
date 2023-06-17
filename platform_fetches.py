import os
import platform
from time import strftime
from time import gmtime

class colors:
    blue = "\033[94m"
    red = "\033[93m"
    end = "\033[0m"
    
user = os.getlogin()

system = platform.uname()[0]
machine = platform.uname()[4]

def fetch_linux():
    import subprocess
    import distro

    linux_distro = distro.id().capitalize()
    linux_version = distro.version()

    shell = os.environ['SHELL']

    hostname = platform.uname()[1]
    kernel = platform.uname()[2]

    with open('/proc/uptime', 'r') as f:
        uptime = int(float(f.readline().split()[0]))
        up_hours = int(strftime("%H", gmtime(uptime)))
        up_minutes = int(strftime("%M", gmtime(uptime)))
        

    print(user + "@" + hostname)
    print("----------------------")
    print(f"{colors.blue}OS:{colors.end}", linux_distro, system, machine)
    print(f"{colors.blue}Version:{colors.end}", linux_version)
    print(f"{colors.blue}Kernel:{colors.end}", kernel)
    print(f"{colors.blue}Uptime:{colors.end}", up_hours, "Hours,", up_minutes, "Minutes")
    print(f"{colors.blue}Shell:{colors.end}", shell)
    
    cpu_info = subprocess.check_output("cat /proc/cpuinfo", shell=True).decode().strip()
    for line in cpu_info.split("\n"):
        if "model name" in line:
            cpu_model = line,1
        if "vendor_id" in line:
            cpu_vendor = line,1  

    print(f"{colors.blue}CPU:{colors.end}", str(cpu_model).strip(repr("('model name\t: ")).strip("', 1)"))
    print(f"{colors.blue}CPU Vendor:{colors.end}", str(cpu_vendor).strip(repr("('vendor_id\t: ")).strip("', 1)"))
    
def fetch_windows():
    
    import ctypes
    
    lib = ctypes.windll.kernel32
    uptime = lib.GetTickCount64()
    up_hours = int(strftime("%H", gmtime(int(str(uptime)[:-3]))))
    up_minutes = int(strftime("%M", gmtime(int(str(uptime)[:-3]))))
    
    release = platform.uname()[2]
    version = platform.uname()[3]
    
    cpu = platform.processor()
    
    print(f"{colors.blue}OS:{colors.end}", system, release, machine)
    print(f"{colors.blue}Version:{colors.end}", version)
    print(f"{colors.blue}Uptime:{colors.end}", up_hours, "Hours,", up_minutes, "Minutes")
    print(f"{colors.blue}CPU:{colors.end}", cpu)

def fetch_freebsd():
    
    import subprocess
    
    release = platform.uname()[2]
    version = platform.uname()[3]
    
    cpu = platform.processor()
    
    print(f"{colors.blue}OS:{colors.end}", system, release, machine)
    print(f"{colors.blue}Version:{colors.end}", version)
    print("Uptime:", subprocess.check_output("uptime"))
    print(f"{colors.blue}CPU:{colors.end}", cpu)