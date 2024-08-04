from typing import Iterable, Set, Tuple
from queue import PriorityQueue
from queue import Queue

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.heuristic = 0
        # substitua a linha abaixo pelo seu codigo
        #raise NotImplementedError

    def __eq__(self, other):
        if other is None:
            return self is None 
        return self.estado == other.estado  and self.custo == other.custo
        
    def __hash__(self):
        return (self.estado + "#" + str(self.acao) + "#" + str(self.custo)).__hash__()

    def __lt__(self, other):
        return (self.getTotalHeuristic()) < (other.getTotalHeuristic()) 

    def getTotalHeuristic(self):
        return self.custo + self.heuristic
            
UP   = "acima"
DOWN = "abaixo"
LEFT = "esquerda"
RIGHT= "direita"
GOAL = "12345678_"

def getNeighbours(stringPos):
    #  | 0 1 2 |
    #  | 3 4 5 |
    #  | 6 7 8 | 
    if stringPos == 0:
        return [                       (RIGHT, 1), (DOWN, 3) ]
    if stringPos == 1:
        return [            (LEFT, 0), (RIGHT, 2), (DOWN, 4) ]
    if stringPos == 2:
        return [            (LEFT, 1),             (DOWN, 5) ]
    if stringPos == 3:
        return [(UP,   0),             (RIGHT, 4), (DOWN, 6) ]
    if stringPos == 4:
        return [(UP,   1),  (LEFT, 3), (RIGHT, 5), (DOWN, 7) ]
    if stringPos == 5:
        return [(UP,   2),  (LEFT, 4),             (DOWN, 8) ]
    if stringPos == 6:
        return [(UP,   3),             (RIGHT, 7)            ]
    if stringPos == 7:
        return [(UP,   4),  (LEFT, 6), (RIGHT, 8)            ]  
    if stringPos == 8:
        return [(UP,   5),  (LEFT, 7)                        ]
    
    print(" Neighbour for <" + str(stringPos) + ">?")
    raise NotImplementedError

def stringSwap(estado:str, i1:int, i2:int):
    novoEstado = list(estado)
    novoEstado[i1] = estado[i2]
    novoEstado[i2] = estado[i1]
    return ''.join(novoEstado)

def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    blankPostion = estado.find('_')
    neighbours = getNeighbours(blankPostion)
    succ = set()
    for neigh in neighbours:
        succ.add((neigh[0], stringSwap(estado, blankPostion, neigh[1])))
    return succ
    

def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    novosEstados = sucessor(nodo.estado)
    novosNodos = set()
    for novoEstado in novosEstados: 
        novoNodo = Nodo(novoEstado[1], nodo, novoEstado[0], nodo.custo+1)
        novosNodos.add(novoNodo)
    return novosNodos

def make_hamming_dist(e1:str, e2:str):
    total = 0
    for i in range(len(e1)):
        if e1[i] != e2[i]:
            total = total +1
    return total
   
def make_manhattan_dist(e1:str, e2:str):
    total = 0
    for i in range(len(e1)):
        if e1[i] != e2[i] and e1[i] != '_':
            posicao_atual = divmod(i, 3)
            alvo = divmod(int(e1[i]) - 1, 3)
            total += abs(posicao_atual[0] - alvo[0]) + abs(posicao_atual[1] - alvo[1])
    return total
        
def astar(estado:str, heuristicFunc)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    FINAL = "12345678_"
    explored = set()
    frontier = PriorityQueue()
    frontier.put(( 
        heuristicFunc(estado, FINAL) ,   Nodo(estado, None, None, heuristicFunc(estado, FINAL) ) 
    ))
    
    finalNode = None
    while not frontier.empty() :
        item = frontier.get()
        currNode = item[1]
        
        if currNode in explored:
            continue
        if currNode.estado == FINAL:
            finalNode = currNode
            break

        explored.add(currNode.estado)
        
        neighbours = expande(currNode)
        for neigh in neighbours:
            neigh.heuristic =  heuristicFunc(estado, FINAL)
            
            if neigh.estado not in explored:     
                frontier.put((neigh.getTotalHeuristic(), neigh))
        
    actions = []
    while finalNode != None and finalNode.acao != None:
        actions = [finalNode.acao] + actions
        finalNode = finalNode.pai
          
    if len(actions) == 0:
        actions = None
    return actions

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return astar(estado, make_hamming_dist)


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return astar(estado, make_manhattan_dist)  

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # Ou, simplesmente 
    #astar(estado,  lambda x:  "ordemDeChegada" ) 
    FINAL = "12345678_"
    explored = set()
    frontier = Queue()
    frontier.put((0,   Nodo(estado, None, None, 0)))
    
    finalNode = None
    while not frontier.empty() :
        item = frontier.get()
        currNode = item[1]
        
        if currNode in explored:
            continue
        if currNode.estado == FINAL:
            finalNode = currNode
            break

        explored.add(currNode.estado)
        
        neighbours = expande(currNode)
        for neigh in neighbours:
            
            if neigh.estado not in explored:     
                frontier.put((neigh.custo, neigh))
        
    actions = []
    while finalNode != None and finalNode.acao != None:
        actions = [finalNode.acao] + actions
        finalNode = finalNode.pai
          
    if len(actions) == 0:
        actions = None
    return actions

#opcional,extra
def dfs_aux(nodo, explorados):
    FINAL = "12345678_"

    if nodo.estado == FINAL:
        return [nodo.acao]

    neighbours = expande(nodo)
    
    explorados = explorados + [nodo.estado]
    for neigh in neighbours:
        if neigh.estado in explorados:
            continue
            
        ans = dfs_aux(neigh, explorados)
        if ans is not None: 
            return [nodo.acao] + ans
    return None

def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    atual = Nodo(estado, None, None, 0)
    return dfs_aux(atual, [])
        
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # Comparing the position of the slot with the final position. Closer is better.
    return astar(estado, (lambda e1, e2 : 10 - e1.find("_"))) 

