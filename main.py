#/bin/python

# Main entrypoint of runtime microservice

from src.runtime import Runtime

if __name__ == '__main__':
     with open('usr/test-agent.py', 'r') as code_file:
          code = code_file.read()
          runtime = Runtime(code)
          runtime.run()