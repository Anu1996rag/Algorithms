"""This file implements the greedy algorithm """

# program to find out the best station for radio station which can cover
# atmost states

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

stations = {
            "kone": {"id", "nv", "ut"},
            "ktwo": {"wa", "id", "mt"},
            "kthree": {"or", "nv", "ca"},
            "kfour": {"nv", "ut"},
            "kfive": {"ca", "az"}
        }

# to hold all the final stations
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        # print(f"Common states between {states_needed} and {states} are : {covered}")
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)

    
