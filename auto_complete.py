from collections import defaultdict
from auto_complete_data import AutoCompleteData

all_sentences = [("hello big world", "file.txt"), ("hello world", "file2.txt")]
subs = defaultdict(set)


def insert_to_dict(sentence):
    length = len(sentence)
    for i in range(length):
        subs[sentence[:i + 1]].add(all_sentences.index(sentence))
        subs[sentence[i:]].add(all_sentences.index(sentence))
    for i in range(length):
        for j in range(length):
            if(j > length-i):
                break
            subs[sentence[j:length - i]].add(all_sentences.index(sentence))



def get_common_sentences(sentences_indexes):
    if len(sentences_indexes) <= 5:
        return list(sentences_indexes)
    return list(sentences_indexes)[:5]

def get_score(sub_string,completed_sentence):
    if sub_string in completed_sentence:
        return len(sub_string)*2

def get_best_k_completions(sub_string):

    indexes = get_common_sentences(subs[sub_string])
    auto_complete_list = []
    for index in indexes:
        completed_sentence = all_sentences[index][0]
        source_text = all_sentences[index][1]
        offset = all_sentences[index][0].index(sub_string)
        score = get_score(sub_string, completed_sentence)
        auto_complete_list.append(AutoCompleteData(completed_sentence, source_text, offset, score))
    return auto_complete_list


def five_auto_complete():
    string = input("Enter your text:")
    auto_complete_data = get_best_k_completions(string)
    for item in auto_complete_data:
        print(item.completed_sentence)


for sentence in all_sentences:
    insert_to_dict(sentence)

five_auto_complete()
