#!/usr/bin/env python3
import requests as req
import os
import time
import os.path
from os import path
import sys
import random

LICENSE = """
MIT License

Copyright (c) 2021 QL0R

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contributors: QL0R

Licensed under the MIT License
"""


logo = """
░██████╗░██╗░░░░░░█████╗░██████╗░  ████████╗██████╗░░█████╗░███████╗███████╗██╗░█████╗░
██╔═══██╗██║░░░░░██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║██╔══██╗
██║██╗██║██║░░░░░██║░░██║██████╔╝  ░░░██║░░░██████╔╝███████║█████╗░░█████╗░░██║██║░░╚═╝
╚██████╔╝██║░░░░░██║░░██║██╔══██╗  ░░░██║░░░██╔══██╗██╔══██║██╔══╝░░██╔══╝░░██║██║░░██╗
░╚═██╔═╝░███████╗╚█████╔╝██║░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░██║░░░░░██║╚█████╔╝
░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░

         ░█████╗░░█████╗░███╗░░██╗███████╗██╗░░░██╗░██████╗███████╗██████╗░
         ██╔══██╗██╔══██╗████╗░██║██╔════╝██║░░░██║██╔════╝██╔════╝██╔══██╗
         ██║░░╚═╝██║░░██║██╔██╗██║█████╗░░██║░░░██║╚█████╗░█████╗░░██████╔╝
         ██║░░██╗██║░░██║██║╚████║██╔══╝░░██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗
         ╚█████╔╝╚█████╔╝██║░╚███║██║░░░░░╚██████╔╝██████╔╝███████╗██║░░██║
         ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
"""

os.system('cls' if os.name == 'nt' else 'clear')

def fast_type(z):
    for x in z:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.02)

def super_type(b):
    for a in b:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.06)

def slow_type(l):
    for o in l:
        sys.stdout.write(o)
        sys.stdout.flush()
        time.sleep(0.1)

def web_check():
    if path.exists("sample.txt"):
       pass
    else:
       super_type("File sample.txt is missing. Creating file...")
       Q = open("sample.txt", "a")
       Q.write("https://www.reddit.com\nhttps://www.github.com\nhttps://www.youtube.com\nhttps://www.facebook.com\nhttps://www.yahoo.com\nhttps://www.weather.com\nhttps://www.cnn.com\nhttps://www.twitter.com\nhttps://www.wikipedia.org\nhttps://www.quora.com\n")
       Q.close()
       super_type("\n\nFile created.\n")
      

def file_check():
    if path.exists("CodeCheck"):
       pass
    else:
       print(LICENSE)
       time.sleep(3)
       os.system('cls' if os.name == 'nt' else 'clear')
       super_type("License display is a one time thing!\n")
       f = open("CodeCheck", "a")
       f.write("\n-- Please don't delete me, I'm just a simple check for the code, I don't take much space :) --")
       f.close()
       

def start_status():
    print(logo)
    super_type("Started...\n\n")

def send_request():
    with open("sample.txt") as f:
         line = f.readlines()[0].rstrip()
         resp = req.get(line)
    if resp.status_code == 200:
       print("Success - " + line)
    else:
       print("Fail - " + line)

def send_request2():
    with open("sample.txt") as f:
         line = f.readlines()[1].rstrip()
         resp = req.get(line)
    if resp.status_code == 200:
       print("Success - " + line)
    else:
       print("Fail - " + line)

def send_request3():
    with open("sample.txt") as f:
         line = f.readlines()[2].rstrip()
         resp = req.get(line)
    if resp.status_code == 200:
       print("Success - " + line)
    else:
       print("Fail - " + line)

def send_request4():
    with open("sample.txt") as f:
         line = f.readlines()[3].rstrip()
         resp = req.get(line)
    if resp.status_code == 200:
       print("Success - " + line)
    else:
       print("Fail - " + line)

