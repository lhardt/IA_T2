from typing import Iterable, Set, Tuple

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
        # substitua a linha abaixo pelo seu codigo
        #raise NotImplementedError

    def __eq__(self, other):
        return self.estado == other.estado  and self.custo == other.custo
        
    def __hash__(self,other):
        return estado + "#" + acao + "#" + custo
        
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
    blankPostion = estado.find("_")
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
        novoNodo = Nodo(novoEstado[0], self, novoEstado[0], self.custo+1)
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
    # TODO
    return total

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

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
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
