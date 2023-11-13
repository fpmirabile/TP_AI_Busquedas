from .dfs import dfs
from .bfs import bfs
from .ucs import ucs
from .a_star import a_star
from .pacman_environment import create_mock_environment

from time import sleep

def run_search(env, algorithm='dfs'):
    if algorithm == 'dfs':
        path = dfs(env, env.pacman_position)
        for position in path:
            env.move_pacman(position)
            env.print_grid()
            sleep(0.5)
            print("\n")
    elif algorithm == 'bfs':
        path = bfs(env, env.pacman_position)
        for all_paths in path:
            for position in all_paths:
                env.move_pacman(position)
                env.print_grid()
                sleep(0.5)
                print("\n")
    elif algorithm == 'ucs':
        path = ucs(env, env.pacman_position)
        for all_paths in path:
            for position in all_paths:
                env.move_pacman(position)
                env.print_grid()
                sleep(0.5)
                print("\n")
    elif algorithm == 'a':
        path = a_star(env, env.pacman_position)
        for all_paths in path:
            for position in all_paths:
                env.move_pacman(position)
                env.print_grid()
                sleep(0.5)
                print("\n")
        pass
    else:
        raise ValueError("Algoritmo desconocido. Elija 'dfs', 'bfs', 'ucs' o 'a'.")

    if not path:
        print("Mapa imposible.")
        return
    
    print(path)

def main():
    env = create_mock_environment()
    env.print_grid()
    algorithm = input("Seleccione el algoritmo de búsqueda (dfs, bfs, a o ucs): ").strip().lower()
    run_search(env, algorithm)

if __name__ == '__main__':
    main()