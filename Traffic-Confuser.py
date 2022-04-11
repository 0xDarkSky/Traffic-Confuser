#!/usr/bin/python3
#your python location ^

try:
   import os, math, time, sys, random, requests as req
   import os.path
   from os import path
   from termcolor import colored
except ModuleNotFoundError:
   print("Some modules might not be installed (termcolor, requests). Would you like to install them? Y/n")
   modules = input("")
   if modules == "y":
      print("Installing modules...")
      os.system("pip install termcolor")
      os.system("pip install requests")
      print("Run the program again.")
      exit()
   else:
      print("Exitting.")
      exit()

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

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4369.0 Safari/537.36"}

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
       Q.write("https://whatsapp.com\nhttps://vimeo.com\nhttps://mozilla.org\nhttps://linkedin.com\nhttps://microsoft.com\nhttps://www.blogger.com\nhttps://apple.com\nhttps://www.reddit.com\nhttps://www.github.com\nhttps://www.youtube.com\nhttps://www.facebook.com\nhttps://www.google.com\nhttps://www.weather.com\nhttps://www.cnn.com\nhttps://www.twitter.com\nhttps://www.wikipedia.org\nhttps://www.quora.com\nhttps://duckduckgo.com\n")
       Q.close()
       super_type("\n\nFile created.\n")


def file_check():
    if path.exists("CodeCheck"):
       pass
    else:
       print(colored(f"{LICENSE}", "red"))
       time.sleep(3)
       os.system('cls' if os.name == 'nt' else 'clear')
       root_check()
       super_type("License check is a one time thing.\n")
       f = open("CodeCheck", "a")
       f.write("\n\n-- Please don't delete me, I'm just a simple check for the Traffic-Confuser.py code, I don't take much space :) --")
       f.close()

try:
   usr_input = sys.argv[1]
except IndexError:
   super_type("Wrong input!\nUsage: specify slow or fast, ex.: python3 traffic-confuser.py slow\n")
   exit()

def start_status():
    print(colored(f"{logo}", "magenta"))
    super_type(colored("Started...\n\n", "yellow"))

def arg():
    if usr_input.lower() == "slow":
       sleeper = random.randint(85,600)
       sleeps = float(sleeper)
       time.sleep(sleeps)
    if usr_input.lower() == "fast":
       sleeper = random.randint(15,35)
       sleeps = int(sleeper)
       time.sleep(sleeps)

def text_stuff():
       with open("sample.txt") as f:
            INFO = colored("Success - ", "green")
            FAILINFO = colored("Failure - ", "red")
            content = f.readlines()
            content_done = [x.strip() for x in content]
            split_content = random.choice(content_done)
            resp = req.get(split_content, headers=headers)
            arg()
            if resp.status_code == 200:
               print("[INFO] " + INFO + split_content)
            else:
               print("[INFO] " + FAILINFO + split_content)

count = 0

def send_count():
       secs = int((time.time() - start_time))
       if secs < 60:
          super_type(f"\nSent {count} requests in " + "%s seconds." % (secs))
       if secs > 60:
          calc = secs / 60
          mins = int(calc)
          super_type(f"\nSent {count} requests in {mins} minutes.\n")
          print("")
       exit()

web_check()
file_check()
start_status()
start_time = time.time()

while True:
    try:
       count += 1
       if count == 100:
          end_count()
       if usr_input.lower() == "slow":
          text_stuff()
       if usr_input.lower() == "fast":
          text_stuff()
    except KeyboardInterrupt:
       send_count()
       time.sleep(2)
       os.system('cls' if os.name == 'nt' else 'clear')
