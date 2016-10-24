#!/usr/bin/python

import sys, os, time
fdesc = open("train.csv", "r")
count = 0
featureDict = dict()
featureDict["cat"] = 0
featureDict["cont"] = 0
for line in fdesc:
    if count < 5:
        if count == 0 :
            features = line.split(',')
            for feature in features:
                if "cat" in feature:
                    featureDict["cat"] = featureDict["cat"] + 1
                if "cont" in feature:
                    featureDict["cont"] = featureDict["cont"] + 1
    count += 1

print "Continuos features are " + str(featureDict["cont"])
print "Categorical features are " + str(featureDict["cat"])
    