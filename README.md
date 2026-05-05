# ED.InsertionSort-H05
Aplicação híbrida (Python/C++) para análise de desempenho do algoritmo Insertion Sort (Listas Encadeadas)

# Insertion Sort Híbrido: C++ & Python

Este repositório contém a solução do nosso grupo para a Atividade 05 de Estruturas de Dados. O projeto implementa o algoritmo de ordenação **Insertion Sort** para processar e organizar uma base de dados de nomes.

Para unir alta performance computacional com uma excelente experiência de usuário, o sistema foi construído sob uma arquitetura híbrida:
* **Backend (C++ & Python):** Responsável pelo processamento, executando o algoritmo de ordenação diretamente sobre uma **Lista Encadeada**.
* **Frontend (Python):** Responsável por prover uma Interface interativa e agradável utilizando a biblioteca `Rich`.

## Pré-requisitos 

Como a aplicação compila o código C++ dinamicamente através do Python, o seu sistema operacional precisa ter os seguintes compiladores instalados:

1. **Python 3.8+**
2. **Compilador g++** (GNU Compiler Collection)
3. Biblioteca Python `rich` para a interface gráfica no terminal

**Objetivo Principal:**
Além da implementação correta do algoritmo de inserção, o objetivo central desta aplicação é realizar uma análise de desempenho comparativa rigorosa.

## Como Executar

**1. Clone o repositório**
```bash
git clone [https://github.com/user/ED.InsertionSort-H05.git](https://github.com/user/ED.InsertionSort-H05.git)
cd ED.InsertionSort-H05
```

**2. Instale as dependências da interface**
```bash
pip install -r requirements.txt
```

**3. Execute o main**
Navegue até a pasta onde está o executável Python e inicie o painel:
```bash
cd python
python main.py
```

```text
📦 ED.InsertionSort-H05
 ┣ 📂 data                 
 ┃ ┣ 📜 nomes.txt            # Base de dados original (Entrada)
 ┃ ┗ 📜 nomes_ordenados.txt  # Gerado automaticamente após a execução
 ┣ 📂 src                    # Código-fonte
 ┃ ┣ 📂 bin                  
 ┃ ┃ ┣ 📜 .gitkeep           
 ┃ ┃ ┗ ⚙️ engine_sort        # Executável nativo C++ 
 ┃ ┣ 📂 cpp                  
 ┃ ┃ ┣ 📜 LinkedList.cpp     # Lógica da Lista
 ┃ ┃ ┣ 📜 LinkedList.hpp     # Definição da Lista
 ┃ ┃ ┣ 📜 main.cpp           # Entrada do subprocess
 ┃ ┃ ┗ 📜 Node.hpp           # Estrutura base do node
 ┃ ┗ 📂 python               
 ┃   ┣ 📜 interface.py       # Painéis no terminal com Rich
 ┃   ┣ 📜 main.py            # Loop principal da aplicação
 ┃   ┣ 📜 runner_cpp.py      # Script Wrapper para compilar/rodar C++
 ┃   ┗ 📜 sort_python.py     # Implementação da lista encadeada em Python
 ┣ 📜 .gitignore             # Ignora binários e ambientes locais (.venv, __pycache__)
 ┣ 📜 Makefile               
 ┣ 📜 README.md              # Documentação do projeto
 ┗ 📜 requirements.txt       # Dependências do Python
 ```

## Inspiração

O design da nossa interface de terminal, incluindo os painéis interativos, tabelas de estatísticas e a paleta de cores construída com a biblioteca `Rich`, foi inspirado por **https://github.com/ReidoBoss/tttui**.

## (Grupo)
* **[João Pedro Oliveira]**
* **[João Filipe]** 
* **[Lauriano Matos]** 

*Desenvolvido para a disciplina de Estruturas de Dados - UFPI 2026.*
