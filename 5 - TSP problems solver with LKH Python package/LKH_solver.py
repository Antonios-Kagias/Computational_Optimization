import tsplib95
import lkh
import networkx as nx
import matplotlib.pyplot as plt

# ----------- PROBLEMS THAT WERE TESTED ----------- CHANGE FILENAME FROM HERE -----------
# a280.tsp
# att48.tsp
# bayg29.tsp
# berlin52.tsp
# eil51.tsp

# br17.atsp
# p43.atsp

# ESC07.sop
# ESC11.sop


# Filename
my_file = "ESC07.sop"

# Define solver and problem path and load the problem
solver_path = "C:/Users/Antoine/Downloads/LKH-3.exe"
problem_path = "C:/Users/Antoine/source/repos/Assignment_LKH/" + my_file
problem=tsplib95.load(problem_path)

# Solve problem and get tour
tour = lkh.solve(solver=solver_path, problem=problem, max_trials=10000, runs=10)

# Create and write tour file
tour_file = open(problem.name + ".opt.tour", "w")
tour_file.write("NAME : " + problem.name + ".opt.tour\n" + \
    "COMMENT : Optimum solution of " + problem.name + "\n" + \
    "TYPE : TOUR\n" + \
    "DIMENSION : " + str(problem.dimension) + "\n" + \
    "TOUR_SECTION\n")
for i in range(len(tour[0])):
    tour_file.write(str(tour[0][i]) + "\n")
tour_file.write("-1\nEOF\n")
tour_file.close()


# Load tour file
opt = tsplib95.load("C:/Users/Antoine/source/repos/Assignment_LKH/" + problem.name + ".opt.tour")

# Print problem name and the optimal tour
print ("PROBLEM NAME: " + problem.name)
print ("OPTIMAL TOUR: " + str(opt.tours[0]))

# Get the problem's graph
G = problem.get_graph()
# Delete default nodes and edges (default edges contain all available edges!)
G.clear()
# Get the nodes from the tour
nodes = opt.tours[0]

# Assign the new nodes and edges to the graph
for i in range(len(opt.tours[0])-1):
    G.add_node(nodes[i])
    G.add_edge(nodes[i], nodes[i+1])

# Plot the graph showing the tour
if (problem.node_coords):
    nx.draw_networkx(G, pos=problem.node_coords, node_size=50, edgelist=G.edges, with_labels = True, node_color='lightblue')
    plt.title("Network Graph of the Tour")
    plt.show()
elif (problem.display_data):
    nx.draw_networkx(G, pos=problem.display_data, node_size=50, edgelist=G.edges, with_labels = True, node_color='lightblue')
    plt.title("Network Graph of the Tour")
    plt.show()
else:
    nx.draw_networkx(G, node_size=50, edgelist=G.edges, with_labels = True, node_color='lightblue')
    plt.title("Network Graph of the Tour")
    plt.show()

