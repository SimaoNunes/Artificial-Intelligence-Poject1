import copy

a = [1,2,3,4,5]

b = copy.deepcopy(a)

b[0] = 2

print(a,b)



#------- FICHEIRO SEARCH--------
# import search
# from search import *
# class sol_state:
#     def __init__(self, board):
#         self.board = board
#     def __lt__(self, other):
#     def path_cost(self, c, s1, a, s2): return c+1
#     def h(self, node):       F=h
#        return node.state.pegs-1
# list < list    só primeiro
# DFS
# GREEDY
# A*

#--------classe-----------------
# class solitaire(problem):
#     def __init__(self, board):
#         self.initial = sol_state(board)
#     # metodos que implementam o problema de procura
#     def actions(self, state):
#     def result(self, state, action):
#     def goal_test(self, state): true se for solucao e false se nao for solucao (guardar num de pecas na classe)
