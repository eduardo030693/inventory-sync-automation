import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
##########################################################################################
#                                   CARGA DE ARCHIVO                                     #
#                                      EN LA WEB                                         #      
##########################################################################################
#-----------------------------------Crea la configuracion de chrome----------------------#
ruta = "/Users/macbookair/Documents/Python_proyectos/comparador_auto/modulo_b"
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": ruta,
    "safebrowsing.enabled": False,
    "download.prompt_for_download": False,
    "profile.default_content_setting_values.automatic_downloads": 1
})
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-web-security")
options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://10.126.244.207")

driver = webdriver.Chrome(options=options)
try:
    driver.get("http://10.126.244.207/inventario")
#-----------------------------------Clicks en xPaths-------------------------------------#
    #Encuentra el boton con find_element, hasta llegar aExportar Excel y descargar el 
    time.sleep(5)
    bot_bd = driver.find_element(By.XPATH,'//button[@class="btn btn-outline-success"]')
    bot_bd.click()
    time.sleep(2)
    print("Click ejecutado")
    time.sleep(1)
#Este while sirve para que se pare un momento la ejecucion mientras exista un documento .crdownload
    while any(f.endswith('.crdownload') for f in os.listdir(ruta)):
        time.sleep(1)
    print("Descarga completada")

#-----------------------------Encontrar archivo descargado--------------------------------#
    archivos = os.listdir(ruta)
    archivo_reciente = max(archivos, key=lambda f: os.path.getmtime(os.path.join(ruta, f)))
##########################################################################################
#                                    PROCESAMIENTO DE                                    #
#                                         EXCEL                                          #
##########################################################################################
#Leer excel de la web de procesamiento de pedidos.
    lee_excel = pd.read_excel(os.path.join(ruta, archivo_reciente))
#Selecciona solo las celdas necesarias del inventario en excel
    celdas_enca = lee_excel[['Codigo','Descripcion','Existencia']]
#Quitar duplicados
    dupli = celdas_enca.drop_duplicates(subset=['Codigo'])
#Guardar las columnas anteriores en un documento csv
    guard_csv = dupli.to_csv(os.path.join(ruta, 'web.csv'), index=False)
#Eliminar todos los archivos .xlsx de la carpeta modulo_b
    for archivo in os.listdir(ruta):
        if archivo.endswith(".xlsx"):
            os.remove(os.path.join(ruta, archivo))
#Se agrega un except para terminar el proceso en caso de algun error, ademas de un print para conocer el error
except Exception as e:
    print(f"Error: {e}")
#Aqui se cierra el navegador 
finally:
    driver.quit()