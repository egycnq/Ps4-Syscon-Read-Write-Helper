# *************************************************************************
# Syscon.py - Read-Write Ps4 Syscon helper Script
# You can use this script to read Sony Ps4 syscon and validate it also produce 512kb firmware after that.
# You Still need stock RL78 for flashing the firmware.
# special thanks to VVildCard777 - Fail0verflow - droogie - juansbeck -Zecoxao - M4j0r - SSL - msalau
# Copyright (C) 2021 RedTeam - egycnq https://twitter.com/egycnq
# *************************************************************************
import subprocess
import filecmp
import serial
import os
import re

def step2 () :
    raw_input("connect Syscon in read mode [check 'SYSGLITCH' Guide] and press any key when you are ready")
    ser = serial.Serial(com2, baudrate=115200, timeout=1)

    while 1:
        data = ser.read_all()
        f = open('syscon.bin', 'ab')
        data = str(data)
        f.write(data)
        f.close()
        print os.stat("syscon.bin").st_size
        if os.stat("syscon.bin").st_size >= 3094304:
            print "done"
            break
    f = open('syscon.bin', 'rb')
    data = f.read()
    pattern = "\x80\x01\xFF\xFF\xFF\xFF"
    regex = re.compile(pattern)
    asd = "syscon"
    for match_obj in regex.finditer(data):
        offset = match_obj.start()
        a = "{:02X}".format(offset)
        a = int(a, 16)
        hex_value = hex(a)
        hex_value = int(hex_value, 16)
        f.seek(hex_value, 0)
        data = f.read(0x80000)
        with open(asd, "wb") as outfile:
            outfile.write(data)
            asd = asd + "a"
    comp = filecmp.cmp("syscon", "syscona", shallow=False)
    if comp == False:
        print "\nError: check your connections Something Wrong"
        os.remove("syscon.bin")
        os.remove("syscon")
        os.remove("syscona")
        step2()

    subprocess.call(["srec_cat.exe", "syscon", "-binary", "-o", "syscon.srec", "-address-length=3"])
    os.rename("syscon.srec", "syscon.mot")
    os.remove("syscona")
    f.close()
    print "\nWell Done"
    start()


def step3():
    com3 = raw_input("Connect USB tty then enter Com (connect RL78 in write mode [check 'rl78flash' guide]")
    a = subprocess.call(["rl78flash.exe", "-i", "com3"])
    if a == 0:

            subprocess.call(["rl78flash.exe", "-ivvewc", com3,"syscon.mot"])
            print "done"

    else:
        print "Oh Nooooooo"
        step3()
    start()



def start():
    user_input = input("Enter 1 for Step 1 [read] \nEnter 2 for Step 2 [write]\n")
    if user_input == 1 :
        step2()
    elif user_input == 2 :
        step3()
    else :
        print "enter correct Input"
        start()

start()