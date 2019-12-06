import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("zh_core_web_sm")

# Process whole documents
text = '王小明在北京的清华大学读书'

doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [token.lemma_ for token in doc if token.tag_ == "NN" or token.tag_ == 'NNP'])
print("Verbs:", [token.lemma_ for token in doc if token.tag_ == "VV"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
