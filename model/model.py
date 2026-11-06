from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, id_biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        #Converto le selezioni "Nessun filtro" o stringhe vuote in None (SQL NULL)
        bib_param = id_biblioteca if id_biblioteca and id_biblioteca != "Nessun filtro" else None
        gen_param= genere if genere and genere != "Nessun filtro" else None

        #Chiamo la query di filtraggio sul DAO dei libri e restituisco il risultato al Controller
        return self._libro_dao.operation_filtrati_from_db(bib_param, gen_param)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        #Chiamo il DAO dei libri per ottenere l'elenco dei generi dal DB
        return self._libro_dao.operation_genere_from_db()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        #Chiamo il DAO delle biblioteche per recuperare la lista completa dal DB
        return self._biblioteca_dao.operation_biblioteca_from_db()
