#!/usr/bin/env python3
import math
import requests as req
import os
import time
import os.path
from os import path
import sys
import random
from datetime import datetime

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

def super_type(b):
    for a in b:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.03)

def web_check():
    if path.exists("sample.txt"):
       pass
    else:
       super_type("File sample.txt is missing. Creating file...")
       Q = open("sample.txt", "a")
       Q.write("https://whatsapp.com\nhttps://vimeo.com\nhttps://mozilla.org\nhttps://linkedin.com\nhttps://microsoft.com\nhttps://www.blogger.com\nhttps://apple.com\nhttps://www.reddit.com\nhttps://www.github.com\nhttps://www.youtube.com\nhttps://www.facebook.com\nhttps://www.google.com\nhttps://www.weather.com\nhttps://www.cnn.com\nhttps://www.twitter.com\nhttps://www.wikipedia.org\nhttps://www.quora.com\n")
       Q.close()
       super_type("\n\nFile created.\n")
    
def file_check():
    if path.exists("CodeCheck"):
       pass
    else:
       print(LICENSE)
       time.sleep(3)
       os.system('cls' if os.name == 'nt' else 'clear')
       super_type("License check is a one time thing.\n")
       f = open("CodeCheck", "a")
       f.write("\n\n-- Please don't delete me, I'm just a simple check for the Traffic-Confuser script, I don't take much space :) --")
       f.close()
            
def start_status():
    print(logo)
    super_type("Started...\n\n")
  
def send_stuff():
    with open("sample.txt") as f:
         content = f.readlines()
         content_done = [x.strip() for x in content]
         split_content = random.choice(content_done)
         resp = req.get(split_content)
         if resp.status_code == 200:
            print("Success - " + split_content)
         else:
            print("Fail - " + split_content)
         sleepr = random.randint(10,30) # edit this if you want it slower/faster
         sleeper = float(sleepr)
         time.sleep(sleeper)
        
count = 0
web_check()
file_check()
start_status()

while True:
    try:
       count += 1
       send_stuff() 
      
    except KeyboardInterrupt:
       super_type(f"\nSent {count} requests.")
       time.sleep(1)
       os.system('cls' if os.name == 'nt' else 'clear')
       exit()
