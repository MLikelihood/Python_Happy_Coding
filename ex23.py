def fileToListOfInts(filename):
    list_to_return = []
    with open(filename) as f:
        line = f.readline()
        while line:
            list_to_return.append(int(line))
            line = f.readline()
        return list_to_return


primeList = fileToListOfInts('primenumbers.txt')
happieslist = fileToListOfInts('happynumbers.txt')

overlaplist = [elem for elem in primeList if elem in happieslist]
print(overlaplist)
