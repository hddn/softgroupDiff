def decorator(argument):
    def true_decorator(function):
        def wrapper(*args, **kwargs):
            print 'Decorator arg is {}'.format(argument)
            return function(*args, **kwargs)
        return wrapper
    return true_decorator


@decorator('some_arg')
def some_function(*args, **kwargs):
    print(args)
    print(kwargs)
