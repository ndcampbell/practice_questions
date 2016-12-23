# Is Unique: Implement an algorith, to determine if a string has all unique characters. What if you cannt use additional data structures?

def unique_char(string): #probably O(n^2) due to comparison
    unique = True
    for i, char in enumerate(string):
        if char in string[i+1:]:
           unique = False
           break
    return unique

def unique_withhash(string): #0(n)
    char_found = {}
    for char in string:
        try:
            if char_found[char]:
                return False
            else:
                char_found[char] = True
        except KeyError:
            char_found[char] = True

    return True

if __name__ == "__main__":
    examples = ["abcdefghijkl", "abcdeefggjklm"]

    for example in examples:
        if unique_char(example):
            print("%s is Unique!", example)
        else:
            print("%s is Not unique", example)
        if unique_withhash(example):
            print("With Hash: %s is Unique!", example)
        else:
            print("With Hash: %s is Not unique", example)
