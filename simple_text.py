import nltk
from nltk.corpus import wordnet as wn
from viz import Visualization

ABB = {'JJ': 'a', 'JJR': 'a', 'JJS': 'a',
       'NN': 'n', 'NNS': 'n', 'NNP': 'n', 'NNPS': 'n',
       'VB': 'v', 'VBG': 'v', 'VBD': 'v', 'VBN': 'v', 'VBP': 'v', 'VBZ': 'v',
       'RB': 'r', 'RBR': 'r', 'RBS': 'r', 'WRB': 'r',
       'IN': 'p', 'PRP': 'p', 'PRP$': 'p', 'WP': 'p', 'WP$': 'p', 'POS': 'p', 'RP': 'p',
       'DT': 'd', 'PDT': 'd', 'WDT': 'd',
       'CC': 'c', 'UH': 'i', 'MD': 'm', 'TO': 't', 'EX': 'e', 'SYM': 's'
    }

class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"{self.name}")

class Syns:

    def get_synonyms(sentence, word_list):
        syn_dict = {}   # initialize ('pos' - str, 'synonyms' - list)
        pos = ''
        tokens = nltk.word_tokenize(sentence)   # tokenize
        pos_tags = nltk.pos_tag(tokens)
        for pos_tag in pos_tags:    # part-of-speech tagging
            if pos_tag[0] in word_list:
                pos = ABB[pos_tag[1]]
                syn_dict[pos_tag[0]] = {}   # initialize
                syn_dict[pos_tag[0]]['pos'] = pos
        for word in word_list:
            try:
                synsets = wn.synsets(word, pos=syn_dict[word]['pos'])   # synonyms
                syn_dict[word]['synonyms'] = [] # initialize
                for syn in synsets:
                    for lemma in syn.lemmas():  # lemmas
                        if lemma.name() not in syn_dict[word]['synonyms']:
                            syn_dict[word]['synonyms'].append(lemma.name())
            except Exception as e:
                print(f"An error occurred: {e}.")
        return syn_dict


if __name__=='__main__':
    hyunji = Person("hyunji")
    #hyunji.print_name()

    sentence1 = 'She always wins, it is not fair.'
    word1 = ['wins', 'fair']
    dict1 = Syns.get_synonyms(sentence1, word1)
    for word in dict1:
        print(f"{word}:\npos: {dict1[word]['pos']}\nsynonyms: {dict1[word]['synonyms']}\n")

    sentence2 = '''In fact, however, though now much farther off than before, the Rostóvs
                all saw Pierre—or someone extraordinarily like him—in a coachman’s coat,
                going down the street with head bent and a serious face beside a small,
                beardless old man who looked like a footman.'''
    word2 = ['serious', 'beardless']
    dict2 = Syns.get_synonyms(sentence2, word2)
    for word in dict2:
        print(f"{word}:\npos: {dict2[word]['pos']}\nsynonyms: {dict2[word]['synonyms']}\n")