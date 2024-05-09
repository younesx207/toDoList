# add dependancies 
- pytest pour les tests 


# Tests
## Installation de pytest

- test files
python -m pip install --upgrade pip 
pip install pytest
pytest --version

## Créer un fichier de test
Dans le dossier "tests", créer un nouveau fichier appelé "test_add.py" et ajouter ce code :
python  
python3
python3.9
print("Hello World")
## Exécuter des tests avec la commande pytest

- Ouvrir une console dans VSCode (F12) puis exécuter
bash: pytest test_add.py
ou simplement
pytest test_add.py

## Les assertions
Les assertions sont utilisées pour définir les résultats attendus. Si l'assertion est vraie, alors tout est bien. Sinon, il y a une erre
Les assertions sont utilisées pour vérifier si un élément est vrai ou non
python
assert True, "This is true"
assert False, "This is false"
La dernière assertion ne s'exécutera pas car elle est fausse. Pour que cela fonctionne, il faut utiliser l'argument "-x" qui arrête à
La ligne ci-dessus va lever une exception AssertionError car l'expression est fausse
## Les messages d'erreur personnalisés
On peut donner un message à afficher en cas d'échec de l'assertion
python
assert False, "This is false because ..."
Le message d'erreur par défaut est "AssertionError". On peut changer cela mais il est préférable de ne pas le faire. Il est mieux de
Le message d'erreur par défaut est "AssertionError". On peut changer cela mais il est préférable de ne pas le faire car c'est décon
Le message d'erreur par défaut est "AssertionError". On peut changer cela en passant un second argument à l'assertion.
Le message d'erreur par défaut est "AssertionError: False is not true" mais on peut modifier cela
python
assert False, "This is false because ...", extra="Extra information here"
Le message d'erreur sera donc "AssertionError: This is false because ...\nExtra information here"
## Les classes de base d'assertion
Il y a plusieurs classes de base d'assertion qui peuvent être utilisée pour définir votre propre assertion. Par exemple, `py
Il y a plusieurs classes de base d'assertion qui peuvent être utilisée pour définir votre propre assertion. Par exemple, `py
Il y a plusieurs classes de base d'assertion qui peuvent être utilisée pour définir votre propre assertion. Par exemple, `pytest.raises
Il existe plusieurs classes de base d'assertion qui peuvent être utiles
- `AssertionError` : La classe de base d'assertion standard. Elle est levée lorsque l'assertion est fausse.
