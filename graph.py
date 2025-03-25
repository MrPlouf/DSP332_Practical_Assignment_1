import graphviz


class GameGraph:
    @staticmethod
    def generate_game_tree(initial_number, human_score, computer_score):
        def build_tree(current_number, p1_score, p2_score, depth, parent_id, dot):
            node_id = f"{current_number}_{p1_score}_{p2_score}_{depth}"
            label = f"N:{current_number}\nP1:{p1_score}\nP2:{p2_score}"

            dot.node(node_id, label=label)
            if parent_id:
                dot.edge(parent_id, node_id)

            if current_number <= 10 or (current_number % 2 != 0 and current_number % 3 != 0):
                return

            if current_number % 2 == 0:
                build_tree(current_number // 2, p1_score, p2_score + 2, depth + 1, node_id, dot)
            if current_number % 3 == 0:
                build_tree(current_number // 3, p1_score + 3, p2_score, depth + 1, node_id, dot)

        dot = graphviz.Digraph(node_attr={'shape': 'box'})
        build_tree(initial_number, human_score, computer_score, 0, None, dot)
        dot.render('game_tree', format='png', view=True)
