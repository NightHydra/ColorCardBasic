from tkinter import *
'''from Actions import *'''
import math
import random
from MovementPVP import *
from Networking import *
from threading import *
import time


root = Tk() 
root.geometry("800x650")

played = True


colors = ["red", 'blue', 'green']
cards = { 'red': "RED", 'blue': "BLUE", 'green': "GREEN", 'white': 'WHITE'}



class Deck:
    def __init__(self, x, y):
        self.place = canvas.create_rectangle(x, y, x-100, y-140, fill = "BLACK")
        self.unshuffled = " ".join(["red"]*17).split()
        self.unshuffled.extend(" ".join(["blue"]*17).split())
        self.unshuffled.extend(" ".join(["green"]*17).split())
        self.unshuffled.extend(" ".join(["white"]*9).split())
        self.order = []
        for i in range(60):
            self.order.append(cards[self.unshuffled.pop(random.randint(0,59-i))])
        
            
        
class Active:
    def __init__ (self, x, y):
        self.active = canvas.create_rectangle(x, y, x-100, y-140, fill = "WHITE")
        self.active_card = "WHITE"

    def fill (self, played):
        canvas.itemconfig(self.active, fill=played.placed)
        self.active_card = played.placed
        played.placed = None
        canvas.itemconfig(played.place, fill = "WHITE")
        

class Hand:
    def __init__(self, x, y):
        self.placed = None
        self.place = canvas.create_rectangle(x, y, x-100, y-140, fill = None)
    def fill (self, top_card, player):
        canvas.itemconfig(self.place, fill = top_card)
        self.placed = top_card
        player['deck'].order.append(player['deck'].order.pop(0))


    
    
    


hand1 = []
hand2 = []







def kinter_setup():

    for i in range (5):
        play1['hand'][i].fill(play1['deck'].order[0], play1)
        
    for i in range (5):
        play2['hand'][i].fill(play2['deck'].order[0], play2)

    
    
    
    presses(canvas, play1, play2, active)




def update():
    global Play2_HP
    global Play1_HP
    global played
    global opp_mov


    '''action = random.randint(0,25)
    if action == 0:
        start_HP = play1["HP"]
        for i in range(5):
            select(play2, i)
            placing(play2, active[0], play1)
            if start_HP != play1['HP']:
                break
                break
                break
        for i in range(5):
            select(play2, i)
            placing(play2, active[1], play1)
            if start_HP != play1['HP']:
                break
                break
                break'''
    # Plays for opponent
    
    if played == False:

        select(play2, int(move[0]))
        opp_placing(play2, active[int(move[1])], play1)
        played = True
        
    
    
    canvas.itemconfig(Play1_HP, text = str(play1['HP']))
    canvas.itemconfig(Play2_HP, text = str(play2['HP']))
    canvas.after(100, update)
    if play1['HP'] <= 0:
        canvas.destroy()
        x = Label(root, text = "Player 2 Wins")
        x.pack()
    if play2['HP'] < 0:
        canvas.destroy()
        x = Label(root, text = "Player 1 Wins")
        x.pack()

canvas = Canvas (root, width = 800, height = 650)
Deck1 = Deck(775, 625)    
Deck2 = Deck(125, 165)
play1 = {'deck':Deck1, 'hand': hand1, 'selected': None, 'HP': 1000}
play2 = {'deck':Deck2, 'hand': hand2, 'selected': None, 'HP': 1000}

def cont():
    global stop
    while stop == False:
        Sender.send(" ".join(play1['deck'].order))
        time.sleep(.01)
        
    

stop = False
t_send = Thread(target = cont)



t_send.start()
order = Recieve.connect().split()

stop = True


move = None
def get_opp_move():
    global move
    global played
    while True:
        move = Recieve.recieve(select, opp_placing, play2, play1, active)
        played = False

play2['deck'].order = order

Recieve.buf = 20

for i in range (5):
    hand1.append(Hand(120*i+130, 625))
    hand2.append(Hand(780-120*i, 165))

active = []
for i in range (2):
    active.append(Active(350+200*i, 395))

r_thread = Thread(target = get_opp_move)
r_thread.start()
kinter_setup()
Play2_HP = canvas.create_text(400,200,text=play2['HP'])
Play1_HP = canvas.create_text(400,450,text=play1['HP'])

canvas.pack() 
canvas.after(100, update)



