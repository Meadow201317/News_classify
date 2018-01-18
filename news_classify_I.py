#To classify the txt score in Industry category

import nltk
import random
#from nltk.corpus import PlaintextCorpusReader 
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
import string
from nltk.corpus import LazyCorpusLoader, CategorizedPlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.classify import ClassifierI
from statistics import mode


# corpus_root = r"C:\Users\lenovo\AppData\Roaming\nltk_data\corpora\news"
# wordlists = PlaintextCorpusReader (corpus_root, '.*')
# print(wordlists.fileids())

industry = LazyCorpusLoader('Industry', CategorizedPlaintextCorpusReader, r'(?!\.).*\.txt', cat_pattern=r'(neg2|neg1|zero|pos1)/.*', encoding='utf-8') 
#在corpus中导入Industry文件，文件是txt格式，分为四个categories，分别是neg2,neg1,zero和pos1

# stop = stopwords.words('english')
# documents = [([w for w in news.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in news.fileids()]
# for i in documents:
    # print (i)

class VoteClassifier(ClassifierI):
	def __init__(self, *classifiers):
		self._classifiers = classifiers
		
	def classify(self, features):
		votes = []
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
		return mode(votes)
	
	def confidence(self, features):
		votes = []
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
			
		choice_votes = votes.count(mode(votes))
		conf = choice_votes / len(votes)
		return conf

documents = [(list(industry.words(fileid)),category)
              for category in industry.categories()
			  for fileid in industry.fileids(category)] #document是以list的方式储存每个news，并在后面添上category
			  
random.shuffle(documents)

#print (documents[j]) 

all_words = [] 

for w in industry.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(15))
# #print (all_words["stupid"])
word_features = list(all_words.keys())[:6000]
# #print(word_features)

def find_features(document):  #可以对比如某个文件中是否存在关键的6000词进行判断
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
		
	return features

# print ((find_features(news.words('C/bb-cp-0002.txt'))))

featuresets = [(find_features(rev),category) for (rev, category) in documents]

training_set = featuresets[:130]
testing_set = featuresets[130:]

classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open("naivebayes_2.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)	
classifier.show_most_informative_features(20)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BNB_classifier accuracy percent:", (nltk.classify.accuracy(BNB_classifier, testing_set))*100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy persent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print ("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

# SVC_classifier = SklearnClassifier(SVC())
# SVC_classifier.train(training_set)
# print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

voted_classifier = VoteClassifier(classifier, NuSVC_classifier, LinearSVC_classifier, SGDClassifier_classifier, MNB_classifier, BNB_classifier, LogisticRegression_classifier)

print ("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)

print("Classification:", voted_classifier.classify(testing_set[0][0]), "Confidence %:",voted_classifier.confidence(testing_set[0][0])*100)
print("Classification:", voted_classifier.classify(testing_set[1][0]), "Confidence %:",voted_classifier.confidence(testing_set[1][0])*100)
print("Classification:", voted_classifier.classify(testing_set[2][0]), "Confidence %:",voted_classifier.confidence(testing_set[2][0])*100)
print("Classification:", voted_classifier.classify(testing_set[3][0]), "Confidence %:",voted_classifier.confidence(testing_set[3][0])*100)
print("Classification:", voted_classifier.classify(testing_set[4][0]), "Confidence %:",voted_classifier.confidence(testing_set[4][0])*100)
print("Classification:", voted_classifier.classify(testing_set[5][0]), "Confidence %:",voted_classifier.confidence(testing_set[5][0])*100)


# save_classifier = open("naivebayes_2.pickle","wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()
