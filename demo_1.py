import json

"""
按根结点词性对句子分类
根结点词性为NN、NNP都是名词，通常对应一个待查实体或者待查关系

"""
if __name__ == '__main__':
    with open('tree.json', 'r') as fr:
        data = json.load(fr)

    result = dict()
    for i in data:
        print(i['index'], i['sentence'])
        for t in i['token']:
            if t['dep'] == 'ROOT':
                print('root:', t['token'], t['tag'])
                ls = result.setdefault(t['tag'], list())
                term = {'sentence': i['sentence'], 'root': t['token'], 'prob': t['prob']}
                ls.append(term)
    with open('root.json', 'w') as fw:
        json.dump(result, fw)

    for k, v in result.items():
        print(k, len(v))
