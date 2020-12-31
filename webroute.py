import requests
import os
a = open("wordlist.txt", "r")
b = a.readlines()
c = len(b)
d = open("wordlist.txt", "r")
for i in range(c):
    e = d.readline()
    f = e[0:len(e)-1]
    print(f)
    g = requests.get("https://uditsingh.com/"+f)
    print("https://uditsingh.com/"+f)

    g.text
