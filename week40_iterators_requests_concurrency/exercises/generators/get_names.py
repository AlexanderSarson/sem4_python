def name_reader(names):
    for name in names:
        yield name


def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row.replace('\n', '')


if __name__ == "__main__":
    names = ["Hans", "Grethe", "Lotte", "Ivan"]
    name_gen = name_reader(names)
    print(next(name_gen))
