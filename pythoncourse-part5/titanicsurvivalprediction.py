import autokeras as ak

# Initialize the classifier.
clf = ak.StructuredDataClassifier(max_trials=120)
# x is the path to the csv file. y is the column name of the column to predict.
clf.fit(x='c:/dev/train.csv', y='survived', epochs=3000)
# Evaluate the accuracy of the found model.
print('Accuracy: {accuracy}'.format(
    accuracy=clf.evaluate(x='c:/dev/eval.csv', y='survived')))
