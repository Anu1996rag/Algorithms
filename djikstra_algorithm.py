'''This file shows the simple implementation of djikstra's algorithm.'''

# declaring the nodes of the graph

graph = {}

# from the start node , adding the neighbors of the start node
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# from node a, also adding the costs or weights of the neighboring nodes
graph["a"] = {}
graph["a"]["finish"] = 1

# from node b, also adding the costs or weights of the neighboring nodes
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["finish"] = 5

# finish node
graph["finish"] = {}

# creating a costs dictionary which stores all the weights or costs which we achieve to get to the node
infinity = float("inf") # for declaring infinite value

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["finish"] = infinity

# parents dictionary to hold the record of the parent node of each node in the graph
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None

# Finally , we need a list to keep the track of all the visited nodes so that we do not take the visited node again.
visited = []

# lets define a function which finds the node with the lowest cost
def find_lowest_cost_node(costs_of_nodes):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs_of_nodes:
        cost = costs_of_nodes[node]
        if cost < lowest_cost and node not in visited : # if the cost of the passed node is less and the node is not visited yet
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# lets define a function which calculates the shortest path
# find the node with the lowest cost that has not been visited yet.
node = find_lowest_cost_node(costs)
print("Lowest Cost node is:", node)
# keep searching till all the nodes are not visited
while node is not None:
    cost_of_the_node = costs[node]  # get the cost of the lowest node and list all of its neighboring nodes
    neighbors = graph[node]
    print("Neighbours of the node {} are:{}".format(node,neighbors))
    for every_neighbor in neighbors.keys():
        new_cost = cost_of_the_node + neighbors[every_neighbor] # if its cheaper to get to this neighbor by going
        print("New cost calculated for node {} is {}:".format(every_neighbor,new_cost))
        if costs[every_neighbor] > new_cost:                    # through this node
            print("Costs of the neighbors updated.")
            costs[every_neighbor] = new_cost                    # update the cost of this node
            parents[every_neighbor] = node                      # this node becomes the new parent
            print("Added the node {} as the parent node".format(node))
    visited.append(node)
    node = find_lowest_cost_node(costs) # find the next node to process and loop
    print("New node with the lowest cost which is not visited yet :",node)

print("Updated parents:",parents)
print("Visited Nodes:", visited)
print("Shortest possible path from start to finish :",visited)





