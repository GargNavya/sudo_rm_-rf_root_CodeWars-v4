import random
import math

name = "navya2"

def central_pirates(pirate):
    # print(pirate.getSignal())
    if pirate.getPosition() == pirate.getDeployPoint():
            sig = "centre"
            pirate.setSignal(sig)
            return moveTo(pirate.getDimensionX()/2, pirate.getDimensionX()/2, pirate)
    if pirate.getPosition() == (pirate.getDimensionX()/2, pirate.getDimensionX()/2):
        if random.randint(1, 4) == 1:
            pirate.setSignal("top-left")
        elif random.randint(1,4)==2:
            pirate.setSignal("bottom-left")
        elif random.randint(1,4)==3:
            pirate.setSignal("top-right")
        else:
            pirate.setSignal("bottom-right")
    if pirate.getSignal() == "centre":
        return moveTo(pirate.getDimensionX()/2, pirate.getDimensionX()/2, pirate)
    if pirate.getSignal() == "top-left":
        if pirate.getPosition()==(0,0):
            pirate.setSignal("centre")
            return 2+random.randint(0,1)
        return moveTo(0, 0, pirate)
    if pirate.getSignal() == "bottom-right":
        if pirate.getPosition()==(pirate.getDimensionX()-1,pirate.getDimensionY()-1):
            pirate.setSignal("centre")
            return 1+3*random.randint(0,1)
        return moveTo(pirate.getDimensionX()-1,pirate.getDimensionY()-1, pirate)
    # return roam(pirate)
    if pirate.getSignal() == "top-right":
        if pirate.getPosition()==(pirate.getDimensionX()-1,0):
            pirate.setSignal("centre")
            return 3+random.randint(0,1)
        return moveTo(pirate.getDimensionX()-1,0,pirate)
    if pirate.getSignal() == "bottom-left":
        if pirate.getPosition()==(1,pirate.getDimensionY()-2):
            pirate.setSignal("centre")
            return 1+random.randint(0,1)
        return moveTo(1,pirate.getDimensionY()-2, pirate)
    if pirate.getSignal()=="":
        return random.randint(1,4)
    

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
                    return random.randint(1, 4)
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
                    return random.randint(1, 4)
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
        return random.randint(1, 4)


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
    print(pirate.getTeamSignal())
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
    island_guards=5

    ##intial L shape formation
    if int(pirate.getID()) < 9:
        if pirate.getCurrentFrame() < 2 * pirate.getDimensionX()-4:
            return roam(pirate)
        else:
            return central_pirates(pirate)
    
    if pirate.getCurrentFrame() < 200:
        return central_pirates(pirate)

    #move to island if found and not reached max capacity
    sigT = pirate.getTeamSignal()
    island1 = ",,0"
    island2 = ",,0"
    island3 = ",,0"
    sigT_list=sigT.split(";")
    island1 = sigT_list[0]
    island2 = sigT_list[1] 
    island3 = sigT_list[2]

    island1_guards = int(island1.split(",")[2])
    island2_guards = int(island2.split(",")[2])
    island3_guards = int(island3.split(",")[2])

    
    # discovery of islands
    
    if (
        (curr == "island1" and s[0] != "myCaptured")
        or (curr == "island2" and s[1] != "myCaptured")
        or (curr == "island3" and s[2] != "myCaptured")
    ):

        # if curr[-1] == "1":
        #     island1_guards += 1
        #     if island1==",,0":
        #         island1 = str(x) + "," + str(y) + "," + str(island1_guards)
        #     else:
        #         island1 = island1.split(',')[0] + "," + island1.split(',')[1] + "," + str(island1_guards)
        # if curr[-1] == "2":
        #     island2_guards += 1
        #     if island2==",,0":
        #         island2 = str(x) + "," + str(y) + "," + str(island2_guards)
        #     else:
        #         island1 = island2.split(',')[0] + "," + island2.split(',')[1] + "," + str(island2_guards)
        # if curr[-1] == "3":
        #     island3_guards += 1
        #     if island3==",,0":
        #         island3 = str(x) + "," + str(y) + "," + str(island3_guards)
        #     else:
        #         island1 = island3.split(',')[0] + "," + island3.split(',')[1] + "," + str(island3_guards)
            
        # sigT = island1 + ";" + island2 + ";" + island3
        # pirate.setTeamSignal(sigT)
        return roam_island(pirate)
    
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        if up[-1] == "1":
            island1_guards += 1
            if island1==",,0":
                island1 = str(x) + "," + str(y-1) + "," + str(island1_guards)
                
        if up[-1] == "2":
            island2_guards += 1
            if island2==",,0":
                island2 = str(x) + "," + str(y-1) + "," + str(island2_guards)
                
        if up[-1] == "3":
            island3_guards += 1
            if island3==",,0":
                island3 = str(x) + "," + str(y-1) + "," + str(island3_guards)
            
        sigT = island1 + ";" + island2 + ";" + island3
        pirate.setTeamSignal(sigT)
        return 1

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        if down[-1] == "1":
            island1_guards += 1
            if island1==",,0":
                island1 = str(x) + "," + str(y+1) + "," + str(island1_guards)
            else:
                island1 = island1.split(',')[0] + "," + island1.split(',')[1] + "," + str(island1_guards)
        if down[-1] == "2":
            island2_guards += 1
            if island2==",,0":
                island2 = str(x) + "," + str(y+1) + "," + str(island2_guards)
            else:
                island2 = island2.split(',')[0] + "," + island2.split(',')[1] + "," + str(island2_guards)
        if down[-1] == "3":
            island3_guards += 1
            if island3==",,0":
                island3 = str(x) + "," + str(y+1) + "," + str(island3_guards)
            else:
                island3 = island3.split(',')[0] + "," + island3.split(',')[1] + "," + str(island3_guards)
            
        sigT = island1 + ";" + island2 + ";" + island3
        pirate.setTeamSignal(sigT)
        return 3

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        if left[-1] == "1":
            island1_guards += 1
            if island1==",,0":
                island1 = str(x-1) + "," + str(y) + "," + str(island1_guards)
            else:
                island1 = island1.split(',')[0] + "," + island1.split(',')[1] + "," + str(island1_guards)
        if left[-1] == "2":
            island2_guards += 1
            if island2==",,0":
                island2 = str(x-1) + "," + str(y) + "," + str(island2_guards)
            else:
                island2 = island2.split(',')[0] + "," + island2.split(',')[1] + "," + str(island2_guards)
        if left[-1] == "3":
            island3_guards += 1
            if island3==",,0":
                island3 = str(x-1) + "," + str(y) + "," + str(island3_guards)
            else:
                island3 = island3.split(',')[0] + "," + island3.split(',')[1] + "," + str(island3_guards)
            
        sigT = island1 + ";" + island2 + ";" + island3
        pirate.setTeamSignal(sigT)
        return 4

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        if right[-1] == "1":
            island1_guards += 1
            if island1==",,0":
                island1 = str(x+1) + "," + str(y) + "," + str(island1_guards)
            else:
                island1 = island1.split(',')[0] + "," + island1.split(',')[1] + "," + str(island1_guards)
        if right[-1] == "2":
            island2_guards += 1
            if island2==",,0":
                island2 = str(x+1) + "," + str(y) + "," + str(island2_guards)
            else:
                island2 = island2.split(',')[0] + "," + island2.split(',')[1] + "," + str(island2_guards)
        if right[-1] == "3":
            island3_guards += 1
            if island3==",,0":
                island3 = str(x+1) + "," + str(y) + "," + str(island3_guards)
            else:
                island3 = island3.split(',')[0] + "," + island3.split(',')[1] + "," + str(island3_guards)
            
        sigT = island1 + ";" + island2 + ";" + island3
        pirate.setTeamSignal(sigT)
        return 2

    if (
        (nw == "island1" and s[0] != "myCaptured")
        or (nw == "island2" and s[1] != "myCaptured")
        or (nw == "island3" and s[2] != "myCaptured")
    ):
        # if nw[-1] == "1":
        #     island1_guards += 1
        #     if island1==",,0":
        #         island1 = str(x-1) + "," + str(y-1) + "," + str(island1_guards)
        #     else:
        #         island1 = island1.split(',')[0] + "," + island1.split(',')[1] + "," + str(island1_guards)
        # if nw[-1] == "2":
        #     island2_guards += 1
        #     if island2==",,0":
        #         island2 = str(x-1) + "," + str(y-1) + "," + str(island2_guards)
        #     else:
        #         island2 = island2.split(',')[0] + "," + island2.split(',')[1] + "," + str(island2_guards)
        # if nw[-1] == "3":
        #     island3_guards += 1
        #     if island3==",,0":
        #         island3 = str(x-1) + "," + str(y-1) + "," + str(island3_guards)
        #     else:
        #         island3 = island3.split(',')[0] + "," + island3.split(',')[1] + "," + str(island3_guards)
            
        # sigT = island1 + ";" + island2 + ";" + island3
        # pirate.setTeamSignal(sigT)
        return 1

    if (
        (ne == "island1" and s[0] != "myCaptured")
        or (ne == "island2" and s[1] != "myCaptured")
        or (ne == "island3" and s[2] != "myCaptured")
    ):
    #     if ne[-1] == "1":
    #         island1_guards += 1
    #         if island1==",,0":
    #             island1 = str(x+1) + "," + str(y-1) + "," + str(island1_guards)
    #         else:
    #             island1 = island1.split(',')[0] + "," + island1.split(',')[1] + "," + str(island1_guards)
    #     if ne[-1] == "2":
    #         island2_guards += 1
    #         if island2==",,0":
    #             island2 = str(x+1) + "," + str(y-1) + "," + str(island2_guards)
    #         else:
    #             island2 = island2.split(',')[0] + "," + island2.split(',')[1] + "," + str(island2_guards)
    #     if ne[-1] == "3":
    #         island3_guards += 1
    #         if island3==",,0":
    #             island3 = str(x+1) + "," + str(y-1) + "," + str(island3_guards)
    #         else:
    #             island3 = island3.split(',')[0] + "," + island3.split(',')[1] + "," + str(island3_guards)
            
    #     sigT = island1 + ";" + island2 + ";" + island3
    #     pirate.setTeamSignal(sigT)
        return 1

    if (
        (sw == "island1" and s[0] != "myCaptured")
        or (sw == "island2" and s[1] != "myCaptured")
        or (sw == "island3" and s[2] != "myCaptured")
    ):
        # if sw[-1] == "1":
        #     island1_guards += 1
        #     if island1==",,0":
        #         island1 = str(x-1) + "," + str(y+1) + "," + str(island1_guards)
        #     else:
        #         island1 = island1.split(',')[0] + "," + island1.split(',')[1] + "," + str(island1_guards)
        # if sw[-1] == "2":
        #     island2_guards += 1
        #     if island2==",,0":
        #         island2 = str(x-1) + "," + str(y+1) + "," + str(island2_guards)
        #     else:
        #         island2 = island2.split(',')[0] + "," + island2.split(',')[1] + "," + str(island2_guards)
        # if sw[-1] == "3":
        #     island3_guards += 1
        #     if island3==",,0":
        #         island3 = str(x-1) + "," + str(y+1) + "," + str(island3_guards)
        #     else:
        #         island3 = island3.split(',')[0] + "," + island3.split(',')[1] + "," + str(island3_guards)
            
        # sigT = island1 + ";" + island2 + ";" + island3
        # pirate.setTeamSignal(sigT)
        return 3

    if (
        (se == "island1" and s[0] != "myCaptured")
        or (se == "island2" and s[1] != "myCaptured")
        or (se == "island3" and s[2] != "myCaptured")
    ):
        # if se[-1] == "1":
        #     island1_guards += 1
        #     if island1==",,0":
        #         island1 = str(x+1) + "," + str(y+1) + "," + str(island1_guards)
        #     else:
        #         island1 = island1.split(',')[0] + "," + island1.split(',')[1] + "," + str(island1_guards)
        # if se[-1] == "2":
        #     island2_guards += 1
        #     if island2==",,0":
        #         island2 = str(x+1) + "," + str(y+1) + "," + str(island2_guards)
        #     else:
        #         island2 = island2.split(',')[0] + "," + island2.split(',')[1] + "," + str(island2_guards)
        # if se[-1] == "3":
        #     island3_guards += 1
        #     if island3==",,0":
        #         island3 = str(x+1) + "," + str(y+1) + "," + str(island3_guards)
        #     else:
        #         island3 = island3.split(',')[0] + "," + island3.split(',')[1] + "," + str(island3_guards)
            
        # sigT = island1 + ";" + island2 + ";" + island3
        # pirate.setTeamSignal(sigT)
        return 3
    
    if pirate.getCurrentFrame() >= 250:
        return random.randint(1, 4)
    
    if sigT!=",,0;,,0;,,0" and pirate.getCurrentFrame()>500:
        ##split using pipe first
        # adding new coordinates to island arrays

        # sending pirates to the unoccupied islands if number on island is less than reqd.
        if island1_guards>island_guards:
            if island1_guards>island_guards:
                if island3_guards>island_guards:
                    return central_pirates(pirate)
                elif island3.split(",")[0] != "":
                    return moveTo( int((island3.split(","))[0]) , int((island3.split(","))[1]) , pirate )
                else:
                    return central_pirates(pirate)
            elif island2.split(",")[0] != "":
                return moveTo( int((island2.split(","))[0]) , int((island2.split(","))[1]) , pirate )
            else:
                return central_pirates(pirate)
        elif island1.split(",")[0] != "":
            return moveTo( int((island1.split(","))[0]) , int((island1.split(","))[1]) , pirate )
        else:
            return central_pirates(pirate)

    if int(pirate.getID())>8:
        return central_pirates(pirate)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()
    if team.getCurrentFrame() == 1:
        team.setTeamSignal(",,0;,,0;,,0")
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    # if s:
    #     ####split using pipe and then split using semi-colon
    #     island_no = int(s[0])
    #     signal = l[island_no - 1]
    #     if signal == "myCaptured":
    #         team.setTeamSignal("")
