# pip install genson


import json
import pyperclip
from genson import SchemaBuilder


def main():
    builder = SchemaBuilder()
    with open("input.json", 'r') as inputf:
        datastore = json.load(inputf)
        builder.add_object(datastore)

    builder.DEFAULT_URI = "http://json-schema.org/draft-06/schema#"
    with open('output.json', 'w') as outf:

        outf.write(builder.to_json(indent=2))

    pyperclip.copy(builder.to_json(indent=2))


if __name__ == "__main__":
    main()
