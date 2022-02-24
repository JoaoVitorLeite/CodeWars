def is_divisible(*args, **kwargs):
    for i in args:
        if args[0] % i != 0:
            return False
    return True