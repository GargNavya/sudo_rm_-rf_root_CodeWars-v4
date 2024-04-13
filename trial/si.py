
import random
import math

name = "scriptblue"

island_backup = 12
friends = {}
pirate=[]
islands=[]
island_guards=[[],[],[]]

def roam(pirate):
    i = int(pirate.getID())
    x = pirate.getDimensionX()
    if pirate.getCurrentFrame() <= 2*x - 4:
        if pirate.getDeployPoint() == (x-1, 0):
            match i:
                case 1:
                    if pirate.getCurrentFrame() <= x:
                        return 4
                    return 3
                case 2:
                    if pirate.getCurrentFrame() == 1:
                        return 4
                    if pirate.getCurrentFrame() == 2:
                        return 3
                    if pirate.getCurrentFrame() <= x:
                        return 4 
                    return 3
                case 3:
                    if pirate.getCurrentFrame() == 1:
                        return 4
                    if pirate.getCurrentFrame() == 2:
                        return 3
                    if pirate.getCurrentFrame() == 3:
                        return 4
                    if pirate.getCurrentFrame() == 4:
                        return 3
                    if pirate.getCurrentFrame() <= x:
                        return 4
                    return 3
                case 4:
                    if pirate.getCurrentFrame() == 1:
                        return 4
                    if pirate.getCurrentFrame() == 2:
                        return 3
                    if pirate.getCurrentFrame() == 3:
                        return 4
                    if pirate.getCurrentFrame() == 4:
                        return 3
                    if pirate.getCurrentFrame() == 5:
                        return 4
                    if pirate.getCurrentFrame() == 6:
                        return 3
                    if pirate.getCurrentFrame() <= x:
                        return 4
                    return 3
                case 5:
                    if pirate.getCurrentFrame() == 1:
                        return 3
                    if pirate.getCurrentFrame() == 2:
                        return 4
                    if pirate.getCurrentFrame() == 3:
                        return 3
                    if pirate.getCurrentFrame() == 4:
                        return 4
                    if pirate.getCurrentFrame() == 5:
                        return 3
                    if pirate.getCurrentFrame() == 6:
                        return 4
                    if pirate.getCurrentFrame() <= x:
                        return 3
                    return 4
                case 6:
                    if pirate.getCurrentFrame() == 1:
                        return 3
                    if pirate.getCurrentFrame() == 2:
                        return 4
                    if pirate.getCurrentFrame() == 3:
                        return 3
                    if pirate.getCurrentFrame() == 4:
                        return 4
                    if pirate.getCurrentFrame() <= x:
                        return 3
                    return 4
                case 7:
                    if pirate.getCurrentFrame() == 1:
                        return 3
                    if pirate.getCurrentFrame() == 2:
                        return 4
                    if pirate.getCurrentFrame() <= x:
                        return 3
                    return 4
                case 8:
                    if pirate.getCurrentFrame() <= x:
                        return 3
                    return 4
                case _:
                    return random.randint(1, 4)
        else:
            match i:
                case 1:
                    if pirate.getCurrentFrame() <= x:
                        return 2
                    return 3
                case 2:
                    if pirate.getCurrentFrame() == 1:
                        return 2
                    if pirate.getCurrentFrame() == 2:
                        return 3
                    if pirate.getCurrentFrame() <= x:
                        return 2
                    return 3
                case 3:
                    if pirate.getCurrentFrame() == 1:
                        return 2
                    if pirate.getCurrentFrame() == 2:
                        return 3
                    if pirate.getCurrentFrame() == 3:
                        return 2
                    if pirate.getCurrentFrame() == 4:
                        return 3
                    if pirate.getCurrentFrame() <= x:
                        return 2
                    return 3
                case 4:
                    if pirate.getCurrentFrame() == 1:
                        return 2
                    if pirate.getCurrentFrame() == 2:
                        return 3
                    if pirate.getCurrentFrame() == 3:
                        return 2
                    if pirate.getCurrentFrame() == 4:
                        return 3
                    if pirate.getCurrentFrame() == 5:
                        return 2
                    if pirate.getCurrentFrame() == 6:
                        return 3
                    if pirate.getCurrentFrame() <= x:
                        return 2
                    return 3
                case 5:
                    if pirate.getCurrentFrame() == 1:
                        return 3
                    if pirate.getCurrentFrame() == 2:
                        return 2
                    if pirate.getCurrentFrame() == 3:
                        return 3
                    if pirate.getCurrentFrame() == 4:
                        return 2
                    if pirate.getCurrentFrame() == 5:
                        return 3
                    if pirate.getCurrentFrame() == 6:
                        return 2
                    if pirate.getCurrentFrame() <= x:
                        return 3
                    return 2
                    
                case 6:
                    if pirate.getCurrentFrame() == 1:
                        return 3
                    if pirate.getCurrentFrame() == 2:
                        return 2
                    if pirate.getCurrentFrame() == 3:
                        return 3
                    if pirate.getCurrentFrame() == 4:
                        return 2
                    if pirate.getCurrentFrame() <= x:
                        return 3
                    return 2
                case 7:
                    if pirate.getCurrentFrame() == 1:
                        return 3
                    if pirate.getCurrentFrame() == 2:
                        return 2
                    if pirate.getCurrentFrame() <= x:
                        return 3
                    return 2
                case 8:
                    if pirate.getCurrentFrame() <= x:
                        return 3
                    return 2
                case _:
                    return random.randint(1, 4)
    else:
        # return random.randint(1,4)
        return spread(pirate)

