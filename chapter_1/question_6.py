#String Compression: compress string using counts. like "aabcccccaaa" would be "a2b1c4a3". Upper and lowercase. Return smallest string (origional or compressed)

def compress_str(string):
    cur_c = ''
    count = 0
    newstr = []
    for c in string:
        if c is cur_c:
            count +=1
        else:
            if count > 0:
                newstr.append(str(count))
                newstr.append(cur_c)
            cur_c = c
            count = 1
    #append final value
    newstr.append(str(count))
    newstr.append(cur_c)
    if len(string) <= len(newstr):
        return string
    else:
        return ''.join(newstr)

if __name__ == "__main__":
    examples = ["aabbcccccdeeef", "abccdef", "ttttttttttyyyyyyyy"]
    for example in examples:
        compressed = compress_str(example)
        print("%s compressed is %s" % (example, compressed))
