
#!basic url shortener
import pyshorteners

link = input("Link >>> ")
shorteners = pyshorteners.Shortener()
shortlink = shorteners.tinyurl.short(link)
print(shortlink)