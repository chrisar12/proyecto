from pandas import read_csv
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.tree import tree, export_graphviz

reglog = linear_model.LogisticRegression()
navidad = tree.DecisionTreeClassifier()
archivo = 'dataset_final.csv'

df = read_csv(archivo)

# print(df)

arreglox = df[df.columns[1:-1]].as_matrix()
arregloy = df[df.columns[-1]].as_matrix()

# print(arregloy)


# jugando con el modelo

X_train, X_test, y_train, y_test = train_test_split(arreglox, arregloy)

entrena = navidad.fit(X_train, y_train)  # reglog.fit(X_train, y_train)
entrena2 = reglog.fit(X_train, y_train)  # reglog.fit(X_train, y_train)

print(entrena)
print(str(entrena.score(X_test, y_test)) + ' scort arbol ')

print(entrena2)
print(str(entrena2.score(X_test, y_test)) + ' scort regresion lineal ')

export_graphviz(navidad, out_file='arbol1.dot',
                impurity=False, filled=True)