def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1

def checkfriends(pirate , quad ):
    sum = 0 
    up = pirate.investigate_up()[1]
    down = pirate.investigate_down()[1]
    left = pirate.investigate_left()[1]
    right = pirate.investigate_right()[1]
    ne = pirate.investigate_ne()[1]
    nw = pirate.investigate_nw()[1]
    se = pirate.investigate_se()[1]
    sw = pirate.investigate_sw()[1]
    
    if(quad=='ne'):
        if(up == 'friend'):
            sum +=1 
        if(ne== 'friend'):
            sum +=1 
        if(right == 'friend'):
            sum +=1 
    if(quad=='se'):
        if(down == 'friend'):
            sum +=1 
        if(right== 'friend'):
            sum +=1 
        if(se == 'friend'):
            sum +=1 
    if(quad=='sw'):
        if(down == 'friend'):
            sum +=1 
        if(sw== 'friend'): 
            sum +=1 
        if(left == 'friend'):
            sum +=1 
    if(quad=='nw'):
        if(up == 'friend'):
            sum +=1 
        if(nw == 'friend'):
            sum +=1 
        if(left == 'friend'):
            sum +=1 

    return sum
    
def spread(pirate):
    sw = checkfriends(pirate ,'sw' )
    se = checkfriends(pirate ,'se' )
    ne = checkfriends(pirate ,'ne' )
    nw = checkfriends(pirate ,'nw' )
   
    my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    x, y = pirate.getPosition()
    
    if( x == 0 , y == 0):
        return random.randint(1,4)
    
    if(sorted_dict[list(sorted_dict())[3]] == 0 ):
        return random.randint(1,4)
    
    if(list(sorted_dict())[0] == 'sw'):
        return moveTo(x-1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'se'):
        return moveTo(x+1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'ne'):
        return moveTo(x+1 , y-1 , pirate)
    elif(list(sorted_dict())[0] == 'nw'):
        return moveTo(x-1 , y-1 , pirate)

# def ActPirate(pirate):

#     up = pirate.investigate_up()[0]
#     down = pirate.investigate_down()[0]
#     left = pirate.investigate_left()[0]
#     right = pirate.investigate_right()[0]
#     nw = pirate.investigate_nw()[0]
#     ne = pirate.investigate_ne()[0]
#     sw = pirate.investigate_sw()[0]
#     se = pirate.investigate_se()[0]

#     x, y = pirate.getPosition()
#     # pirate.setSignal("")
#     s = pirate.trackPlayers()
    
#     global island_guards

#     if pirate.getSignal()!="":
#         pirate_signal = pirate.getSignal()
#         l = pirate_signal.split(",")
#         pirate_dest_x = int(l[0])
#         pirate_dest_y = int(l[1])

#         if (pirate.getID() in island_guards[0]):
#             if pirate.trackPlayers()[0] == "myCapturing":
#                 return moveTo(pirate_dest_x,pirate_dest_y,pirate)
            
#         if (pirate.getID() in island_guards[1]):
#             if pirate.trackPlayers()[1] == "myCapturing":
#                 return moveTo(pirate_dest_x,pirate_dest_y,pirate)

