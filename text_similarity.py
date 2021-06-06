# 基于词频的文本相似度
import nltk
from nltk import FreqDist

text1 = 'I like the movie so much '
text2 = 'That is a good movie '
text3 = 'This is a great one '
text4 = 'That is a really bad movie '
text5 = 'This is a terrible movie'

text = text1 + text2 + text3 + text4 + text5
words = nltk.word_tokenize(text)
freq_dist = FreqDist(words)
print(freq_dist['is'])  # 4

# 取最常用的前N个词
N = 5
most_common_words = freq_dist.most_common(N)
print(most_common_words)  # [('movie', 4), ('is', 4), ('a', 4), ('That', 2), ('This', 2)]


def lookup_position(most_common_words):
    """
    查找常用单词的位置
    """
    res = {}
    for idx, i in enumerate(most_common_words):
        res[i[0]] = idx
    return res


std_pos_dict = lookup_position(most_common_words)
print(std_pos_dict)  # {'movie': 0, 'is': 1, 'a': 2, 'That': 3, 'This': 4}

# 新文本
new_text = 'That one is a good movie. This is so good!'
# 初始化向量
freq_vec = [0] * N

# 分词
new_words = nltk.word_tokenize(new_text)

# 在常用单词列表上计算词频
for i in new_words:
    if i in std_pos_dict:
        freq_vec[std_pos_dict[i]] += 1
print(freq_vec)  # [1, 2, 1, 1, 1]
