##############
# Name: Darren Bowers
# Coding 07
# Purpose: Files use to identify true planets and which of them are closest and farthest from the sun.
######################

def planets_list(sol, status):
    planets = []
    index = 0
    for key in sol:
        if status[index] == True:
            index += 1
            planets.append(key)
    return(planets)


def furthest(sol, mixflag=True):
    furthest = 0
    distance = 0
    for key in sol:
        if (mixflag):
            if sol[key][1] > distance:
                distance = sol[key][1]
                furthest = key
        else:
            if sol[key][0] > distance:
                distance = sol[key][0]
                furthest = key
    return(furthest)    


def closest(sol, mixflag=True):
    closest = 0
    distance = 10000
    for key in sol:
        if (mixflag):
            if sol[key][0] < distance:
                distance = sol[key][0]
                closest = key
        else:
            if sol[key][1] < distance:
                distance = sol[key][1]
                closest = key
    return(closest)





