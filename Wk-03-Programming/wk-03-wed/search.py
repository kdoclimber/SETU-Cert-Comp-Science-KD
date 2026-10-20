sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.find("fox")) # index of fox, includes spaces, starts at 0
print(sentence.find("cat")) 
print(sentence.count("the"))
print(f'The {sentence.count("The")}')
print(f'The and the {sentence.count("The" and "the")}') # just finds the first The

print(sentence.startswith("The"))
print(sentence.startswith("the"))

text = "aaa bbb aaa ccc aaa"
print(text.replace("aaa", "YYY", 2))