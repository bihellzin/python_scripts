#!/usr/bin/env python3

from subprocess import check_output

cpu_output = check_output(['sensors']).decode("utf-8").split("\n")[3:9]
gpu_output = check_output(['nvidia-smi']).decode("utf-8").split("\n")[9]


for i in cpu_output:
  print(i)

print("GPU:           +{}.0°C  (high = +90.0°C, crit = +120.0°C)".format(gpu_output[8:10]))