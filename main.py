import json
import re
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


def replace_textmate_syntax(text):
    placeholders_map = {}

    def default_text_repl(m: re.Match):
        placeholder = f'${m[0][2]}'
        default_text = m[0][4:-1]
        placeholders_map[placeholder] = default_text
        return default_text

    number_of_subs_made = 1
    while True:
        if number_of_subs_made == 0:
            break
        text, number_of_subs_made = re.subn(r"\${\d:[\w+-_, ]*}", default_text_repl, text)

    def placeholder_repl(m: re.Match):
        return placeholders_map.get(m[0], '')

    return re.sub(r"\$\d", placeholder_repl, text)


def main():
    go_snippets = get_go_snippets()
    for k, v in go_snippets['.source.go'].items():
        prefix = v['prefix']
        description = v['description']
        body = replace_textmate_syntax(v['body'])

        print(f'`{prefix}`: {description}')
        print(f"```go\n{body}\n```\n")


if __name__ == '__main__':
    sys.exit(main())
