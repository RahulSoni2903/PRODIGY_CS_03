from array import*
import string
import re
def Password_Checker(password):
    #checking password criteria
    n=len(password)
    number_case=any(char.isdigit() for char in password)
    upper_case=any(char.isupper() for char in password )
    lower_case=any(char.islower() for char in password)
    length_password= n>=8
    special_char=bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))


    #checking criteria
    criteria=sum([number_case,upper_case,lower_case,length_password,special_char])

    #allocation of password strength in this
    if criteria==5:
        print("your password level is:Strong(all possible criteria is full fill)")
    elif criteria==4:
        print("your password level is:Strong(4 Criteria fullfill out of 5 criteria)")
    elif criteria==3:
        print("your password level is:Middium(3 Criteria fullfill out of 5 Criteria)")
    elif criteria==2:
        print("your password level is:Low(2 Criteria fullfill out of 5 Criteria)")
    elif criteria==1:
        print("your password level is:VeryLow(only 1 criteria full fill out of 5 criteria)")
    

#main function 
print("Follow some criterials releted to strong password.")
print("1.Atleat password length must be >=8 character.")
print("2.Use Uppercase,Lowercase,Digit,Special characters in your password.")
print("3.Don't Use Seqancial Assecending Order or Seqancial Dessending Order Number,character etc.")
print("4.Don't Use Phon Number or Birthdate in your password.")
print("5.Unique for Each Account: Don't reuse passwords across multiple accounts.")
print("6.Enable 2FA in your Device.")
print("7.Change your password Periodically")
print("8. Avoid entering passwords on suspicious sites")

# get password from User
password=input("Enter your password in this")

#hide your password 
if len(password) > 2:
    masked_password = password[0] + '#' * (len(password) - 2) + password[-1]
else:
    masked_password = password

print("Entered password:-",masked_password)

Password_Checker(password)