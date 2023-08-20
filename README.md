# Meine MNIST Zeichen-Erkennung
Auf dem PC wird durch "Supervised Machine Learning" ein Klassifikator für die Erkennung der handgeschriebenen Zeichen 0 bis 9 erstellt. Der Klassifikator wird auf MicroPython portiert und auf einem ESP32 ausgeführt. 

## Voraussetzungen
Auf dem PC müssen folgende Bibliotheken installiert sein:
- scikit-learn
- everywhereml

Diese sind auf https://pypi.org/ verfügbar. 

## Ausführung auf dem PC
1. Auf dem PC wird das Programm MNIST_digits_classification.py gestartet. Das Programm importiert die Bibliotheken und die Testdaten. Die Testdaten stammen aus der MNIST Datenbank (Modified National Institute of Standards and Technology database). 
2. Das Programm erstellt einen RandomForestClassifier und trainiert ihn mit MNIST Trainingsdaten. Anschließend wird der Klassifikator auf MNIST Testdaten angewandt und die Erkennungsleistung angegeben (score). Der Klassifikator darf nicht zu komplex werden. Deshalb sind wir mit einer Erkennungsleistung von unter 90 % zufrieden. 
3. Danach wird der Klassifikator nach MicroPython portiert. Das Ergebnis ist die Datei random_forest.py.  

## Ausführung auf dem ESP32
1. Auf den ESP32 werden kopiert:
- main.py
- mnist.py (Testdaten)  
- random_forest.py
2. Auf dem ESP32 wird main.py (durch reboot) gestartet. Das Ergebnis ist eine Liste mit erwarteten Zeichen und erkannten Zeichen. Wir sehen 1 oder  2 falsch erkannte Zeichen. Das liegt an der oben angegebenen Erkennungsleistung. 

## Testdaten als Bild anzeigen
Die Testdaten in mnist.py sind ein Array mit der Dimension (10, 64). Es sind 10 handgeschriebene Zeichen, die durch eine Reihe mit 64 Grauwerten dargestellt werden. Der Index 0 enthält eine handgeschriebene Null, usw. 

Das PC-Programm show_test_digits.py stellt die ursprünglichen 8 x 8 Grauwerte wieder her. Anschließend wird für jedes Zeichen eine Funktion aus der matplotlib aufgerufen, die das Zeichen als Bild anzeigt. test_digits.png zeigt das Ergebnis. Das Zeichen '5' ist wirklich schlecht erkennbar. 

## Quellen
Die Idee und die Programme stammen von hier: https://eloquentarduino.com/micropython-machine-learning/ Ich habe die Programme kommentiert und erweitert. Hinweis: Bei der Ausführung von MNIST_digits_classification.py werden "Warnings" ausgegeben.

Der Code für die Anzeige der Testdaten als Bild stammt von hier:  https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html 

## Dank 
Ich danke dem Autor "eloquentarduino" für seinen hilfreichen Beitrag. 