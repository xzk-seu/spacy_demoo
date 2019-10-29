import json

import spacy

# spacy版本要小于2.1

nlp = spacy.load("zh_core_web_sm")


def main():
    doc = nlp("1399350807的爸爸是谁")
    print('text, tag_, dep_, head')
    dep_list = list()
    for token in doc:
        data = {'index': token.i, 'token': token.text, 'tag': token.tag_, 'dep': token.dep_,
                'head': token.head.text, 'head_i': token.head.i, 'is_oov': token.is_oov}
        dep_list.append(data)
        print(token, token.text, token.tag_, token.dep_, token.head,
              token.shape_, token.is_alpha, token.is_stop, token.has_vector,
              token.ent_iob_, token.ent_type_,
              token.vector_norm, token.is_oov)
    with open('test.json', 'w') as fw:
        json.dump(dep_list, fw)


if __name__ == "__main__":
    main()
