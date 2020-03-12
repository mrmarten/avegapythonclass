import autokeras as ak
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import cifar100

# %matplotlib inline


# Prepare the dataset.
(x_train, y_train), (x_test, y_test) = cifar100.load_data()
print(x_train.shape)  # (60000, 28, 28)
print(y_train.shape)  # (60000,)
print(y_train[:3])  # array([7, 2, 1], dtype=uint8)

_, canvas = plt.subplots(1, 2)
_ = canvas[0].imshow(x_train[1234])
x_train[1234].show()
_ = canvas[1].imshow(x_test[1234])

# Initialize the ImageClassifier.
clf = ak.ImageClassifier(max_trials=3)
# Search for the best model.
clf.fit(x_train, y_train, epochs=10)
# Evaluate on the testing data.
print('Accuracy: {accuracy}'.format(
    accuracy=clf.evaluate(x_test, y_test)))
