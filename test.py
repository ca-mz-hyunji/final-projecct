import wn
from wn.morphy import Morphy
from nltk.corpus import wordnet as wnet
from sentence_transformers import SentenceTransformer
from scipy.spatial import distance

from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModel
import torch
import pickle
import numpy

model = SentenceTransformer("all-MiniLM-L6-v2")

class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"{self.name}")

class Test:

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
    
    def sbert(sentences):
        test = "I liked the movie"
        print(f'Test sentense: {test}')
        test_vec = model.encode([test])[0]

        for sent in sentences:
            similarity_score = 1 - distance.cosine(test_vec, model.encode([sent])[0])
            print(f"\nFor {sent}\nSimilarity Score = {similarity_score}")


if __name__=='__main__':
    word = 'wins'

    syns = Test.test_wn(word)
    #print(syns)

    hyunji = Person("hyunji")
    #hyunji.print_name()

    sentences = ["The movie is awesome. It was a good thriller",
                 "We are learning NLP throughg GeeksforGeeks",
                 "The baby learned to walk in the 5th month itself"]
    Test.sbert(sentences)