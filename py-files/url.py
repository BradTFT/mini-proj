
#!basic url shortener
import pyshorteners

link = input("")
shorteners = pyshorteners.Shortener()
shortlink = shorteners.tinyurl.short(link)
print(shortlink)