from collections import defaultdict

all_sentences = ["hello big world", "hello world"]
sub = defaultdict(set)


def insert_to_dict(sentence):
    length = len(sentence)
    for i in range(length):
        sub[sentence[:i+1]].add(all_sentences.index(sentence))
        sub[sentence[i:]].add(all_sentences.index(sentence))
    for i in range(length):
        for j in range(length):
            if(j > length-i):
                break
            sub[sentence[j:length-i]].add(all_sentences.index(sentence))



def get_common_sentences(sentences_indexes):
    if len(sentences_indexes) <= 5:
        return list(sentences_indexes)
    return list(sentences_indexes)[:5]


def five_auto_complete():
    string = input("Enter your text:")
    indexes = get_common_sentences(sub[string])
    for index in indexes:
        print(all_sentences[index])


for sentence in all_sentences:
    insert_to_dict(sentence)

five_auto_complete()
