import os

file_dir = os.path.dirname(os.path.realpath(__file__))
path_list = file_dir.split("\\")
path_list[7] = "New"
del path_list[-1]
final_path = "/".join(path_list[0:8])

os.chdir(final_path)


def create_dir():
    name = input("Please enter the name of the project: ")
    try:
        os.mkdir(name)
    except FileExistsError as F:
        print(F)
        create_dir()
    except WindowsError as W:
        print(W)
        create_dir()
    else:
        os.chdir(final_path + "/" + name)
        url = f"https://github.com/Ishaan-Datta/{name.replace(' ', '-')}.git"
        description = input("Please enter the description of the project: ")
        commands = [
            f'gh repo create "{name}" --private --description "{description}"',
            'echo "" >> "main.py"',
            f'echo "{description}" >> "README.md"',
            "git init",
            "git add .",
            'git commit -m "first commit"',
            "git branch -M main",
            f"git remote add origin {url}",
            "git remote -v",
            "git push -u origin main",
        ]

        for command in commands:
            os.system(command)


create_dir()

# always add option to do another project w/ Y or N
# change repositories to public?
# terminal command: create ProjectName
# python argparse, command line arguments for python
