def dfs(environment, start_position):
    stack = [(start_position, [start_position])]
    visited = set()
    pills_collected = set()
    all_pills = set(environment.get_pill_positions())
    final_path = None

    while stack:
        position, path = stack.pop()

        if environment.is_pill(position) and position not in pills_collected:
            pills_collected.add(position)
            if pills_collected == all_pills:
                final_path = path

        if position in visited:
            continue

        visited.add(position)

        for direction in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            next_position = (position[0] + direction[0], position[1] + direction[1])
            if environment.is_valid_move(next_position) and next_position not in visited:
                stack.append((next_position, path + [next_position]))

    return final_path
