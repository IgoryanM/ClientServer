import yaml

data = {
    '1': [1, 2, 3],
    '2': 5,
    '3': {'a': '1€', 'b': '2😀', 'c': '3£'}
}

with open('data.yaml', 'w', encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False,)

with open('data.yaml', encoding='utf-8') as f:
    content = yaml.load(f)
    print(content)
