# import sys
# import argparse

# parser = argparse.ArgumentParser(
#                     prog='wc',
#                     description='it counts the lines, words and characters of the input',
#                     epilog='thank you:)')
# parser.add_argument('-f','--filename')
# parser.add_argument('-c','--content')
# args=parser.parse_args()
# print(args.filename,args.content)
# file_content=None
# content=None

# if(args.filename):
#     try:
#         with open(args.filename,"r") as file:
#             file_content=file.read()
#     except:
#         raise FileNotFoundError(f"file {args.filename} could not be found")

# if(args.content):
#     content=args.content

# def word_count(string):
#     if string is None:
#         raise TypeError("input could not be None")
#     word=len(string.split())
#     line=string.count('\n')+1
#     char=len(string)
#     return f"{line}  {word}  {char}"

# if content:
#     sys.stdout.write(f"{word_count(content)}")
# if file_content:
#     sys.stdout.write(f"{word_count(file_content)}")
# # sys.stdout.write(f"{word_count(content)}\n{word_count(file_content)}")

import sys
import argparse

def word_count(string):
    if string is None:
        raise TypeError("Input cannot be None")
    word = len(string.split())
    line = string.count('\n') + 1
    char = len(string)
    return f"{line}  {word}  {char}"

def main():
    parser = argparse.ArgumentParser(
        prog='wc',
        description='Count lines, words, and characters of the input',
        epilog='Thank you :)'
    )
    parser.add_argument('-f', '--filename')
    parser.add_argument('-c', '--content')
    args = parser.parse_args()

    print(args.filename, args.content)

    file_content = None
    content = None

    if args.filename:
        try:
            with open(args.filename, "r") as file:
                file_content = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File {args.filename} could not be found")

    if args.content:
        content = args.content

    if content:
        sys.stdout.write(f"{word_count(content)}")

    if file_content:
        sys.stdout.write(f"{word_count(file_content)}")

if __name__ == "__main__":
    main()
