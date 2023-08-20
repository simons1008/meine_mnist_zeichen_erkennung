# MNIST digits classification
# MNIST - Modified National Institute of Standards and Technology databaset
# Quelle: https://eloquentarduino.com/micropython-machine-learning/

# Bibliotheken importieren
from everywhereml.sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

# Trainingsdaten laden
X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Modell erstellen
clf = RandomForestClassifier(n_estimators=7, max_leaf_nodes=20)
# Mit den Trainingsdaten trainieren (fit - dazupassen)
clf.fit(X_train, y_train)

# Ergebnis ausgeben
print('Training completed')
print('Score: {:5.2f}'.format(clf.score(X_test, y_test)))
input('Continue? ')

# Klassifikator zu MicroPython portieren
# Ergebnis speichern und drucken
print(clf.to_micropython_file('random_forest.py'))
print('Port to MicroPython completed')

# Ende
input('Done? ')
