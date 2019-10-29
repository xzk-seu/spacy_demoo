"""
将json列表中的树结构转化为递归的树结构
"""
import json


def build_tree(token_list, root_id):
    root_token = token_list[root_id]
    children_ids = root_token['children_ids']
    if len(children_ids) == 0:
        return token_list[root_id]

    sub_tree = list()
    for i in children_ids:
        t = build_tree(token_list, i)
        sub_tree.append(t)
    root_token['children'] = sub_tree
    return root_token


def item_process(item):
    token_list = item['dep']
    root_id = None
    for token in token_list:
        token['children_ids'] = list()
    for token in token_list:
        if token['dep'] == 'ROOT':
            root_id = token['index']
            continue
        head_i = token['head_i']
        token_list[head_i]['children_ids'].append(token['index'])

    assert type(root_id) == int
    tree = build_tree(token_list, root_id)
    result = {'index': item['index'],
              'sentence': item['sentence'],
              # 'html': os.path.join(os.getcwd(), 'html', '%d.html' % item['index']),
              'token': item['dep'],
              'tree': tree}
    return result


def main():
    with open('question_dep.json', 'r') as fr:
        data = json.load(fr)
    result = list()
    for item in data:
        t = item_process(item)
        result.append(t)
    with open('tree.json', 'w') as fw:
        json.dump(result, fw)


if __name__ == '__main__':
    main()
