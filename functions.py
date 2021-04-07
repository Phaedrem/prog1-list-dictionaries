##############
# Name: Darren Bowers
# Coding 07
# Purpose: Files use to identify true planets and which of them are closest and farthest from the sun.
######################

def planets_list(sol, status):
# I tried a whole bunch of stuff but I recreated a streamlined version
# of my throught process below


# This is where I started - the way I understand this is it couldn't check if
# status was true because the index of sol were keys instead of 0,1,2 etc. 
    planets = [] #TypeError: list indices must be intergers or slices, not str
    for key in sol:
        if status[key] == True:
            planets.append(sol[key])
    return(planets)

# So I made this instead, using that to cycle through status indexes to verify
# if true. But I get the KeyError on line 15. Which if I understand correctly means
# when its trying to append planets it's using the index of status and not finding
# a corresponding element. I don't understand why though. 
    planets = [] #KeyError: 0
    for key in range(len(status)):
        if status[key] == True:
            planets.append(sol[key])
    return(planets)

# So I added an extra loops thinking this way it would grab the keys instead of 
# an element associated with the index of status. But it just pulled the elements
# over and over.
    planets = [] # Grabs full list elements over and over
    for i in range(len(status)):
        if status[i] == True:
            for key in sol:
                planets.append(sol[key])
    return(planets)

# Since the last one was grabbing elements, I thought reducing it from (sol[key])
# to (key) would resolve that, but it grabs the entire list of keys instead
# of one at a time
    planets = [] #Grabs all keys, over and over. 
    for i in range(len(status)):
        if status[i] == True:
            for key in sol:
                planets.append(key)
    return(planets)

# So I thought maybe its because the loop for sol in inside the loop of status
# and I moved it around a bit but then that grabs multiples of the keys again
    planets = []
    for key in sol:
        for i in range(len(status)):
            if status[i] == True:
                planets.append(key)
    return(planets)

# From there thats where I decided to pull the two loops apart.
    full_list = [] #works but inefficent 
    planets = []
    for key in sol:
        full_list.append(key)

    for value in range(len(status)):
        if status[value] == True:
            planets.append(full_list[value])
    return(planets)

# write a function called planets_list()
# pass it the planets dictionary and status list
# return the list of planets that are true planets
# base on the status list
#
# you may NOT use python methods; min, max, sum, or mean
# or any "magic" functions. you must use a loop to do
# this manually




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




