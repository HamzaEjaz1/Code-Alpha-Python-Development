import random
import string


print("Welcome to Radom Password generator ")

def PasssWord () :
    len = int(input("Enter the Lenght of Password : "))
    Num = string.digits
    L_Alpha = string.ascii_lowercase
    U_Alpha = string.ascii_uppercase
    Pun = string.punctuation
    Let = string.ascii_letters
    combine = Num + L_Alpha + U_Alpha + Pun + Let
    X = random.sample(combine, len)
    password = "".join(X)
    print(password)
    PasssWord()
PasssWord()
