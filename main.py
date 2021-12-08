'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#rock paper scissor game
print("rock paper scissor game")
import random
import math
computer_choice=random.choice(["r","p","s"])
n=int(input("enter no of times you want to play: "))
human_choice=[]
print("enter p for paper, s for scissor, r for rock")
for i in range(n):
   human_choice.append(input())
c_wins=0
h_wins=0
for i in range(n):
   if(human_choice[i]==computer_choice):
       c_wins+=1
       h_wins+=1
   elif((human_choice[i]=='r' and computer_choice=='s') or (human_choice[i]=='s' and computer_choice=='p') or (human_choice[i]=='p' and computer_choice=='r')):
       h_wins+=1
   else:
      c_wins+=1
if(h_wins>(n//2)):
   print("you win and your score is:",h_wins)
elif(h_wins==c_wins):
   print("it is a tie!!!")
else:
   print("you LOSE try again later, your points are:",h_wins )
   print("you loose by:",abs(h_wins-c_wins)," points.")
    
    
    


