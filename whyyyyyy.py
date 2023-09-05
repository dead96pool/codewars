# dont know how this works!!!

def zero(f=None): return 0 if not f else f(0)

def temp(i):
    return "printing through the temp function"

print(zero(temp()))