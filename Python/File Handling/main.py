from pathlib import Path

def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}. {items}")


def createfile():
    try:
        readfileandfolder()
        name=input("Enter the name of the file: ")
        p=Path(name)
        if not p.exists() and p.is_file():
            with open(p,"w") as fs:
                data=input("Enter the data to write to the file: ")
                fs.write(data)

            print(f"File '{name}' created successfully.")
        else:
            print(f"File '{name}' already exists.")

    except Exception as err:
        print(f"Error: {err}")


def readfile():
    try:
        readfileandfolder()
        name=input("Enter the name of the file to read: ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data=fs.read()
                print(f"Contents of '{name}':\n{data}")
        else:
            print(f"File '{name}' does not exist.")

    except Exception as err:
        print(f"Error: {err}")


def update():
    try:
        readfileandfolder()
        name=input("Enter the name of the file to write to: ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,"a") as fs:
                data=input("Enter the data to write to the file:")
                fs.write(data)

            print(f"File '{name}' updated successfully.")
        else:
            print(f"File '{name}' does not exist.")

    except Exception as err:
        print(f"Error: {err}")


def deletefile():
    try:
        readfileandfolder()
        name=input("Enter the name of the file to delete: ")
        p=Path(name)
        if p.exists() and p.is_file():
            p.delete()

        print(f"File '{name}' deleted successfully.")
    except Exception as err:
        print(f"Error: {err}")



print("Press 1 to create a new file.")
print("Press 2 to read a file.")
print("Press 3 to update a file.")
print("Press 4 to delete a file.")

check=int(input("Enter your response: "))
name=input("Enter the name of the file: ")
readfileandfolder()

if check==1:
    createfile()

elif check==2:
    readfile()

elif check==3:
    update()
    
elif check==4:
    deletefile()
    