def send_request5():
    with open("sample.txt") as f:
         line = f.readlines()[4].rstrip()
         resp = req.get(line)
    if resp.status_code == 200:
       print("Success - " + line)
    else:
       print("Fail - " + line)

def send_request6():
    with open("sample.txt") as f:
         line = f.readlines()[5].rstrip()
         resp = req.get(line)
    if resp.status_code == 200:
       print("Success - " + line)
    else:
       print("Fail - " + line)

def send_request7():
    with open("sample.txt") as f:
         line = f.readlines()[6].rstrip()
         resp = req.get(line)
    if resp.status_code == 200:
       print("Success - " + line)
    else:
       print("Fail - " + line)

def send_request8():
    with open("sample.txt") as f:
         line = f.readlines()[7].rstrip()
         resp = req.get(line)
    if resp.status_code == 200:
       print("Success - " + line)
    else:
       print("Fail - " + line)

def send_request9():
    with open("sample.txt") as f:
         line = f.readlines()[8].rstrip()
         resp = req.get(line)
    if resp.status_code == 200:
       print("Success - " + line)
    else:
       print("Fail - " + line)

def send_request10():
    with open("sample.txt") as f:
         line = f.readlines()[9].rstrip()
         resp = req.get(line)
    if resp.status_code == 200:
       print("Success - " + line)
    else:
       print("Fail - " + line)

dic = [send_request, send_request2, send_request3, send_request4, send_request5, send_request6, send_request7, send_request8, send_request9, send_request10]

def non_random():
    random.choice(dic)()
    random.choice(dic)()
    random.choice(dic)()
    random.choice(dic)()
    random.choice(dic)()
    random.choice(dic)()
    random.choice(dic)()
    random.choice(dic)()
    random.choice(dic)()
    random.choice(dic)()

def true_random():
    a1 = (random.randint(0,3))
    a2 = (random.randint(0,3))
    a3 = (random.randint(0,3))
    a4 = (random.randint(0,3))
    a5 = (random.randint(0,3))
    a6 = (random.randint(0,3))
    a7 = (random.randint(0,3))
    a8 = (random.randint(0,3))
    a9 = (random.randint(0,3))
    a10 = (random.randint(0,3))
    random.choice(dic)()
    time.sleep(a1)
    random.choice(dic)()
    time.sleep(a2)
    random.choice(dic)()
    time.sleep(a3)
    random.choice(dic)()
    time.sleep(a4)
    random.choice(dic)()
    time.sleep(a5)
    random.choice(dic)()
    time.sleep(a6)
    random.choice(dic)()
    time.sleep(a7)
    random.choice(dic)()
    time.sleep(a8)
    random.choice(dic)()
    time.sleep(a9)
    random.choice(dic)()
    time.sleep(a10)

def true_random_slow():
    a1 = (random.randint(0,10))
    a2 = (random.randint(0,10))
    a3 = (random.randint(0,10))
    a4 = (random.randint(0,10))
    a5 = (random.randint(0,10))
    a6 = (random.randint(0,10))
    a7 = (random.randint(0,10))
    a8 = (random.randint(0,10))
    a9 = (random.randint(0,10))
    a10 = (random.randint(0,10))
    random.choice(dic)()
    time.sleep(a1)
    random.choice(dic)()
    time.sleep(a2)
    random.choice(dic)()
    time.sleep(a3)
    random.choice(dic)()
    time.sleep(a4)
    random.choice(dic)()
    time.sleep(a5)
    random.choice(dic)()
    time.sleep(a6)
    random.choice(dic)()
    time.sleep(a7)
    random.choice(dic)()
    time.sleep(a8)
    random.choice(dic)()
    time.sleep(a9)
    random.choice(dic)()
    time.sleep(a10)

count = 0
web_check()
file_check()
start_status()
while True:
    try:
       count += 10
       true_random() #you can switch to other modes by changing this function to another       

    except KeyboardInterrupt:
       super_type(f"\nSent about {count} requests.\n")
       os.system('cls' if os.name == 'nt' else 'clear')
       exit()
