import pandas as pd
import numpy as np
from numpy import delete
import matplotlib

# lectura del excel
data = pd.read_excel('libro1.xlsx')
# creamos dataframe del excel
df = pd.DataFrame(data)

# jugamos con el dataframe, contamos la cantidad de la columna raza
df['raza'].count()
df.isnull().any().any()
# verificar si el dataframe tiene algun campo vacio, si es true=si tiene campos vacios
df.isnull().any()

# eliminamos los duplicados, considerando el campp/atributo num_paciente y solo tomamos el primero
df_elimina = df.drop_duplicates(subset='num_paciente', keep='first')

# ahora eliminamos las filas que tiwnen datos perdidos = '?'
# eliminar filas con raza = ?
df_elimina = df_elimina[df_elimina['raza'] != '?']
# eliminamos los otros campos con datos perdidos
# eliminar filas con dadoalta_tipo=11
df_elimina = df_elimina[df_elimina['dadoalta_tipo'] != 11]
# eliminar filas con dadoalta_tipo=13
df_elimina = df_elimina[df_elimina['dadoalta_tipo'] != 13]
# eliminar filas con dadoalta_tipo=14
df_elimina = df_elimina[df_elimina['dadoalta_tipo'] != 14]
# eliminar filas con dadoalta_tipo=19
df_elimina = df_elimina[df_elimina['dadoalta_tipo'] != 19]
# eliminar filas con dadoalta_tipo=20
df_elimina = df_elimina[df_elimina['dadoalta_tipo'] != 20]
# eliminar filas con dadoalta_tipo=21
df_elimina = df_elimina[df_elimina['dadoalta_tipo'] != 21]
# eliminar filas con dadoalta_tipo=25
df_elimina = df_elimina[df_elimina['dadoalta_tipo'] != 25]
# eliminar filas con dadoalta_tipo=21
df_elimina = df_elimina[df_elimina['dadoalta_tipo'] != 18]
# eliminar filas con dadoalta_tipo=21
df_elimina = df_elimina[df_elimina['dadoalta_tipo'] != 26]

# eliminar filas con tipo_admision=6
df_elimina = df_elimina[df_elimina['tipo_admision'] != 6]

# eliminar filas con origen_admision=9
df_elimina = df_elimina[df_elimina['origen_admision'] != 9]
# eliminar filas con origen_admision=9
df_elimina = df_elimina[df_elimina['origen_admision'] != 15]
# eliminar filas con origen_admision=9
df_elimina = df_elimina[df_elimina['origen_admision'] != 17]
# eliminar filas con origen_admision=9
df_elimina = df_elimina[df_elimina['origen_admision'] != 20]
# eliminar filas con origen_admision=9
df_elimina = df_elimina[df_elimina['origen_admision'] != 21]

# completamons los campos vacios el atributo/campo especialidad_medica con la moda de toda la columna
# mode = df_elimina['especialidad_medica'].mode()
# df_elimina['especialidad_medica'] = df_elimina['especialidad_medica'].fillna(mode)

# completamons los campos vacios el atributo/campo especialidad_medica con el valor Faltante
df_elimina['especialidad_medica'] = df_elimina['especialidad_medica'].str.replace("?", "Faltante")

# cambiando los valores categoricos a valores enteros
df_elimina.loc[df_elimina['edad'] == "[0-10)", 'edad'] = 0;
df_elimina.loc[df_elimina['edad'] == "[10-20)", 'edad'] = 10;
df_elimina.loc[df_elimina['edad'] == "[20-30)", 'edad'] = 20;
df_elimina.loc[df_elimina['edad'] == "[30-40)", 'edad'] = 30;
df_elimina.loc[df_elimina['edad'] == "[40-50)", 'edad'] = 40;
df_elimina.loc[df_elimina['edad'] == "[50-60)", 'edad'] = 50;
df_elimina.loc[df_elimina['edad'] == "[60-70)", 'edad'] = 60;
df_elimina.loc[df_elimina['edad'] == "[70-80)", 'edad'] = 70;
df_elimina.loc[df_elimina['edad'] == "[80-90)", 'edad'] = 80;
df_elimina.loc[df_elimina['edad'] == "[90-100)", 'edad'] = 90;
df_elimina['edad'] = df_elimina['edad'].astype(np.int32)

