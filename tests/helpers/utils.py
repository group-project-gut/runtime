def create_code_file(code: str) -> str:
    '''
    Returns path to created file
    '''
    import tempfile
    path = tempfile.NamedTemporaryFile().name
    f = open(path, "a")
    f.write(code)
    f.close()
    return path
