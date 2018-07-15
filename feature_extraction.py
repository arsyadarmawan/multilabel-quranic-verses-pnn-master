import numpy as np
from math import log10

def build_vocabulary(text):
    # build vocabulary based on preprocessed text
    # param text: preprocessed text
    vocabulary = set()
    for words in text:
        vocabulary.update([word for word in words])
    return list(vocabulary)

def term_frequency(verse, term):
    # count term in verse
    return verse.count(term)

def build_tf_matrix(text, vocab):
    # build term frequency matrix using the frequency of term for each verse
    # param text: preprocessed text
    _tf_matrix = []
    for verse in text:
        # count each word in vocab that appear in each verse
        _tf_vector = [term_frequency(verse, word) for word in vocab]
        _tf_matrix.append(_tf_vector)
    return _tf_matrix

def weighted_term_frequency(vector):
    # calculate weighted tf (see text book)
    return [0 if val == 0 else 1 + log10(1 + log10(val)) for val in vector]

def weighted_tf_matrix(matrix):
    # create weighted term frequency matrix
    wtf_matrix = []
    for vector in matrix:
        wtf_matrix.append(weighted_term_frequency(vector))
    return wtf_matrix

def count_term_in_verses(term, text):
    # len of verses(document) that contain term
    # param text: preprocessed text
    verse_contained = 0
    for verse in text:
        if term_frequency(verse, term) > 0:
            verse_contained += 1
    return verse_contained

def inverse_document_frequency(term, text):
    # idf (see text book)
    # param text: preprocessed text
    return log10((1+len(text))/count_term_in_verses(term, text))

def build_idf_vector(text, vocab):
    # build idf vector
    # param text: preprocessed text
    _idf_vector = [inverse_document_frequency(word, text) for word in vocab]
    return _idf_vector

def build_idf_matrix(idf_vector):
    # to create tf*idf, we need to change idf_vector to diagonal matrix so we can multiply it directly
    _idf_matrix = np.zeros((len(idf_vector), len(idf_vector)))
    np.fill_diagonal(_idf_matrix, idf_vector)
    return _idf_matrix

def build_tfidf_matrix(wtf_matrix, idf_matrix):
    return [np.dot(wtf_vector, idf_matrix).tolist() for wtf_vector in wtf_matrix]

# sum up
def tf_idf(preprocessed_text):
    # vocabulary
    vocab = build_vocabulary(preprocessed_text)
    # term frequency matrix
    tf_matrix = build_tf_matrix(preprocessed_text, vocab)
    # weighted term frequency matrix
    wtf_matrix = weighted_tf_matrix(tf_matrix)
    # idf vector
    idf_vector = build_idf_vector(preprocessed_text, vocab)
    # idf matrix
    idf_matrix = build_idf_matrix(idf_vector)
    # tfidf matrix
    tfidf_matrix = build_tfidf_matrix(wtf_matrix, idf_matrix)
    return tfidf_matrix