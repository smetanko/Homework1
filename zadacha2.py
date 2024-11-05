files = ['1.txt', '2.txt', '3.txt']
def read_file(file):
    with open (file, 'r', encoding='UTF-8') as f:
        spisok_strok = []

        for line in f:
            spisok_strok.append(line.strip())
        return file, len(spisok_strok), spisok_strok

name_file, len_spisok, text = read_file('1.txt')
def all_files(files):
    safe = []
    for file in files:
        safe.append(read_file(file))
    sorted_data_list = sorted(safe, key=lambda x: x[1])
    return sorted_data_list
print(all_files(files))
def write_file(name, files):
    with open(name, 'a', encoding='UTF-8') as f:
        for stroka in all_files(files):
            for element in stroka:
                if type(element) == str or type(element) == int:
                    f.write(str(element) + '\n')
                elif type(element) == list:
                    f.write(('\n').join(element) + '\n')
    return name
print(write_file('5.txt', files))




