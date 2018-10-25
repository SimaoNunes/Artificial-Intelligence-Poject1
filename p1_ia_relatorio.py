from search import *
from utils  import *
from projeto  import *
import time

game5x5 = [["_","O","O","O","_"], ["O","_","O","_","O"], ["_","O","_","O","_"], ["O","_","O","_","_"], ["_","O","_","_","_"]]
game4x4 = [["O","O","O","X"], ["O","O","O","O"], ["O","_","O","O"], ["O","O","O","O"]]
game4x5 = [["O","O","O","X","X"], ["O","O","O","O","O"], ["O","_","O","_","O"], ["O","O","O","O","O"]]
game4x6 = [["O","O","O","X","X","X"], ["O","_","O","O","O","O"], ["O","O","O","O","O","O"], ["O","O","O","O","O","O"]]

games     = [game5x5, game4x4, game4x5, game4x6]
gameNames = ['game5x5', 'game4x4', 'game4x5', 'game4x6']

game      = solitaire(game5x5)
numGame   = 0
print()

while (numGame < 4):
    print('###' + gameNames[numGame] + '###')
    print()
    game = solitaire(games[numGame])

    p = InstrumentedProblem(game)

    start  = time.time()
    result = greedy_best_first_graph_search(p, p.h)
    end    = time.time()
    print('greedy_best_first_graph_search:')
    print(end - start)
    print('Nos expandidos ->' + str(p.succs))
    print('Nos gerados    ->' + str(p.goal_tests))
    print(p.states)
    print()

    start  = time.time()
    result = astar_search(p)
    end    = time.time()
    print("astar_search:")
    print(end-start)
    print("Nos expandidos ->" + str(p.succs))
    print("Nos gerados    ->" + str(p.goal_tests))
    print(p.states)
    print()

    start  = time.time()
    result = depth_first_tree_search(p)
    end    = time.time()
    print("depth_first_tree_search:")
    print(end-start)
    print("Nos expandidos ->" + str(p.succs))
    print("Nos gerados    ->" + str(p.goal_tests))
    print(p.states)
    print()
    print()

    numGame += 1
