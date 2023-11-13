from .dfs import dfs
from .bfs import bfs
from .ucs import ucs
from .a_star import a_star
from .pacman_environment import create_mock_environment

import curses
from time import sleep

def ui_show(position, env, stdscr):
    if env.move_pacman(position):
        stdscr.clear()
        for i, row in enumerate(env.grid):
            stdscr.addstr(i, 0, ''.join(row))
        stdscr.refresh()
        sleep(0.3)
    else:
        stdscr.addstr(env.height, 0, "Invalid move attempted.")
        stdscr.refresh()

def run_search(stdscr, env, algorithm='dfs'):
    if algorithm == 'd':
        path = dfs(env, env.pacman_position)
        for position in path:
            ui_show(position, env, stdscr)
    elif algorithm == 'b':
        path = bfs(env, env.pacman_position)
        for all_paths in path:
            for position in all_paths:
                ui_show(position, env, stdscr)
    elif algorithm == 'a':
        path = a_star(env, env.pacman_position)
        for all_paths in path:
            for position in all_paths:
                ui_show(position, env, stdscr)
    elif algorithm == 'u':
        path = ucs(env, env.pacman_position)
        for all_paths in path:
            for position in all_paths:
                ui_show(position, env, stdscr)
    else:
        raise ValueError("Algoritmo desconocido. Elija 'dfs' o 'bfs'.")
    
    if not path:
        stdscr.addstr("No path found to all pills.")
        stdscr.refresh()
        sleep(2)
        return

    

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr("Seleccione el algoritmo de búsqueda (d para DFS, b para BFS, u para UCS, a para A*): ")
    stdscr.refresh()

    algorithm = ''
    while algorithm not in ('d', 'b', 'u', 'a'):
        try:
            key = stdscr.getkey()
            if key in ('d', 'b', 'u', 'a'):
                algorithm = key
        except curses.error:
            continue

    stdscr.clear()
    stdscr.refresh()
    env = create_mock_environment()
    run_search(stdscr, env, algorithm)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass