"""
this code is for making the tree just change the (initial_number) var and make sure the number is divisible by 2 & 3 (multi by 6) it will show you a .png of the game tree
make sure you download graphviz


pip install graphviz

"""

import graphviz


def build_game_tree(current_number, player1_score, player2_score, depth, parent_node_id):
    node_id = f"{current_number}_{player1_score}_{player2_score}_{depth}"
    node_label = f"N:{current_number}\nP1:{player1_score}\nP2:{player2_score}"

    if current_number <= 10:
        return graphviz.Digraph(node_attr={
            'shape': 'box'}), node_id, f"Winner: {'Player 1' if player1_score > player2_score else 'Player 2' if player2_score > player1_score else 'Draw'}"

    dot = graphviz.Digraph(node_attr={'shape': 'box'})

    if parent_node_id:
        dot.node(node_id, label=node_label)
        dot.edge(parent_node_id, node_id)
    else:
        dot.node(node_id, label=node_label)

    if depth % 2 == 0:  # Player 1's turn
        if current_number % 2 == 0:
            child_dot1, child_node_id1, winner1 = build_game_tree(current_number // 2, player1_score, player2_score + 2,
                                                                  depth + 1, node_id)
            dot.subgraph(child_dot1)
        if current_number % 3 == 0:
            child_dot2, child_node_id2, winner2 = build_game_tree(current_number // 3, player1_score + 3, player2_score,
                                                                  depth + 1, node_id)
            dot.subgraph(child_dot2)
    else:  # Player 2's turn
        if current_number % 2 == 0:
            child_dot1, child_node_id1, winner1 = build_game_tree(current_number // 2, player1_score + 2, player2_score,
                                                                  depth + 1, node_id)
            dot.subgraph(child_dot1)
        if current_number % 3 == 0:
            child_dot2, child_node_id2, winner2 = build_game_tree(current_number // 3, player1_score, player2_score + 3,
                                                                  depth + 1, node_id)
            dot.subgraph(child_dot2)

    return dot, node_id, ""

# Example usage (start with an initial number)
# initial_number = 1002
# dot, _, _ = build_game_tree(initial_number, 0, 0, 0, None)
# dot.render('game_tree', format='png', view=True)