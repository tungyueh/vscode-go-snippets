import json
import sys


class Snippet:
    def __init__(self, name, prefix, body, description):
        self.name = name
        self.prefix = prefix
        self.body = body
        self.description = description


def get_go_snippets():
    with open('go.json', 'rb') as fp:
        return json.loads(fp.read())


def main():
    go_snippets = get_go_snippets()
    for k, v in go_snippets['.source.go'].items():
        prefix = v['prefix']
        description = v['description']
        body = v['body']

        print(f'`{prefix}`: {description}')
        print(f"```go\n{body}\n```\n")


if __name__ == '__main__':
    sys.exit(main())
