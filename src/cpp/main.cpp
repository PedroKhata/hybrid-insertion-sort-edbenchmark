// Subprocess

#include <iostream>
#include <chrono>
#include "LinkedList.hpp"
#include <iomanip>

// argc: Conta quantas palavras foram digitadas no terminal
// argv: Um vetor que guarda as palavras digitadas
int main(int argc, char* argv[]) {

    // Caminho padrao
    std::string pathArquivo = "../../data/nomes.txt";
    
    // Se passar o caminho do arquivo, substitui o caminho padrão pelo que foi digitado
    if (argc > 1) {
        pathArquivo = argv[1];
    }

    LinkedList lista;

    // Carrega os dados
    lista.carregarArquivo(pathArquivo);

    if (lista.getTamanho() == 0) {
        std::cout << "Erro: Nenhum dado foi carregado do arquivo.\n";
        return 1; 
    }
    // Inicia o cronometro
    auto tempoInicial = std::chrono::high_resolution_clock::now();
    // Executa a iS
    lista.insertionSort();
    // Para o cronometro
    auto tempoFinal = std::chrono::high_resolution_clock::now();
    // Double (segundos)
    std::chrono::duration<double> tempoTotal = tempoFinal - tempoInicial;

    // Imprime apenas o tempo para o Python capturar
    std::cout << std::fixed << std::setprecision(10) << tempoTotal.count() << "\n";

    return 0; 
}