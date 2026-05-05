#include "LinkedList.hpp"
#include <iostream>
#include <fstream> 

// Construtor
LinkedList::LinkedList() {
    this->inicio = nullptr; 
    this->tamanho = 0;      
}

// Destrutor
LinkedList::~LinkedList() {
    Node* atual = this->inicio; 
    
    while (atual != nullptr) {
        Node* lixo = atual;     
        atual = atual->prox;    
        delete lixo;            
    }
}

int LinkedList::getTamanho() const {
    return this->tamanho;
}

void LinkedList::inserirFim(std::string nome) {
    Node* novoNode = new Node(nome); 
    novoNode->prox = nullptr;        

    if (this->inicio == nullptr) {
        this->inicio = novoNode;     
    } 
    else {
        Node* atual = this->inicio;   
        
        while (atual->prox != nullptr) {
            atual = atual->prox;      
        }
        
        atual->prox = novoNode;      
    }
    
    this->tamanho = this->tamanho + 1; 
}

void LinkedList::carregarArquivo(const std::string& caminho) {
    std::ifstream arquivo;
    arquivo.open(caminho.c_str()); 

    if (arquivo.is_open() == false) {
        std::cout << "Erro: Arquivo nao encontrado!\n";
        return; 
    }

    std::string linha;
    while (std::getline(arquivo, linha)) {
        if (linha != "") { 
            this->inserirFim(linha);
        }
    }
    arquivo.close(); 
}

void LinkedList::imprimir() const {
    Node* atual = this->inicio;
    
    while (atual != nullptr) {
        std::cout << atual->nome << "\n";
        atual = atual->prox;
    }
}

void LinkedList::insertionSort() {
    if (this->inicio == nullptr || this->inicio->prox == nullptr) {
        return; 
    }

    Node* ordenada = nullptr; // Início lista ordenada
    Node* atual = this->inicio; 

    while (atual != nullptr) {
        Node* proxOriginal = atual->prox; 

        // Insercao no inicio da lista ordenada
        if (ordenada == nullptr || atual->nome < ordenada->nome) {
            atual->prox = ordenada;
            ordenada = atual;
        } 
        else {
            Node* aux = ordenada; // Auxiliar para iterar a lista ordenada
            while (aux->prox != nullptr && atual->nome > aux->prox->nome) {
                aux = aux->prox; 
            }
            
            atual->prox = aux->prox; 
            aux->prox = atual;       
        }
        atual = proxOriginal; 
    }
    this->inicio = ordenada; 
}