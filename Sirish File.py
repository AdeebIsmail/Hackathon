def scramble(s1, s2):
    # your code here
    for i in range(0, len(s2)):
        if (s1.__contains__(s2[i])):
            letter_count_inString1 = 0
            letter_count_inString2 = 0

            for j in range(0, len(s1)):
                if (s1[j] == s2[i]):
                    letter_count_inString1 += 1
            for j in range(0, len(s2)):
                if (s2[j] == s2[i]):
                    letter_count_inString2 += 1

            if (letter_count_inString1 >= letter_count_inString2):
                continue
            else:
                return False
        else:
            return False
    return True

print(scramble(input(),input()))