import sys
import argparse

def read_content_from_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} could not be found")
    except Exception as e:
        raise Exception(f"Error reading file: {e}")

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

    file_content = None
    content = None

    if args.filename:
        try:
            file_content = read_content_from_file(args.filename)
        except FileNotFoundError:
            print(f"Error: File {args.filename} could not be found")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    if args.content:
        content = args.content

    if content:
        sys.stdout.write(f"{word_count(content)}")

    if file_content:
        sys.stdout.write(f"{word_count(file_content)}")

    sys.exit(0)

if __name__ == "__main__":
    main()
