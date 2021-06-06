# nltk.corpus
from nltk.corpus import brown
from nltk.corpus import names

# 查看介绍
print(brown.readme())
# 查看类别
print(brown.categories())

# 查看句子数
print(len(brown.sents()))
# 查看单词数
print(len(brown.words()))
