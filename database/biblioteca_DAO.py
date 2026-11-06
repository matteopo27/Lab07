from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO

    def operation_biblioteca_from_db(self):
        #Recupero la connessione al database tramite il metodo di classe
        cnx = DBConnect.get_connection()

        if cnx is not None:
            print("Connection established")

        #Definisco la query SQL per estrarre tutte le biblioteche
        query = "SELECT * FROM biblioteca"
        cursor = cnx.cursor()
        cursor.execute(query)

        result=[]

        #Scorro le righe restituite dal database, creo l'oggetto Biblioteca e lo aggiungo alla lista
        for row in cursor:
            biblioteca_DTO=Biblioteca(*row)
            result.append(biblioteca_DTO)

        #Chiudo il cursore e la connessione
        cnx.close()
        #Restituisco la lista di oggetti Biblioteca al Model
        return result




