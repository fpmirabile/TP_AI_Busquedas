import heapq

# Utiliza una funcion de costo para determinar la ruta mas eficiente hacia un objetivo
# Necesita de una funcion heuristica para tener eficiencia, que logra un csto mas bajo desde un punt odado hasta el objetivo

# Funcion heuristica
# Sirve en este caso pq implementamos el pacman como una cuadricula, y es efectiva para determinar el costo (o distancia)
# mas bajo entre dos puntos. Aparte es simple
def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def a_star(environment, start_position):
    current_position = start_position
    paths = []
    visited_global = set()
    pill_positions = environment.get_pill_positions()

    while pill_positions:
        queue = [(0, current_position, [])]
        visited = set([current_position])

        while queue:
            _, position, path = heapq.heappop(queue)

            if position in pill_positions:
                pill_positions.remove(position)
                paths.append(path + [position])
                current_position = position
                break

            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_position = (position[0] + direction[0], position[1] + direction[1])
                if next_position not in visited and environment.is_valid_move(next_position):
                    visited.add(next_position)
                    new_path = path + [next_position]
                    heuristic_cost = manhattan_distance(next_position, min(pill_positions, key=lambda x: manhattan_distance(next_position, x)))
                    total_cost = len(new_path) + heuristic_cost
                    heapq.heappush(queue, (total_cost, next_position, new_path))  

    return paths
