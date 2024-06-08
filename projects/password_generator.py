#password generator
import string
import random

if __name__ =="__main__":
    s1 = string.ascii_lowercase
    
    s2 = string.ascii_uppercase
    
    s3 = string.digits
    
    s4 = string.punctuation

    password_lenth = int(input("Enter password length:\n"))   
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    #print(s)
    print("Your password is:")
    print("".join(random.sample(s,password_lenth)))
    # We can also use thisprint statement to print the generated password -----print("".join(s[0:password_lenth]))