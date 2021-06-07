# -*- coding: utf-8 -*-

"""
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/06/03
"""

import configparser
import os


class ConfigConnection: 

    def __init__(self, path): 
        try: 
            self.path = path
            self.parser = configparser.ConfigParser()
            self.parser.read(self.path)

        except os.error as e:
            print("Problemas con la ruta: {}".format(e))


    #Toma los valores del archivo de configuración; retorna un diccionario
    def getConfig(self): 
        
        #Sección por defecto dentro del archivo de configuración (config.ini)
        config = self.parser["client"]
        
        #Configuración de la conexión a la base de datos
        config = dict(zip( 
                        map(lambda key: key.upper(), config.keys()), 
                        config.values())
                    )

        return config