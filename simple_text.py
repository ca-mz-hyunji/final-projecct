import wn
from wn.morphy import Morphy
from nltk.corpus import wordnet as wnet
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

def test_wn(word):
    syns = {}
    en = wn.Wordnet('oewn:2023', lemmatizer=Morphy())    # Create Wordnet object to query
    try:
        w = en.words(word)[0]
        pos = w.pos
        synsets = en.synsets(word, pos=pos)
        for synset in synsets:
            lemma_names = synset.lemmas()
            if lemma_names:
                lemma_name = lemma_names[0]
                definition = synset.definition() # Get the synset's definition
                syns[lemma_name] = definition
    except Exception as e:
        print(f"An error occurred: {e}")
    return syns

def test_wnet(word):
    syn_dict = {}
    pos = pos_tag(word_tokenize(word))[0]
    synsets = wnet.synsets(word, pos=pos[1])
    for syn in synsets:
        definition = syn.definition()
        syn_dict[syn] = definition
    return syn_dict


if __name__=='__main__':
    word = 'wins'

    syns = test_wn(word)
    #print(syns)

    syns2 = test_wnet(word)
    print(syns2)