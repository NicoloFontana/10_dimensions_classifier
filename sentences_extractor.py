import csv
import json
import random

## from Reddit conversations
file = open('C:\\Users\\fonta\\PycharmProjects\\10_dimensions_classifier\\data\\cornell_reddit_corpus_small\\utterances.json')
corpus = json.load(file)
enough_words = [s for s in corpus if ((s['text'].count(' ') + s['text'].count('\t') + s['text'].count('\n')) > 9 and
                                      (s['text'].count(' ')+s['text'].count('\t')+s['text'].count('\n')) < 12)]
print(f"#long_enough: {len(enough_words)}")
samples = random.sample(enough_words, k=10)
print(samples)
samples_min = [{"id": sample["id"], "text": sample["text"]} for sample in samples]
print(samples_min)
samples_min_dict = {sample["id"]: sample["text"] for sample in samples_min}
print(samples_min_dict)

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

with open('C:\\Users\\fonta\\PycharmProjects\\10_dimensions_classifier\\out\\reddit_samples.txt', 'w') as convert_file:
     convert_file.write(json.dumps(samples_min_dict))

## from Twitter sentiment analysis
# with open('C:\\Users\\fonta\\PycharmProjects\\10_dimensions_classifier\\data\\sentiment140\\testdata.manual.2009.06.14.csv', newline='') as csvfile:
#     tweets = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
#     selected = random.sample(tweets, k=5)