""" Program to return shortest equivalent path names """


def shortest_equivalent_path(path: str) -> str:
    if not path:
        raise ValueError("Path invalid")

    path_names = []
    # special case : which starts with '/' , which is an absolute path
    if path[0] == '/':
        path_names.append('/')

    for token in (file_name for file_name in path.split('/') if file_name not in ['.', ' ']):
        print(f'token from split path : {token}')
        if token == "..":
            if not path_names or path_names[-1] == "..":
                path_names.append(token)
            else:
                if path_names[-1] == "/":
                    raise ValueError("Path invalid")
                path_names.pop()
        else:
            path_names.append(token)

    result = '/'.join(path_names)
    # avoid starting with "//"
    return result[result.startswith("//"):]


print(shortest_equivalent_path("sc//./../tc/awk/././"))
