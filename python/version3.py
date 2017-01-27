def fizzbuzz():
    number = 1
    goal = 100
    while number <= goal:
        answer = ''
        if number % 3 is 0: answer += 'Fizz'
        if number % 5 is 0: answer += 'Buzz'
        if len(answer) is 0: answer = number
        print answer
        number += 1
