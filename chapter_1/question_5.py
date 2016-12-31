#One Away: There are three edits that can be done on a string. Insert, remove, or replace a character. Given two strings, write a function
#to check if there are one or zero edits apart


#Thoughts: If strings are same length, all but one character will be the same
#If strings strings are >1 character different, fail
def edit_distance(str1, str2):
    if str1 == str2: #return true if strings are equal
        return True
    if abs(len(str1) - len(str2)) > 1:
        return False

    total_dif = 0
    for c in str1:
        if c not in str2:
            total_dif += 1
        else: #remove char
            str2 = str2.replace(c, '', 1)
            str1 = str1.replace(c, '', 1)
        if total_dif > 1:
            return False
    if len(str1) > 1 or len(str2) > 1:
        return False
    return True

if __name__ == "__main__":
    examples = [ ("pale", "ple"), ("pales, pale"), ("pale", "bale"), ("pale", "bake")]
    for example in examples:
        if edit_distance(example[0], example[1]):
            print ("True: %s and %s are <= 1 edit apart" % (example[0], example[1]))
        else:
            print ("False: %s and %s are > 1 edit apart" % (example[0], example[1]))
