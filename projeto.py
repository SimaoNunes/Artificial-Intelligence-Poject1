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




def board_moves(b):
    columns = len(b)
    lines   = len(b[0])
    res     = []
    # percorrer colunas
    for l in range(lines):
        # percorrer linhas
        for c in range(columns):
            # conteudo da posicao
            content = b[c][l]
            #Se for espaco vazio, entao ha possibilidade de haver jogada
            if(is_empty(content)):
                # teste das linhas da esquerda
                if l>=2 and l<lines and b[c][l-1] == c_peg() and b[c][l-2] == c_peg():
                    move = [ (c,l-2), (c,l) ]
                    res.append(move)
                # teste das linhas da direita
                if l<lines-2 and b[c][l+1] == c_peg() and b[c][l+2] == c_peg():
                    move = [ (c,l+2), (c,l) ]
                    res.append(move)
                # teste das colunas de cima
                if c>=2 and b[c-1][l] == c_peg() and b[c-2][l] == c_peg():
                    move = [ (c-2,l), (c,l) ]
                    res.append(move)
                # teste das colunas de baixo
                if c<columns-2 and b[c+1][l] == c_peg() and b[c+2][l] == c_peg():
                    move = [ (c+2,l), (c,l) ]
                    res.append(move)
    return res


class sol_state:
    def __init__(self, board):
        self.board = board 
    def __lt__(self, other):
         return self.board < other.board
    def is_goal(self):
        n = 0
        columns = len(self.board)
        lines   = len(self.board[0])
        # percorrer colunas
        for c in range(columns):
            # percorrer linhas
            for l in range(lines):
                # conteudo da posicao
                content = self.board[c][l]
                # se tiver peca, incrementar n
                if(is_peg(content)):
                    n+=1
                    if n>1:
                        return False
        return True

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
        return state.is_goal()
    def path_cost(self, c, state1, action, state2):
        return c+1
    def h(self, state):
        return len(self.actions(state))
# """Needed for informed search."""
