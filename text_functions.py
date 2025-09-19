# # returns just letters in all lowercase; default no spaces 
# # option to maintain spaces and keep capitalization
# def letters_only():

# #returns just capitals
# def capitals_only():

# # removes spaces and inessential grammar (e.g. does not include quotation, mid-word hyphen, etc.)
# # note: make sure to include hyphen and long dash as grammar points, but not mid-word hyphens/dashes
# # note: do not include marks periods before numbers 
# def letters_and_grammar():

# # returns capitals and grammar marks
# # options to include all punctuation points
# # note: do not include marks periods before numbers 
# def capitals_and_grammar():

# #removes spaces
# def remove_spaces():

# #capitalize all letters
# def capitalize():

# #de-capitalize all letters
# def decapitalize():

# # writes text to external file
# def output_to_file():

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
