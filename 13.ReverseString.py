
string = "Hello World"
rev_string= ""
index = len(string)-1 

while index >= 0:
    rev_string = rev_string + string[index]
    index = index-1

print(rev_string)