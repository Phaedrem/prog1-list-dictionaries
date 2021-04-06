######################
# Name: Darren Bowers
# Coding 07
# Purpose: Files use to identify true planets and which of them are closest and farthest from the sun.
######################

import functions as fn

def main():
    # do not modify this function except while coding to help you figure
    # out the functions you are writing. before you submit, main() must be
    # returned to exactly this state or there may be severe grade penalty.
    
    sol = {"Uranus":[2750, 3000, 2880], "Mercury":[46, 70, 57], "Earth":[147, 152, 150], "Venus":[107, 109, 108], "Mars":[205, 249, 228], "Saturn":[1350, 1510, 1430], "Jupiter":[741, 817, 779], "Pluto":[4440, 7380, 5910], "Neptune":[4450, 4550, 4500]}
    status = [True, True, True, True, True, True, True, False, True]
    # note that the "arrays" above are what are known as "parallel arrays"
    # this means that have values that relate to each other. The first "True"
    # in status relates to "Uranus" in sol. The second "True" to "Mercury", etc.
    
    print()
    print("The closest by nearest distance is:", fn.closest(sol))
    print("The closest by furthest distance is:", fn.closest(sol, False))
    print("The furthest by nearest distance is:", fn.furthest(sol, False))
    print("The furthest by furthest distance is:", fn.furthest(sol))
    print("The list of all planets is:", fn.planets_list(sol, status))
    print()
    
main()
