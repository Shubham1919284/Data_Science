import random
import string
import json
from pathlib import Path


class Bank:
    database='C:\\Users\\sk191\\Desktop\\DS\\Python\\BANK_MANAGEMENT\\data.json'
    data=[]

    @classmethod
    def _load_data(cls):
        try:
            if Path(cls.database).exists():
                with open(cls.database, encoding='utf-8') as fs:
                    content = fs.read().strip()
                    cls.data = json.loads(content) if content else []
            else:
                print("Database file not found. Creating a new one.")
        except Exception as err:
            print(f"Error occurred while reading database: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w', encoding='utf-8') as fs:
            json.dump(cls.data, fs, indent=4)

    def __init__(self):
        self._load_data()
        print("Welcome to the Bank Management System")
        print("press 1 to create a new account")
        print("press 2 for deposit money in your account")
        print("press 3 for withdraw money from your account")
        print("press 4 for details in your account")
        print("press 5 for updating your account details")
        print("press 6 for deleting your account")
        # if Bank.data:
        #     print(type(Bank.data[0].get('age')))


    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spcha=random.choices("!@#$%&^*",k=1)
        id=alpha+num+spcha
        random.shuffle(id)
        return ''.join(id)



    


    def create_account(self):
        data={
            "name":input("Enter your name: "),
            "age":int(input("Enter your age: ")),
            "email":input("Enter your email: "),
            "account_number":Bank.__accountgenerate(),
            "balance":0,
            "pin":int(input("Enter your pin: "))
        }
        l=len(str(data['pin']))
        if data['age'] < 18 or l != 4:
            print("Invalid age or pin. Age must be 18 or older and pin must be 4 digits.")
        else:
            Bank.data.append(data)
            Bank.__update()
            print("Account created successfully!")
            for i in data:
                print(f"{i}: {data[i]}")
            print("Please note down your account number and pin for future reference.")

        Bank.data.append(data)

        Bank.__update()


    def depositmoney(self):
        print("Please enter your account number and pin to deposit money.")
        accnumber=input("Enter your account number: ")
        pin=int(input("Enter your pin: "))

        userdata=[i for i in Bank.data if i['account_number']==accnumber and i['pin']==pin]

        if not userdata:
            print("Invalid account number or pin. Please try again.")

        else:
            amount=int(input("Enter the amount to deposit: "))
            if amount>=10000:
                print("Deposit limit exceeded. You can only deposit up to 10,000 at a time.")
            elif amount<0:
                print("Invalid amount. Please enter a positive value.")
            else:
                print(userdata)
                print(f"Depositing {amount} to your account.")
                userdata[0]['balance']+=amount
                Bank.__update()
                print(f"Deposit successful! Your new balance is: {userdata[0]['balance']}")


    def withdrawmoney(self):
            print("Please enter your account number and pin to withdraw money.")
            accnumber=input("Enter your account number: ")
            pin=int(input("Enter your pin: "))
    
            userdata=[i for i in Bank.data if i['account_number']==accnumber and i['pin']==pin]
    
            if not userdata:
                print("Invalid account number or pin. Please try again.")
    
            else:
                amount=int(input("Enter the amount to withdraw: "))
                if userdata[0]['balance']<amount:
                    print("Insufficient balance.")
                elif amount<0:
                    print("Invalid amount. Please enter a positive value.")
                else:
                    print(userdata)
                    print(f"Withdrawing {amount} from your account.")
                    userdata[0]['balance']-=amount
                    Bank.__update()
                    print(f"Withdrawal successful! Your new balance is: {userdata[0]['balance']}")


    def userdetails(self):
        print("Please enter your account number and pin to view your account details.")
        accnumber=input("Enter your account number: ")
        pin=int(input("Enter your pin: "))
        userdata=[i for i in Bank.data if i['account_number']==accnumber and i['pin']==pin]

        if not userdata:
            print("Invalid account number or pin. Please try again.")

        else:
            print(f"\n\n{userdata}")
            print("Account details:")
            for i in userdata[0]:
                print(f"{i}: {userdata[0][i]}")


    def update_account(self):
        print("please enter your account number and pin to update your account details.")  
        accnumber=input("Enter your account number: ")
        pin=int(input("Enter your pin: "))
        userdata=[i for i in Bank.data if i['account_number']==accnumber and i['pin']==pin]

        if not userdata:
            print("Invalid account number or pin. Please try again.")

        else:
            print("You cannot change Age, Account number and pin. You can only change your name and email.")

            print("Enter the new details you want to update. Leave blank if you don't want to change a field.")

            newdata={
                "name":input("Enter your new name: "),
                "email":input("Enter your new email: "),
                "pin":input("Enter your new pin: ")
            }

            if userdata["name"]=="":
                newdata["name"]=userdata[0]["name"]

            if userdata["email"]=="":
                newdata["email"]=userdata[0]["email"]

            if userdata["pin"]=="":
                newdata["pin"]=userdata[0]["pin"]

            newdata['Age']=userdata[0]['age']
            newdata['account_number']=userdata[0]['account_number']
            newdata['balance']=userdata[0]['balance']

            if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin'])

            for i in newdata:
                if userdata[0][i]==newdata[i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]

            Bank.__update()
            print("Account details updated successfully!")


    def delete_account(self):
        print("Please enter Your account number and pin to delete your account.")
        accnumber=input("Enter your account number: ")
        pin=int(input("Enter your pin: "))

        userdata=[i for i in Bank.data if i['account_number']==accnumber and i['pin']==pin]

        if not userdata:
            print("Invalid account number or pin. Please try again.")
        else:
            check=input("Are you sure you want to delete your account? This action cannot be undone. (y/n): ")
            if check=='n' or check=='N':
                print("Account deletion cancelled.")
            else:
                Bank.data.remove(userdata[0])
                Bank.__update()
                print("Account deleted successfully!")



    

user=Bank()
check=int(input("Enter your response: "))
if check==1:
    user.create_account()

elif check==2:
    user.depositmoney()

elif check==3:
    user.withdrawmoney()

elif check==4:
    user.userdetails()

elif check==5:
    user.update_account()

elif check==6:
    user.delete_account()