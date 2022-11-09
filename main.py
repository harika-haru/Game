import random
import math

user_wins=0
pc_wins=0

choices=["r","p","s"]

for i in range (0,100):

    

        user_input=input("Enter your choice r (for rock), p (for paper), s (for scissors)")

        pc_input=choices[random.randint(0,2)]
        print("pc input :",pc_input)



        if user_input==pc_input:
            print("play again ,its a draw")
        
        elif user_input=="r" and pc_input=="s" :
            print("You won")
            user_wins+=1
        elif user_input=="s" and pc_input=="p" :
            print("You won")
            user_wins+=1
        elif user_input=="p" and pc_input=="r" :
            print("You won")
            user_wins+=1
        else:
            print("PC won")
            pc_wins+=1
    
            if user_wins==10 or pc_wins ==10:
                break

print("User score :",user_wins)
print("PC score :",pc_wins)

if user_wins > pc_wins:
    print("You Won, CONGRATULATIONS")
if user_wins < pc_wins:
    print("You Lost, Better Luck Next Time")

