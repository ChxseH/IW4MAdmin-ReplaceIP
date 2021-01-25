#!/usr/bin/env python3

# Make Update-Public-IP.bat a task schedule for 1 am or something.
#
# What: Replaces first key (and every instance after) in IW4MAdminSettings.json's "IPAddress" 
#     with whatever content is in Documents\IP.txt
#
# Example:
# "IPAddress": "123.456.789.123",
# into
# "IPAddress": "99.88.123.456",
#
# This *won't* modify other IPs, only the first one it will replace. 
# If you have multiple IPs ["123.123.123.123", "456.456.456.456", "127.0.0.1"]
# It'll only pick up the first one, and replace that throughout.
# This is useful since I *do* host game servers on 127.0.0.1 of that box & don't want it to be replaced.
#

# Variables, feel free to change me.
iw4madminconfig="C:\\IW4MAdmin\\Configuration\\IW4MAdminSettings.json" # IW4MAdmin Settings.
ipfile="C:\\Users\\user\\Documents\\IP.txt" # Should ONLY contain an IP. Example: 123.456.789.123



# Don't change unless you know what you're doing.
list=[]
myfile = open(iw4madminconfig, "rt")
contents = myfile.read()
ip1 = open(ipfile, "rt")
ip = ip1.read()

def lines_that_contain(string, fp):
    return [line for line in fp if string in line]
    
with open(iw4madminconfig, "r") as fp:
    for line in lines_that_contain("IPAddress", fp):
        newline=line[20:]
        newline2=newline[:(len(newline))-3]
        break

reading_file = open(iw4madminconfig, "r")
new_file_content = ""
for line in reading_file:
  stripped_line = line.strip()
  new_line = stripped_line.replace(newline2, ip)
  new_file_content += new_line +"\n"
reading_file.close()
writing_file = open(iw4madminconfig, "w")
writing_file.write(new_file_content)
writing_file.close()
myfile.close()
ip1.close()
fp.close()
