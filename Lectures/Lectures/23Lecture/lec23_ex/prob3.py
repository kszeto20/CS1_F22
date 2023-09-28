
def fib(n):
    if n == 0 or n == 1:
        return n
    total = 1
    one = 1
    two = 1
    
    for i in range(n-2):
        holder = two + one
        
        one = two
        two = holder

        total = holder
        
    return total

if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
