#!/usr/bin/env python3

from subprocess import check_output

def get_output_list(command: str, *args) -> list:
  command_line = []
  command_line.append(command)

  for arg in args:
    command_line.append(arg)

  return check_output(command_line).decode("utf-8").split("\n")


if __name__ == "__main__":
  cpu_output = get_output_list("sensors")[3:9]
  gpu_output = get_output_list("nvidia-smi")[9]
  nvme_output = get_output_list("sudo", "nvme", "smart-log", "/dev/nvme0n1")[2]

  print("+-------------------------------------------------------------+")
  for i in cpu_output:
    print("|  {i}  |".format(i=i))
  print("|=============================================================|")
  print("|  GPU:           +{}.0°C  (high = +90.0°C, crit = +120.0°C)  |".format(gpu_output[8:10]))
  print("|  NVMe:          +{}.0°C  (high = +70.0°C, crit = + 70.0°C)   |".format(nvme_output[38:40]))

  print("+-------------------------------------------------------------+")
