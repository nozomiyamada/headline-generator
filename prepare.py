import numpy as np
import glob
import csv
from pythainlp import word_tokenize
import random

def tokenize(filename='thairath1.tsv'):
    """
    tokenize headline (line[1]) & description (line[2])
    save as txt with whitespace
    """
    path = '/Users/Nozomi/files/metonymy/'
    open_name = path + filename
    save_name = open_name.rsplit('.tsv')[0]
    open_file = open(open_name, 'r', encoding='utf-8')

    title_file = open(save_name + '_title.tsv', 'w', encoding='utf-8')
    description_file = open(save_name + '_description.tsv', 'w', encoding='utf-8')

    articles = csv.reader(open_file, delimiter='\t')
    write1 = csv.writer(title_file, lineterminator='\n', delimiter='\t')
    write2 = csv.writer(description_file, lineterminator='\n', delimiter='\t')

    for article in articles:
        if article[2] != '':
            ID = [article[0]]
            title = word_tokenize(article[1])
            description = word_tokenize(article[2])

            write1.writerow(ID + title)
            write2.writerow(ID + description)

    open_file.close()
    title_file.close()
    description_file.close()
