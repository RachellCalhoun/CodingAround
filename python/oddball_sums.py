def oddball_sum(numbers):
    total = 0
    for x in numbers:
        if x%2 == 0:
            continue
        else:
            total += x


    return total

oddball_sum((1,2,1))
