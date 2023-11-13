import heapq

# Este es el camino mas corto teniendo en cuenta el costo o peso
# y termina eligiendo el camino que tiene el costo mas bajo

def ucs(environment, start_position):
    current_position = start_position
    paths = []
    visited_global = set()

    while True:
        queue = [(0, current_position, [])]
        visited = set([current_position])
        found_pill = False

        while queue and not found_pill:
            cost, position, path = heapq.heappop(queue)
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
                    new_path = path + [next_position]
                    new_cost = cost + 1 # cost = 1 per movement
                    heapq.heappush(queue, (new_cost, next_position, new_path))  

        if not found_pill:
            break

    return paths
