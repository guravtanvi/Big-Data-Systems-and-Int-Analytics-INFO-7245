import os
import string


def annotate(file_path):

    cleaned_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Clean_data', 'Cleaned_annotation.txt'))
    with open(file_path) as infile, open(cleaned_file, 'w') as outfile:
        for line in infile:
            if not line.strip(): continue
            string.punctuation = '!"#&'
            new_line = ' '.join(word.strip(string.punctuation) for word in line.split())
            outfile.write(new_line + '\n')  # non-empty line. Write it to output

    sentences = []
    with open(cleaned_file) as infile:
        for line in infile:
            text = line[:-1]
            sentences.append(text)

    return {"data": sentences}