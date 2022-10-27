#!/bin/bash

# Entry point for container running !unsafe! user code

file_name="code.py"

python "/runtime/main.py" "/code/$file_name"
