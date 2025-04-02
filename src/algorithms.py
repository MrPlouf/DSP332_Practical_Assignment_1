import math

def _minimax_recursive(number, depth, is_maximizing, max_depth_limit, game_logic, tree_dict):

    node_key = (number, is_maximizing)

    # 1. Memoization Check (using the shared tree_dict)
    if node_key in tree_dict:
        return tree_dict[node_key]['value']

    # 2. Base Case Check (Terminal State or Depth Limit)
    if game_logic['is_terminal'](number) or depth >= max_depth_limit:
        heuristic_value = game_logic['evaluate'](number, 0, 0) # Evaluate static potential
        tree_dict[node_key] = {'value': heuristic_value, 'best_move': None, 'children': {}}
        return heuristic_value

    # 3. Recursive Step
    possible_moves = game_logic['get_moves'](number)
    children_nodes = {}
    best_move = None

    # Handle cases where non-terminal but no moves (e.g., stuck num > 10)
    if not possible_moves:
        heuristic_value = game_logic['evaluate'](number, 0, 0)
        tree_dict[node_key] = {'value': heuristic_value, 'best_move': None, 'children': {}}
        return heuristic_value

    if is_maximizing:
        max_eval = -math.inf
        for move in possible_moves:
            next_number = number // move
            child_key = (next_number, False)
            children_nodes[move] = child_key # Store child reference *before* recursive call

            # Recursive call to evaluate the child
            evaluation = _minimax_recursive(next_number, depth + 1, False, max_depth_limit, game_logic, tree_dict)

            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
        # Store results for the current node in the shared tree_dict
        tree_dict[node_key] = {'value': max_eval, 'best_move': best_move, 'children': children_nodes}
        return max_eval

    else: # Minimizing player
        min_eval = math.inf
        for move in possible_moves:
            next_number = number // move
            child_key = (next_number, True)
            children_nodes[move] = child_key

            # Recursive call
            evaluation = _minimax_recursive(next_number, depth + 1, True, max_depth_limit, game_logic, tree_dict)

            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
        # Store results for the current node
        tree_dict[node_key] = {'value': min_eval, 'best_move': best_move, 'children': children_nodes}
        return min_eval


def _alphabeta_recursive(number, depth, alpha, beta, is_maximizing, max_depth_limit, game_logic, tree_dict):

    node_key = (number, is_maximizing)

    # 1. Memoization Check
    if node_key in tree_dict:
        # If already visited, return stored value, alpha/beta don't matter for this path now
        return tree_dict[node_key]['value']

    # 2. Base Case Check
    if game_logic['is_terminal'](number) or depth >= max_depth_limit:
        heuristic_value = game_logic['evaluate'](number, 0, 0)
        tree_dict[node_key] = {'value': heuristic_value, 'best_move': None, 'children': {}}
        return heuristic_value

    # 3. Recursive Step
    possible_moves = game_logic['get_moves'](number)
    children_nodes = {}
    best_move = None

    if not possible_moves:
        heuristic_value = game_logic['evaluate'](number, 0, 0)
        tree_dict[node_key] = {'value': heuristic_value, 'best_move': None, 'children': {}}
        return heuristic_value

    if is_maximizing:
        max_eval = -math.inf
        for move in possible_moves:
            next_number = number // move
            child_key = (next_number, False)
            # Store child key before recursive call in case of pruning
            children_nodes[move] = child_key

            evaluation = _alphabeta_recursive(next_number, depth + 1, alpha, beta, False, max_depth_limit, game_logic, tree_dict)

            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move

            alpha = max(alpha, evaluation)
            if beta <= alpha:
                # print(f"Pruning (Beta): a={alpha}, b={beta} at {node_key}, move {move}") # Debug
                break # Beta cutoff

        # Store results even if pruned (stores partial children list in that case)
        tree_dict[node_key] = {'value': max_eval, 'best_move': best_move, 'children': children_nodes}
        return max_eval

    else: # Minimizing player
        min_eval = math.inf
        for move in possible_moves:
            next_number = number // move
            child_key = (next_number, True)
            children_nodes[move] = child_key

            evaluation = _alphabeta_recursive(next_number, depth + 1, alpha, beta, True, max_depth_limit, game_logic, tree_dict)

            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move

            beta = min(beta, evaluation)
            if beta <= alpha:
                # print(f"Pruning (Alpha): a={alpha}, b={beta} at {node_key}, move {move}") # Debug
                break # Alpha cutoff

        tree_dict[node_key] = {'value': min_eval, 'best_move': best_move, 'children': children_nodes}
        return min_eval