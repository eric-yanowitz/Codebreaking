def file_content(file_path, lines = False, strip = False):
    with open(file_path, 'r') as file:
        if lines == False:
            file_content = file.read()
        elif lines == True:
            file_content = file.readlines()
        elif lines == True and strip == True:
            file_content_temp = file.readlines()
            file_content = []
            for line in file_content_temp:
                file_content.append(line.strip())
    return file_content


def words_of_length(text, n):
    all_words = text.split()
    words = {}
    for i in all_words:
        if len(i) == n: 
            if i not in words:
                words[i] = 1
            else: 
                words[i] += 1
    return words
