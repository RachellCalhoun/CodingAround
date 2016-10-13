def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    results = []
    for x in string:
        if x in vowels:
            pass
        else:
            results.append(x)
    results = ("").join(results)
    return results

disemvowel("aeiou")
