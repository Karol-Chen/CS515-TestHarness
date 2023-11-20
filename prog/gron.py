import sys
import argparse
import json

parser = argparse.ArgumentParser(prog="gron", description="", epilog="thank you:)")
parser.add_argument('-f', '--filename')
parser.add_argument('-c', '--content')
args = parser.parse_args()

def main():
    content = None

    if args.filename:
        try:
            with open(args.filename, "r") as file:
                file_content = file.read()
        except FileNotFoundError:
            print(f"File {args.filename} could not be found")
            sys.exit(1)

    if args.content:
        content = args.content

    type_dict = {"<class 'list'>": '[]', "<class 'set'>": '{}', "<class 'dict'>": "{}", "<class 'tuple'>": "()"}

    if content:
        try:
            result = gron(content, type_dict)
            sys.stdout.write(result)
            with open("../test/gron.json1.out", "w") as output_file:
                output_file.write(result)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    if file_content:
        try:
            result = gron(file_content, type_dict)
            sys.stdout.write(result)
            with open("../test/gron.json1.out", "w") as output_file:
                output_file.write(result)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


def gron(string, type_dict):
    if string is None:
        raise TypeError("Input could not be None")
    try:
        json_content = json.loads(string)
    except json.JSONDecodeError:
        raise ValueError("Input should be a valid JSON file")
    res = ["json = {};"]
    flatten(json_content, keys="json", res=res, type_dict=type_dict)
    return '\n'.join(res)

def flatten(my_dict, keys, res, type_dict):
    if isinstance(my_dict, (int, float, str, bool)):
        res.append(f"{keys} = {my_dict};")
    elif isinstance(my_dict, list):
        for idx, value in enumerate(my_dict):
            new_keys = f"{keys}[{idx}]"
            if isinstance(value, (dict, list)):
                res.append(f"{new_keys} = {type_dict.get(str(type(value)))};")
                flatten(value, new_keys, res, type_dict)
            else:
                res.append(f"{keys}[{idx}] = {value};")
    elif isinstance(my_dict, dict):
        for key, value in my_dict.items():
            new_keys = f"{keys}.{key}"
            if isinstance(value, (list, dict)):
                res.append(f"{new_keys} = {type_dict.get(str(type(value)))};")
                flatten(value, new_keys, res, type_dict)
            else:
                res.append(f"{new_keys} = {value};")

if __name__ == "__main__":
    main()
