#!/usr/bin/python3
#Created by @TH3_4N5W3R

import os
from time import sleep
import pyshorteners


def banner():
    print("\033[93m--------------------------------------------")
    print("                 ADVURLHIDER                      ")
    print("   Hide custom URL for social engineering   ")
    print("                @TH3_4N5W3R                     ")
    print("--------------------------------------------")

def programm():
    os.system('clear')
    banner()
    print("\nEx:google.com")
    original_domain = str(input("\nInput a original domain. : "))

    os.system('clear') 
    
    banner()
    print("\nInput something that: new-video-in-youtube-this-is-a-perez-mascato")
    postlink = str(input("Postlink: "))

    os.system('clear')
    
    banner()
    url_to_short = str(input("Input URL to hidde:"))
    s = pyshorteners.Shortener()
    shorten=(s.dagd.short(f'{url_to_short}'))
    withoutprotocol = shorten[8:]
    
    os.system('clear')
    banner()
    print("Input URL you want to redirect without the scheme and domain \n that is without http://google.com")
    url_to_redirect = str(input("redirect link"))
    
    os.system('clear')
    banner()
    print(f"\033[95m\nYour link is: https://{original_domain}-{postlink}@{withoutprotocol}/{url_to_redirect}")


    defanother()
    

def defanother():
    another=str(input("\033[93m\nConvert another URL? (y/n): ")) 
    if another == "y":
        programm()

    elif another == "n":
        exit()

    else:
        print("Retry")
        sleep(3)
        os.system('clear')
        defanother()

programm()