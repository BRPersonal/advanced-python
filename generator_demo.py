def fibonacci():
    """Infinite FIbnocci sequence generator"""
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b #rhs will fully evaluate first and then assignment will happen

def filter_even(generator):
    """Filter even numbers from a generator"""
    for num in generator:
        if num % 2 == 0:
            yield num

def take(n,generator):
    """Take first n items from a generator"""
    for _ in range(n):
        yield next(generator)

#create a generator pipeline that prints first 20 even fibnocci numbers
fib = fibonacci()
even_fib = filter_even(fib)
first_twenty_even_fib = take(20,even_fib)
print("--------First twenty even fibonacci numbers------")
for num in first_twenty_even_fib:
    print(num)

fib2 = fibonacci()
first_20_fib = take(20, fib2)
even_fib = filter_even(first_20_fib)
print("--------Even numbers wthin first twenty fibonacci numbers------")
for num in even_fib:
    print(num)