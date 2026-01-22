def compare_strings(str1, str2):
    list1 = list(str1)
    list2 = list(str2)

    i = 0
    while i < len(list1):
        char = list1[i]
        if char in list2:
            list2.remove(char)
            list1.pop(i)  # remove from list1 and don't increment i
        else:
            i += 1

    # Convert remaining letters back to strings
    missing_from_str1 = ''.join(list2)
    missing_from_str2 = ''.join(list1)

    return missing_from_str1, missing_from_str2


# Example usage:
s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

missing1, missing2 = compare_strings(s1, s2)

if not missing1 and not missing2:
    print("The strings are anagrams.")
else:
    print("The strings are NOT anagrams.")
    print("Letters in second but not in first:", missing1)
    print("Letters in first but not in second:", missing2)