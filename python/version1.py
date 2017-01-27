def fizzbuzz():
    goal = 100
    current = 1
    while current <= goal:
        if current % 3 is 0 and current % 5 is 0:
            print "FizzBuzz"
        elif current % 3 is 0 or current % 5 is 0:
            print "Fizz" if current % 3 is 0 else "Buzz"
        else:
            print current
        current += 1
