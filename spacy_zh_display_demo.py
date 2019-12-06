import spacy
from spacy import displacy

# spacy版本要小于2.1
spacy.prefer_gpu()
nlp = spacy.load("zh_core_web_sm")


def main():
    """
    # sent = '东南大学的汪老师是谁'
    # sent = '张三是谁的爸爸'
    :return:
    """
    # sent = '99554422775@126.com的同乡的手机号码'
    sent = '烽火科技的工商注册号是多少'
    doc = nlp(sent)
    print('text, tag_, dep_, head')
    for token in doc:
        print(token.like_email, token.text, token.tag_, token.dep_, token.head,
              token.shape_, token.is_alpha, token.is_stop, token.has_vector,
              token.ent_iob_, token.ent_type_,
              token.vector_norm, token.is_oov)

    # displacy.serve(doc, options={'fine_grained': True, 'compact': True})
    html = displacy.render(doc, options={'fine_grained': True, 'compact': True})
    with open('test.html', 'w', encoding='gbk') as fw:
        fw.write(html)


if __name__ == "__main__":
    main()
