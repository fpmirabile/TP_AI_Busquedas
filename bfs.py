from collections import deque

# Este algoritmo trata de encontrar la pastilla más cercana a la posición del pacman
# Por cada pastilla debemos reiniciar la queue ya que no hay forma de hacerlo de otra manera
# Pero la idea es conseguir el camino mas corto a un objetivo


def bfs(environment, start_position):
    current_position = start_position
    paths = []
    visited_global = set()

    while True:
        queue = deque([(current_position, [])])
        visited = set([current_position])
        found_pill = False

        while queue and not found_pill:
            position, path = queue.popleft() 
            if environment.is_pill(position) and position not in visited_global:
                visited_global.add(position)
                paths.append(path + [position])
                current_position = position
                found_pill = True
                break

            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_position = (position[0] + direction[0], position[1] + direction[1])
                if next_position not in visited and environment.is_valid_move(next_position):
                    visited.add(next_position)
                    queue.append((next_position, path + [next_position]))  
                    
        if not found_pill:
            break

    return paths