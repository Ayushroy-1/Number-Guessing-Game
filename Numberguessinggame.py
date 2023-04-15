import random

def game(comp,user):
    if user>comp:
        print("Guess a lower number")
        
    elif user<comp:
        print("Guess a higher number")
        
    elif user==comp:
        print("comp choses",comp)
        print("You Guess it correct") 
        
        
        
    
while True:
    i=0
    a=input("Enter 'end' to end the game or press enter to continue\t")
    if a=="end":
        print("Game is end")
        break
    else:
        print("Welcome to number guessing game")
        comp=random.randint(1,100)
        
    
        while True:
            i+=1
            user=int(input("Input the numbers between 1 to 100:-\t"))
            if comp!=user:
        
                print("You entered",user)
                
                game(comp,user)       
                
            else:
                game(comp,user)
                print("Thank you")
                print("You take",i, "attempts to guess the number")
                
                
                break
        
