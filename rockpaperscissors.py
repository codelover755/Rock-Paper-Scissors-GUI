from tkinter import *

player_scorec = 0
computer_scorec = 0

options = [('rock',0),('paper',1),('scissors',2)]
print(options)

def player_choice(pinput):
    print(str(pinput[0]))

game = Tk()
game.geometry("600x400")
game.title("Rock Paper Scissors Game")
game.config(background="honeydew3")

title = Label(game,text="Rock Paper Scissors", fg="black", bg="honeydew3", font=("Calibri",30))
winner = Label(game,text="Let's play!", fg="green", bg="honeydew3", font=("Calibri",12))
options = Label(game,text="Your Options:", fg="black",bg="honeydew3", font=("Calibri",12))
score = Label(game,text="Score:", fg="black",bg="honeydew3", font=("Calibri",12))
playerselect = Label(game,text="You selected:", fg="black",bg="honeydew3", font=("Calibri",12))
computerselect = Label(game,text="Computer selected:", fg="black",bg="honeydew3", font=("Calibri",12))
playerscore = Label(game,text="Player total score:", fg="black",bg="honeydew3", font=("Calibri",12))
computerscore = Label(game,text="Computer total score:", fg="black",bg="honeydew3", font=("Calibri",12))

rock = Button(game,text="Rock",bg="LightPink2",command=lambda: player_choice(options[0]))
paper = Button(game,text="Paper",bg="gray60",command=lambda: player_choice(options[1]))
scissors = Button(game,text="Scissors", bg="LightBlue1",command=lambda: player_choice(options[2]))

title.grid(row=1,column=1)
winner.grid(row=2,column=1)
options.grid(row=3,column=1)
rock.grid(row=4,column=1)
paper.grid(row=4,column=2)
scissors.grid(row=4,column=3)
score.grid(row=5,column=1)
playerselect.grid(row=6,column=1)
playerscore.grid(row=6,column=2)
computerselect.grid(row=7,column=1)
computerscore.grid(row=7,column=2)

game.mainloop()
