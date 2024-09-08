import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        lista=self._model.ottieniDD()
        self._view._ddcolor.options.clear()
        self._view._ddyear.options.clear()
        self._view._ddyear.options.append(ft.dropdown.Option("2015"))
        self._view._ddyear.options.append(ft.dropdown.Option("2016"))
        self._view._ddyear.options.append(ft.dropdown.Option("2017"))
        self._view._ddyear.options.append(ft.dropdown.Option("2018"))
        for i in lista:
            self._view._ddcolor.options.append(ft.dropdown.Option(i))
        self._view.update_page()


    def handle_graph(self, e):
        colore=self._view._ddcolor.value
        anno=self._view._ddyear.value
        if colore=="" or colore=="Colore" or colore==None:
            self._view.txtOut.clean()
            self._view.txtOut.controls.append(ft.Text("Selezionare un colore"))
            self._view.update_page()
            return
        if anno=="" or anno=="Anno" or anno==None:
            self._view.txtOut.clean()
            self._view.txtOut.controls.append(ft.Text("Selezionare un anno"))
            self._view.update_page()
            return

        self._view.txtOut.clean()

        self._model.creaGrafo(anno,colore)
        self._view.txtOut.controls.append(ft.Text(f"Numero di nodi: {len(self._model._grafo.nodes())}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {len(self._model._grafo.edges())}"))
        listaArchiOrdinatiPerPesoInTupleNodo1Nodo2=self._model.ottieniListaArchiOrdinatiPerPesoInTupleNodo1Nodo2()#fondamentali parentesi()!!!!!!!!!!!!!!!!!!!

        for tupla in listaArchiOrdinatiPerPesoInTupleNodo1Nodo2[0:3]:
            #i tre archi con peso maggiore sono i primi tre di questa lista, quindi da indice 0incluso a indice 3escluso
            self._view.txtOut.controls.append(ft.Text(f"Arco da {tupla[0]} a {tupla[1]}, peso={tupla[2]}"))

        diz={}
        for tupla in listaArchiOrdinatiPerPesoInTupleNodo1Nodo2[0:3]:
            if tupla[0] not in diz: #se non è gia chiave di quel dizionario
                diz[tupla[0]]=1
            else:
                diz[tupla[0]]+=1
            if tupla[1] not in diz: #se non è gia chiave di quel dizionario
                diz[tupla[1]]=1#aggiungo
            else:
                diz[tupla[1]]+=1 #altrimenti solo aggiorno

        self._view.txtOut.controls.append(ft.Text(f"I nodi ripetuti sono:"))

        for vertice in diz:
            if diz[vertice]>1: #se numero di volte che compare nei tre archi sopra (quindi il valore ad esso associarto in diz) è maggiore di 1:
                self._view.txtOut.controls.append(ft.Text(f"{vertice}"))

        self._view.update_page()

    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
