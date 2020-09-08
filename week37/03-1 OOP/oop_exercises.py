import string


class TextContainer():
    def __init__(self, text):
        self.text = text

    def countWords(self):
        return len(self.text.split(' '))

    def countChars(self):
        return len(self.text)

    def countLetters(self):
        letter_list = [
            letter for letter in self.text if string.ascii_letters.find(letter) != -1]
        return len(letter_list)

    def removePunctuation(self):
        letter_list = [
            letter for letter in self.text if string.punctuation.find(letter) == -1]
        self.text = "".join(letter_list)


words = "hej med ...dig flere ord. %"

container = TextContainer(words)


print(container.countWords())
print(container.countChars())
print(container.countLetters())

print(container.text)
container.removePunctuation()
print(container.text)
