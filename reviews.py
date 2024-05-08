import pandas as pd

#read in data from given csv file
wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv/winemag-data-130k-v2.csv")

#create summary of data that contains: name, # of reviews, and average points for each unique country
count = wine_reviews.groupby('country').size()
points_mean = wine_reviews.groupby('country')['points'].mean()

#creat dataframe
reviews_sum = pd.DataFrame({
    'country': count.index,
    'count': count,
    'points': points_mean.values.round(1)})

#set index of dataframe
reviews_sum.set_index('country', inplace=True)

#write data to csv file
reviews_sum.to_csv('data/reviews-per-country.csv')