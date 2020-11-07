from collections import defaultdict
from SRC.read_files import all_sentences
import string
import collections
import re

subs = defaultdict(set)

def insert_to_dict():

    for i in range(len(all_sentences)):
        my_sentence = all_sentences[i].completed_sentence
        sentence = valid_string(my_sentence)
        length = len(sentence)
        for j in range(length):
            if sentence[j] != ' ':
                subs[sentence[:j + 1]].add(i)
                subs[sentence[j:]].add(i)

        for k in range(length):
            for j in range(length):
                if(j > length-k):
                    break
                if sentence[j] != ' ' and sentence[length-k-1] != ' ':
                    subs[sentence[j:length - k]].add(i)


def valid_string(string):

    string = re.sub(" +", " ", string.lower())
    return re.sub(r'[^a-z0-9 ]', '', string)


def get_common_sentences(score):

    sorted_dict = collections.OrderedDict(sorted(score.items(), reverse=True))
    five_common_sentences = []
    for key in sorted_dict.keys():
        while sorted_dict[key] and len(five_common_sentences) < 5:
            index = sorted_dict[key].pop()
            if index not in five_common_sentences:
                all_sentences[index].score = key
                five_common_sentences.append(index)

    return five_common_sentences

def delete_letter(sub_string, basis_score, score):

    for i in range(len(sub_string)):
        indexes = subs.get(sub_string[:i] + sub_string[i+1:])
        if indexes:
            if i < 4:
                score[basis_score - (10-i*2)].update(indexes)
            else:
                score[basis_score - 2].update(indexes)
    return score

def add_letter(sub_string, basis_score, score):

    all_alphabet = string.ascii_lowercase
    for i in range(len(sub_string)):
        for letter in all_alphabet:
            indexes = subs.get(sub_string[:i] + letter + sub_string[i:])
            if indexes:
                if i < 4:
                    score[basis_score - (10 - i * 2)].update(indexes)
                else:
                    score[basis_score - 2].update(indexes)
    return score

def replace_letter(sub_string, basis_score, score):

    all_alphabet = string.ascii_lowercase
    for i in range(len(sub_string)):
        for letter in all_alphabet:
            indexes = subs.get(sub_string.replace(sub_string[i], letter, 1))
            if indexes:
                if i < 5:
                    score[basis_score - (5 - i)].update(indexes)
                else:
                    score[basis_score - 1].update(indexes)
    return score

def get_score(sub_string):

    basis_score = len(sub_string) * 2
    score = defaultdict(set)
    indexes = subs[sub_string]
    if indexes:
        score[basis_score] = indexes
        if len(indexes) >= 5:
            return score

    score = delete_letter(sub_string, basis_score, score)
    score = add_letter(sub_string, basis_score, score)
    score = replace_letter(sub_string, basis_score, score)
    return score


def get_best_k_completions(sub_string):

    indexes = get_common_sentences(get_score(sub_string))
    auto_complete_data = []
    for index in indexes:
        auto_complete_data.append(all_sentences[index])
    return auto_complete_data


def five_auto_complete():

    while True:
        my_string = input("Enter your text:")
        if my_string == "stop":
            break
        string = ""
        while True:
            my_string += string
            auto_complete_data = get_best_k_completions(valid_string(my_string))
            if auto_complete_data:
                length = len(auto_complete_data)
                print(f"Here are {length} suggestions")
                for i in range(length):
                    print(f"{i+1}.{auto_complete_data[i].completed_sentence}, path = {auto_complete_data[i].source_text}")
            string = input(my_string)
            if string == '#':
                break



insert_to_dict()
#five_auto_complete()
