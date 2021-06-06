import nltk

# tokenize
sentence = "python is a widely used language"
words = nltk.word_tokenize(sentence)
print(words)
# ['python', 'is', 'a', 'widely', 'used', 'language']
print(nltk.pos_tag(words))
# [('python', 'NN'), ('is', 'VBZ'), ('a', 'DT'), ('widely', 'RB'), ('used', 'VBN'), ('language', 'NN')]
