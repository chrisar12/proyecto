import pandas as pd
import numpy as np


def leerarchivo():
    data = pd.read_excel('Libro1.xlsx')
    # creamos dataframe del excel
    return pd.DataFrame(data)


def eliminardup(df):
    return df.drop_duplicates(subset='num_paciente', keep='first')


def eliminardatos1(df_elimina):
    df_elimina[df_elimina['raza'] != '?']
    df_elimina[df_elimina['dadoalta_tipo'] != 11]
    df_elimina[df_elimina['dadoalta_tipo'] != 13]
    df_elimina[df_elimina['dadoalta_tipo'] != 14]
    df_elimina[df_elimina['dadoalta_tipo'] != 19]
    df_elimina[df_elimina['dadoalta_tipo'] != 20]
    df_elimina[df_elimina['dadoalta_tipo'] != 21]
    df_elimina[df_elimina['dadoalta_tipo'] != 25]
    df_elimina[df_elimina['dadoalta_tipo'] != 18]
    df_elimina[df_elimina['dadoalta_tipo'] != 26]
    df_elimina[df_elimina['tipo_admision'] != 6]
    df_elimina[df_elimina['origen_admision'] != 9]
    df_elimina[df_elimina['origen_admision'] != 15]
    df_elimina[df_elimina['origen_admision'] != 17]
    df_elimina[df_elimina['origen_admision'] != 20]
    df_elimina[df_elimina['origen_admision'] != 21]
    return df_elimina


def reemplazar(df_elimina):
    df_elimina['especialidad_medica'] = df_elimina['especialidad_medica'].str.replace("?", "Faltante")
    return df_elimina


def categorias1(df_elimina):
    df_elimina.loc[df_elimina['edad'] == "[0-10)", 'edad'] = 0
    df_elimina.loc[df_elimina['edad'] == "[10-20)", 'edad'] = 10
    df_elimina.loc[df_elimina['edad'] == "[20-30)", 'edad'] = 20
    df_elimina.loc[df_elimina['edad'] == "[30-40)", 'edad'] = 30
    df_elimina.loc[df_elimina['edad'] == "[40-50)", 'edad'] = 40
    df_elimina.loc[df_elimina['edad'] == "[50-60)", 'edad'] = 50
    df_elimina.loc[df_elimina['edad'] == "[60-70)", 'edad'] = 60
    df_elimina.loc[df_elimina['edad'] == "[70-80)", 'edad'] = 70
    df_elimina.loc[df_elimina['edad'] == "[80-90)", 'edad'] = 80
    df_elimina.loc[df_elimina['edad'] == "[90-100)", 'edad'] = 90
    df_elimina['edad'] = df_elimina['edad'].astype(np.int32)
    df_elimina.loc[df_elimina['max_glu_serum'] == "None", "max_glu_serum"] = 0
    df_elimina.loc[df_elimina['max_glu_serum'] == "Norm", "max_glu_serum"] = 100
    df_elimina.loc[df_elimina['max_glu_serum'] == ">200", "max_glu_serum"] = 200
    df_elimina.loc[df_elimina['max_glu_serum'] == ">300", "max_glu_serum"] = 300
    df_elimina['max_glu_serum'] = df_elimina['max_glu_serum'].astype(np.int32)
    df_elimina.loc[df_elimina['A1resultado'] == "None", 'A1resultado'] = 0
    df_elimina.loc[df_elimina['A1resultado'] == "Norm", 'A1resultado'] = 5
    df_elimina.loc[df_elimina['A1resultado'] == ">7", 'A1resultado'] = 7
    df_elimina.loc[df_elimina['A1resultado'] == ">8", 'A1resultado'] = 8
    df_elimina['A1resultado'] = df_elimina['A1resultado'].astype(np.int32)
    df_elimina.loc[df_elimina['cambiomed'] == "No", 'cambiomed'] = 0
    df_elimina.loc[df_elimina['cambiomed'] == "Ch", 'cambiomed'] = 1
    df_elimina['cambiomed'] = df_elimina['cambiomed'].astype(np.int8)
    df_elimina.loc[df_elimina['diabetesMed'] == "No", 'diabetesMed'] = 0
    df_elimina.loc[df_elimina['diabetesMed'] == "Yes", 'diabetesMed'] = 1
    df_elimina['diabetesMed'] = df_elimina['diabetesMed'].astype(np.int8)
    return df_elimina


def categorias6(df_elimina):
    medicamentos = ["metformin", "repaglinide", "nateglinide", "chlorpropamide", "glimepiride", "glipizide",
                    "glyburide", "pioglitazone", "rosiglitazone", "acarbose", "miglitol",
                    "insulin", "glyburide-metformin"]
    for med in medicamentos:
        df_elimina.loc[df_elimina[med] == "No", med] = -20
        df_elimina.loc[df_elimina[med] == "Down", med] = -10
        df_elimina.loc[df_elimina[med] == "Steady", med] = 0
        df_elimina.loc[df_elimina[med] == "Up", med] = 10
        df_elimina[med] = df_elimina[med].astype(np.int32)
    return df_elimina


def categorias7(df_elimina):
    categoria = ['raza', 'genero', 'num_paciente', 'especialidad_medica', 'diag_1', 'diag_2', 'diag_3']

    for c in categoria:
        df_elimina[c] = pd.Categorical(df_elimina[c]).codes
    return df_elimina


def categorias8(df_elimina):
    df_elimina.loc[df_elimina['readmision'] != 'NO', 'readmision'] = 0
    df_elimina.loc[df_elimina['readmision'] == 'NO', 'readmision'] = 1
    df_elimina['readmision'] = df_elimina['readmision'].astype(np.int8)
    return df_elimina


def eliminacolumna(df):
    df.drop(labels=['admision_id', 'id', 'peso',
                    'codigo_vendedor', 'num_proce', 'number_outpatient',
                    'number_emerg', 'number_inpatient', 'num_diag', 'acetohexamide',
                    'tolbutamide', 'tolazamide', 'examide', 'troglitazone',
                    'citoglipton', 'metformin-rosiglitazone', 'metformin-pioglitazone',
                    'glipizide-metformin', 'glimepiride-pioglitazone'],
            axis=1, inplace=True)


def guardar(df_elimina):
    df_elimina.reset_index().to_csv('dataset_final.csv', header=True, index=False)
