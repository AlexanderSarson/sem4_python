import utils
import os


utils.write_filenames_to_file_from_path(os.getcwd(), "new.txt")
utils.write_filenames_to_file_from_path_recursively(os.getcwd(), "new.txt")


utils.print_first_line_from_each_file_in_list(['new.txt', 'text.txt'])
utils.print_first_email_from_each_file_in_list(['new.txt', 'text.txt'])
utils.print_headlines_from_each_file_in_list(['headline1.md', 'headline2.md'])
