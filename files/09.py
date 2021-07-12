import shelve
 
FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"
 
with shelve.open(FILENAME) as states:
    print(states["London"])
    print(states["Madrid"])

with shelve.open(FILENAME) as states:
 
    states["London"] = "United Kingdom"
    states["Brussels"] = "Belgium"
    for key in states:
        print(key, " - ", states[key])
