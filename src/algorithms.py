import math

def evaluate(state, game_logic):
    if game_logic['is_terminal'](state):
        return -100
    possible_moves = game_logic['get_moves'](state)
    if possible_moves == [3] or possible_moves == [2] or possible_moves == [3,2] or possible_moves == [2,3]:
        return 100
    return len(possible_moves) * 10 

def minimax_recursive(number, depth, is_maximizing, max_depth_limit, game_logic, tree_dict):
    node_key = (number, is_maximizing)

    # Memoization Check
    if node_key in tree_dict:
        return tree_dict[node_key]['value']

    # Base Case Check
    if game_logic['is_terminal'](number) or depth >= max_depth_limit:
        heuristic_value = evaluate(number, game_logic) 
        tree_dict[node_key] = {'value': heuristic_value, 'best_move': None, 'children': {}}
        return heuristic_value

    # Recursive Step
    possible_moves = game_logic['get_moves'](number)
    children_nodes = {}
    best_move = None

    if not possible_moves:
        heuristic_value = evaluate(number, game_logic)
        tree_dict[node_key] = {'value': heuristic_value, 'best_move': None, 'children': {}}
        return heuristic_value

    if is_maximizing:
        max_eval = -math.inf
        for move in possible_moves:
            next_number = number // move
            child_key = (next_number, False)
            children_nodes[move] = child_key

            evaluation = minimax_recursive(next_number, depth + 1, False, max_depth_limit, game_logic, tree_dict)

            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move

        tree_dict[node_key] = {'value': max_eval, 'best_move': best_move, 'children': children_nodes}
        return max_eval

    else:  # Minimizing player
        min_eval = math.inf
        for move in possible_moves:
            next_number = number // move
            child_key = (next_number, True)
            children_nodes[move] = child_key

            evaluation = minimax_recursive(next_number, depth + 1, True, max_depth_limit, game_logic, tree_dict)

            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move

        tree_dict[node_key] = {'value': min_eval, 'best_move': best_move, 'children': children_nodes}
        return min_eval


def alphabeta_recursive(number, depth, alpha, beta, is_maximizing, max_depth_limit, game_logic, tree_dict):
    node_key = (number, is_maximizing)

    # Memoization Check
    if node_key in tree_dict:
        return tree_dict[node_key]['value']

    # Base Case Check
    if game_logic['is_terminal'](number) or depth >= max_depth_limit:
        heuristic_value = evaluate(number, game_logic)
        tree_dict[node_key] = {'value': heuristic_value, 'best_move': None, 'children': {}}
        return heuristic_value

    # Recursive Step
    possible_moves = game_logic['get_moves'](number)
    children_nodes = {}
    best_move = None

    if not possible_moves:
        heuristic_value = evaluate(number, game_logic)
        tree_dict[node_key] = {'value': heuristic_value, 'best_move': None, 'children': {}}
        return heuristic_value

    if is_maximizing:
        max_eval = -math.inf
        for move in possible_moves:
            next_number = number // move
            child_key = (next_number, False)
            children_nodes[move] = child_key

            evaluation = alphabeta_recursive(next_number, depth + 1, alpha, beta, False, max_depth_limit, game_logic, tree_dict)

            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move

            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break  # Beta cutoff

        tree_dict[node_key] = {'value': max_eval, 'best_move': best_move, 'children': children_nodes}
        return max_eval

    else:  # Minimizing player
        min_eval = math.inf
        for move in possible_moves:
            next_number = number // move
            child_key = (next_number, True)
            children_nodes[move] = child_key

            evaluation = alphabeta_recursive(next_number, depth + 1, alpha, beta, True, max_depth_limit, game_logic, tree_dict)

            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move

            beta = min(beta, evaluation)
            if beta <= alpha:
                break  # Alpha cutoff

        tree_dict[node_key] = {'value': min_eval, 'best_move': best_move, 'children': children_nodes}
        return min_eval
