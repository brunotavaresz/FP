with open("names.txt" , "r", encoding="utf-8" ) as file:
    names = {}
    file.readline()
    for line in file:
        name_as_list = line.rstrip().split(" ")
        first_name = name_as_list[0]
        last_name = name_as_list[-1]
        if last_name in names:
            names[last_name].add(first_name)
        else:
            names[last_name] = {first_name}
    print(names)


