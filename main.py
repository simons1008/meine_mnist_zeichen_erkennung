# Klassifikator auf Testdaten anwenden und Voraussage machen
# Quelle: https://eloquentarduino.com/micropython-machine-learning/

from random_forest import RandomForestClassifier
from mnist import mnist

clf = RandomForestClassifier()

for idx, x in enumerate(mnist):
    print('expected {:}, got {:}'.format(idx, clf.predict(x)))

# Ende
input("Fertig? ")
