import time
import os
from sort_python import ListaEncadeada
from interface import mostrar_menu, console, mostrar_estatisticas_teste, mostrar_painel_mensagem, aguardar_enter

COR_VERDE = "bold green"
COR_BRANCA = "white"
COR_CINZA = "dim white"

def main():
    lista_original = ListaEncadeada()
    lista_ordenada = None
    tempo_python = 0.0
    
    while True:
        option = mostrar_menu() 
        
        if option == "1":
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))
            path_arquivo = os.path.join(diretorio_atual, "..", "..", "data", "nomes.txt")
            path_arquivo = os.path.abspath(path_arquivo)
            
            if os.path.exists(path_arquivo):
                with console.status("[bold green]Acessando banco de dados[/bold green]", spinner="point"):
                    lista_original = ListaEncadeada() 
                    lista_original.arquivo(path_arquivo)
                
                mostrar_painel_mensagem(f"Sucesso! {lista_original.tamanho} nomes carregados da base.")
            else:
                mostrar_painel_mensagem("Erro: Arquivo nomes.txt não encontrado!", cor="red")
                
            aguardar_enter()
        
        elif option == "2":
            if lista_original.tamanho == 0:
                mostrar_painel_mensagem("Aviso: Carregue os dados antes da ordenação.", cor=COR_BRANCA)
            else:
                with console.status("[bold green]Executando Insertion Sort em Python[/bold green]", spinner="point"):
                    tempo_inicial = time.time()
                    lista_ordenada = lista_original.insertionSort()
                    tempo_final = time.time()
                
                tempo_python = tempo_final - tempo_inicial
                mostrar_painel_mensagem(f"Ordenação Python concluída em {tempo_python:.6f} s")
                
            aguardar_enter()
            
        elif option == "3":
            if lista_original.tamanho > 0:
                console.print()
                for atual in iterar_lista(lista_original):
                    console.print(f"[dim white]>[/dim white] [bold green]{atual.nome}[/bold green]")
            else:
                mostrar_painel_mensagem("A lista original está vazia.", cor="bold white")
                
            aguardar_enter()

        elif option == "4":
            if lista_ordenada is not None:
                console.print()
                for atual in iterar_lista(lista_ordenada):
                    console.print(f"[dim white]>[/dim white] [bold green]{atual.nome}[/bold green]")
            else:
                mostrar_painel_mensagem("Execute a ordenação primeiro!", cor='yellow')
                
            aguardar_enter()
            
        elif option == "5":
            if lista_original.tamanho == 0 or tempo_python == 0.0:
                mostrar_painel_mensagem("Execute a ordenação primeiro!", cor="yellow")
            else:
                tempo_cpp_ficticio = 0.0012 
                mostrar_estatisticas_teste(lista_original.tamanho, tempo_python, tempo_cpp_ficticio) 
                
            aguardar_enter()

        elif option == "0":
            break

def iterar_lista(lista):
    elementos = []
    atual = lista.inicio
    while atual:
        elementos.append(atual)
        atual = atual.prox
    return elementos

if __name__ == "__main__":
    main()