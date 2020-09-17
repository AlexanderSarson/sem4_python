import os
import argparse


def write_filenames_to_file_from_path(folder_path, file_path):
    list_of_filenames = [files for root, dirs, files in os.walk(folder_path)]
    write_to_file(file_path, make_lists_to_string(list_of_filenames[0]))


def write_filenames_to_file_from_path_recursively(folder_path, file_path):
    list_of_filenames = [files for root, dirs, files in os.walk(folder_path)]
    write_to_file(file_path, make_lists_to_string(list_of_filenames))


def write_to_file(file_path, lines):
    with open(file_path, 'a') as file:
        file.writelines(lines)


def make_lists_to_string(lst):
    for idx, value in enumerate(lst):
        if isinstance(value, list):
            lst.extend(lst.pop(idx))
            make_lists_to_string(lst)
    return "\n".join(lst)


def print_first_line_from_each_file_in_list(filename_list):
    for file in filename_list:
        with open(file) as file_to_print:
            print(file_to_print.readline())


def print_first_email_from_each_file_in_list(filename_list):
    for file in filename_list:
        with open(file) as file_to_print:
            lines = file_to_print.readlines()
            for line in lines:
                if line.find('@', 0) != -1:
                    print(line)


def print_headlines_from_each_file_in_list(filename_list):
    for file in filename_list:
        with open(file) as file_to_print:
            lines = file_to_print.readlines()
            for line in lines:
                if line.find('#', 0, 1) != -1:
                    print(line)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Read and write file contents from directories")

    parser.add_argument("-wf", "--write_filenames_to_file_from_path",
                        help="Write filenames to file from path")
    parser.add_argument(
        "-wfr", "--write_filenames_to_file_from_path_recursively", help="Filenames to file from path recursively")
    parser.add_argument(
        "-pfl", "--print_first_line_from_each_file_in_list", help="Print first line from each file in list")
    parser.add_argument(
        "-pfe", "--print_first_email_from_each_file_in_list", help="Print first email from each file in list")
    parser.add_argument(
        "-pfh", "--print_headlines_from_each_file_in_list", help="Print headlines from each file in list")
    args = parser.parse_args()

    if args.write_filenames_to_file_from_path:
        options = args.write_filenames_to_file_from_path.split(" ")
        write_filenames_to_file_from_path(options[0], options[1])
    elif args.write_filenames_to_file_from_path_recursively:
        options = args.write_filenames_to_file_from_path_recursively.split(" ")
        write_filenames_to_file_from_path_recursively(options[0], options[1])
    elif args.print_first_line_from_each_file_in_list:
        options = args.print_first_line_from_each_file_in_list.split(" ")
        print_first_line_from_each_file_in_list(options)
    elif args.print_first_email_from_each_file_in_list:
        options = args.print_first_email_from_each_file_in_list.split(" ")
        print_first_email_from_each_file_in_list(options)
    elif args.print_headlines_from_each_file_in_list:
        options = args.print_headlines_from_each_file_in_list.split(" ")
        print_headlines_from_each_file_in_list(options)
