from pandas import *
import os
import math
from AESCipher import AESCipher

def list_files(path):
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files

# Configuration
csv_dir = "/Users/padmakar/PycharmProjects/csv_encrrypt/csv_sample"
csv_files = list_files(os.path.join(csv_dir))
cypher_obj = AESCipher('2805')
header_row = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7',
              'col8', 'col9', 'col10', 'col11','col12', 'col13', 'col14', 'col15']
columns_to_decrypt = ['col5']

encrpyt_mapping = []
for col in columns_to_decrypt:
    encrpyt_mapping.append(col)
    encrpyt_mapping.append(str(col) + " decrypted_value")

for csv_file in csv_files:
    print "Parsing csv file  %s" % csv_file
    mapping_df = DataFrame(columns=encrpyt_mapping)
    data = read_csv(os.path.join(csv_dir, csv_file), error_bad_lines=False, names=header_row, dtype='unicode')
    print "Encrypting of data in csv file %s is starting" % csv_file

    for col in columns_to_decrypt:
        print(col)
        for index, row in data.iterrows():
            # i = 0
            #print str(row[col])
            """if isinstance(row[col], float):
                if math.isnan(row[col]):
                    row[col] = str(row[col])
                else:
                    row[col] = int(row[col])"""
            data.loc[index, col] = cypher_obj.decrypt(str(row[col]))
            #encoded = cypher_obj.encrypt(str(row[col]))
            #data.loc[index, col] = encoded
            # print(encoded + " " + cypher_obj.decrypt(encoded))
            # mapping_df.loc[index, encrpyt_mapping[i]] = row[col]
            # mapping_df.loc[index, encrpyt_mapping[i+1]] = encoded
            # i += 2
    print "Decrypting of data in csv file %s is completed" % csv_file
    print "Writing CSV file for decrypted data"
    data.to_csv(os.path.join(csv_dir, "dec_" + csv_file), encoding='utf-8')
    # mapping_df.to_csv(os.path.join(csv_dir, "mapping_" + csv_file), encoding='utf-8')
