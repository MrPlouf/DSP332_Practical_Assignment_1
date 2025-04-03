import math
from algorithms import minimax_recursive, alphabeta_recursive

def generate_complete_tree(start_number, start_is_maximizing, max_depth, algorithm_choice, game_logic_funcs):

    game_tree = {} 
    if algorithm_choice == "Minimax":

        #Recursive function alled to build the tree
        minimax_recursive(number=start_number, depth=0, is_maximizing=start_is_maximizing, max_depth_limit=max_depth, game_logic=game_logic_funcs, tree_dict=game_tree)
        
        #debug of the trees
        print(game_tree)
        debug_tree(game_tree)

        return game_tree
    
    elif algorithm_choice == "Alpha-Beta":

        #Recursive function called for lpha-Beta
        alphabeta_recursive(number=start_number, depth=0, alpha=-math.inf, beta=math.inf, is_maximizing=start_is_maximizing, max_depth_limit=max_depth, game_logic=game_logic_funcs, tree_dict=game_tree)

        #debug agains
        print(game_tree)
        debug_tree(game_tree)

        return game_tree
    else:

        print(f"HUH ?! '{algorithm_choice}' is not an algo")
        return None

#Give node we're on in debug and possible children in debug
def debug_tree(game_tree):
    for node, data in game_tree.items():
            state_id = node
            children = data['children']
            values = data['value']
            print(f"Node {state_id}, value: {values}, next nodes poss: {children}")