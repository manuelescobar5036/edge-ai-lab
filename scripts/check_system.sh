#!/bin/bash

echo "===== DEVICE INFO ====="
echo "Hostname: $(hostname)"
echo "Date: $(date)"
echo "Uptime: $(uptime -p)"
echo "IP: $(hostname -I)"

echo ""
echo "===== OS ====="
cat /etc/os-release | head -n 5

echo ""
echo "===== CPU ====="
lscpu | head -n 15

echo ""
echo "===== MEMORY ====="
free -h

echo ""
echo "===== DISK ====="
df -h

echo ""
echo "===== TEMPERATURE ====="
if [ -f /sys/class/thermal/thermal_zone0/temp ]; then
  temp=$(cat /sys/class/thermal/thermal_zone0/temp)
  echo "$((temp/1000)) °C"
else
  echo "Temperature file not found"
fi
