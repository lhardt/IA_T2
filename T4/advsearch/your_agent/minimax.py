import random
from typing import Tuple, Callable

def maximization(state, alfa, beta, player, depth, max_depth, eval_func):
    if (state.is_terminal() or (max_depth > 0 and depth >= max_depth)):
        return eval_func(state, player), None
    value = float("-inf")
    action = None
    for legal_move in state.legal_moves():
        next_state = state.next_state(legal_move)
        pot_value, _ = min_gain(next_state, alfa, beta, player, depth + 1, max_depth, eval_func)
        if (pot_value > value):
            value = pot_value
            action = legal_move
        alfa = max(alfa, value)
        if (alfa >= beta):
            break
    return value, action

def minimization(state, alfa, beta, player, depth, max_depth, eval_func):
    if (state.is_terminal() or (max_depth > 0 and depth >= max_depth)):
        return eval_func(state, player), None
    value = float("+inf")
    action = None
    for legal_move in state.legal_moves():
        next_state = state.next_state(legal_move)
        pot_value, _ = max_gain(next_state, alfa, beta, player, depth + 1, max_depth, eval_func)
        if pot_value < value:
            value = pot_value
            action = legal_move
        beta = min(beta, value)
        if beta <= alfa:
            break
    return value, action

def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    player = state.player
    value, action =  max_gain(state, float("-inf"), float("+inf"), player, 0, max_depth, eval_func)
    return action
