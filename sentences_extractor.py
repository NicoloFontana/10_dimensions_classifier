import csv
import json
import random
import sys
from datetime import datetime as dt

## from Reddit conversations
file = open(
    'C:\\Users\\fonta\\PycharmProjects\\10_dimensions_classifier\\data\\cornell_reddit_corpus_small\\utterances.json')
corpus = json.load(file)

words_LB = 10
words_UB = 15
enough_words = [s for s in corpus if
                ((s['text'].count(' ') + s['text'].count('\t') + s['text'].count('\n')) > words_LB and
                 (s['text'].count(' ') + s['text'].count('\t') + s['text'].count('\n')) < words_UB)]
# print(f"#long_enough: {len(enough_words)}")
k = 10
samples = random.sample(enough_words, k=k)
# print(samples)
samples_min = [{"id": sample["id"], "text": sample["text"]} for sample in samples]
# print(samples_min)
samples_min_dict = {sample["id"]: sample["text"] for sample in samples_min}
# print(samples_min_dict)

# for s in samples:
#     ## printing debug
#     text = s['text']
#     spaces = text.count(' ')
#     tabs = text.count('\t')
#     newlines = text.count('\n')
#     words = spaces + tabs + newlines
#     print(f"text: {s['text']}")
#     print(f"#words: {words}")
#     print(f"#chars: {len(s['text'])}")

timestamp = dt.now().strftime("%Y%m%d%H%M")
OUT_FILE_NAME = f"{k}_reddit_samples_{timestamp}.txt"
OUT_FILE_PATH = f'C:\\Users\\fonta\\PycharmProjects\\10_dimensions_classifier\\out\\{OUT_FILE_NAME}'
# print(OUT_FILE_PATH)

with open(OUT_FILE_PATH, 'w') as convert_file:
    convert_file.write(json.dumps(samples_min_dict))
with open(OUT_FILE_PATH, 'a') as f:
    f.write(
        '\n\nAnswer with a single JSON-formatted text containing the id, the text and the scores for each sentence.')

print(f"Generated file {OUT_FILE_NAME} of {k} sentences between {words_LB} and {words_UB} words")

## from Twitter sentiment analysis
# with open('C:\\Users\\fonta\\PycharmProjects\\10_dimensions_classifier\\data\\sentiment140\\testdata.manual.2009.06.14.csv', newline='') as csvfile:
#     tweets = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
#     selected = random.sample(tweets, k=5)
