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


class TrafficConfuser:
    def __init__(self):
        ## I put it here to always clean screen when using the class
        os.system("cls" if os.name == "nt" else "clear")

    ## changed variable name to something clearer
    def super_type(self, text_to_type):
        for text_character in text_to_type:
            sys.stdout.write(text_character)
            sys.stdout.flush()
            time.sleep(0.03)

    def root_check(self):
        ## didn't work on windows - added a bypass
        if sys.platform == "win32" or not hasattr(os, "geteuid"):
            return True
        else:
            self.sudo_check = os.geteuid() == 0

        if self.sudo_check == True:
            raise ValueError("Sudo check failed!")
        else:
            self.super_type("Run script as root! (Only for the first time)\n")
            exit()

    def web_check(self):
        if path.exists("sample.txt") == False:
            self.super_type("File sample.txt is missing. Creating file...")

            ## added context manager - more pythonic
            ## changed variable name to something clearer
            with open("sample.txt", "a") as sample_file:
                sample_file.write(
                    "https://whatsapp.com\nhttps://vimeo.com\nhttps://mozilla.org\nhttps://linkedin.com\nhttps://microsoft.com\nhttps://www.blogger.com\nhttps://apple.com\nhttps://www.reddit.com\nhttps://www.github.com\nhttps://www.youtube.com\nhttps://www.facebook.com\nhttps://www.google.com\nhttps://www.weather.com\nhttps://www.cnn.com\nhttps://www.twitter.com\nhttps://www.wikipedia.org\nhttps://www.quora.com\n"
                )
            self.super_type("\n\nFile created.\n")

    def run_anywhere(self):
        self.super_type(
            "Do you want to copy the file to /usr/local/bin? This will let you run the code from any directory by typing Traffic-Confuser. Don't do it if you're on Windows or Termux because it won't work."
        )
        ch = input("\nY/n? ")
        if "y" == ch.lower():
            os.system("mv traffic-confuser.py Traffic-Confuser")
            os.system("cp Traffic-Confuser /usr/local/bin")
            self.super_type("Now you can run it anywhere by typing: Traffic-Confuser")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
        if "n" == ch.lower():
            ## don't understand this yet but single pass is bad
            pass

    def file_check(self):
        if path.exists("CodeCheck"):
            x = os.stat("CodeCheck")
            age = time.time() - x.st_mtime
            if age > 356029.69091153145:
                self.super_type(
                    "\nYou should check the repository https://github.com/QL0R/Traffic-Confuser, the files might be outdated.\n"
                )
                time.sleep(2)
                pass
        else:
            print(LICENSE)
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            self.root_check()
            self.super_type("License check is a one time thing.\n")

            ## added context manager - more pythonic
            ## changed variable name to something clearer
            with open("CodeCheck", "a") as check_file:
                check_file.write(
                    "\n\n-- Please don't delete me, I'm just a simple check for the Traffic-Confuser.py code, I don't take much space :) --"
                )
            self.run_anywhere()

    def start_status(self):
        print(logo)
        self.super_type("Started...\n\n")

    def send_stuff(self):
        with open("sample.txt") as input_file:
            url_list = input_file.readlines()
            url_list_done = [element.strip() for element in url_list]
            split_url_list = random.choice(url_list_done)
            resp = req.get(split_url_list)
            if resp.status_code == 200:
                print("Success - " + split_url_list)
            else:
                print("Fail - " + split_url_list)
            sleepr = random.randint(10, 30)
            sleeper = float(sleepr)
            time.sleep(sleeper)


if __name__ == "__main__":
    confuser = TrafficConfuser()
    count = 0
    confuser.web_check()
    confuser.file_check()
    confuser.start_status()

    while True:
        try:
            count += 1
            confuser.send_stuff()
        except KeyboardInterrupt:
            confuser.self.super_type(f"\nSent {count} requests.")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            exit()
