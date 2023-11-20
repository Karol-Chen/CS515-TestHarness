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

def word_count(string, count_lines=True, count_words=True, count_chars=True):
    if string is None:
        raise TypeError("Input cannot be None")

    lines, words, chars = 0, 0, 0

    if count_lines:
        lines = string.count('\n') + 1

    if count_words:
        words = len(string.split())

    if count_chars:
        chars = len(string)

    return lines, words, chars

def main():
    parser = argparse.ArgumentParser(
        prog='wc',
        description='Count lines, words, and characters of the input',
        epilog='Thank you :)'
    )
    parser.add_argument('files', nargs='+', help='Input files')
    parser.add_argument('-l', '--lines', action='store_true', help='Count lines only')
    parser.add_argument('-w', '--words', action='store_true', help='Count words only')
    parser.add_argument('-c', '--chars', action='store_true', help='Count characters only')
    parser.add_argument('-o', '--output_file', default=None, help='Output file to write results')
    args = parser.parse_args()

    if not any([args.lines, args.words, args.chars]):
        # If no flags are provided, default to counting all
        args.lines, args.words, args.chars = True, True, True

    for filename in args.files:
        try:
            file_content = read_content_from_file(filename)
            lines, words, chars = word_count(file_content, args.lines, args.words, args.chars)

            output = ''
            if args.lines:
                output += f"{lines}\t"

            if args.words:
                output += f"{words}\t"

            if args.chars:
                output += f"{chars}\t"

            if args.output_file:
                with open(args.output_file, 'a') as output_file:
                    output_file.write(f"{output}{filename}\n")
            else:
                print(f"{output}{filename}")

        except FileNotFoundError:
            print(f"Error: File {filename} could not be found")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