#         if (pirate.getID() in island_guards[2]):
#             if pirate.trackPlayers()[2] == "myCapturing":
#                 return moveTo(pirate_dest_x,pirate_dest_y,pirate)


#     if (
#         (up == "island1" and s[0] != "myCaptured")
#         or (up == "island2" and s[1] != "myCaptured")
#         or (up == "island3" and s[2] != "myCaptured")
#     ):
#         s = up[-1] + str(x) + "," + str(y - 1)
#         island_guards[int(up[-1])-1].append(pirate.getID())
#         if s not in islands:
#             islands.append(s)
#             pirate.setTeamSignal(s)

#     if (
#         (down == "island1" and s[0] != "myCaptured")
#         or (down == "island2" and s[1] != "myCaptured")
#         or (down == "island3" and s[2] != "myCaptured")
#     ):
#         s = down[-1] + str(x) + "," + str(y + 1)
#         if s not in islands:
#             islands.append(s)
#             pirate.setTeamSignal(s)

#     if (
#         (left == "island1" and s[0] != "myCaptured")
#         or (left == "island2" and s[1] != "myCaptured")
#         or (left == "island3" and s[2] != "myCaptured")
#     ):
#         s = left[-1] + str(x - 1) + "," + str(y)
#         if s not in islands:
#             islands.append(s)
#             pirate.setTeamSignal(s)

#     if (
#         (right == "island1" and s[0] != "myCaptured")
#         or (right == "island2" and s[1] != "myCaptured")
#         or (right == "island3" and s[2] != "myCaptured")
#     ):
#         s = right[-1] + str(x + 1) + "," + str(y)
#         if s not in islands:
#             islands.append(s)
#             pirate.setTeamSignal(s)

#     if (
#         (nw == "island1" and s[0] != "myCaptured")
#         or (nw == "island2" and s[1] != "myCaptured")
#         or (nw == "island3" and s[2] != "myCaptured")
#     ):
#         s = nw[-1] + str(x - 1) + "," + str(y-1)
#         if s not in islands:
#             islands.append(s)
#             pirate.setTeamSignal(s)

#     if (
#         (ne == "island1" and s[0] != "myCaptured")
#         or (ne == "island2" and s[1] != "myCaptured")
#         or (ne == "island3" and s[2] != "myCaptured")
#     ):
#         s = ne[-1] + str(x + 1) + "," + str(y-1)
#         if s not in islands:
#             islands.append(s)
#             pirate.setTeamSignal(s)

#     if (
#         (sw == "island1" and s[0] != "myCaptured")
#         or (sw == "island2" and s[1] != "myCaptured")
#         or (sw == "island3" and s[2] != "myCaptured")
#     ):
#         s = sw[-1] + str(x - 1) + "," + str(y+1)
#         if s not in islands:
#             islands.append(s)
#             pirate.setTeamSignal(s)

#     if (
#         (se == "island1" and s[0] != "myCaptured")
#         or (se == "island2" and s[1] != "myCaptured")
#         or (se == "island3" and s[2] != "myCaptured")
#     ):
#         s = se[-1] + str(x + 1) + "," + str(y+1)
#         if s not in islands:
#             islands.append(s)
#             pirate.setTeamSignal(s)

