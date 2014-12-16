from __future__ import unicode_literals
import nltk
from nltk.classify import NaiveBayesClassifier

def gender_features(n):
	return {'last letter': n[-1]}
from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name,'female') for name in names.words('female.txt')])
import random
random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender) for (n,gender) in labeled_names]
train_set = featuresets[:500]
test_set = featuresets[500:]
#classifier = nltk.classify.naivebayes.train(train_set)
classifier = NaiveBayesClassifier.train(train_set)
print classifier.classify(gender_features('Dickshitha'))
print(nltk.classify.accuracy(classifier, test_set))