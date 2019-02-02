from Networking import *

def presses(can, play1, play2, Active):
    

            
        can.tag_bind(play1['hand'][0].place, '<Button>', lambda event:select(play1, 0))
        can.tag_bind(play1['hand'][1].place, '<Button>', lambda event:select(play1, 1))
        can.tag_bind(play1['hand'][2].place, '<Button>', lambda event:select(play1, 2))
        can.tag_bind(play1['hand'][3].place, '<Button>', lambda event:select(play1, 3))
        can.tag_bind(play1['hand'][4].place, '<Button>', lambda event:select(play1, 4))


        can.tag_bind(Active[0].active, '<Button>', lambda event:placing(play1, Active[0], play2, 0))        
        can.tag_bind(Active[1].active, '<Button>', lambda event:placing(play1, Active[1], play2, 1))
        

def select(player, place):
    player['selected'] = place
        





def placing(player, active, other, num):
        pass_ = False
        global Active
        
        if player['hand'][player['selected']].placed == "GREEN" and active.active_card == ("BLUE"):
                pass_ = True
        if player['hand'][player['selected']].placed == "RED" and active.active_card == ("GREEN"):
                pass_ = True
        if player['hand'][player['selected']].placed == "BLUE" and active.active_card == ("RED"):
                pass_ = True
        if active.active_card == "WHITE":
                pass_ = True
        if player['hand'][player['selected']].placed == "WHITE":
                pass_ = True

        if pass_ == True:
                active.fill(player['hand'][player['selected']])
                player['hand'][player['selected']].fill(player['deck'].order[0], player)
                other['HP'] -= 20
                Sender.send(str(player['selected']) + " " + str(num))


def opp_placing(player, active, other):

        active.fill(player['hand'][int(player['selected'])])
        player['hand'][int(player['selected'])].fill(player['deck'].order[0], player)
        other['HP'] -= 20



