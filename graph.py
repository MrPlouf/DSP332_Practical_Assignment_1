import graphviz

import GameLogic as gl
class GameGraph:
    @staticmethod
    def build_game_tree(current_number, player1_score, player2_score, depth=0, parent_node_id=None, dot=None):
        if dot is None:
            dot = graphviz.Digraph(node_attr={'shape': 'box'})

        node_id = f"{current_number}_{player1_score}_{player2_score}_{depth}"
        node_label = f"N:{current_number}\nP1:{player1_score}\nP2:{player2_score}"
        dot.node(node_id, label=node_label)

        if parent_node_id:
            dot.edge(parent_node_id, node_id)

        if current_number > 10:
            for move in gl.GameLogic.valid_moves(current_number):
                new_number, score = gl.GameLogic.apply_move(current_number, move, 'human' if depth % 2 == 0 else 'computer')
                new_p1_score = player1_score + (score if depth % 2 == 0 else 0)
                new_p2_score = player2_score + (score if depth % 2 == 1 else 0)
                GameGraph.build_game_tree(new_number, new_p1_score, new_p2_score, depth + 1, node_id, dot)

        return dot

    @staticmethod
    def render_tree(dot):
        dot.render('game_tree', format='png', view=True)