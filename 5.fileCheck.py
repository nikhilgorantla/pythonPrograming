# More Pythonic way of file checking 
#!/usr/bin/python3  

try:
    f = open("/etc/hosts")
    #go ahead and read the file 
except FileNotFoundError:
    print("no hostsfile")