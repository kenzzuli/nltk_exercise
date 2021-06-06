from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

words = ["activities", "activists", "went", "looked", "was", "were"]
# PorterStemmer
porter_stemmer = PorterStemmer()
print([porter_stemmer.stem(i) for i in words])
# ['activ', 'activist', 'went', 'look', 'wa', 'were']

# SnowballStemmer
snowball_stemmer = SnowballStemmer(language="english")
print([snowball_stemmer.stem(i) for i in words])
# ['activ', 'activist', 'went', 'look', 'was', 'were']

# LancasterStemmer
lancaster_stemmer = LancasterStemmer()
print([lancaster_stemmer.stem(i) for i in words])
# ['act', 'act', 'went', 'look', 'was', 'wer']

# WordNetLemmatizer  词性还原还是有一点点用的
wordnet_lemmatizer = WordNetLemmatizer()
print([wordnet_lemmatizer.lemmatize(i) for i in words])
print([wordnet_lemmatizer.lemmatize(i, pos="v") for i in words])  # 可以指定词性
# ['activity', 'activist', 'went', 'looked', 'wa', 'were']
# ['activities', 'activists', 'go', 'look', 'be', 'be']
