from collections import defaultdict
from auto_complete_data import AutoCompleteData
from read_file import all_sentences
import string

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

def get_score(sub_string):
    basis_score = len(sub_string) * 2
    score = defaultdict(set)
    indexes = subs.get(sub_string)
    if indexes:
        score[basis_score] = indexes
        if indexes >= 5:
            return score

    for i in range(len(sub_string)):
        indexes = subs.get(sub_string.replace(sub_string[i], ""))
        if i < 4:
            score[basis_score - (10-i*2)] = indexes
        else:
            score[basis_score - 2] = indexes


    all_alphabet = string.ascii_lowercase
    for i in range(len(sub_string)):
        for letter in all_alphabet:
            indexes = subs.get(sub_string[:i]+letter+sub_string[i:])
            if indexes:
                if i < 4:
                    score[basis_score - (10-i*2)] = indexes
                else:
                    score[basis_score - 2] = indexes

    all_alphabet = string.ascii_lowercase
    for i in range(len(sub_string)):
        for letter in all_alphabet:
            indexes = subs.get(sub_string.replace(sub_string[i],letter))
            if indexes:
                if i < 5:
                    score[basis_score - (5-i)] = indexes
                else:
                    score[basis_score - 1] = indexes
    return score



def get_best_k_completions(sub_string):

    indexes = get_common_sentences(subs[sub_string])
    auto_complete_list = []
    for index in indexes:
        completed_sentence = all_sentences[index][0]
        source_text = all_sentences[index][1]
        offset = all_sentences[index][0].index(sub_string)
        score = get_score(sub_string)
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
