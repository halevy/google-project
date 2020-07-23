from collections import defaultdict
from auto_complete_data import AutoCompleteData
from read_file import all_sentences
import string
import collections

subs = defaultdict(set)


def insert_to_dict():
    for i in range(len(all_sentences)):
        sentence = all_sentences[i].completed_sentence
        length = len(sentence)
        for j in range(length):
            subs[sentence[:j + 1]].add(i)
            subs[sentence[j:]].add(i)
        for k in range(length):
            for j in range(length):
                if(j > length-i):
                    break
                subs[sentence[j:length - k]].add(i)



def get_common_sentences(score):

    sorted_dict = collections.OrderedDict(sorted(score.items(), reverse=True))
    print(sorted_dict)
    five_common_sentences = []
    for key in sorted_dict.keys():
        while sorted_dict[key] and len(five_common_sentences) < 5:
            index = sorted_dict[key].pop()
            if index not in five_common_sentences:
                all_sentences[index].score = key
                five_common_sentences.append(index)

    return five_common_sentences

def get_score(sub_string):
    basis_score = len(sub_string) * 2
    score = defaultdict(set)
    indexes = subs[sub_string]
    if indexes:
        score[basis_score] = indexes
        if len(indexes) >= 5:
            return score

    for i in range(len(sub_string)):
        indexes = subs.get(sub_string.replace(sub_string[i], "", 1))
        if indexes:
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
            indexes = subs.get(sub_string.replace(sub_string[i], letter, 1))
            if indexes:
                if i < 5:
                    score[basis_score - (5-i)] = indexes
                else:
                    score[basis_score - 1] = indexes
    return score



def get_best_k_completions(sub_string):

    indexes = get_common_sentences(get_score(sub_string))
    auto_complete_data = []
    for index in indexes:
        auto_complete_data.append(all_sentences[index])
    return auto_complete_data


def five_auto_complete():
    string = input("Enter your text:")
    auto_complete_data = get_best_k_completions(string)
    if auto_complete_data:
        for item in auto_complete_data:
            print(item.completed_sentence)
            print(item.source_text)


insert_to_dict()

five_auto_complete()
