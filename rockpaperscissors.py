from tkinter import *

game = Tk()
game.geometry("600x400")
game.title("Rock Paper Scissors Game")
game.config(background="honeydew3")

title = Label(game,text="Rock Paper Scissors", fg="black", bg="honeydew3", font=("Calibri",30))
winner = Label(game,text="Let's play!", fg="green", bg="honeydew3", font=("Calibri",12))
options = Label(game,text="Your Options:", fg="black",bg="honeydew3", font=("Calibri",12))
score = Label(game,text="Score:", fg="black",bg="honeydew3", font=("Calibri",12))
playerselect = Label(game,text="You selected", fg="black",bg="honeydew3", font=("Calibri",12))
computerselect = Label(game,text="Computer selected:", fg="black",bg="honeydew3", font=("Calibri",12))
playerscore = Label(game,text="Player total score:", fg="black",bg="honeydew3", font=("Calibri",12))
computerscore = Label(game,text="Computer total score:", fg="black",bg="honeydew3", font=("Calibri",12))

game.mainloop()