import requests
import csv
import contextlib
import os

print("""
 __   __  _____  _     _ _______ _     _ ______  _______     _______ _     _ _______ _______ _     _ _______  ______
   \_/   |     | |     |    |    |     | |_____] |______ ___ |       |_____| |______ |       |____/  |______ |_____/
    |    |_____| |_____|    |    |_____| |_____] |______     |_____  |     | |______ |_____  |    \_ |______ |    \_
                                                                                                                    
                               ______  __   __                                                                      
                               |_____]   \_/                                                                        
                               |_____]    |                                                                         
                                                                                                                    
                          _______ _______ _______  ______  ______ __   __             _____   ______ ______         
                          |______    |    |_____| |_____/ |_____/   \_/   ___ |      |     | |_____/ |     \        
                          ______|    |    |     | |    \_ |    \_    |        |_____ |_____| |    \_ |_____/        
                                                                                                                   
""")

try:
    f = open('wordlist.csv','r')
    f.close()
except FileNotFoundError:
    url = 'https://docs.google.com/spreadsheets/d/1ozg1Cnm6SdtM4M5rATkANAi07xAzYWaKL7HKxyvoHzk/gviz/tq?gid=674179785&tqx=out:csv'
    r = requests.get(url)
    wordlist = open('wordlist.csv', 'w')
    wordlist.write(r.text)
    wordlist.close()
    print("list downloaded")
finally:
    print("wordlist check done :3")

print("""
Usage: python3 youtubechecker.py

Description: Run the title or description text of your Youtube video through the list to better anticipate demonetization.

Note: to update the list use "rm wordlist*" and rerun.
""")

try:
    f = open("wordlist_clean","r")
    f.close()
except FileNotFoundError:
    with open("wordlist.csv", "r", newline="") as o :
        with open("wordlist_clean", "w") as f:
            reader = csv.reader(o, delimiter=",")
            with contextlib.redirect_stdout(f):
                for row in reader:
                    print(row[0])

    #print('wordlist_clean created successfully')
finally:
    print("wordlist cleanup check done :3")

# input

inpuT = input('Input your title or description here : ')
i = inpuT.split(' ')

# compare

badword_list = open('wordlist_clean').read().splitlines()

flag = 0
for word in i:
    if (word in badword_list) == True:
        print(word)
        #print("Change your words!")
        flag = 1
    elif word not in badword_list:
        flag = flag

if flag == 0 :
    print("$$$ Yay, Youtube should pay! $$$")
    print("Such polite! :3")
else :
    print("Change your words!")
