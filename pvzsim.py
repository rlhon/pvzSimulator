import plant
import zombie


obj_board = []

straightShooterIds = [1, 5, 7, 8, 9, 10, 12, 15, 18]
zombieCosts = [50, 75, 75, 125, 175, 350, 125, 125, 150]
zombieMetalTool = [0, 0, 0, 55, 70, 0, 5, 0, 25]

sunCost = [50, 100, 50, 50, 25, 175, 75, 125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

zombieDict = {
    "imp": [0,10,0],
    "con": [1,28,0],
    "pol": [2,17,0],
    "buc": [3,65,0],
    "foo": [4,80,0],
    "dan": [5,17,0], #UNUSED
    "dig": [6,15,0],
    "bun": [7,23,0],
    "lad": [8,42,0]
   
}

plantDict = {
#           id,hp,damage,period,range,negRange
    "brai": [0,6,0,0,0,0],        # brain
    "peas": [1,6,20,1.5,10,0],      # peashooter
    "sunf": [2,6,0,0,0,0],    # sunflower
    "wall": [3,72,0,0,0,0],        # walnut
    "pota": [4,1670,0,0,0],        # potato
    "snow": [5,6,20,1.5,0,0],      # snowpea
    "chom": [6,6,1670,1.5,0,0,False], # chomper, last state is to determine if it is eating
    "repe": [7,6,40,1.5,0,0],         # repeater
    "puff": [8,6,20,1.5,3,0],         # puff shroom
    "fume": [9,6,20,1.5,0,0],         # fume shroom
    "scar": [10,6,20,1.5,0,0],        # scaredy shroom
    "squa": [11,6,1670,0,1,1],        # squash
    "thre": [12,6,20,1.5,0,0],        # threepeater
    "spik": [13,6,20,1,0,0],        # spikeweed
    "torc": [14,6,0,0,0,0],        # torchwood
    "spli": [15,6,20,1.5,0,0],     # split pea
    "star": [16,6,20,1.5,0,0],        # starfruit
    "magn": [17,6,0,0,0,0],        # magnet shroom
    "kern": [18,6,1,3,0,0],        # kernel pult
    "umbr": [19,6,0,0,0,0],       # umbrella leaf
    "empt": [20,0,0,0,0,0]
}



def convertStringArray(arr):
    print(len(arr[0]))
    for i in range(0,len(arr)):
        for x in range(0, len(arr[i])):
            #print(arr[i][x])
            arr[i][x] = plantDict[arr[i][x].lower()[:4]]
    return arr

def reconvertArray(arr):
    for i in range(len(arr)):
        for x in range(0, len(arr[i])):
            key, list1 = list(plantDict.items())[arr[i][x][0]]
            arr[i][x] = key
    return arr
            

def convertZombieString(zombie1):
    return zombieDict[zombie1.lower()[:3]] #3 characters cause of imp

def calcdamage(arr):
    totaldmg = [0] * 5
    ind = 0
    for i in arr:
        templen = len(i)
        for x in i:
            if ((i) >= templen): # i should be changed to the range of the plant for damage
                totaldmg[ind] += i # i should be changed to the dmg per second of the plant
        templen += 1
    return totaldmg
                
                
def simulateState(zomb, laneNo):
    #zomb state length time * totaldmg[laneNo]  
    #if special plant in front i.e. butter (calculate probability, eating(if full no, )) 
    pass    

def simulate(zomb, laneNo):
    #placed down -> simulate state
    #starts eating -> simulate state continue until zombie dead or brain dead
    pass

def simulateStep(currMap1, zombie1, row, col):
    zombieStatus = True #alive
    
    row = int(row) - 1
    col = int(col)
    currMap = convertStringArray(currMap1)
    zombie = convertZombieString(zombie1)
    
    slowMult = 1
    iced = False
    for plant in currMap[row]: #currMap is from the GUI
        if (plant[0] == 5): #snowpea
            iced = True
        if (plant[0] == 14):#torchwood //what if torchwood is before the snowpea???
            iced = False
            
    if (iced):
        slowMult = 2
        
    for plant in currMap[row]:
        if (plant[0] == 18):
            slowMult *= 1.41 
            
    shootDPS = 0
    peasDPS = 0
    snowpeas = 0
    
    for i in range(0, col):
        plant = currMap[row][i]
        if (plant[0] in straightShooterIds):
            if (plant[0] == 18): #kernel
                shootDPS += 25/3
            elif (plant[0] == 7): #repeater
                shootDPS += 40/1.5
                peasDPS += 40/1.5
            elif(plant[0] == 8): #puff shroom
                shootDPS += 20/1.5
            else:
                shootDPS += 20/1.5
                if(plant[0] == 5):
                    snowpeas += 20/1.5
                else:
                    peasDPS += 20/1.5
        elif(plant[0] == 14):
            shootDPS += peasDPS
            
    totalDPS = shootDPS * slowMult   
    
    isMagnetRange = checkMagnet(currMap, row, col) 
    if (isMagnetRange):
        pass #if zombie has a metal object tool hp = 0
    
    if(col == 6):
        zombie[1] -= totalDPS *2 #FIX
    else:
        zombie[1] -= shootDPS * slowMult * zombie.walkingTime   #FIX
    
    col -= 1
    
    isMagnetRange = checkMagnet(currMap, row, col) 
    if (isMagnetRange):
        pass #if zombie has a metal object tool hp = 0
    
    if(currMap[row][col][0] == 4):
        currMap[row][col] = plant(plantDict["pota"])
        zombie.hp -= 1670 #FIX
        return(currMap)
    
     #if zombie is on a row before chomper, make chomper eating=true and kill zombie
    #if zombie is on a row before squash, kill squash and zombie

    #if zombie is on a spikeweed, zombie.hp -= walkingTime*20 and zombie.col++

    #if zombie is dead, return game board the same
    
    dmgWhileEating = totalDPS*3
    # #if dmgWhileEating > zombie.hp
    #     damage the plant a certain amount
    # else
    #     kill plant
    # #zombie.hp -= totalDPS*3 # eating time 3s

    # elif ()
    currMap = reconvertArray(currMap)
    return currMap, zombieStatus
    
      
            
def checkSpecialCases(currMap, zombie, row, col):
    if currMap[row][col][0] == 4:
        currMap[row][col] == plant("pota", 1670, 0, 0, 0)


def checkMagnet(currMap, row, col):
    for x in range(0, len(currMap)):
        for y in range(0, len(currMap[x])):
            if currMap[x][y][0] == 17 and abs(y - col) <= 2 and abs(x - row) <= 2:
                return True
    
    return False
            
    

