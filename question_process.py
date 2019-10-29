import json
import os

import spacy
from spacy import displacy

spacy.prefer_gpu()
nlp = spacy.load("zh_core_web_sm")


def get_dep(sentence, index):
    if sentence[-1] == '？':
        # 去除问句末尾的问号
        sentence = sentence[:-1]
    doc = nlp(sentence)
    dep_list = list()
    for token in doc:
        data = {'index': token.i, 'token': token.text, 'tag': token.tag_, 'dep': token.dep_,
                'head': token.head.text, 'head_i': token.head.i, 'is_oov': token.is_oov,
                'offset': token.idx, 'prob': token.prob}
        dep_list.append(data)
    html = displacy.render(doc, options={'fine_grained': True, 'compact': True})
    path = os.path.join(os.getcwd(), 'html')
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = os.path.join(path, '%d.html' % index)
    with open(file_path, 'w') as fw:
        fw.write(html)
    return dep_list


def main():
    path = os.path.join(os.getcwd(), '问句汇总', '第一轮测试', '问句.txt')
    w_path = 'question_dep.json'
    result = list()
    with open(path, 'r', encoding='utf-8') as fr:
        fr.readline()
        index = 0
        for line in fr.readlines():
            line = line.strip()
            dep = get_dep(line, index)
            result.append({'index': index, 'sentence': line, 'dep': dep})
            index += 1

    with open(w_path, 'w') as fw:
        json.dump(result, fw)


if __name__ == '__main__':
    main()
