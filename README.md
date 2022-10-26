# LNX-runtime

- [LNX-runtime](#lnx-runtime)
  - [Architecture](#architecture)
  - [Development](#development)

Runtime responsible for creating games environment, running users code and returning the results through other microservices to LNX-frontend

## Architecture

Small runtime running users code in randomly generated environment. User can perform specific `callbacks` in order to change state of the games world. Then, changes to the world are printed to `stdout` which is captured by `runner` microservice and passed further until it reaches frontend service which displays it in a visual environment.

## Development

#### version 0.1:

- [X] Create basic classes for level, agents etc.
- [X] Add game main loop.
- [X] Users code execution inside `exec` using predefined `__builtins__`.