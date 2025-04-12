import json

username = input("What is your username? ")

social_stuff = ""

with open("posts.txt", "r") as f:
    print(f.read(), "\n")

print("Welcome to CodeBox! You can use this program to package your files in just a few seconds! It's also a place where devs can post their work and get feedback!")

action_choice = input("What would you like to do?\nA: Package a file\nB: Access the dev community\nEnter your choice's letter here (this is case-sensitive): ")

if action_choice == "A":
    filename = input("What's your file's name? ")
    requirements = input("What does your file require to run? (make sure to seperate each one with a comma) ")
    version = input("What version is your file currently in? (ie 0.1) ")
    author = input("Who is the author of your file? (if there are multiple, they must be comma seperated) ")
    filetype = input("What language was your file written in? ")

    data = {
        "name": filename,
        "install_requires": requirements,
        "py_modules": [filename],
        "version": version,
        "filetype": filetype,
        "author": author
    }

    print("Generating file...")

    with open(f"{filename}.json", "w") as f:
        json.dump(data, f, indent=4)

    print("File generated!")

elif action_choice == "B":
    with open("posts.txt", "r") as f:
        print(f.read(), "\n")

    postchoice = input("Would you like to post something? (y/n) ")
    if postchoice == "y":
        post = input("Enter your post here: ")

        social_stuff += f"{username} posted: {post}\n"
        with open("posts.txt", "a") as f:
            f.write(social_stuff)
    
    with open("posts.txt", "r") as f:
        print(f.read())
    
    if postchoice == "n":
        print("Thanks for using CodeBox! Bye!!!")