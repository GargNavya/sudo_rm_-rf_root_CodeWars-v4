import random
import math

name = "avi_v2"

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
    
    if( x == 0 and y == 0):
        return random.randint(1,4)
    
    if(sorted_dict[list(sorted_dict.keys())[3]] == 0 ):
        return random.randint(1,4)
    
    if(list(sorted_dict)[0] == 'sw'):
        return moveTo(x-1 , y+1 , pirate)
    elif(list(sorted_dict)[0] == 'se'):
        return moveTo(x+1 , y+1 , pirate)
    elif(list(sorted_dict)[0] == 'ne'):
        return moveTo(x+1 , y-1 , pirate)
    elif(list(sorted_dict)[0] == 'nw'):
        return moveTo(x-1 , y-1 , pirate)

def central_pirates(pirate):
    dimension_x = pirate.getDimensionX()
    dimension_y = pirate.getDimensionY()

    if pirate.getPosition() == pirate.getDeployPoint():
        sig = "centre"
        _rand = random.randint(1,5)
        if (_rand < 3):
            sig= "centre1"
            pirate.setSignal(sig)
            return moveTo(dimension_x // 2, dimension_y - pirate.getDeployPoint()[1], pirate)
        elif (_rand<5):
            sig = "centre2"
            pirate.setSignal(sig)
            return moveTo(dimension_x - pirate.getDeployPoint()[0], dimension_y // 2, pirate)
        sig="centre"
        pirate.setSignal(sig)
        return moveTo(dimension_x // 2, dimension_y // 2, pirate)

    if pirate.getSignal()=="centre" and pirate.getPosition() == (dimension_x // 2, dimension_y // 2):
        x = random.randint(1, 12)
        if x == 1:
            pirate.setSignal("top-left")
        elif x == 2:
            pirate.setSignal("bottom-left")
        elif x == 3:
            pirate.setSignal("top-right")
        elif x == 4:
            pirate.setSignal("bottom-right")
        elif x == 5:
            pirate.setSignal("top1")
        elif x == 6:
            pirate.setSignal("top2")
        elif x == 7:
            pirate.setSignal("right1")
        elif x == 8:
            pirate.setSignal("right2")
        elif x == 9:
            pirate.setSignal("bottom1")
        elif x == 10:
            pirate.setSignal("bottom2")
        elif x == 11:
            pirate.setSignal("left1")
        else:
            pirate.setSignal("left2")
    if pirate.getSignal()=="centre1" and pirate.getPosition() == (dimension_x // 2, dimension_y - pirate.getDeployPoint()[1]):
        x = random.randint(1, 12)
        if x == 1:
            pirate.setSignal("top-left")
        elif x == 2:
            pirate.setSignal("bottom-left")
        elif x == 3:
            pirate.setSignal("top-right")
        elif x == 4:
            pirate.setSignal("bottom-right")
        elif x == 5:
            pirate.setSignal("top1")
        elif x == 6:
            pirate.setSignal("top2")
        elif x == 7:
            pirate.setSignal("right1")
        elif x == 8:
            pirate.setSignal("right2")
        elif x == 9:
            pirate.setSignal("bottom1")
        elif x == 10:
            pirate.setSignal("bottom2")
        elif x == 11:
            pirate.setSignal("left1")
        else:
            pirate.setSignal("left2")
    if pirate.getSignal()=="centre2" and pirate.getPosition() == (dimension_x - pirate.getDeployPoint()[0], dimension_y // 2):
        x = random.randint(1, 12)
        if x == 1:
            pirate.setSignal("top-left")
        elif x == 2:
            pirate.setSignal("bottom-left")
        elif x == 3:
            pirate.setSignal("top-right")
        elif x == 4:
            pirate.setSignal("bottom-right")
        elif x == 5:
            pirate.setSignal("top1")
        elif x == 6:
            pirate.setSignal("top2")
        elif x == 7:
            pirate.setSignal("right1")
        elif x == 8:
            pirate.setSignal("right2")
        elif x == 9:
            pirate.setSignal("bottom1")
        elif x == 10:
            pirate.setSignal("bottom2")
        elif x == 11:
            pirate.setSignal("left1")
        else:
            pirate.setSignal("left2")
    if pirate.getSignal() == "centre":
        return moveTo(dimension_x // 2, dimension_y // 2, pirate)
    elif pirate.getSignal() == "centre1":
        return moveTo(dimension_x // 2, dimension_y - pirate.getDeployPoint()[1], pirate)
    elif pirate.getSignal() == "centre2":
        return moveTo(dimension_x - pirate.getDeployPoint()[0], dimension_y // 2, pirate)
    elif pirate.getSignal() == "top-left": #1
        if pirate.getPosition() == (0, 0):
            pirate.setSignal("centre")
            return moveTo(0, 0, pirate)
        return moveTo(0, 0, pirate)
    elif pirate.getSignal() == "bottom-right": #2
        if pirate.getPosition() == (dimension_x - 1, dimension_y - 1):
            pirate.setSignal("centre")
            return moveTo(0, 0, pirate)
        return moveTo(dimension_x - 1, dimension_y - 1, pirate)
    elif pirate.getSignal() == "top-right": #3
        if pirate.getPosition() == (dimension_x - 1, 0):
            pirate.setSignal("centre")
            return moveTo(0, 0, pirate)
        return moveTo(dimension_x - 1, 0, pirate)
    elif pirate.getSignal() == "bottom-left": #4
        if pirate.getPosition() == (0, dimension_y - 1):
            pirate.setSignal("centre")
            return moveTo(0, 0, pirate)
        return moveTo(0, dimension_y - 1, pirate)
    elif pirate.getSignal() == "top1": #5
        if pirate.getPosition() == (dimension_x // 3, 0):
            pirate.setSignal("centre")
            return moveTo(0, 0, pirate)
        return moveTo(dimension_x // 3, 0, pirate)
    elif pirate.getSignal() == "top2": #6
        if pirate.getPosition() == (2*dimension_x //3, 0):
            pirate.setSignal("centre")
            return moveTo(0, 0, pirate)
        return moveTo(2*dimension_x // 3, 0, pirate)
    elif pirate.getSignal() == "right1": #7
        if pirate.getPosition() == (dimension_x-1, dimension_y // 3):
            pirate.setSignal("centre")
            return moveTo(0, 0, pirate)
        return moveTo(dimension_x-1, dimension_y // 3, pirate)
    elif pirate.getSignal() == "right2": #8
        if pirate.getPosition() == (dimension_x-1, 2*dimension_y // 3):
            pirate.setSignal("centre")
            return moveTo(0, 0, pirate)
        return moveTo(dimension_x-1, 2*dimension_y // 3, pirate)
    elif pirate.getSignal() == "bottom1": #9
        if pirate.getPosition() == (2*dimension_x // 3, dimension_y-1):
            pirate.setSignal("centre")
            return moveTo(0, 0, pirate)
        return moveTo(2*dimension_x // 3, dimension_y-1, pirate)
    elif pirate.getSignal() == "bottom2": #10
        if pirate.getPosition() == (dimension_x // 3, dimension_y-1):
            pirate.setSignal("centre")
            return moveTo(0, 0, pirate)
        return moveTo(dimension_x // 3, dimension_y-1, pirate)
    elif pirate.getSignal() == "left1": #11
        if pirate.getPosition() == (0, 2*dimension_y // 3):
            pirate.setSignal("centre")
            return moveTo(0, 0, pirate)
        return moveTo(0, 2*dimension_y // 3, pirate)
    
    elif pirate.getSignal() == "":
        return spread(pirate)



def roam_island(pirate):
    L = []
    up = pirate.investigate_up()[0]
    if up[0:6] == "island":
        L.append(1)
    down = pirate.investigate_down()[0]
    if down[0:6] == "island":
        L.append(3)
    left = pirate.investigate_left()[0]
    if left[0:6] == "island":
        L.append(4)
    right = pirate.investigate_right()[0]
    if right[0:6] == "island":
        L.append(2)
    return L[random.randint(0, len(L) - 1)]


def roam(pirate):
    i = int(pirate.getID())
    x = pirate.getDimensionX()
    if pirate.getCurrentFrame() <= 2 * x - 4:
        if pirate.getDeployPoint() == (0, x - 1):
            match i:
                case 1:
                    if pirate.getCurrentFrame() <= x - 1:
                        return 2
                    return 1
                case 2:
                    if pirate.getCurrentFrame() == 1:
                        return 2
                    if pirate.getCurrentFrame() == 2:
                        return 1
                    if pirate.getCurrentFrame() <= x - 1:
                        return 2
                    return 1
                case 3:
                    if pirate.getCurrentFrame() == 1:
                        return 2
                    if pirate.getCurrentFrame() == 2:
                        return 1
                    if pirate.getCurrentFrame() == 3:
                        return 2
                    if pirate.getCurrentFrame() == 4:
                        return 1
                    if pirate.getCurrentFrame() <= x - 1:
                        return 2
                    return 1
                case 4:
                    if pirate.getCurrentFrame() == 1:
                        return 2
                    if pirate.getCurrentFrame() == 2:
                        return 1
                    if pirate.getCurrentFrame() == 3:
                        return 2
                    if pirate.getCurrentFrame() == 4:
                        return 1
                    if pirate.getCurrentFrame() == 5:
                        return 2
                    if pirate.getCurrentFrame() == 6:
                        return 1
                    if pirate.getCurrentFrame() <= x - 1:
                        return 2
                    return 1
                case 5:
                    if pirate.getCurrentFrame() == 1:
                        return 1
                    if pirate.getCurrentFrame() == 2:
                        return 2
                    if pirate.getCurrentFrame() == 3:
                        return 1
                    if pirate.getCurrentFrame() == 4:
                        return 2
                    if pirate.getCurrentFrame() == 5:
                        return 1
                    if pirate.getCurrentFrame() == 6:
                        return 2
                    if pirate.getCurrentFrame() <= x - 1:
                        return 1
                    return 2
                case 6:
                    if pirate.getCurrentFrame() == 1:
                        return 1
                    if pirate.getCurrentFrame() == 2:
                        return 2
                    if pirate.getCurrentFrame() == 3:
                        return 1
                    if pirate.getCurrentFrame() == 4:
                        return 2
                    if pirate.getCurrentFrame() <= x - 1:
                        return 1
                    return 2
                case 7:
                    if pirate.getCurrentFrame() == 1:
                        return 1
                    if pirate.getCurrentFrame() == 2:
                        return 2
                    if pirate.getCurrentFrame() <= x - 1:
                        return 1
                    return 2
                case 8:
                    if pirate.getCurrentFrame() <= x - 1:
                        return 1
                    return 2
                case _:
                    return spread(pirate)
        elif pirate.getDeployPoint() == (x - 1, x - 1):
            match i:
                case 1:
                    if pirate.getCurrentFrame() <= x - 1:
                        return 4
                    return 1
                case 2:
                    if pirate.getCurrentFrame() == 1:
                        return 4
                    if pirate.getCurrentFrame() == 2:
                        return 1
                    if pirate.getCurrentFrame() <= x - 1:
                        return 4
                    return 1
                case 3:
                    if pirate.getCurrentFrame() == 1:
                        return 4
                    if pirate.getCurrentFrame() == 2:
                        return 1
                    if pirate.getCurrentFrame() == 3:
                        return 4
                    if pirate.getCurrentFrame() == 4:
                        return 1
                    if pirate.getCurrentFrame() <= x - 1:
                        return 4
                    return 1
                case 4:
                    if pirate.getCurrentFrame() == 1:
                        return 4
                    if pirate.getCurrentFrame() == 2:
                        return 1
                    if pirate.getCurrentFrame() == 3:
                        return 4
                    if pirate.getCurrentFrame() == 4:
                        return 1
                    if pirate.getCurrentFrame() == 5:
                        return 4
                    if pirate.getCurrentFrame() == 6:
                        return 1
                    if pirate.getCurrentFrame() <= x - 1:
                        return 4
                    return 1
                case 5:
                    if pirate.getCurrentFrame() == 1:
                        return 1
                    if pirate.getCurrentFrame() == 2:
                        return 4
                    if pirate.getCurrentFrame() == 3:
                        return 1
                    if pirate.getCurrentFrame() == 4:
                        return 4
                    if pirate.getCurrentFrame() == 5:
                        return 1
                    if pirate.getCurrentFrame() == 6:
                        return 4
                    if pirate.getCurrentFrame() <= x - 1:
                        return 1
                    return 4

                case 6:
                    if pirate.getCurrentFrame() == 1:
                        return 1
                    if pirate.getCurrentFrame() == 2:
                        return 4
                    if pirate.getCurrentFrame() == 3:
                        return 1
                    if pirate.getCurrentFrame() == 4:
                        return 4
                    if pirate.getCurrentFrame() <= x - 1:
                        return 1
                    return 4
                case 7:
                    if pirate.getCurrentFrame() == 1:
                        return 1
                    if pirate.getCurrentFrame() == 2:
                        return 4
                    if pirate.getCurrentFrame() <= x - 1:
                        return 1
                    return 4
                case 8:
                    if pirate.getCurrentFrame() <= x - 1:
                        return 1
                    return 4
                case _:
                    return spread(pirate)
        elif pirate.getDeployPoint() == (x - 1, 0):
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
                    return spread(pirate)
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
                    return spread(pirate)
    else:
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


def ActPirate(pirate):
    curr = pirate.investigate_current()[0]
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    nw = pirate.investigate_nw()[0]
    ne = pirate.investigate_ne()[0]
    sw = pirate.investigate_sw()[0]
    se = pirate.investigate_se()[0]
    x, y = pirate.getPosition()
    s = pirate.trackPlayers()
    sigT = pirate.getTeamSignal()

    if int(pirate.getID()) < 9:
        return roam(pirate)
    
    if pirate.getCurrentFrame() >= 200:


        if (
            (curr == "island1" and s[0] != "myCaptured")
            or (curr == "island2" and s[1] != "myCaptured")
            or (curr == "island3" and s[2] != "myCaptured")
        ):
            s = curr[-1] + str(x) + "," + str(y)
            pirate.setTeamSignal(s)
            return roam_island(pirate)
        

        if (
            (up == "island1" and s[0] != "myCaptured")
            or (up == "island2" and s[1] != "myCaptured")
            or (up == "island3" and s[2] != "myCaptured")
        ):
            s = up[-1] + str(x) + "," + str(y - 1)
            pirate.setTeamSignal(s)
            return 1

        if (
            (down == "island1" and s[0] != "myCaptured")
            or (down == "island2" and s[1] != "myCaptured")
            or (down == "island3" and s[2] != "myCaptured")
        ):
            s = down[-1] + str(x) + "," + str(y + 1)
            pirate.setTeamSignal(s)
            return 3

        if (
            (left == "island1" and s[0] != "myCaptured")
            or (left == "island2" and s[1] != "myCaptured")
            or (left == "island3" and s[2] != "myCaptured")
        ):
            s = left[-1] + str(x - 1) + "," + str(y)
            pirate.setTeamSignal(s)
            return 4

        if (
            (right == "island1" and s[0] != "myCaptured")
            or (right == "island2" and s[1] != "myCaptured")
            or (right == "island3" and s[2] != "myCaptured")
        ):
            s = right[-1] + str(x + 1) + "," + str(y)
            pirate.setTeamSignal(s)
            return 2

        if (
            (nw == "island1" and s[0] != "myCaptured")
            or (nw == "island2" and s[1] != "myCaptured")
            or (nw == "island3" and s[2] != "myCaptured")
        ):
            s = nw[-1] + str(x - 1) + "," + str(y-1)
            pirate.setTeamSignal(s)
            return 1

        if (
            (ne == "island1" and s[0] != "myCaptured")
            or (ne == "island2" and s[1] != "myCaptured")
            or (ne == "island3" and s[2] != "myCaptured")
        ):
            s = ne[-1] + str(x + 1) + "," + str(y-1)
            pirate.setTeamSignal(s)
            return 1

        if (
            (sw == "island1" and s[0] != "myCaptured")
            or (sw == "island2" and s[1] != "myCaptured")
            or (sw == "island3" and s[2] != "myCaptured")
        ):
            s = sw[-1] + str(x - 1) + "," + str(y+1)
            pirate.setTeamSignal(s)
            return 3

        if (
            (se == "island1" and s[0] != "myCaptured")
            or (se == "island2" and s[1] != "myCaptured")
            or (se == "island3" and s[2] != "myCaptured")
        ):
            s = se[-1] + str(x + 1) + "," + str(y+1)
            pirate.setTeamSignal(s)
            return 3

    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])

        if pirate.getCurrentFrame() >= 1000:
            return moveTo(x, y, pirate)
        else:
            return central_pirates(pirate)

    else:
        return central_pirates(pirate)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

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
