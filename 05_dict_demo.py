my_dict = {
    "double": 2,
    "half": 0.5
}

your_num = int(input("Enter a number: "))
to_do = input ("double or half? ").lower()

# look up value
multiply_by = my_dict[to_do]

# do math!
answer = your_num * multiply_by
print("{} x {} = {}".format(your_num, multiply_by, answer))