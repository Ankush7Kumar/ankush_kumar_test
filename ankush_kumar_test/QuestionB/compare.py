# compare checks if version string s1 is greater, equal, or less than the version string s2

def compare(s1, s2):
    if s1 == s2: return "equal"
    
    else:
        for i in range(0, min(len(s1), len(s2))):

            # if the index is odd or if the integers are equal
            if i%2 != 0 or s1[i] == s2[i]: continue

            # if the integers are different
            if s1[i] > s2[i]:
                return "greater"
            else:
                #s2[i] > s1[i]
                return "lesser"

