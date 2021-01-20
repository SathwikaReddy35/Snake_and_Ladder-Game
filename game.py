import random
from tkinter import *
from PIL import ImageTk, Image
import time

root =Tk()
canv=Canvas(root,width=470,height=470,bg="white")
canv.grid(row=0,column=0)
img=ImageTk.PhotoImage(Image.open("snakeandladder.jpg"))
canv.create_image(0,0,anchor=NW,image=img)

print("Here's the \"SNAKE & LADDER\" game.\nAll the best for your Game with computer!")
end_pos=25

def dice_show(num):
    if(num==1):
        print(" _______")
        print("|       |")
        print("|   o   |")
        print("|_______|")
        return num
        
    if(num==2):
        print(" _______")
        print("|       |")
        print("|  o o  |")
        print("|_______|")
        return num
        
    if(num==3):
        print(" _______")
        print("|       |")
        print("| o o o |")
        print("|_______|")
        return num
        
    if(num==4):
        print(" _______")
        print("|   o   |")
        print("| o   o |")
        print("|___o___|")
        return num
        
    if(num==5):
        print(" _______")
        print("|   o   |")
        print("| o o o |")
        print("|___o___|")
        return num
        
    if(num==6):
        f=0
        print(" _______")
        print("| o o o |")
        print("|       |")
        print("|_o_o_o_|")
        print("\n")
        print("Heyy, as you rolled six,you have an extra chance")
        num=random.randint(1,6)
        print("Dice rolling...")
        t=5
        while t:
            mins,secs=divmod(t,60)
            timer='{:02d}:{:02d}'.format(mins,secs)
            print(timer,end="\r")
            time.sleep(1)             
            t=t-1
            print("This time you rolled:")
            dice_show(num)
            if(num==6):
                print("No more chances inspite of six\"")
            f=6+num
            return f
        
def ladder(pos):
    if(pos==2):
        print("\nheyy! You got a Ladder")
        return 8

    elif(pos==10):
        print("\nheyy! You got a Ladder")
        return 18

    elif(pos==15):
        print("\nheyy! You got a Ladder")
        return 17

    else:
        return pos

def snake(pos):
    if(pos==6):
        print("\nOops! A snake")
        return 4

    elif(pos==20):
        print("\nOops! A snake ")
        return 9

    elif(pos==22):
        print("\nOops! A snake")
        return 17

    else:
        return pos

def play():
    player_pos=0
    c_pos=0
    turn=0
    while(True):
        if turn%2==0:
            print("\nNow,its your turn-(press y to roll the dice and continue; n to quit the game)")
            choice=input()

            if choice=="n":
                print("Your are at ",player_pos)
                print("Computer is at ",c_pos)
                print('THANKS FOR PLAYING,Quitting the game.')
                exit(0)
            else:
                num=random.randint(1,6)
                print("Dice rolling...")
                t=5
                while t:
                    mins,secs=divmod(t,60)
                    timer='{:02d}:{:02d}'.format(mins,secs)
                    print(timer,end="\r")
                    time.sleep(1)
                    t=t-1

                print("You rolled:")
                num=dice_show(num)
                turn=turn+1
                player_pos=player_pos + num
                player_pos=ladder(player_pos)
                player_pos=snake(player_pos)

                if(player_pos>=end_pos):
                    print("\nYour are at ",end_pos)
                    print("Computer is at ",c_pos)
                    print("Hurrah!Yeahhh! You won the game\n")
                    break
                else:
                    print("\nPOSITIONS:")
                    print("Your are at ",player_pos)
                    print("Computer is at ",c_pos)

        t=1
        print("\n")
        while t:
            mins,secs=divmod(t,60)
            print("Chance to your opponent;",end="\r")
            time.sleep(2)
            t=t-1 
        
        print("\n")                
        if turn%2 !=0:
            print("\nIts computer's turn")
            num=random.randint(1,6)
            print("Dice rolling...")
            t=5
            while t:
                mins,secs=divmod(t,60)
                timer='{:02d}:{:02d}'.format(mins,secs)
                print(timer,end="\r")
                time.sleep(1)
                t=t-1
            print("Computer rolled:")
            num=dice_show(num)
            turn=turn+1
            c_pos=c_pos + num
            c_pos=ladder(c_pos)
            c_pos=snake(c_pos)

            if(c_pos>=end_pos):
                print("\nYour are at ",player_pos)
                print("Computer is at ",end_pos)
                print("Computer won the game,Thanks for playing\n")
                break
            else:
                print("\nPOSITIONS:")
                print("Your are at ",player_pos)
                print("Computer is at ",c_pos)
                
play()

while(True):
    print('Do you want to play an other game? if yes press y else press n for no')
    choice2=input()
    if(choice2=="y"):
        play()
    else:
        print("See you in the next game :)")
        exit(0)





