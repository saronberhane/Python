
# takes two integer and return true if n is a multipe of m
def is_multiple(n, m):
    if n % m == 0:
       return True
    else:
        return False

print(is_multiple(9, 9))