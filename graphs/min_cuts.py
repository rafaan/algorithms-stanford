import copy
import random
import numpy as np
import pandas as pd
import time

graph = {}
with open("/Users/rafaan/Desktop/week4.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "999999999")
        line = line.split("\t")
        line = [int(i) for i in line]
        graph[int(line[0])] = line[1:-1]

vertices = [int(i) for i in list(graph.keys())]
edges = []
for vertex, adjacent in graph.items():
    edge_list = [(vertex, i) for i in adjacent]
    edges.extend(edge_list)

def contract(vertices, edges):
    random_edge = random.choice(edges)
    v1 = random_edge[0]
    v2 = random_edge[1]
    edges = [(v2, j) if i == v1 else (i, j) for i, j in edges]
    edges = [(i, v2) if j == v1 else (i, j) for i, j in edges]
    edges = [i for i in edges if i not in [(v1, v1), (v2, v2)]]
    vertices = [i for i in vertices if i != v1]
    return vertices, edges

def random_contraction(vertices, edges):
    while len(vertices) > 2:
        vertices, edges = contract(vertices, edges)
    min_cut = len(edges)/2
    return vertices, edges, min_cut

min_cuts = []
start = time.time()

n = 200
for i in range(0, n):
    v = copy.deepcopy(vertices)
    e = copy.deepcopy(edges)
    v, e, mc = random_contraction(v, e)
    min_cuts.append(mc)
    if i % 50 == 0:
        end = time.time()
        elapsed = round((end - start)/60, 2)
        print("Completed: {}.  Elapsed time: {} minutes.  Current min_cut: {}.  Edges: n={}, set={}".format(i, elapsed, np.min(min_cuts), len(e), set(e)))
