#string rotation: assume you have isSubstring function to check if one word is a substring of another. given two strings, see if s2 is a
# rotation if s1 with only one call to isSubstring.

#s1 would be a substring of s2+s2. like "stuff" "fstuf", "fustuffustf"
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    cons2 = s2 + s2
    if s1 in cons2:
        return True
    else:
        return False

if __name__ == "__main__": #morestuff
    examples = [("waterbottle", "erbottlewat"), ('stuff', 'fstuf'), ('morestuff', 'ufsmorest')]
    for example in examples:
        if is_rotation(example[0], example[1]):
            print("%s is a rotation of %s" % (example[1], example[0]))
        else:
            print("%s is NOT a rotation of %s" % (example[1], example[0]))

