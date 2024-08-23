import wn
from wn.morphy import Morphy
from nltk.corpus import wordnet as wnet

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


if __name__=='__main__':
    word = 'wins'

    syns = test_wn(word)
    #print(syns)