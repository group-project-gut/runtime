# lynx-runtime

- [lynx-runtime](#lynx-runtime)
  - [Architecture](#architecture)
  - [Development](#development)
      - [version 0.1:](#version-01)

Runtime responsible for creating game's environment, running user's code and returning the results through other microservices to lynx-frontend.

## Architecture

Small runtime running user's code in randomly generated environment. User can perform specific `callbacks` in order to change state of the game's world. Then, changes to the world are printed to `stdout` which is captured by `runner` microservice and passed further until it reaches frontend service which displays it in a visual environment.

## Running in container
In order to run `code.py` found inside `./usr` directory use:

    podman run -v./usr/:/code:ro lynx-runtime:0.1

## Development

#### version 0.1:

- [X] Create basic classes for level, agents etc.
- [X] Add game main loop.
- [X] User's code execution inside `exec` using predefined `__builtins__`.