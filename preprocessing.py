import re
from nltk import pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def cleaning(text):
    # substitute single quotes in word to space e.g. Allah's -> Allahs, other's -> others
    # text = re.sub("'", "", text)

    # substitute single quotes in word to space e.g. Allah's -> Allah, other's -> other
    text = re.sub("'\s", "", text)

    # substitute other than a letter and digit (or underscore)
    return re.sub('\W+', ' ', text)

def casefolding(text):
    # to lower case
    return text.lower()

def tokenization(text):
    # tokenize word
    return word_tokenize(text)

def stopword_removal(tokenized_word):
    # set list stopwords in english
    list_stopwords = set(stopwords.words('english'))

    # eliminate stopword in english using list_stopwords
    return [word for word in tokenized_word if not word in list_stopwords]

# lemmatization process
def pos_tagging(filtered_word):
    # tag each word using pos tag
    return pos_tag(filtered_word)

def get_wordnet_pos(treebank_tag):
    # change each pos tag to wordnet
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        # as default pos in lemmatization is Noun
        return wordnet.NOUN

def lemmatizer(tagged_wordnet_words):
    # lemmatization foreach words that has wordnet tag
    return [WordNetLemmatizer().lemmatize(word, get_wordnet_pos(tag)) for word, tag in tagged_wordnet_words]

# sum up
def text_preprocessing(text):
    return lemmatizer(pos_tagging(stopword_removal(tokenization(casefolding(cleaning(text))))))
    