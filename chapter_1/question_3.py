#URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

#this question seems to be targeted towards Java datatypes, in python there would be no need to have suffiecent space or given the true length.

#Easy function
def urlify_easy(string):
    urlstring = string.replace(' ', '%20')
    return urlstring

#manually replace after turning string into List. 0(n)
def urlify_hard(string):
    lst_str = list(string)
    newchars = list('%20')
    done = False
    i = 0
    while not done:
        if i >= len(lst_str):
            done = True
        elif lst_str[i] == ' ':
            lst_str = lst_str[:i] + newchars + lst_str[i+1:]
        i += 1
    return "".join(lst_str)

if __name__ == "__main__":
    examples = ["this is a test", "more test strings  "]

    for example in examples:
        print("Easy: %s" % urlify_easy(example))
        print("Hard: %s" % urlify_hard(example))



