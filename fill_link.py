import re
import os

with open("input.txt", "r") as f:
    content = f.read()

rex = r"\[(.*?)\]\(\)"
matches = re.findall(rex, content)

for match in matches:
    print(match)
    url = input("Link:")
    content = content.replace("[{}]()".format(match), "[{}]({})".format(match, url))
    with open("input.txt", "w") as f:
      f.write(content)
    os.system("clear");