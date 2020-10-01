def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row


def name_reader(names):
    for name in names:
        yield name


names = ["Hans", "Grethe", "Lotte", "Ivan"]
csv_gen = csv_reader("unisex_names.txt")
row_count = 0

# for row in csv_gen:
#     row_count += 1

# print(f"Row count is {row_count}")
# print(next(csv_gen))
# print(next(csv_gen))
# print(next(csv_gen))
# print(next(csv_gen))
name_gen = name_reader(names)

print(next(name_gen))
print(next(name_gen))
print(next(name_gen))
print(next(name_gen))
