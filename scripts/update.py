import os
import sys
import requests

def get_new_joke():
    information = requests.get(url="https://icanhazdadjoke.com/", headers= {"Accept":"application/json"})
    result = information.json()
    new_joke = result["joke"]
    return new_joke

if __name__ == "__main__":
    new_joke = get_new_joke()
    nlines = new_joke.count('\n')
    while (nlines != 0):
        new_joke = get_new_joke()
        nlines = new_joke.count('\n')
    joke_signature = "😂 {} - {}".format(new_joke, os.getenv("ISSUE_USER_LOGIN", "icanhazdadjoke"))
    read_readme_file = open('README.md', 'r') 
    lines = read_readme_file.readlines()
    old_joke = lines[-1]
    write_readme_file = open('README.md', 'w')
    for line in lines:
        if line != old_joke:
            write_readme_file.write(line)
    write_readme_file.write(joke_signature)
    append_previous_file = open('archive/PREVIOUS.md', 'a')
    append_previous_file.write('\n')
    append_previous_file.write(old_joke)