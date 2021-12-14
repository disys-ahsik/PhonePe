import random
import math
import sys



contacts = {"Amma":9952853238,"Sheik":9442030861,"Yasin":9150148146,
            "Dawoud":6382421835,"Suhail":7945217876,"abshal":9745831987,
            "Mufa":9553311754,"Bahubali":9987647581,"Babu":9987784538,
            "Deepan":9911560926,"Gokul":8547654908,"Nela":9813232145}
class phonepe :

    def __init__(self):
        self.pay=input ("Enter The Person Name : ")

    def payment(self):

        if self.pay.isalpha():
            keychecker=contacts.keys()
            if self.pay in keychecker :
                paymentconfirmation()
            else:
                conts=input("Do You Want To Add New Contact yes/no?")
                if conts=='yes':
                    newpayment()
                else:
                    sys.exit()
                    
def paymentconfirmation():
    amount=int(input("Enter the Amount :"))
    key=otpgen()
    print("\n")
    value=int(input("Enter The Received OTP:"))
    print("\n")
    if key==value:
        print("                       Transaction Successfully Paid %d RS"%amount)
        print("\n")
        cont=input("Do You Want To Continue yes/no?")
        print("\n")
        if cont=='yes':
            menu()
        else:
            print("Bye")
            sys.exit()
    else:
        print("  Transaction Failed    ")
        print("\n")
        j=input("Do You Want To Continue yes/no?")
        print("\n")
        if j=='yes':
            menu()
        else:
            print("""    Bye            """)
            sys.exit()      

            
def otpgen(): 
    otp=""
    digits="0123456789"

    for i in range(6):
        otp=otp+digits[math.floor(random.random()*10)]

    print("The OTP is:",otp)

    return (int(otp))
        
def newpayment(): 
    upiid=input("Enter The Name:")
    phonenumber=input("Enter Your Phone Number:")
    if len(phonenumber)==10:
        contacts[upiid]=int(phonenumber)
    else:
        raise ValueError("Invalid Number")
    print("\n")
    menu()            

def mycontacts(): 
    for i,j in contacts.items():
        print("         ",i," : ",j)

    print("\n")
    menu()

def menu():  
    print("""
    1.Pay
    2.New Payment
    3.My Contacts
    4.Exit App
    """)
    pref=int(input("Select the Menu :"))
    print("\n")
    if pref==1:
        pay=phonepe()
        pay.payment()
    elif pref==2:
        newpayment()
    elif pref==3:
        mycontacts()
    elif pref==4:
        print("""                 Bye                           """)
        sys.exit()


menu()
