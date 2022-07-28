def myfunction(numbers, order):
    casefolded = order.casefold()

    if casefolded == "asc" or casefolded == "desc" or casefolded == "none":
        if casefolded == "asc":
            numbers.sort()
        elif casefolded == "desc":
            numbers.sort(reverse=True)

        return numbers
    else:
        return []


numbers = [25, 42, 57, 99, 106, 102, 453, 333, 17, 20, 3, 7, 30, 8, 1, 2, 24]
sortedvalues = myfunction(numbers, "asc")

for x in sortedvalues:
    print(x)