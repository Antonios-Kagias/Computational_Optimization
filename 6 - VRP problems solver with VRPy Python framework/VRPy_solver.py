import tsplib95
from networkx import DiGraph
from vrpy import VehicleRoutingProblem
import numpy as np

# CVRP Explicit lower_col
def lowerCol(dim, Matrix_of_distances_1, problem):
    stoixeia= dim*(dim-1)/2
    all_numbers=[]
    for z in range(0,len(problem.as_keyword_dict()['EDGE_WEIGHT_SECTION'])):
        for arithmos_seiras in range(len(problem.as_keyword_dict()['EDGE_WEIGHT_SECTION'][z])):
          all_numbers.append(problem.as_keyword_dict()['EDGE_WEIGHT_SECTION'][z][arithmos_seiras])
    metritis_arithmou=0
    for i in range(dim-1,0,-1):
        list_0=np.zeros(dim-i)
        sthlh=all_numbers[:i]
        all_numbers=all_numbers[i:]
        list_0=np.append(list_0,sthlh)
        Matrix_of_distances_1[:,dim-i-1]=list_0
    for i in range(dim):
        for j in range(i,dim):
            Matrix_of_distances_1[i][j]=Matrix_of_distances_1[j,i]
    return(Matrix_of_distances_1)

# CVRP Explicit upper_col
def upperCol(dim, Matrix_of_distances_1, problem):
    stoixeia= dim*(dim-1)/2
    all_numbers=[]
    for z in range(0,len(problem.as_keyword_dict()['EDGE_WEIGHT_SECTION'])):
        for arithmos_seiras in range(len(problem.as_keyword_dict()['EDGE_WEIGHT_SECTION'][z])):
            all_numbers.append(problem.as_keyword_dict()['EDGE_WEIGHT_SECTION'][z][arithmos_seiras])
    metritis_arithmou=0
    for i in range(1,dim):
        list_0=np.zeros(dim-i)
        sthlh=all_numbers[:i]
        all_numbers=all_numbers[i:]
        list_0=np.append(sthlh,list_0)
        Matrix_of_distances_1[:,i]=list_0
    for j in range(dim):
        for i in range(j,dim):
            Matrix_of_distances_1[i][j]=Matrix_of_distances_1[j,i]
    return(Matrix_of_distances_1)


# Load the problem
problem = tsplib95.load("eil13.vrp")

G = problem.get_graph()
H = G.to_directed()

# EDGE_WEIGHT_TYPE: EXPLICIT
if (problem.edge_weight_type == "EXPLICIT"):
    distance_matrix = np.zeros((problem.dimension, problem.dimension))
    # EDGE_WEIGHT_FORMAT: LOWER_COL
    if (problem.edge_weight_format == "LOWER_COL"):
        distance_matrix = lowerCol(problem.dimension, distance_matrix, problem)
    # EDGE_WEIGHT_FORMAT: UPPER_COL
    elif (problem.edge_weight_format == "UPPER_COL"):
        distance_matrix = upperCol(problem.dimension, distance_matrix, problem)
# EDGE_WEIGHT_TYPE: ATT
elif (problem.edge_weight_type == "ATT"):
    distance_matrix = np.zeros((problem.dimension, problem.dimension))
    for x in range(len(list(problem.get_nodes()))):
        for y in range(len(list(problem.get_nodes()))):
            # Get distance between nodes x, y
            distance_matrix[x][y] = tsplib95.distances.pseudo_euclidean(problem.node_coords[x+1], problem.node_coords[y+1])
# EDGE_WEIGHT_TYPE: EUC_2D
elif (problem.edge_weight_type == "EUC_2D"):
    distance_matrix = np.zeros((problem.dimension, problem.dimension))
    for x in range(len(list(problem.get_nodes()))):
        for y in range(len(list(problem.get_nodes()))):
            # Get distance between nodes x, y
            distance_matrix[x][y] = tsplib95.distances.euclidean(problem.node_coords[x+1], problem.node_coords[y+1])


# Define Source and Sink nodes
for i in problem.depots:
    for v in range(problem.dimension):
        H.remove_edge(v+1, i)
        H.add_edge("Source", v+1, cost = distance_matrix[i][v])
        H.add_edge(v+1, "Sink", cost = distance_matrix[i][v])
H.remove_node(i)

# Remove edges from each node to itself [ (1, 1), (2, 2) etc. ]
for v in range(2, problem.dimension + 1):
    H.remove_edge(v, v)

# Add costs to edges
for i in range(1, problem.dimension):
    for j in range(1, problem.dimension):
        if (i != j):
            H.add_edge(i+1, j+1, cost = distance_matrix[i][j])

# Define the Vehicle Routing Problem
prob = VehicleRoutingProblem(H, load_capacity=problem.capacity)

# Solve and display solution value
prob.solve()
print(prob.best_value)
print(prob.best_routes)
