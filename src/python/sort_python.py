import time
import os

class Node:
    def __init__(self, nome):
        self.nome = nome
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, nome):
        novo = Node(nome)
         
        if self.tamanho == 0:
            self.inicio = novo
            self.tamanho += 1
            return
        
        atual = self.inicio
        while atual.prox:
            atual = atual.prox

        atual.prox = novo
        self.tamanho += 1
    
    def inserir_ordenado(self, other, nome: str):
        novo = Node(nome)

        if other.inicio is None:
            other.inicio = novo
            other.tamanho += 1
            return

        if nome < other.inicio.nome:
            novo.prox = other.inicio
            other.inicio = novo
            other.tamanho += 1
            return
        
        atual = other.inicio
        while atual.prox and atual.prox.nome < nome:
            atual = atual.prox
        
        novo.prox = atual.prox
        atual.prox = novo   
        other.tamanho += 1
        
    def insertionSort(self):
        ordenada = ListaEncadeada()
        atual = self.inicio
        while atual:
            self.inserir_ordenado(ordenada, atual.nome)
            atual = atual.prox
        
        return ordenada

    def arquivo(self, nome_arquivo):
        with open(nome_arquivo, "r") as f:
            for linha in f:
                nome = linha.strip()
                self.adicionar(nome)
    
    def imprimir_lista(self):
        atual = self.inicio
        while atual:
            print(atual.nome)
            atual = atual.prox