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

# write a function called planets_list()
# pass it the planets dictionary and status list
# return the list of planets that are true planets
# base on the status list
#
# you may NOT use python methods; min, max, sum, or mean
# or any "magic" functions. you must use a loop to do
# this manually

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


# write a function called furthest()
# pass it the planets dictionary and an OPTIONAL boolean flag
# the flag decides if you use the CLOSEST distance or the FURTHEST
# distance to decide which planet is furthest
# in other words, use index 0 or 1 from the distance lists
# return the name of the furthest planet
#
# you may not use python methods; min, max, sum, or mean
# or any "magic" functions. you must use a loop to do
# this manually

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


# write a function called closest()
# pass it the planets dictionary and an OPTIONAL boolean flag
# the flag decides if you use the CLOSEST distance or the FURTHEST
# distance to decide which planet is closest
# in other words, use index 0 or 1 from the distance lists
# return the name of the closest planet
#
# you may not use python methods; min, max, sum, or mean
# or any "magic" functions. you must use a loop to do
# this manually




