import pandas as pd
import json
import random
word_list = pd.read_csv("C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/data/french_words.csv", header=None, index_col=0)
word_list = word_list[1]
del(word_list["French"])
json_wordlist = "C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/data/french_words.json"
output = word_list.to_json(json_wordlist, indent = 4)
decoded_output = json.dumps(output, ensure_ascii=False).encode('utf8')



    

with open("C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/data/words_to_learn.json") as inputfile:
    df = pd.DataFrame(inputfile)


df.to_csv("C:/Users/Asanka/Desktop/Python Practice/flash-card-capstone/data/words_to_learn.csv", index=False)
       