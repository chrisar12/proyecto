from numpy import reshape


def Diabetes(raza=3
             , genero=0
             , edad=0
             , tipo_admision=6
             , dadoalta_tipo=25
             , origen_admision=1
             , tiempo_hospital=1
             , especialidad_medica=37
             , num_proce_lab=41
             , num_medicaciones=1
             , diag1=673
             , diag2=631
             , diag3=644
             , cambiomed=0
             , diabetesMed=0
             ):
    return reshape([raza, genero, edad, tipo_admision, dadoalta_tipo, origen_admision, tiempo_hospital,
            especialidad_medica, num_proce_lab, num_medicaciones, diag1, diag2, diag3, cambiomed,
            diabetesMed])
