import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def populate_dropdowns(self):
        #Recupero la lista di biblioteche dal Model e popolo le opzioni della tendine con l'opzione di default
        biblioteche = self._model.get_biblioteche()
        self._view.dd_biblioteca.options = [ft.dropdown.Option("Nessun filtro")]
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(b.nome))

        #Recupero la lista dei generi dal Model e popolo le opzioni della tendina con l'opzione di default
        generi = self._model.get_generi()
        self._view.dd_genere.options = [ft.dropdown.Option("Nessun filtro")]
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(g))

        #Aggiorno l'interfaccia grafica per mostrare le opzioni caricate
        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def read_biblioteca(self, e):
        #Memorizzo il valore selezionato dal dropdown biblioteca
        self.biblioteca_selezionata = e.control.value

    def read_genere(self, e):
        #Memorizzo il valore selezionato dal dropdown genere
        self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    # TODO
    def handle_mostra_libri(self, e):
        #Recupero i valori correnti selezionati
        bib = self.biblioteca_selezionata if self.biblioteca_selezionata else self._view.dd_biblioteca.value
        gen = self.genere_selezionato if self.genere_selezionato else self._view.dd_genere.value

        #Interrogo il Model per ottenere la lista dei libri filtrati
        libri = self._model.get_libri_filtrati(bib, gen)

        #Pulisco i risultati precedenti dalla vista
        self._view.lst_libri.controls.clear()

        #Mostro un messaggio d'avviso se la ricerca non produce risultati, altrimenti aggiungo il libro alla lista
        if not libri:
            self._view.show_alert("Nessun libro trovato per i filtri selezionati.")
        else:
            for libro in libri:
                self._view.lst_libri.controls.append(
                    ft.Text(str(libro))
                )

        #Aggiorno visivamente la pagina con i nuovi dati
        self._view.update()
