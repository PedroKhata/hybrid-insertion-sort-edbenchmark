#ifndef NODE_HPP
#define NODE_HPP

#include <string>

struct Node {
    std::string nome;
    Node* prox;
    Node(std::string n) : nome(n), prox(nullptr) {}
};

#endif