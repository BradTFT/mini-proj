getfirst = input("Enter your first name. >>> ")
getlast = input("Enter your last name. >>> ")
getcomp = input('Enter your company name >>> ')
getdot = input('Which domain would you like: \n.com \n.org \n.net? \n>>> ')
com = '.com'
net = '.net'
org = '.org'
string = getfirst.lower() + '.' + getlast.lower() + '@' + getcomp.lower() 

if getdot == 'com' or getdot == '.com':
    print(string + com)
elif getdot == 'net' or getdot == '.net':
    print(string + net)
elif getdot == 'org' or getdot == '.org':
    print(string + org)
    