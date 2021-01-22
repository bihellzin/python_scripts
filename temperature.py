#!/usr/bin/env python3

from subprocess import check_output

cpu_output = check_output(['sensors']).decode("utf-8").split("\n")[3:9]
gpu_output = check_output(['nvidia-smi']).decode("utf-8").split("\n")[9]
nvme_output = check_output(["sudo", "nvme", "smart-log", "/dev/nvme0n1"]).decode("utf-8").split("\n")[2]

print("+-------------------------------------------------------------+")
for i in cpu_output:
  print("|  {i}  |".format(i=i))
print("|=============================================================|")
print("|  GPU:           +{}.0°C  (high = +90.0°C, crit = +120.0°C)  |".format(gpu_output[8:10]))
print("|  NVMe:           +{}.0°C  (high = +70.0°C, crit = +70.0°C)  |".format(nvme_output[38:40]))

print("+-------------------------------------------------------------+")
