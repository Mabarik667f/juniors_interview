def strict(func):
    def wrapper(*args, **kwargs):
        
        ls_annotations = list(func.__annotations__.values())
        for i, v in enumerate(args):
            if type(v) != ls_annotations[i]:
                raise TypeError
        for k in kwargs:
            if type(kwargs[k]) != func.__annotations__[k]:
                raise TypeError
        return func(*args, **kwargs)
    return wrapper
