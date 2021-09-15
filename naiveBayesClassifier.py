import pandas as pd
import re

train_file = "train.csv"
test_file = "test.csv"
evaluation_file = "evaluation.csv"

train_set = pd.read_csv(train_file)
test_set = pd.read_csv(test_file)
evaluation_set = pd.read_csv(evaluation_file)


# Some of data include HTML tags, hashtags, mentions, emojis etc. so you need to do pre-processing.
def clean_up_data(data):
    clean_reviews = []
    
    for review in data.text:
        # remove links
        clean_review = re.sub(r"http\S+", "", review)
        # remove @ mentions
        clean_review = re.sub("@[A-Za-z0-9_]+","", clean_review)
        # remove hashtags
        clean_review = re.sub("#[A-Za-z0-9_]+","", clean_review)
        # remove HTML tags
        clean_review = re.sub("<.*?>", "", clean_review)
        # remove emjois
        clean_review = re.sub("[\U00010000-\U0010ffff]", "", clean_review)
        
        clean_reviews.append(clean_review)
    return clean_reviews
    
train_set.text = clean_up_data(train_set)

print(train_set)