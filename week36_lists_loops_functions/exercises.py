# Exercise 1
# Create a program that can take an input and an output file and write the content of the input file into a list, the console or to the output file.
import csv
import argparse


def write_list_to_file(output_file, lst):
    with open(output_file, 'a') as file_to_copy_to:
        for element in lst:
            if isinstance(element, list):
                for item in element:
                    file_to_copy_to.write(item + "\n")
            else:
                file_to_copy_to.write(element + "\n")


def print_file_content(file):
    with open(file) as file_to_print:
        lines = file_to_print.readlines()
        print(''.join(lines))


def print_list_content(lst):
    for element in lst:
        if isinstance(element, list):
            for item in element:
                print(item)
        print(element)


def read_file(input_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        csv_list = []
        for row in reader:
            csv_list.append(row)
        return csv_list


def check_for_extra_words(argument):
    inputfile = argument.strip()
    if ' ' in inputfile:
        list_words = inputfile.split(" ")
        return list_words
    else:
        return argument


parser = argparse.ArgumentParser(
    description="Writes contents to console or output file")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true",
                   help="increase output verbosity")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("-f", "--file", help="output file to write to")
parser.add_argument("inputfile", help="path to input file")
args = parser.parse_args()

if args.file:
    if args.verbose:
        print("Checking for extra words")
    words = check_for_extra_words(args.inputfile)
    if isinstance(words, list):
        if args.verbose:
            print("Found extra words")
            print("Writing to file")
        file_list = read_file(words.pop(0))
        words.extend(file_list)
        write_list_to_file(args.file, words)
    else:
        if args.verbose:
            print("Did not find extra words")
            print("Writing to file")
        write_list_to_file(args.file, read_file(words))
else:
    words = check_for_extra_words(args.inputfile)
    if args.verbose:
        print("Checking for extra words")
    if isinstance(words, list):
        if args.verbose:
            print("Found extra words")
            print("Writing to console")
        print_file_content(words.pop(0))
        print(''.join(words))
    else:
        if args.verbose:
            print("Did not find extra words")
            print("Writing to console")
        print_file_content(words)
