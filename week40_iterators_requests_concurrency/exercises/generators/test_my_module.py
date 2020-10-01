import get_names

names = ["Hans", "Grethe", "Lotte", "Ivan"]
name_gen = get_names.name_reader(names)
csv_gen = get_names.csv_reader("unisex_names.txt")


def get_names_n(n):
    counter = 0
    while counter < n:
        counter += 1
        print(next(csv_gen))


get_names_n(10)
