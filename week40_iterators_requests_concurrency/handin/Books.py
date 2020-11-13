from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import requests
import glob
import os


class NotFoundException(Exception):
    def __init__(self, message, status_code):
        error_message = f"Error message : {message}. status code : {status_code}"
        super().__init__(error_message)


class Books():
    def __init__(self, url_list, filenames):
        self.url_list = url_list
        self.filenames = filenames

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < len(self.url_list):
            self.count += 1
            return self.url_list[self.count - 1]
        else:
            raise StopIteration

    def _write_text_to_file(filename, text):
        with open(filename, 'w') as file_to_write_to:
            file_to_write_to.write(text)

    def download(url, filename):
        req = requests.get(url)
        if req.status_code == 404:
            raise NotFoundException('Website not found', req.status_code)
        response = req.text
        Books._write_text_to_file(
            f"{os.path.dirname(os.path.realpath(__file__))}/{filename}", response)

    def multi_download(self):
        workers = 4
        with ThreadPoolExecutor(workers) as ex:
            res = ex.map(lambda p: Books.download(
                *p), zip(self.url_list, self.filenames))
        return list(res)

    def urllist_generator(self):
        for url in self.url_list:
            yield url

    def avg_vowels(text):
        vowels = "AaEeIiOoUu"
        count = len([char for char in text if char in vowels])
        return count / len(text.split(' '))

    def _read_file_to_string(filename):
        with open(filename) as file_object:
            contents = file_object.read()
        return contents

    def _read_multi_files(filenames):
        workers = 4
        args = filenames
        with ThreadPoolExecutor(workers) as ex:
            res = ex.map(Books._read_file_to_string, args)
        return list(res)

    def _get_basename(filename):
        base = os.path.basename(filename)
        return os.path.splitext(base)[0]

    def hardest_read():
        txt_files = [f for f in glob.glob(
            os.path.dirname(os.path.realpath(__file__))+"/*.txt")]
        books = Books._read_multi_files(txt_files)
        filenames = [Books._get_basename(filename) for filename in txt_files]
        workers = 4
        with ProcessPoolExecutor(workers) as ex:
            res = ex.map(Books.avg_vowels, books)
        results = list(res)
        # {txt_files[results.index(max(results))]: max(results)}
        return filenames, results


# if __name__ == "__main__":
#     urls = ["https://www.gutenberg.org/files/1342/1342-0.txt",
#             "https://www.gutenberg.org/ebooks/16328.txt.utf-8", "https://www.gutenberg.org/files/25344/25344-0.txt", "https://www.gutenberg.org/files/1250/1250-0.txt", "https://www.gutenberg.org/files/84/84-0.txt", "https://www.gutenberg.org/files/1952/1952-0.txt", "https://www.gutenberg.org/files/11/11-0.txt", "https://www.gutenberg.org/ebooks/2542.txt.utf-8", "https://www.gutenberg.org/ebooks/23.txt.utf-8", "https://www.gutenberg.org/files/1080/1080-0.txt"]
#     filenames = ["pride_and_prejudice.txt",
#                  "Beowulf.txt", "Scarlet_letter.txt", "Anthem.txt", "Frankenstein.txt", "Yellow_WallPaper.txt", "Alice_Adventures.txt", "doll_house.txt", "Life_of_Frederick.txt", "Modest_Proposal.txt"]
#     book = Books(urls, filenames)
#     book.multi_download()
#     hard_read = Books.hardest_read()
#     print(hard_read)

    ##book.download(url, "test.txt")
