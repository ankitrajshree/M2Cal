# -*- coding: utf-8 -*
import spacy

nlp = spacy.load('en_core_web_sm')
text = ''
time = ''
date = ''

with open('MessageBody.txt', 'r') as fp:
        text = ' '.join(fp)
print text

uni_text = unicode(text, "utf-8")
doc = nlp(uni_text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    if entity.label_ == 'DATE':
        date = entity.text.strip()
    print(entity.text, entity.label_)

# Determine semantic similarities
#doc1 = nlp(u"my fries were super gross")
#doc2 = nlp(u"such disgusting fries")
#similarity = doc1.similarity(doc2)
#print(doc1.text, doc2.text, similarity)

