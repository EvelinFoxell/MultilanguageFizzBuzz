def fizzbuzz():
    result = []
    goal = 100

    def recursive(current_iteration):
        answer = current_iteration \
            if not (current_iteration % 3 is 0 or current_iteration % 5 is 0) \
            else "FizzBuzz" if (current_iteration % 3 is 0 and current_iteration % 5 is 0) \
            else "Fizz" if current_iteration % 3 is 0 \
            else "Buzz"
        print answer
        result.append(answer)
        if current_iteration < goal:
            recursive(current_iteration + 1)

    recursive(1)
    return result
