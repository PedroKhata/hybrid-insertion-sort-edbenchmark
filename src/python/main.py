import time
import os
from sort_python import ListaEncadeada
from interface import mostrar_menu, console, mostrar_estatisticas, mostrar_painel_mensagem, aguardar_enter
from runner_cpp import executar_cpp

COR_VERDE = "bold green"
COR_BRANCA = "white"
COR_CINZA = "dim white"

def main() -> None:
    """
    Função principal que orquestra o menu, as chamadas para os motores 
    de ordenação (Python e C++) e a exibição de resultados.
    """
    lista_original = ListaEncadeada()
    lista_ordenada = None
    # Históricos de tempo em lista pra calcular a média depois (float)
    historico_python: list[float] = []
    historico_cpp: list[float] = []
    
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    path_arquivo = os.path.abspath(os.path.join(diretorio_atual, "..", "..", "data", "nomes.txt"))
    
    while True:
        option = mostrar_menu() 
        
        if option == "1":
            if os.path.exists(path_arquivo):
                with console.status("[bold green]Acessando o arquivo nomes.txt[/bold green]", spinner="point"):
                    lista_original = ListaEncadeada() 
                    lista_original.arquivo(path_arquivo)
                    
                    # Limpa os históricos ao carregar nova data
                    historico_python.clear()
                    historico_cpp.clear()
                
                mostrar_painel_mensagem(f"{lista_original.tamanho} nomes carregados", cor="bold green")
            else:
                mostrar_painel_mensagem("(!) Erro: Arquivo nomes.txt não encontrado!", cor="red")
                
            aguardar_enter()
        
        elif option == "2":
            if lista_original.tamanho == 0:
                mostrar_painel_mensagem("(!) Aviso: Carregue os dados antes da ordenação.", cor="white")
            else:
                with console.status("[bold green]Executando Insertion Sort em Python[/bold green]", spinner="point"):
                    tempo_inicial = time.time()
                    lista_ordenada = lista_original.insertionSort()
                    tempo_final = time.time()
                
                tempo_python = tempo_final - tempo_inicial
                historico_python.append(tempo_python)
                
                # Cria/Sobrescreve o arquivo nomes_ordenados.txt na pasta data
                path_salvar = os.path.abspath(os.path.join(diretorio_atual, "..", "..", "data", "nomes_ordenados.txt"))
                lista_ordenada.salvar_arquivo(path_salvar)
                
                # Parte do C++
                with console.status("[bold green]Executando Insertion Sort em C++[/bold green]", spinner="point"):
                    tempo_cpp, erro_cpp = executar_cpp(path_arquivo)
                    
                if erro_cpp:
                    mostrar_painel_mensagem(f"(!) Erro ao executar C++:\n{erro_cpp}", cor="red")
                else:
                    historico_cpp.append(tempo_cpp)
                    execucao_atual = len(historico_python)
                    
                    mostrar_painel_mensagem(
                        f"Execução #{execucao_atual} Concluída!\n"
                        f"Python: {tempo_python:.6f} s\n"
                        f"C++: {tempo_cpp:.6f} s", 
                        cor="green"
                    )
                
            aguardar_enter()
            
        elif option == "3":
            if lista_original.tamanho > 0:
                console.print()
                for atual in iterar_lista(lista_original):
                    console.print(f"[dim white]>[/dim white] [bold green]{atual.nome}[/bold green]")
            else:
                mostrar_painel_mensagem("(!) Aviso: A lista original está vazia.", cor="white")
                
            aguardar_enter()

        elif option == "4":
            if lista_ordenada is not None:
                console.print()
                for atual in iterar_lista(lista_ordenada):
                    console.print(f"[dim white]>[/dim white] [bold green]{atual.nome}[/bold green]")
            else:
                mostrar_painel_mensagem("(!) Aviso: Execute a ordenação primeiro.", cor='white')
                
            aguardar_enter()
            
        elif option == "5":
            if lista_original.tamanho == 0 or not historico_python or not historico_cpp:
                mostrar_painel_mensagem("(!) Aviso: Execute a ordenação primeiro.", cor="white")
            else:
                # Calcula a média somando todos os tempos e dividindo pela quantidade
                media_python = sum(historico_python) / len(historico_python)
                media_cpp = sum(historico_cpp) / len(historico_cpp)
                qtd_execucoes = len(historico_python)
                
                mostrar_estatisticas(lista_original.tamanho, qtd_execucoes, media_python, media_cpp) 
                
            aguardar_enter()

        elif option == "0":
            break

def iterar_lista(lista: ListaEncadeada) -> list:
    """
    Extrai os nós da lista encadeada e os retorna em uma lista do Python 
    para facilitar a iteração
    """
    elementos = []
    atual = lista.inicio
    while atual:
        elementos.append(atual)
        atual = atual.prox
    return elementos

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        from interface import console, COR_CINZA
        console.print(f"\n[{COR_CINZA}]Programa encerrado pelo usuário. Até logo![/{COR_CINZA}]")
        import sys
        sys.exit(0)