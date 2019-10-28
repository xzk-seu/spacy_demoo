from spacy import displacy
import spacy
# spacy版本要小于2.1
import zh_core_web_sm

# nlp = zh_core_web_sm.load()
spacy.prefer_gpu()
nlp = spacy.load("zh_core_web_sm")


def main():
    # sent = '东南大学的汪老师是谁'
    # sent = '张三是谁的爸爸'
    sent = '烽火科技的张经理是谁'
    doc = nlp(sent)
    print('text, tag_, dep_, head')
    for token in doc:
        print(token, token.text, token.tag_, token.dep_, token.head,
              token.shape_, token.is_alpha, token.is_stop, token.has_vector,
              token.ent_iob_, token.ent_type_,
              token.vector_norm, token.is_oov)

    # displacy.serve(doc, options={'fine_grained': True, 'compact': True})
    html = displacy.render(doc, options={'fine_grained': True, 'compact': True})
    with open('test.html', 'w', encoding='gbk') as fw:
        fw.write(html)


if __name__ == "__main__":
    main()
