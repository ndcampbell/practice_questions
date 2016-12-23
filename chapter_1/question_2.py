#Check permutation: Given two strings, write a method to decide if one is a permutation of the other

def check_permutation(str1, str2):
    if len(str1) != len(str2): #if length is not equal, they can not be permutations
        return False

    #My idea is to keep a hash/dictionary of a count of all characters in each string and the compare
    str1dict = make_dict(str1)
    str2dict = make_dict(str2)
    if str1dict != str2dict:
        return False
    else:
        return True

def make_dict(string):
    newdict = {}
    for c in string:
        try:
            newdict[c] += 1
        except KeyError:
            newdict[c] = 1
    return newdict

if __name__ == "__main__":
    examples = [ ("abcdefg", "gfeabcd"), ("qwerty", "qwdrty"), ('abcdefg', 'abcdefgh')]

    for example in examples:
        if check_permutation(example[0], example[1]):
            print("%s and %s are permutations" % (example[0], example[1]))
        else:
            print("%s and %s are NOT permutations" % (example[0], example[1]))
