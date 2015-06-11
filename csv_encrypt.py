from pandas import *
import os
from AESCipher import AESCipher

def list_files(path):
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files

csv_dir = os.getcwd()
csv_files = list_files(os.path.join(csv_dir, "csv_sample"))
columns_to_encrypt = ['Time','User ID']
cypher_obj = AESCipher("2805")

encrpyt_mapping = []
for col in columns_to_encrypt:
    encrpyt_mapping.append(col)
    encrpyt_mapping.append(col + " encrpted_value")

for csv_file in csv_files:
    mapping_df = DataFrame(columns=(encrpyt_mapping))
    data =  read_csv(os.path.join(csv_dir, "csv_sample",csv_file))
    for index, row in data.iterrows():
        i=0
        for col in columns_to_encrypt:
            encoded = cypher_obj.encrypt(row[col])
            data.loc[index,col] = encoded
            mapping_df.loc[index,encrpyt_mapping[i]] = row[col]
            mapping_df.loc[index,encrpyt_mapping[i+1]] = encoded
            i += 2
            #decrypt_user = cypher_obj.decrypt(encoded)
            #print("decrypted : %s" % decrypt_user)
    data.to_csv(os.path.join(csv_dir, "csv_sample","enc_" + csv_file), encoding='utf-8')
    mapping_df.to_csv(os.path.join(csv_dir, "csv_sample","mapping_" + csv_file), encoding='utf-8')