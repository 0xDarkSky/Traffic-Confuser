#!/usr/bin/env python3
# path to your python3 ^
import os
import time
import os.path
from os import path
import sys
import random
import argparse

#####################################
###   The code might be a little  ###
###     messy because 2 coders    ###
###      are editing it lol,       ###
###      so feel free to          ###
###        optimize it            ###
#####################################


try:
    import requests as req
except ImportError:
    print('\nMissing dependencies!\nInstalling requests module...') if input(
        "Install requests module? Y/n\n").lower() == 'y' else sys.exit("Can't run the script without requests module!")
    os.system("pip3 install requests")

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


class Confuser:
    def __init__(self):  # used
        self.parser = argparse.ArgumentParser()
        self.arguments()
        self.args = self.parser.parse_args()

        self.sleeps = 0
        self.count = 0

        self.start_time = time.time()

    def arguments(self):  # used
        self.parser.add_argument('--pace', '-p', help="Set the pace", type=str)
        self.parser.add_argument('--_global', '-g', help='call it from anywhere', action='store_true')

    def super_type(self, b):  # used
        for a in b:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.03)

    def web_check(self):
        if path.exists("sample.txt"):
            pass
        else:
            self.super_type("File sample.txt is missing. Creating file...")
            with open("sample.txt", 'a') as Q:
                Q.write(
                    "https://whatsapp.com\nhttps://vimeo.com\nhttps://mozilla.org\nhttps://linkedin.com\nhttps"
                    "://microsoft.com\nhttps://www.blogger.com\nhttps://apple.com\nhttps://www.reddit.com\nhttps"
                    "://www.github.com\nhttps://www.youtube.com\nhttps://www.facebook.com\nhttps://www.google.com"
                    "\nhttps://www.weather.com\nhttps://www.cnn.com\nhttps://www.twitter.com\nhttps://www.wikipedia"
                    ".org\nhttps://www.quora.com\n")
            self.super_type("\n\nFile created.\n")

    def run_anywhere(self):
        self.super_type("Making it global")

        os.system("sudo cp Traffic-Confuser.py /usr/local/bin")
        os.system("sudo chmod +x /usr/local/bin/Traffic-Confuser.py")
        os.system("sudo mv /usr/local/bin/Traffic-Confuser.py /usr/local/bin/Traffic-Confuser")
        self.super_type("Now you can run it anywhere by typing: Traffic-Confuser")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        self.decide()

    def file_check(self):
        if path.exists("CodeCheck"):
            pass
        else:
            print(LICENSE)
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.super_type("License check is a one time thing.\n")
            with open("CodeCheck", 'a') as f:
                f.write(
                    "\n\n-- Please don't delete me, I'm just a simple check for the Traffic-Confuser.py.py code, "
                    "I don't take "
                    "much space :) --")

    def start_status(self):
        print(logo)
        self.super_type("Started...\n\n")

    def decide(self):
        if self.args._global:
            self.run_anywhere()
        if self.args.pace.lower() == 'slow':
            self.sleeps = float(random.randint(5, 20))
        elif self.args.pace.lower() == 'fast':
            self.sleeps = float(random.randint(0, 5))
        else:
            sys.exit(
                self.super_type("Wrong input!"))

    def send(self):
        with open("sample.txt") as f:
            content = f.readlines()
            content_done = [x.strip() for x in content]
            split_content = random.choice(content_done)
            resp = req.get(split_content)
            self.decide()

            if resp.status_code == 200:
                print("Success - " + split_content)
            else:
                print("Fail - " + split_content)

    def main(self):
        while True:
            try:
                self.send()
                self.count += 1
                time.sleep(self.sleeps)

            except KeyboardInterrupt:
                secs = int((time.time() - self.start_time))
                if secs < 60:
                    self.super_type(f"\nSent {self.count} requests in " + "%s seconds." % secs)
                if secs > 60:
                    self.super_type(
                        f"\nSent {self.count} requests in {str(int(secs / 60))}mins")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                exit(0)


if __name__ == '__main__':
    c = Confuser()
    c.web_check()
    c.file_check()
    c.start_status()
    c.decide()
    c.main()
