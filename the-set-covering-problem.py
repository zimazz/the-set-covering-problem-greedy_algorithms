#make a list of all the states i want to cover
statesNeeded = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

#a dictionary containing the stations with all states they cover
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

#a set to hold the final set of stations
finalStations = set()

#loop until statesNeeded is empty
while statesNeeded:
    bestStation = None
    statesCovered = set()
    for station, states in stations.items():
        covered = statesNeeded & states             #union between statesNedded amd states
        if len(covered) > len(statesCovered):       #check if this station covers more states than the best one so far
            bestStation = station                   #change the best station to that station
            statesCovered = covered                 #change statsesCovered to these states
    statesNeeded -= statesCovered                   #remove these states from the statesNeeded set
    finalStations.add(bestStation)                  #add the station to the finalStation set

print(finalStations)
