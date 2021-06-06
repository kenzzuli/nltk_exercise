import nltk
from nltk.tokenize import WordPunctTokenizer

# 加载分句模型
path = "/Users/ken/nltk_data/tokenizers/punkt/english.pickle"
sent_tokenizer = nltk.data.load(path)

# 分句
paragraph = "The first time I heard that song was in Hawaii on radio.  I was just a kid, and loved it very much! What a fantastic song!"
sentences = sent_tokenizer.tokenize(paragraph)
print(sentences)

# 分词
words = [WordPunctTokenizer().tokenize(sentence.lower()) for sentence in sentences]
print(words)

# ['The first time I heard that song was in Hawaii on radio.', 'I was just a kid, and loved it very much!', 'What a fantastic song!']
# [['the', 'first', 'time', 'i', 'heard', 'that', 'song', 'was', 'in', 'hawaii', 'on', 'radio', '.'], ['i', 'was', 'just', 'a', 'kid', ',', 'and', 'loved', 'it', 'very', 'much', '!'], ['what', 'a', 'fantastic', 'song', '!']]
