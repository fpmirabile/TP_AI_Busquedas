import random

class PacmanEnvironment:
    WALL = '#'
    PACMAN = 'P'
    GHOST = 'G'
    PILL = '*'
    EMPTY = ' '

    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
        self.pacman_position = self.get_start_position()
        self.pills = self.get_pill_positions()

    def print_grid(self):
        for row in self.grid:
            print(''.join(row))

    def get_start_position(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == self.PACMAN:
                    return (x, y)
        return None

    def get_pill_positions(self):
        positions = []
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == self.PILL:
                    positions.append((x, y))

        return positions

    def is_wall(self, position):
        x, y = position
        return self.grid[y][x] == self.WALL

    def is_valid_move(self, position):
        x, y = position
        return (0 <= x < self.width and 0 <= y < self.height and
                not self.is_wall(position) and
                position not in self.get_ghost_positions())

    def is_pill(self, position):
        x, y = position
        return self.grid[y][x] == self.PILL

    def eat_pill(self, position):
        x, y = position
        if self.is_pill(position):
            self.grid[y][x] = self.EMPTY
            self.pills.remove((x, y))  

    def move_pacman(self, position):
        x, y = position
        if not self.is_valid_move(position):
            return False

        old_x, old_y = self.pacman_position
        self.grid[old_y][old_x] = self.EMPTY
        self.pacman_position = position
        self.grid[y][x] = self.PACMAN

        if self.is_pill(position):
            self.eat_pill(position)

        return True

    def get_ghost_positions(self):
        positions = []
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == self.GHOST:
                    positions.append((x, y))
        return positions
    

def create_mock_environment(width = 15, height = 12, num_ghosts=3, pill_density=0.2, wall_density=0.1):
    if width < 3 or height < 3:
        raise ValueError("El ancho y el alto deben ser al menos 3.")

    WALL = '#'
    PACMAN = 'P'
    GHOST = 'G'
    PILL = '*'
    EMPTY = ' '

    # Crear el grid inicial con paredes en los bordes
    grid = [[WALL if x == 0 or y == 0 or x == width-1 or y == height-1 else EMPTY 
             for x in range(width)] for y in range(height)]

    # Posición inicial de Pac-Man
    pacman_x, pacman_y = 1, 1
    grid[pacman_y][pacman_x] = PACMAN

    # Colocar fantasmas
    for _ in range(num_ghosts):
        ghost_x, ghost_y = pacman_x, pacman_y
        while grid[ghost_y][ghost_x] != EMPTY or (ghost_x, ghost_y) == (pacman_x, pacman_y):
            ghost_x = random.randint(1, width - 2)
            ghost_y = random.randint(1, height - 2)
        grid[ghost_y][ghost_x] = GHOST

    # Colocar pastillas
    for y in range(1, height-1):
        for x in range(1, width-1):
            if grid[y][x] == EMPTY and random.random() < pill_density:
                grid[y][x] = PILL

    # Añadir paredes aleatorias en el interior
    for y in range(1, height-1):
        for x in range(1, width-1):
            if grid[y][x] == EMPTY and random.random() < wall_density:
                grid[y][x] = WALL

    return PacmanEnvironment(grid)

if __name__ == "__main__":
    env = create_mock_environment()
    env.print_grid()
