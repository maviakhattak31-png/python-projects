import random  
import string 

pass_len=8
character_val= string.ascii_letters + string.digits + string.punctuation
password=""
for i in range(pass_len):
    password+=random.choice(character_val)
print("my password is:",password)
