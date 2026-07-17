import os
import subprocess
import platform
import socket
import psutil
import json
import time
from pathlib import Path

def get_temperature():
    path = Path("/sys/class/thermal/thermal_zone0/temp")
    if path.exists():
        return round(int(path.read_text().strip()) / 1000, 2)
    return None

def get_ip():
    interfaces = ["eth0", "enP8p1s0"]
    result = subprocess.check_output(
        ["ip", "-4", "addr", "show"]
    ).decode()
    for line in result.splitlines():
        for interface in interfaces:
            if interface in line:
                if "inet " in line:
                    return line.strip().split()[1].split("/")[0]
    raise RuntimeError("unknwon IP address")


def get_board_info():
    try:
        with open("/proc/device-tree/model") as f:
            return f.read().strip("\x00")
    except FileNotFoundError:
        pass


def get_os_info():
    os_info = {"platform": "unknown",
               "distro": "unknown"}
    os_info["platform"] = platform.system()
    if os_info["platform"] == "Linux":
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("PRETTY_NAME="):
                    os_info["distro"] = line.strip().split("=")[1].strip('"')
    return os_info

def get_cpu_info():
    cpu_info = {"processor": "unknown",
            "architecture": "unknown"}
    output = subprocess.check_output(["lscpu"]).decode()
    for line in output.splitlines():
        if "Architecture:" in line:
            cpu_info["architecture"] = line.split(":")[1].strip()
        elif "Model name:" in line:
            cpu_info["processor"] = line.split(":")[1].strip()
    return cpu_info


os_info = get_os_info()
cpu_info = get_cpu_info()

info = {
    "hostname": socket.gethostname(),
    "ip": get_ip(),
    "device": get_board_info(),
    "os platform": os_info["platform"],
    "os distro": os_info["distro"],
    "processor": cpu_info["processor"],
    "architecture": cpu_info["architecture"],
    "cpu_count": psutil.cpu_count(),
    "ram_gb": round(psutil.virtual_memory().total / (1024**3), 2),
    "ram_percent": psutil.virtual_memory().percent,
    "temperature_c": get_temperature(),
    "timestamp": time.time()
}

print(json.dumps(info, indent=2))