# cambiando los valores categoricos a valores enteros
df_elimina.loc[df_elimina['max_glu_serum'] == "None", "max_glu_serum"] = 0;
df_elimina.loc[df_elimina['max_glu_serum'] == "Norm", "max_glu_serum"] = 100;
df_elimina.loc[df_elimina['max_glu_serum'] == ">200", "max_glu_serum"] = 200;
df_elimina.loc[df_elimina['max_glu_serum'] == ">300", "max_glu_serum"] = 300;
df_elimina['max_glu_serum'] = df_elimina['max_glu_serum'].astype(np.int32)

# cambiando los valores categoricos a valores enteros
df_elimina.loc[df_elimina['A1resultado'] == "None", 'A1resultado'] = 0;
df_elimina.loc[df_elimina['A1resultado'] == "Norm", 'A1resultado'] = 5;
df_elimina.loc[df_elimina['A1resultado'] == ">7", 'A1resultado'] = 7;
df_elimina.loc[df_elimina['A1resultado'] == ">8", 'A1resultado'] = 8;
df_elimina['A1resultado'] = df_elimina['A1resultado'].astype(np.int32)

# cambiando los valores categoricos a valores enteros
df_elimina.loc[df_elimina['cambiomed'] == "No", 'cambiomed'] = 0;
df_elimina.loc[df_elimina['cambiomed'] == "Ch", 'cambiomed'] = 1;
df_elimina['cambiomed'] = df_elimina['cambiomed'].astype(np.int8)

# cambiando los valores categoricos a valores enteros
df_elimina.loc[df_elimina['diabetesMed'] == "No", 'diabetesMed'] = 0;
df_elimina.loc[df_elimina['diabetesMed'] == "Yes", 'diabetesMed'] = 1;
df_elimina['diabetesMed'] = df_elimina['diabetesMed'].astype(np.int8)

# hacemos un lista de medicamentos para trabajar conjuntamente y con el for cambiar datos categoricos a datos numericos
medicamentos = ["metformin", "repaglinide", "nateglinide", "chlorpropamide", "glimepiride", "glipizide",
                "glyburide", "pioglitazone", "rosiglitazone", "acarbose", "miglitol",
                "insulin", "glyburide-metformin"]
for med in medicamentos:
    df_elimina.loc[df_elimina[med] == "No", med] = -20;
    df_elimina.loc[df_elimina[med] == "Down", med] = -10;
    df_elimina.loc[df_elimina[med] == "Steady", med] = 0;
    df_elimina.loc[df_elimina[med] == "Up", med] = 10;
    df_elimina[med] = df_elimina[med].astype(np.int32)

categoria = ['raza', 'genero', 'num_paciente', 'especialidad_medica', 'diag_1', 'diag_2', 'diag_3']

for c in categoria:
    df_elimina[c] = pd.Categorical(df_elimina[c]).codes

# cambiando los valores categoricos a valores enteros
df_elimina.loc[df_elimina['readmision'] != 'NO', 'readmision'] = 0;
df_elimina.loc[df_elimina['readmision'] == 'NO', 'readmision'] = 1;
df_elimina['readmision'] = df_elimina['readmision'].astype(np.int8)

# otra forma de eliminar las filas vacias utilizando el index
# for i in range(1,len(df)):
#   if df.loc[i,'raza']=='?':
#      df.loc[i, 'raza'] = 66

#     df.set_index("raza", inplace=True)

#    df.drop(df.index[66], inplace=True)

# for i in range(1, len(df)):
#   if df.loc[i, 'raza'] == '?':
#      df.drop(df.index[i], inplace=True)
# else:
#    print('aumenta: ',i)

# for i in range(0, 20):
#   if df.loc[i, 'raza'] == '?':
#      df.drop(df.index[?], inplace=True)


# eliminar las columnas que no se utilizaran
df.drop(labels=['admision_id', 'id', 'peso',
                'codigo_vendedor', 'num_proce', 'number_outpatient',
                'number_emerg', 'number_inpatient', 'num_diag', 'acetohexamide',
                'tolbutamide', 'tolazamide', 'examide', 'troglitazone',
                'citoglipton', 'metformin-rosiglitazone', 'metformin-pioglitazone',
                'glipizide-metformin', 'glimepiride-pioglitazone'],
        axis=1, inplace=True)

# df.dropna(subset=["raza","genero"])
# df.drop(df.loc[i, 'raza'],axis=0, inplace=True)


# terminando creamos un nuevo dataset en donde guardaremos el dataframe final
df_elimina.reset_index().to_csv('dataset_final.csv', header=True, index=False)
