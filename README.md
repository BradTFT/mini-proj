# Mini projects that im using to learn and problem solve (i guess)

**When errors occur, i will be placing them here with an explanation for the prob and solution**
**also may be used to log changes or other things idk**

## error 1:
4.25.22: attempting to learn to make webscrapers. bs4 and requests were getting error "reportMissingModuleSource". after some reading on many forums, i came across this: (https://exerror.com/import-flask-could-not-be-resolved-from-source-pylance/). it states to check your venv root. turns out vscode thinks i am in a venv when the venv was in a different directory so all installs went to other venv.

## error 2:
4.28.22: <br />
error code:<br />

making a webscraper from a tutorial, finding prices on a webpage. getting this traceback call:
```
Traceback (most recent call last):

  File "/home/user/randomcode/scraping/scraper.py", line 13, in <module> 
    parent = prices[0].parent
IndexError: list index out of range
```
**SOLVED** see lines 19-23 in webscraping.py


## error 3:
4.29.22:<br />
i moved files into folders so they would be more organized and git decided that it needs to track every file in the dir EVEN THOUGH THEY ARE GITIGNORED. not yet sure what i should do becuase i have recreated the gitignore file and nothing has changed.

**SOLVED:**<br />
so it turns out im not very smart and when i moved the files into their organized folders, i put gitignore in the github folder. but i realized after about an hour that gitignore only workings in the directory that its in. so it will only gitignore whats in the github folder. all fixed tho 

**ANOTHER THING:**<br />
after pushing the commit with the solved error 3 entry, i also realized that the README file needs to be outside of the github folder. so im just gonna delete the github folder and move everything out of it to the main dir.


4.30.22<br />
**Tomorrow I want to** figure out how to do custom bash commands and make them run so i dont have to remember/dig thru files for my venv command. this is a little side thing but i wanted to log it in this readme. not necciserrily related to this repo

## error 4
5.1.22 <br />
Git just asked me to auth and there was a ton of errors but i think its because the PAC i used to create the origin remote expired today. so i generated a new token and removed the old remote, made a new one, and its fixed. although it pushed all changes before i reset the remote so im not sure what caused it to push bc it was a pretty hard NO that it wasnt going to be pushed without auth. but its fixed. Ok so im pushing the commit to commit this file and its denying me to push. i think i can fix this with the PAC but im going to re-config all my user, ect. full error message at the end of this entry. command line git does not like me right now but i think vscode version control tab will let me thru. ok so vscode tab lets me push without error but command line is forcing me to enter all this stuff. its whatever ill figure it out soon.


**error output** (sorry if formatting is bad)
```
$ git push  <br />
Username for 'https://github.com': BradTFT
Password for 'https://BradTFT@github.com':  
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 558 bytes | 139.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/BradTFT/mini-proj.git
   6a92d29..98c159a  main -> main 
```


**FIXED FOR THE MOMENT** <br />

I followed this stackoverflow thread and reset the remote using this command (git remote set-url origin https://(token)@github.com/(username)/(repo)). for now it works to push to git from command line. at the moment i dont see any other issues with git command line.





## error 5: <br /> 
**5.2.22** <br />
I solved the inital issue on the webscraper.py file but i have run into another issue. i run the script and i get this error
```
line 31, in <module> 
    items = div.find_all(text=re.compile(gpu)) 
AttributeError: 'NoneType' object has no attribute 'find_all' 
```

currently on the lookout for the solution to this problem