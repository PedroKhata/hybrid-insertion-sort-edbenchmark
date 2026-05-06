class Node:
    """
    ### Representa um nó em uma lista encadeada com um descritor
    """
    def __init__(self, nome):
        self.nome = nome
        self.prox = None # Ponteiro para o próximo nó

class ListaEncadeada:
    """
    ### Implementação de uma Lista Encadeada com suporte a leitura de arquivos e ordenação por Insertion Sort
    """
    def __init__(self):
        self.inicio = None
        self.fim = None  # Ponteiro de cauda para otimizar inserções
        self.tamanho = 0

    def adicionar(self, nome):
        """
        ### Adiciona um novo nó ao final da lista encadeada instantaneamente
        """
        novo = Node(nome)
         
        # Se a lista estiver vazia, o início e o fim apontam para o novo nó
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            # Pula direto para o fim usando o ponteiro de cauda
            self.fim.prox = novo
            self.fim = novo
            
        self.tamanho += 1
    
    def inserir_ordenado(self, other, nome: str):
        """
        Insere um novo elemento em uma lista mantendo a ordem alfabética
        """
        novo = Node(nome)

        if other.inicio is None:
            other.inicio = novo
            other.fim = novo # Mantém a integridade da cauda na nova lista
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
        
        # Se o elemento foi inserido no finalzinho, atualiza a cauda
        if novo.prox is None:
            other.fim = novo
            
        other.tamanho += 1
        
    def insertionSort(self):
        """
        ### Ordena a lista atual criando uma nova lista encadeada e inserindo os elementos na posição correta
        """
        ordenada = ListaEncadeada()
        atual = self.inicio
        while atual:
            self.inserir_ordenado(ordenada, atual.nome)
            atual = atual.prox
        
        return ordenada

    def arquivo(self, nome_arquivo):
        # Força o uso de UTF-8 para não dar erro de leitura no Windows
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                nome = linha.strip()
                self.adicionar(nome)
    
    def imprimir_lista(self):
        """
        Imprime todos os elementos da lista encadeada
        """
        atual = self.inicio
        while atual:
            print(atual.nome)
            atual = atual.prox
            
    def salvar_arquivo(self, nome_arquivo: str) -> None:
        """
        Percorre a lista e salva em um arquivo .txt.
        """
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            atual = self.inicio
            while atual:
                f.write(f"{atual.nome}\n")
                atual = atual.prox 