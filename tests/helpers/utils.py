def create_code_file(code: 'String') -> 'String':
    '''
    Returns path to created file
    '''
    import tempfile
    path = tempfile.NamedTemporaryFile().name
    f = open(path, "a")
    f.write(code)
    f.close()
    return path
