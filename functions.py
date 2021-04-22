from numbers import Number

FUNCTIONS = {
    'a': lambda x: x ** 2,
    'b': lambda x: 2 * x + 1,
    'c': lambda x: x - 1,
    'd': lambda x: x / 10,
    'e': lambda x: x + 10,
    'f': lambda x: x / 2,
}


def resolve(func: str, value: Number):
    """
    Takes func and value.
    If provided a not existing
    function, return original value.
    """
    try:
        result = FUNCTIONS[func](value)
    except (KeyError, TypeError):
        return value
    else:
        return result


def resolve_consistently(funcs: list, value: Number):
    """
    Takes the list of functions and value.
    Applies all the functions to the value.
    """
    for func in funcs:
        value = resolve(func, value)
    return value


def resolve_list_consistently(funcs: list, values: list):
    """
    Takes the list of functions and values
    and applies all the functions to each value.
    """
    results = []
    for value in values:
        results.append(resolve_consistently(funcs, value))
    return results
