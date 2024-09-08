from operator import itemgetter

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodi=[]
        self._archi=[]
        self._grafo=nx.Graph()

    def ottieniDD(self):
        return DAO.ottieniDDfromDB()

    def creaGrafo(self, anno, colore):
        self._nodi.clear()
        self._archi.clear()
        self._grafo.clear()

        self._nodi=DAO.ottieniNodi(colore)
        self._grafo.add_nodes_from(self._nodi)
        self._listaArchi=DAO.ottieniArchi(colore, anno)
        for tupla in self._listaArchi:
            self._grafo.add_edge(tupla[0], tupla[1], weight=tupla[2])

    def ottieniListaArchiOrdinatiPerPesoInTupleNodo1Nodo2(self):
        #listaDiTuple=[]
        # self._grafo.edges(data=True) è una lista di tuple
        # dove le tuple sono formate da nodo1 . nodo2 e dizionario con chiave "peso" a cui associato valore del peso dell'arco;
        # mentre self._grafo.edges() è lista di tuple nodo1, nodo2 senza il peso;
        # in questo esercizio in self._archi ho gia tuple (nodo1,nodo2,peso);
        # se non la avessi potrei costruirla cosi:
        listaArchiTupleNodo1Nodo2Peso=[]
        for tuplaNodo1Nodo2 in self._grafo.edges():
            listaArchiTupleNodo1Nodo2Peso.append((tuplaNodo1Nodo2[0], tuplaNodo1Nodo2[1], self._grafo[tuplaNodo1Nodo2[0]][tuplaNodo1Nodo2[1]]["weight"]))
        #ora questa lista di tuple la posso ordinare con itemgetter:
        listaArchiTupleNodo1Nodo2Peso.sort(key=itemgetter(2), reverse=True)
        #reverse perche voglio peso da maggiore a minore
        return listaArchiTupleNodo1Nodo2Peso







        '''
        list=DAO.ottieniList()
        r={}
        for i in list:
            if i[0] not in r:
                r[i[0]]={}
                r[i[0]][i[1]] = (i[2], i[3])
            else:
                r[i[0]][i[1]]=(i[2], i[3])

        for retailer in r:
            for p1 in r[retailer]:
                for p2 in r[retailer]:
                    if r[retailer][p1][1]==r[retailer][p2][1] and r[retailer][p1][0]==anno and r[retailer][p2][0]==anno:
                        if self._grafo.get_edge_data(p1,p2)==None :
                            self._grafo.add_edge(p1, p2, weight=1) #inizializzo peso a zero poi in caso lo cambio
                            #if r[retailer][p1][0]==anno:
                               # self._grafo[p1][p2]['weight']+=1
                        else:
                            #if r[retailer][p1][0]==anno:
                                self._grafo[p1][p2]['weight']+=1

            '''












