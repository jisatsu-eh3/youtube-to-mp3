import os
import re

files = [f for f in os.listdir('.') if os.path.isfile(f)]

mp3s = [x for x in files if ".mp3" in x]

new_files = []
for f in range(len(mp3s)):
    #print(mp3s[f])
    #new_files =  re.sub(r'\(.*?\)', '', mp3s[f])
    new_file =  re.sub("[\(\[].*?[\)\]]", "", mp3s[f])
    new_file = new_file.replace('＂', '')
    new_file = new_file.replace('"', '')
    new_file = new_file.replace('Music Video', '')
    while " .mp3" in new_file:
        new_file = new_file.replace(" .mp3", ".mp3")

    new_files.append(new_file)

for i in range(len(mp3s)):

    print("Renaming " + mp3s[i] + "\n to \n" + new_files[i])
    os.rename(mp3s[i], new_files[i])