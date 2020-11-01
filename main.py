# This program gets string and markers and delete all text after markers. Any whitespace at the end of the line
# is also stripped out.
# Author: Vladyslav Dyshkant

import re

def solution(string,markers):
    arr = string.split("\n")
    result = []
    addBackSlash = False
    for i in arr:
        for j in range(len(markers)):
            if not addBackSlash:
                markers[j] = '\%s' % markers[j]
            if re.search(markers[j], i):
                temp = re.search(markers[j], i)
                if temp != None:
                    i = i[:temp.start()]
        addBackSlash = True
        result.append(i.strip())
    return '\n'.join(result)


result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

expected = "apples, pears\ngrapes\nbananas"

if expected == result:
    print("TRUE\n")
else:
    print("FALSE\n")

print("Result:\n", result, end="\n\n")
print("Expected:\n", expected)



