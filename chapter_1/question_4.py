#Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
#The Palindrome does not need to be limited to just dictionary words
#
#example: Input: "Tact Coa", Output: True ("taco cat", "atco cta")

#Assumptions: Spaces to not count

#Thoughts: each character except one must exist twice (or even amount). If all characters exist in even amounts, it counts
def is_palindrome(string):
    c_count = {}
    odd_count = 0
    for c in string:
        try:
            c_count[c] += 1
        except KeyError:
            c_count[c] = 1
        if c_count[c] % 2 != 0 :
            odd_count +=1
        else:
            odd_count -= 1
    return odd_count <= 1

if __name__ == "__main__":
    examples = [ "tacocat", "abcdedcba", "stuff"]

    for example in examples:
        if is_palindrome(example):
            print("%s has a palindrome" % example)
        else:
            print("%s does not have a palindrome" % example)

