# Traffic-Confuser

![traffic](https://user-images.githubusercontent.com/84932430/131347411-0c05b0d6-c062-42b9-ac55-c85913d939e5.jpg)


**Python script** to send **random HTTP requests**, to *hide* your traffic and **confuse your ISP/VPN**. Your web traffic will be cheaper to sell and useless for ads. Your traffic will look weird and hard to identify, what you browse and are interested in.

![traffic-confuser](https://user-images.githubusercontent.com/84932430/126857034-96fc345b-7d71-403b-b1fd-63af2860585b.GIF)


Libraries to install: `pip install requests`, `pip install termcolor`

How to install the project: `git clone https://github.com/QL0R/Traffic-Confuser.git`

Usage: `python3 Traffic-Confuser.py`

You can edit the sample.txt file to other websites you want.

Support on **Linux** (The code would work on Windows and MAC as well if you edit it that way. I might make a **Windows version** in the *future* !)

# How does it work?

Basically it sends HTTP requests to random websites, the websites are stored in the `sample.txt` file, (you can add more websites in it, modify it). The script chooses what website to open randomly,
the time periods betweeen requests are also random: 
you can set it to be slower/faster ex.: `random.randint(20,50)` for fast (not recommended since some websites might block you) or `random.randint(40,180)` for slow, looks more realistic (recommended).

You can run it in the background on your daily browsing.

There's like a million of most used websites in the `sample.txt` file lol

*Note: give it a try running it again if you encounter any errors.*

# Author: 0xDarkSky
