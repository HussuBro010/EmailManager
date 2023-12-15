import pyfiglet
import inquirer
import json

title = pyfiglet.figlet_format("Email Manager", font="digital")
print(title)

def addEmail(label: str, email: str, pswd: str):
    dataDict = {label:{"Email": email, "Password": pswd}}
    f = open(f"emailDatas/{label}.json", "a")
    f.write(json.dumps(dataDict, indent=4))



while True:
    modeOptionsInquirer = [
        inquirer.List(
            'modes',
            message="Select a mode",
            choices=['Add Email', 'Delete Email', 'Edit Email', 'Quit']
        )
    ]

    modes = inquirer.prompt(modeOptionsInquirer)

    if modes['modes'] == 'Add Email':
        label = input('Name: ')
        email = input('Email: ')
        password = input('Password: ')
        print("\n\n")

        addEmail(label, email, password)
    if modes['modes'] == 'Quit':
        break
