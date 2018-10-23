import copy

#-----------------------------------
#------------VARIAVEIS--------------    
#-----------------------------------

b1 = [ ["_","O","O","O","_"], 
       ["O","_","O","_","O"], 
       ["_","O","_","O","_"],
       ["O","_","O","_","_"],
       ["_","O","_","_","_"] ]

#-----------------------------------
#--------------TIPOS----------------    
#-----------------------------------

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


#-----------------------------------
#------------FUNCOES--------------    
#-----------------------------------

def board_perform_move(board, move):
    #definir coordenadas iniciais
    start  = move[0]
    lStart = pos_l(start)
    cStart = pos_c(start)
    #definir coordenadas finais
    final  = move[1]
    lFinal = pos_l(final)
    cFinal = pos_c(final)
    #verificar que o movimento e valido
    if(is_empty(board[lStart][lFinal])):
        return "Can't perform move because there is no peg in position " + str(move[0])
    #copiar tabuleiro
    replicaBoard = copy.deepcopy(board)
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

print(b1)
print(board_perform_move(b1, [(4,4),(4,3)]))


