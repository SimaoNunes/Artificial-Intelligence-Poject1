from search import *
import copy

#-----------------------------------#
#------------VARIAVEIS--------------#    
#-----------------------------------#

b1=[
["_","O","O","O","_"],
["O","_","O","_","O"],
["_","O","_","O","_"],
["O","_","O","_","_"],
["_","O","_","_","_"]]

#-----------------------------------#
#--------------TIPOS----------------#    
#-----------------------------------#

# TAI content
def c_peg():
    return "O"
def c_empty():
    return "_"
def c_blocked ():
    return "X"
def is_empty(e):
    return e == c_empty()
def is_peg (e):
    return e == c_peg()
def is_blocked(e):
    return e == c_blocked()

# TAI pos
# Tuplo (l, c)
def make_pos(l, c):
    return (l, c)
def pos_l(pos):
    return pos[0]
def pos_c(pos):
    return pos[1]

# TAI move
# Lista [p_initial, p_final]
def make_move (i, f):
    return [i, f]
def move_initial (move):
    return move[0]
def move_final (move):
    return move[1]


#-----------------------------------#
#-------------FUNCOES---------------#
#-----------------------------------#

def board_perform_move(board, move):
    #definir coordenadas iniciais
    start  = move[0]
    lStart = pos_l(start)
    cStart = pos_c(start)
    #definir coordenadas finais
    final  = move[1]
    lFinal = pos_l(final)
    cFinal = pos_c(final)
    #copiar tabuleiro
    replicaBoard = copy.deepcopy(board)
    #verificar que o movimento e valido
    if(is_empty(board[lStart][cStart])):
        return replicaBoard 
    #colocar peca no novo local, bem como o lugar vazio deixado por ela
    replicaBoard[lStart][cStart] = c_empty()
    replicaBoard[lFinal][cFinal] = c_peg()
    #apagar a peca que foi comida - descobrir coordenadas da peca comida
    #caso a jogada seja na mesma linha, a linha mantem se
    if lStart == lFinal:
        removePeg = int((cStart+cFinal)/2)
        replicaBoard[lFinal][removePeg] = c_empty()
    #caso a jogada seja na mesma coluna, a coluna mantem se 
    else:
        removePeg = int((lStart+lFinal)/2)
        replicaBoard[removePeg][cFinal] = c_empty()
    #devolver novo tabuleiro
    return replicaBoard




def board_moves(board):
    lines   = len(board)
    columns = len(board[0])
    moves     = []
    # percorrer colunas
    for l in range(lines):
        # percorrer linhas
        for c in range(columns):
            # conteudo da posicao
            content = board[l][c]
            #Se for espaco vazio, entao ha possibilidade de haver jogada
            if(is_empty(content)):
                # teste das linhas de cima
                if l>=2 and l<lines and is_peg(board[l-1][c]) and is_peg(board[l-2][c]):
                    move = [ (l-2,c), (l,c) ]
                    moves.append(move)
                # teste das linhas da direita
                if l<lines-2 and is_peg(board[l+1][c]) and is_peg(board[l+2][c]):
                    move = [ (l+2,c), (l,c) ]
                    moves.append(move)
                # teste das colunas da esquerda
                if c>=2 and is_peg(board[l][c-1]) and is_peg(board[l][c-2]):
                    move = [ (l,c-2), (l,c) ]
                    moves.append(move)
                # teste das colunas de baixo
                if c<columns-2 and is_peg(board[l][c+1]) and is_peg(board[l][c+2]):
                    move = [ (l,c+2), (l,c) ]
                    moves.append(move)
    return moves


class sol_state:
    def __init__(self, board):
        self.board = board
        pegs = 0
        lines   = len(board)
        columns = len(board[0])
        # percorrer linhas
        for l in range(lines):
            # percorrer colunas
            for c in range(columns):
                # conteudo da posicao
                content = board[l][c]
                # se tiver peca, incrementar n
                if(is_peg(content)):
                    pegs+=1
        self.pegs = pegs
    def __lt__(self, other):
         return self.board < other.board
    def __eq__(self, other):
        return isinstance(other, sol_state) and self.board == other.board and self.pegs == other.pegs


class solitaire(Problem):
# """Models a Solitaire problem as a satisfaction problem.
# A solution cannot have more than 1 peg left on the board."""
    def __init__(self, board):
        self.initial = sol_state(board)
    def actions(self, state):
        return board_moves(state.board)
    def result(self, state, action):
        return sol_state(board_perform_move(state.board, action)) 
    def goal_test(self, state):
        if state.pegs == 1:
            return True
        else:
            return False
    def path_cost(self, c, state1, action, state2):
        return c+1
    def h(self, state):
        return state.pegs-1
        
# """Needed for informed search."""

#print(solitaire([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]).h(sol_state([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]])))
#print(solitaire([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]).result(sol_state([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]),[(3, 0), (3, 2)]).board)
