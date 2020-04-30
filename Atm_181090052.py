
class Atm:
    def __init__(self,k, name=[], phone_no=[], balance=[], pin=[] ):

        self.name= name
        self.phone_no = phone_no
        self.balance = balance
        self.pin = pin
        self.k = int(k)

        username = str(input("Enter Your Name : "))
        for i in range(6):
            if username != self.name[i]:
                self.k += 1
            else:
                break


    def pin_verification(self):

        if self.k>6:
            print("User Not Found")
        else:
            i = 0
            flag = 1
            while i < 3:
                check_pin = int(input("Enter your pin : "))
                if check_pin == int(pin[self.k]):
                    flag = 1
                    break
                else:
                    i += 1
                    flag += 1

            if flag==1:
                print("Correct pin!!")
            else:
                print("Invalid User!!")


    def changepin(self):


        oldpin = int(input("Enter The old Password : "))
        if oldpin == int(self.pin[self.k]):
            newpin = int(input("Enter the new Password : "))
        else:
            print("Wrong Password !!")
        self.pin[self.k]= newpin
        print("New Password : ", self.pin[self.k])

    def AccountInfo(self):
        print("Name : ", self.name[self.k])
        print("Mobile Number : ", self.phone_no[self.k])
        print("Balance : ", self.balance[self.k])

    def MoneyGet(self):
        n = int(input("Enter the Amount to withdraw : "))
        self.balance[self.k] = int(self.balance[self.k]) - n
        print("Remaining Balance : ", self.balance[self.k])

    def MoneyPut(self):
        n = int(input("Enter the Amount to deposit : "))
        self.balance[self.k] = int(self.balance[self.k]) + n
        print("Balance : ", self.balance[self.k])


with open('try.txt', 'r') as document:
    answer = {}
    for line in document:
        line = line.split()
        if not line:  # empty line?
            continue
        answer[line[0]] = line[1:]
name=[]
phone_no=[]
balance=[]
pin=[]
for i in answer:
    name.append(i)
    balance.append(answer[i][0])
    phone_no.append(answer[i][1])
    pin.append(answer[i][2])
user = Atm(0,name,phone_no,balance,pin)

user.pin_verification()
x=0
while(x!=5):
    x = int(input("1 : To Change Pin\n2 : View Account Info\n3 : Withdraw Money\n4 : Deposit Money\n5 : Exit\n"))

    if x==1:user.changepin()
    elif x==2:user.AccountInfo()
    elif x==3:user.MoneyGet()
    elif x==4:user.MoneyPut()
    elif x==5:break



