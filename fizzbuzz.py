def fizzbuzz(fizz, buzz):
    for fizzbuzz in range(100):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print(fizz+buzz)
            continue
        elif fizzbuzz % 3 == 0:
            print(buzz)
            continue
        elif fizzbuzz % 5 == 0:
            print(buzz)
            continue
        print(fizzbuzz)

fizzbuzz("beep", "boop")