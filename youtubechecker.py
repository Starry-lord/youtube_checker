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

# create local list
url = 'https://docs.google.com/spreadsheets/d/1ozg1Cnm6SdtM4M5rATkANAi07xAzYWaKL7HKxyvoHzk/gviz/tq?gid=674179785&tqx=out:csv'
r = requests.get(url)
wordlist = open('wordlist.csv', 'w')
wordlist.write(r.text)
wordlist.close()

print("""
Notes about the ***Youtube Demonetization Words*** List:
- Capitalization has no effect on monetization status
- This list is being updated periodically, and will change over time
- Some results are outdated, and might be inaccurate
- These results were tested in titles only. Descriptions and tags are less strict
- dashes (-) act the same way as spaces in compound words

The original list project is available here:
https://docs.google.com/spreadsheets/d/1ozg1Cnm6SdtM4M5rATkANAi07xAzYWaKL7HKxyvoHzk/edit#gid=1380702445

Usage: python3 youtubechecker.py

Description: Run the title or description text of your Youtube video through the list to better anticipate demonetization.


""")

with open("wordlist.csv", "r", newline="") as o :
    with open("wordlist_clean", "w") as f:
        reader = csv.reader(o, delimiter=",")
        with contextlib.redirect_stdout(f):
            for row in reader:
                print(row[0])

print('wordlist.csv and wordlist_clean created successfully!')

# input

inpuT = input('Input your title or description here : ')
i = inpuT.split(' ')

# compare

badword_list = open('wordlist_clean').read().splitlines()
#print(badword_list)

for word in i:
    if word in badword_list:
        print(word)

if any(bad in word for word in i for bad in badword_list):
    print("Change your words!")
else:
    print("$$$ Yay, Youtube should pay! $$$")
    print("such polite :3")

os.remove("wordlist.csv")
os.remove("wordlist_clean")

print("\nwordlist.csv and wordlist_clean removed :3")

