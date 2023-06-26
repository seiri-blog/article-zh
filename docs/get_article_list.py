import os
import re
import pandas as pd


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)


df = pd.DataFrame()
for file in find_all_files('./targetDir'):
    if file[-3:].lower() == '.md':
        file_new = file.replace('./targetDir', '')
        year = file_new[1:5]
        month_day = file_new[6:11]
        month_day = re.search(r'\d+-\d+', month_day).group(0)
        dirs = file_new.split('\\')
        article_name = dirs[2].replace(month_day, '')[1:].replace('-', ' ')
        df = df.append(pd.DataFrame({'date': [year + '-' + month_day],
                                     'name': ['[' + article_name + '](' + file + ')']}))
df.to_csv('result.csv', encoding='utf-8')
