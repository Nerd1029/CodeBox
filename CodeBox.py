import json

print("Welcome to CodePit! You can use this program to package your Python files in just a few seconds!")

filename = input("What's your file's name? ")
requirements = input("What does your file require to run? (make sure to seperate each one with a comma) ")
version = input("What version is your file currently in? (ie 0.1) ")
author = input("Who is the author of your file? (if there are multiple, they must be comma seperated) ")

data = {
    "name": filename,
    "install_requires": requirements,
    "py_modules": [filename],
    "version": version,
    "author": author
}

print("Generating file... ")

with open(f"{filename}.json", "w") as f:
    json.dump(data, f, indent=4)

print("File generated!")