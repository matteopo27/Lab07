from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO

    def operation_genere_from_db(self):
        #Recupero la connessione al database tramite il metodo di classe
        cnx = DBConnect.get_connection()

        if cnx is not None:
            print("Connection established")

        #Definisco ed eseguo la query per estrarre la lista dei generi ordinati alfabeticamente
        query = "SELECT DISTINCT genere FROM libro ORDER BY genere;"
        cursor = cnx.cursor()
        cursor.execute(query)

        #Scorro i risultati estraendo il singolo valore della colonna 'genere'
        result_genere = []
        for row in cursor:
            result_genere.append(row[0])

        #Chiudo il cursore e la connessione
        cursor.close()
        cnx.close()
        #Restituisco la lista di stringhe dei generi
        return result_genere

    def operation_filtrati_from_db(self,id_biblioteca : str =None,genere : str =None):
        #Recupero la connessione al database tramite il metodo di classe
        cnx = DBConnect.get_connection()
        #Converto "Nessun filtro" o stringhe vuote in None (SQL NULL) per gestire il COALESCE nella query
        bib_param=id_biblioteca if id_biblioteca and id_biblioteca != "Nessun filtro" else None
        gen_param=genere if genere and genere != "Nessun filtro" else None

        if cnx is not None:
            print("Connection established")

        #Definisco la query SQL con JOIN e COALESCE per filtrare in modo opzionale su biblioteca e genere
        query = """
                        SELECT l.* 
                        FROM libro l
                        JOIN biblioteca b ON b.id = l.id_biblioteca
                        WHERE b.nome = COALESCE(%s, b.nome)
                          AND l.genere = COALESCE(%s, l.genere);
                    """
        #Uso un cursor in modalità dizionario per mappare i nomi delle colonne con gli attributi del DTO
        cursor= cnx.cursor(dictionary=True)
        cursor.execute(query,(bib_param,gen_param))

        #Scorro le righe restituite dal database, creo l'oggetto libri (formato dai campi del diz) e lo aggiungo alla lista
        result_libri = []
        for row in cursor:
            libri= Libro(**row)
            result_libri.append(libri)

        #Chiudo il cursore e la connessione
        cursor.close()
        cnx.close()
        #Restituisco la lista di oggetti Libro filtrati
        return result_libri
