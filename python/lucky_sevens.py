def lucky_sevens(numbers):
    count = 1
    count2 = 2
    for x in numbers:
        if count2 < len(numbers):
            total = x + numbers[count] + numbers[count2]
            if total == 7:
                return True
        else:
            continue
        count += 1
        count2 += 1
    return False
