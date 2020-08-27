
def main():

    # Take input of n and k:
    n_and_k = input()
    n = int(n_and_k.split(' ')[0])
    k = int(n_and_k.split(' ')[1])

    dictionary = []
    valid = set(())
    invalid = set(())

    # Take input of words for dictionary:
    for i in range(0, n):
        dictionary.append(input())

    # Loop over everything that belongs in the dictionary:
    for i in range(0, len(dictionary)):
        sorted_word = str(sorted(dictionary[i]))

        # If an anagram of the word exists in valid, remove it from valid and add
        # it to invalid.
        if sorted_word in valid:
            valid.remove(sorted_word)
            invalid.add(sorted_word)

        # Else if the sorted word does not exist in invalid, add it to valid.
        elif sorted_word not in invalid:
            valid.add(sorted_word)

    print(len(valid))

    return


if __name__ == '__main__':
    main()
