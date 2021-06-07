# -*- coding: utf-8 -*-

"""
    @author kenneth.cruz@unah.hn
    @version 0.1.1
    @date 2021/06/03
"""

import re
from django.db import connection

class MySQLEngine: 


    """
        Conexión con la base de datos
    """
    def __init__(self):
        
        self.mydb = connection
        self.link = self.mydb.cursor()
    

    """
         Realiza la operación de insert en la base de datos
         @attributes tupla de elementos
         @values tupla de elementos
    """
    def insert(self, table_name: str, attributes=(), values=()) -> None: 
        
        if len(attributes) == len(values):
            
            query = "INSERT INTO {} ({}) VALUES ({})".format(table_name, ",".join(attributes), self.process_insert(values))
            self.link.execute(query)
        else:
            print("La cantidad de Atributos y valores no son iguales")


    def process_insert(self, data):
        
        return ",".join(tuple(map(lambda x: "'{}'".format(x) if type(x) is not int else "{}".format(x), data)))


    """
        Cláusula SELECT
    """
    def select(self, query: str) -> list: 

        self.link.execute(query)
        row = self.link.fetchall()

        return row


    """
        Cláusula Select utilizando paginador con rango de resultado
    """
    def selectPage(self, query: str, page=0, count=10): 

        query = re.sub(r"\s+[Ll][Ii][Mm][Ii][Tt]\s+\d+([, ]\d+)?\s*;\s*", "", query)

        query = ("{} LIMIT {},{};".format(query, page, count))

        self.link.execute(query)
        row = self.link.fetchall()
        
        return row
    

    
    """
        Ejecuta la operación Update en la base de datos
    """
    def update(self, table: str, fields: list, values: list, condition = None):
        
        query = "UPDATE {} SET ".format(table)

        if (len(fields) == len(values)):
            for (field, value) in zip(fields, values):
                query += "{} = {}, ".format(field, value)

            query = re.sub(r"(,)(\s)*$", " ", query)

            condition = re.sub(r"(\s)*([Ww][Hh][Ee][Rr][Ee])+(\s)*", " ", condition)
            query += "WHERE {} ".format(condition)
            query = re.sub(r"(\s)*(;)?(\s)*$", "", query)
            query += ";"
        self.link.execute(query)