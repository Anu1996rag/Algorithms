from collections import deque

# declaring all the persons
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["claire"]
graph["claire"] = ["thom", "johnny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []


# function to print if the person is a seller or not
# this returns the boolean value if a person's name ends with 'm' or not
def is_person_seller(name):
    return name[-1] == 'm'


# logic for breadth-first search algorithm

def search(name):
    search_queue = deque()
    search_queue += graph[name] # adding the first degree node
    searched = []  # if the name is already searched
    while search_queue: # while the queue is not empty
        person = search_queue.popleft() # pop the first element from the leftmost side
        if not person in searched: # if the person is not in the searched list
            if is_person_seller(person):
                print("Person found:", person)
                return True                   # if the person is found, break out of the loop
            else:
                search_queue += graph[person] # attach the neighbouring nodes of the searched person
                searched.append(person) # add the name of that person to the searched list
    return False


search("you")
