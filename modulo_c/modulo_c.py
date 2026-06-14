import pandas as pd 


#Lectura de csv
df_ficnx = pd.read_csv('/Users/macbookair/Documents/Python_proyectos/comparador_auto/modulo_c/ficnx.csv').dropna()
df_web = pd.read_csv('/Users/macbookair/Documents/Python_proyectos/comparador_auto/modulo_c/web.csv').dropna()
#Eliminar espacios y antes de aplicar el merge para que no se haya codigos diferentes solo por un espacio
df_ficnx['Codigo']= df_ficnx['Codigo'].str.strip()
df_web['Codigo']= df_web['Codigo'].str.strip()
#Comparacion con merge, utilizando outer que permite conservar todos los datos 
comp_01 = pd.merge(df_ficnx, df_web, on='Codigo', how='outer')
#Cambia NAN con cero solo en existencias de la columna Existencias_x, porque se pierde el identificador NAN
comp_01['Existencias_x'] = comp_01['Existencias_x'].fillna(0)
#Cambia los NAN de la columna Descripcion_x por el contenido de la columna Descripcion_y
comp_01['Descripcion_x'] = comp_01['Descripcion_x'].fillna(comp_01['Descripcion_y'])
#Crea las columnas para la nueva tabla
colum = comp_01[['Codigo', 'Descripcion_x', 'Existencias_x']]
#Cambia el nombre de las columnas
renam = colum.rename(columns={'Codigo':'Codigo', 'Descripcion_x':'Descripcion', 'Existencias_x':'Existencias'})
#Cambia los negativos a cero con clip, para no entorpecer el proceso
renam['Existencias'] = renam['Existencias'].clip(lower=0)
#Crea un documento csv con la tabla
renam.to_csv('inventario_actualizado.csv', index=False, float_format='%.0f')

