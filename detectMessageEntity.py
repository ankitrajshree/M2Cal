# -*- coding: utf-8 -*
import spacy
import re
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokenizer import Tokenizer

nlp = spacy.load('en_core_web_sm')
text = ''
time = ''
date = ''


def regexCleaner(abstct):
    abstct = re.sub(r'\n+', '', abstct)
    abstct = re.sub(r'\([^)]*\)', '', abstct)
    abstct = re.sub(r'[,;.]', '', abstct)
    abstct = re.sub(r'\s+', ' ', abstct)
    return abstct


# Find the Abstract section and apply summarization over it
def getAbstractTokens(text):
    startidx = re.search(r"\bABSTRACT\b", text).start() + len("ABSTRACT")
    abstract = text[startidx:].lower()
    cleaned_abst = regexCleaner(abstract)
    tokenizer = Tokenizer(nlp.vocab)
    tokens = tokenizer(cleaned_abst)
    final_tokens = [token.text for token in tokens if token.text not in STOP_WORDS]
    return final_tokens

def getDateTimeEntities():
    pass


with open('MessageBody.txt', 'r') as fp:
    text = ' '.join(fp)
uni_text = unicode(text, "utf-8")
abstct_tokens = getAbstractTokens(uni_text)


doc = nlp(uni_text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    if entity.label_ == 'DATE':
        date = entity.text.strip()
    #print(entity.text, entity.label_)

print('Date : '+date)


