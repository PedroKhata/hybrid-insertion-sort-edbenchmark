#ifndef LINKEDLIST_HPP
#define LINKEDLIST_HPP

#include "Node.hpp"
#include <string>

class LinkedList {
private:
    Node* inicio;
    int tamanho;

public:
    LinkedList();
    ~LinkedList();

    void inserirFim(std::string nome);
    void imprimir() const;
    int getTamanho() const;
    void carregarArquivo(const std::string& caminho);
    void insertionSort();
};

#endif