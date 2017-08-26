s1 = str(input("a word please:"))
s2 = str(input("Please enter another word:"))
assert sorted(list(input1), key=str.lower) == sorted(list(input2), key=str.lower)
   
