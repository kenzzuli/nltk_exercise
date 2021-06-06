import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

raw_text = "Life is like a box of chocolate. You never know what you're gonna get."

# 分词
tokenized_text = nltk.word_tokenize(raw_text)

# 词形还原
lemmatizer = WordNetLemmatizer()
lemmatized_text = [lemmatizer.lemmatize(word) for word in tokenized_text]

# 去除停用词
filtered_text = [i for i in lemmatized_text if i not in stopwords.words("english")]

print(raw_text)
print(filtered_text)
# Life is like a box of chocolate. You never know what you're gonna get.
# ['Life', 'like', 'box', 'chocolate', '.', 'You', 'never', 'know', "'re", 'gon', 'na', 'get', '.']
