# Pac-Man Python Project

## Description
This project implements a Pac-Man game simulation in Python, featuring two different execution modes: `main.py` and `main2.py`. The key difference between these two is the use of the `curses` library in `main.py` for a more interactive terminal interface, making `main2.py` more suitable for testing and non-interactive environments.

## Installation

### Requirements

Ensure you have Python installed on your system. This project requires Python 3.x.

### Setting up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. To set up a virtual environment, follow these steps:

1. Navigate to the project directory.
2. Run the following command to create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

  ```powershell
  venv\Scripts\activate
  ```

- On Unix or MacOS:

  ```bash
  source venv/bin/activate
  ```

### Installing Dependencies

After activating the virtual environment, install the required dependencies by running:

```bash
pip install -r requirements.txt
```


## Execution

To run the game, use one of the following commands:

- For the interactive version with curses:

```bash
python -m main
```

- For testing or non-interactive environments:

```bash
python -m main2
```

## Game Grid Examples

The game grid is randomly generated with walls, ghosts, and pills. Here are some examples of what the grid might look like:

```bash
##########
#P  *    #
# ###    #
#    ### #
# G      #
##########
```

In this example:

- `#` represents walls.

- `P` is Pac-Man.

- `*` are pills.

- `G` stands for ghosts.
