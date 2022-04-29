# Mini projects that im using to learn and problem solve (i guess)

When errors occur, i will be placing them here with an explanation for the prob and solution


# error 1:
4.25.22: attempting to learn to make webscrapers. bs4 and requests were getting error "reportMissingModuleSource". after some reading on many forums, i came across this: (https://exerror.com/import-flask-could-not-be-resolved-from-source-pylance/). it states to check your venv root. turns out vscode thinks i am in a venv when the venv was in a different directory so all installs went to other venv.

# error 2:
4.28.22:
making a webscraper from a tutorial, finding prices on a webpage. getting this traceback call:
Traceback (most recent call last):

  File "/home/user/randomcode/scraping/scraper.py", line 13, in <module>
    parent = prices[0].parent
IndexError: list index out of range

fixes have **not** been determined yet.