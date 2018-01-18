# News_classify
the program is based on the news_crawl repository and rating by the professionals.

all the news I crawled are in the NEWS folder and the ratings are saved in excel ratings.xlsx

procedure:
1. open the rating.xlsx, classify the news according to Industry and Company and then transpose these news name for each category.
2. copy the news name labeled as "I" and "C" and plaste them on the document_classify.py then we can save them into two folders as "I" and "C".
3. New a folder name "news" in C:\Users\lenovo\AppData\Roaming\nltk_data\corpora. Copy the "I" and "C" folder into it. (this procedure is designed to conveniently use the corpus exist in NLTK package.
4. open the news_classifiy.py. comment these three lines:
    classifier_f = open("naivebayes.pickle","rb")
    classifier = pickle.load(classifier_f)
    classifier_f.close()
   and clear block commet of these three lines:
    # save_classifier = open("naivebayes.pickle","wb")
    # pickle.dump(classifier, save_classifier)
    # save_classifier.close()    
   Then we get the naivebayes.pickle
5. Do the above thing in reverse way, save it, and run it 
   Then we can get the classification of Industry news and Company news
