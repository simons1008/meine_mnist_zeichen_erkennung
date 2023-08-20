# Testdaten anzeigen
# Quellen: https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#sphx-glr-auto-examples-classification-plot-digits-classification-py
#          https://eloquentarduino.com/micropython-machine-learning/ 

# Bibliotheken importieren
import matplotlib.pyplot as plt
import numpy as np
# Testdaten importieren
from mnist import mnist

# Testdaten in numpy-array konvertieren
mnist_array = np.array(mnist)
# Testdaten von 10 x 64 Grauwerte in 10 x 8 x 8 Grauwerte konvertieren
mnist_array = np.reshape(mnist_array, (10, 8, 8))

# Testdaten als Bilder anzeigen
_, axes = plt.subplots(nrows=1, ncols=10, figsize=(20, 3))
# Bei den Testdaten entspricht der Index (idx) dem Sollwert
# x enthält die 8 x 8 Grauwerte
for idx, x in enumerate(mnist_array):
    ax = axes[idx]
    ax.set_axis_off()
    ax.imshow(x, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Soll: {:}".format(idx))
plt.show()
