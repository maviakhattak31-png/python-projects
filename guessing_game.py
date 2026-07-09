import random

target=random.randint(1,100)
while True:
    person=(input("guess the target or quit(Q):"))
    if(person=="Q"):
        break
        
    person=int(person)
    if(target==person):
        print("succees: correct guess!!")
        break
    elif(target<person):
        print("wrong guess pick a small number")
    elif(target>person):
        print("wrong guess pick a big number")
    
    
print( "_____game over_____")      
    
