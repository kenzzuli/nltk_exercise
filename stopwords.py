from nltk.corpus import stopwords
import nltk

sentence = "python is a widely used language"
words = nltk.word_tokenize(sentence)
filtered_words = [i for i in words if i not in stopwords.words("english")]
print(words)
print(filtered_words)

# ['python', 'is', 'a', 'widely', 'used', 'language']
# ['python', 'widely', 'used', 'language']
