""" This is the main py file to run the program.

It accepts three outputs:
 1. Name of the first artist
 2. Name of the second artist
 3. The lyrics that the user wants to predict

 If the csv file of the artist's lyrics doesnt exist the program scrape it and
 save it as csv file and train a naive bayes model to predict the artitst of
 the given lyrics.
 """
import os.path
from vectorize_and_train import clean_vectorize_train_naive_bayes
from get_urls_and_scrape import get_urls, lyrics_scraper
from get_urls_and_scrape import get_urls_scrape_save_as_csv
from clean_and_save import clean_and_save_as_csv


if __name__ == '__main__':
    print("Please enter the name of the first artist:")
    ARTIST_1 = input()
    print("Please enter the name of the second artist:")
    ARTIST_2 = input()
    print("Write a song that you want to predict to which artist it belongs:")
    LYRICS = input()

    get_urls_scrape_save_as_csv(ARTIST_1)
    get_urls_scrape_save_as_csv(ARTIST_2)

    clean_vectorize_train_naive_bayes(ARTIST_1, ARTIST_2, LYRICS)