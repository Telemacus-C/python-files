from itertools import chain, product

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


bruteList = str(list(bruteforce('abcdefghijklmnopqrstuvwxyz', 4)))

file = open("bruteList.txt", "w")
file.write(bruteList)
print(len(bruteList))
