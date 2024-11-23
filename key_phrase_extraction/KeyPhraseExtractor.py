from typing import List
from sklearn.metrics.pairwise import cosine_similarity
from BaseExtractor import BaseExtractor
from SBERTEmbedder import SBERTEmbedder
import re, pickle
import numpy as np


class KeyPhraseExtractor(BaseExtractor):
    def __init__(self, model: str = "all-MiniLM-L6-v2", top_k: int = 10):
        BaseExtractor.__init__(self)
        self.model = SBERTEmbedder(model)
        self.probs = dict()
        self.prob_file = "nr_of_words_in_phrase_prob.pkl"
        self.top_k = top_k
        with open(self.prob_file, "rb") as f:
            self.probs = pickle.load(f)

    def extractKeyWords(self, doc: str):
        sentence_list = self.split_into_sentences(doc)
        phrases = self.generate_candidate_keywords(sentence_list)
        phrases = self.remove_duplicates(phrases)

        doc_embedding = self.model.embed([doc])[0].reshape(1, -1)
        word_embeddings = self.model.embed(phrases)
        similarity = cosine_similarity(doc_embedding, word_embeddings)[0]
        similarity = self.transform_by_word_count(similarity, phrases)
        keywords = [
            (phrases[index], round(float(similarity[index]), 4))
            for index in similarity.argsort()[-self.top_k :]
        ][::-1]
        return list(map(lambda x: x[0], keywords))

    def generate_candidate_keywords(self, sentence_list):
        phrase_list = []
        for s in sentence_list:
            tmp = re.sub(self.stop_words_pattern, "|", s.strip().lower())
            phrases = tmp.split("|")
            for phrase in phrases:
                phrase = phrase.strip()
                if phrase != "":
                    phrase_list.append(phrase)
        return phrase_list

    def remove_duplicates(self, phrases):
        filtered_phrases = []
        stemmed_phrases = set()
        for phrase in phrases:
            stemmed = " ".join(self.porter.stem(word) for word in phrase.split())
            if stemmed not in stemmed_phrases:
                stemmed_phrases.add(stemmed)
                filtered_phrases.append(phrase)
        return filtered_phrases

    def transform_by_word_count(self, similarity, phrases: List[str]):
        for idx in range(len(similarity)):
            count = len(phrases[idx].split(" "))
            count_probability = self.probs.get(count, 0.0001)
            if count_probability < 0.01 or similarity[idx] < 0:
                similarity[idx] = 0
            else:
                similarity[idx] *= np.log(count_probability * 100 + 15)
        return similarity
