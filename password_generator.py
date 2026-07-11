import random
import string

pass_len=int(input("password length:"))

symbol_choice=input("include symbols?(yes/no):")
if symbol_choice == "yes":
    character_val=string.ascii_letters + string.digits + string.punctuation
else:
    character_val = string.ascii_letters
        
password=""
for i in range(pass_len):
    password+=random.choice(character_val)
print("your password is:",password)
