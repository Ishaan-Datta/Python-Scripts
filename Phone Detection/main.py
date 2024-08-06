# import sys
# import subprocess
# import os

# IP_NETWORK = config("IP_NETWORK")
# IP_DEVICE = config("IP_DEVICE")

# proc = subprocess.Popen(["ping", IP_NETWORK], stdout=subprocess.PIPE)
# while True:
#     line = proc.stdout.readline()
#     if not line:
#         break
#     # the real code does filtering here
#     connected_ip = line.decode("utf-8").split()[3]

#     if connected_ip == IP_DEVICE:
#         subprocess.Popen(["say", "Linnea just connected to the network"])
#         # push notifications via FCM


# from re import findall
# from subprocess import Popen, PIPE


# def ping(host, ping_count):
#     for ip in host:
#         data = ""
#         output = Popen(f"ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")

#         for line in output.stdout:
#             data = data + line
#             ping_test = findall("TTL", data)

#         if ping_test:
#             print(f"{ip} : Successful Ping")
#         else:
#             print(f"{ip} : Failed Ping")


# nodes = ["8.8.8.8", "20.20.20.50", "facebook.com", "192.168.1.20"]

# ping(nodes, 3)

# dont necessarily need DHCP, just something to test what devices are connected, make list, figure out host names and if they fit under category, print they are currently here,
# update spreadsheet or smth, ping if they arrive or leave

# # importing subprocess
# import subprocess

# # getting meta data of the wifi network
# meta_data = subprocess.check_output(["netsh", "wlan", "show", "profiles"])

# # decoding meta data from byte to string
# data = meta_data.decode("utf-8", errors="backslashreplace")

# # splitting data by line by line
# # string to list
# data = data.split("\n")

# # creating a list of wifi names
# names = []

# # traverse the list
# for i in data:
#     # find "All User Profile" in each item
#     # as this item will have the wifi name
#     if "All User Profile" in i:
#         # if found split the item
#         # in order to get only the name
#         i = i.split(":")

#         # item at index 1 will be the wifi name
#         i = i[1]

#         # formatting the name
#         # first and last character is use less
#         i = i[1:-1]

#         # appending the wifi name in the list
#         names.append(i)

# # printing the wifi names
# print("All wifi that system has connected to are ")
# print("-----------------------------------------")
# for name in names:
#     print(name)
# from who_is_on_my_wifi import *

# WHO = who()  # who(n)
# for j in range(0, len(WHO)):
#     comm = (
#         f"\n{WHO[j][0]} {WHO[j][1]}\n{WHO[j][2]} {WHO[j][3]}\n{WHO[j][4]} {WHO[j][5]}\n"
#     )
#     print(comm)

# import subprocess

# results = subprocess.check_output(["netsh", "wlan", "show", "network"])
# results = results.decode("ascii")
# results = results.replace("\r", "")
# ls = results.split("\n")
# ls = ls[4:]
# ssids = []
# x = 0
# while x < len(ls):
#     if x % 5 == 0:
#         ssids.append(ls[x])
#     x += 1
# print(ssids)

import who_is_on_my_wifi

who_is_on_my_wifi.who()
# need to scan this shit
# Phone detect little ui with checks or exes for who is home
# Maybe npcap terminal commands and store/analyze output

# scan  bluetooth and wifi devices
# can use npcap with terminal commands 
# and use that to scan, output to csv file, read csv file and combine with data scrubbed from bluetooth detection

import bluetooth
import time


def scan_devices():
    devices = bluetooth.discover_devices(
        duration=8,
        lookup_names=True,
        device_id=-1,
        lookup_class=True,
        device_id=-1,
        device_name=None,
        device_class=None,
        device_services=None,
    )

    print("Scanning for Bluetooth devices...")
    if devices:
        print("\nFound devices:")
        for addr, name, _ in devices:
            print(f"  Address: {addr}")
            print(f"  Name: {name}")
            print("-" * 20)
    else:
        print("No Bluetooth devices found.")


if __name__ == "__main__":
    while True:
        scan_devices()
        print("\nWaiting for the next scan...")
        time.sleep(10)  # Adjust the sleep duration based on your preferences