def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    nw = pirate.investigate_nw()[0]
    ne = pirate.investigate_ne()[0]
    sw = pirate.investigate_sw()[0]
    se = pirate.investigate_se()[0]
    curr = pirate.investigate_current()[0]

    x, y = pirate.getPosition()
    s = pirate.trackPlayers()
    
    if (curr == "island1" and s[0] != "myCaptured") or (up == "island2" and s[1] != "myCaptured") or (up == "island3" and s[2] != "myCaptured"):
        if nw == up and ne == up:
            s = up[-1] + str(x) + "," + str(y - 2)
        elif nw == up and ne != up:
            s = up[-1] + str(x - 1) + "," + str(y - 2)
        elif ne == up and nw != up:
            s = up[-1] + str(x + 1) + "," + str(y - 2)
        if s not in islands:
            islands.append(s)
        return 0
    
    if (up == "island1" and s[0] != "myCaptured") or (up == "island2" and s[1] != "myCaptured") or (up == "island3" and s[2] != "myCaptured"):
        if nw == up and ne == up:
            s = up[-1] + str(x) + "," + str(y - 2)
        elif nw == up and ne != up:
            s = up[-1] + str(x - 1) + "," + str(y - 2)
        elif ne == up and nw != up:
            s = up[-1] + str(x + 1) + "," + str(y - 2)
        if s not in islands:
            islands.append(s)
            pirate.setTeamSignal(s)
        return 1

    if (down == "island1" and s[0] != "myCaptured") or (down == "island2" and s[1] != "myCaptured") or (down == "island3" and s[2] != "myCaptured"):
        if sw == down and se == down:
            s = down[-1] + str(x) + "," + str(y + 2)
        elif sw == down and se != down:
            s = down[-1] + str(x - 1) + "," + str(y + 2)
        elif se == down and sw != down:
            s = down[-1] + str(x + 1) + "," + str(y + 2)
        if s not in islands:
            islands.append(s)
            pirate.setTeamSignal(s)
        return 3

    if (left == "island1" and s[0] != "myCaptured") or (left == "island2" and s[1] != "myCaptured") or (left == "island3" and s[2] != "myCaptured"):
        if nw == left and sw == left:
            s = left[-1] + str(x - 2) + "," + str(y)
        elif nw == left and sw != left:
            s = left[-1] + str(x - 2) + "," + str(y - 1)
        elif sw == left and nw != left:
            s = left[-1] + str(x - 2) + "," + str(y + 1)
        if s not in islands:
            islands.append(s)
            pirate.setTeamSignal(s)
        return 4

    if (right == "island1" and s[0] != "myCaptured") or (right == "island2" and s[1] != "myCaptured") or (right == "island3" and s[2] != "myCaptured"):
        if ne == right and se == right:
            s = right[-1] + str(x + 2) + "," + str(y)
        elif ne == right and se != right:
            s = right[-1] + str(x + 2) + "," + str(y - 1)
        elif se == right and ne != right:
            s = right[-1] + str(x + 2) + "," + str(y + 1)
        if s not in islands:
            islands.append(s)
            pirate.setTeamSignal(s)
        return 2

    if (nw == "island1" and s[0] != "myCaptured") or (nw == "island2" and s[1] != "myCaptured") or (nw == "island3" and s[2] != "myCaptured"):
        s = nw[-1] + str(x - 2) + "," + str(y - 2)
        if s not in islands:
            islands.append(s)
            pirate.setTeamSignal(s)

    if (ne == "island1" and s[0] != "myCaptured") or (ne == "island2" and s[1] != "myCaptured") or (ne == "island3" and s[2] != "myCaptured"):
        s = ne[-1] + str(x + 2) + "," + str(y - 2)
        if s not in islands:
            islands.append(s)
            pirate.setTeamSignal(s)

    if (se == "island1" and s[0] != "myCaptured") or (se == "island2" and s[1] != "myCaptured") or (se == "island3" and s[2] != "myCaptured"):
        s = se[-1] + str(x + 2) + "," + str(y + 2)
        if s not in islands:
            islands.append(s)
            pirate.setTeamSignal(s)
    
    if (sw == "island1" and s[0] != "myCaptured") or (sw == "island2" and s[1] != "myCaptured") or (sw == "island3" and s[2] != "myCaptured"):
        s = sw[-1] + str(x - 2) + "," + str(y + 2)
        if s not in islands:
            islands.append(s)
            pirate.setTeamSignal(s)
     
    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])

        global friends
        global island_backup

        if pirate.getCurrentFrame()<x:
            island_backup = 3
        elif pirate.getCurrentFrame()<400:
            island_backup = 12
        elif pirate.getCurrentFrame()<1000:
            island_backup = 20
        else:
            island_backup = 30
        if pirate.getID() not in friends.keys():
            x_pirate,y_pirate = pirate.getPosition()
            d = abs(x_pirate-x) + abs(y_pirate-y)
            friends[pirate.getID()]=d
            friends = dict(sorted(friends.items(), key=lambda item: item[1]))

        else:
            nearest_friends=list(friends.keys())[1:island_backup+1]
            islands.append(nearest_friends)
            if pirate.getID() in nearest_friends:
                pirate.setSignal(f"{x},{y}")
                return moveTo(x,y,pirate)
            else:
                return roam(pirate)

    else:
        return roam(pirate)

def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()
    
    # print(team.getTeamSignal())

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")