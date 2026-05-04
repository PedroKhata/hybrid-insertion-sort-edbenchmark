from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich import box
import os

console = Console(force_terminal=True)

COR_VERDE = "bold green"
COR_BRANCA = "white"
COR_CINZA = "dim white"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    limpar_tela()
    
    ascii_art = f"""[{COR_VERDE}]
██████████████████████████████████████
              UFPI 2026              
██████████ ED - INSERTION ████████████
[/{COR_VERDE}]"""
    
    menu_opcoes = f"""
[{COR_VERDE}]1.[/{COR_VERDE}] [{COR_BRANCA}]Carregar dados de arquivo txt[/{COR_BRANCA}]
[{COR_VERDE}]2.[/{COR_VERDE}] [{COR_BRANCA}]Executar ordenação[/{COR_BRANCA}]
[{COR_VERDE}]3.[/{COR_VERDE}] [{COR_BRANCA}]Listar originais[/{COR_BRANCA}]
[{COR_VERDE}]4.[/{COR_VERDE}] [{COR_BRANCA}]Listar ordenados[/{COR_BRANCA}]
[{COR_VERDE}]5.[/{COR_VERDE}] [{COR_BRANCA}]Ver Estatísticas[/{COR_BRANCA}]
[{COR_CINZA}]0. Sair[/{COR_CINZA}]"""

    conteudo_painel = (
        f"{ascii_art}\n"
        f"\n[{COR_CINZA}]──────────────────────────────────────[/{COR_CINZA}]\n"
        f"{menu_opcoes}\n"
        f"\n[{COR_CINZA}]──────────────────────────────────────[/{COR_CINZA}]\n"
        f"[{COR_CINZA}]      Digite o número desejado[/{COR_CINZA}]"
    )
    
    painel_principal = Panel(
        conteudo_painel,
        box=box.SQUARE,
        border_style="white",
        expand=False
    )
    
    console.print(painel_principal)
    
    escolha = Prompt.ask(
        f"[{COR_VERDE}]> Opção[/{COR_VERDE}]", 
        choices=["0", "1", "2", "3", "4", "5"],
        show_choices=False
    )
    return escolha

def mostrar_painel_mensagem(mensagem, cor="bold green"):
    """Envelopa as mensagens do main em um painel à esquerda."""
    painel = Panel(
        f"[{cor}]{mensagem}[/{cor}]",
        box=box.SQUARE,
        border_style="white",
        expand=False
    )
    console.print()
    console.print(painel)

def aguardar_enter():
    """Pausa simples e encostada na margem"""
    console.print()
    Prompt.ask(f"[{COR_CINZA}]Pressione Enter para voltar ao menu[/{COR_CINZA}]")

def mostrar_estatisticas_teste(tamanho_base, tempo_python, tempo_cpp):
    limpar_tela()
    
    titulo = f"[{COR_VERDE}]RESULTADOS DA ORDENAÇÃO[/{COR_VERDE}]"
    tabela = Table(show_header=False, box=None, padding=(0, 4))
    
    tabela.add_column("Métrica", justify="left", style=COR_CINZA)
    tabela.add_column("Valor", justify="left", style=COR_BRANCA)

    if tempo_cpp > 0 and tempo_python > 0:
        if tempo_python > tempo_cpp:
            mais_rapido = "C++"
            fator = tempo_python / tempo_cpp
            blocos_py = 40
            blocos_cpp = max(1, int(40 * (tempo_cpp / tempo_python)))
        else:
            mais_rapido = "Python"
            fator = tempo_cpp / tempo_python
            blocos_cpp = 40
            blocos_py = max(1, int(40 * (tempo_python / tempo_cpp)))
    else:
        mais_rapido = "N/A"
        fator = 0
        blocos_py = 0
        blocos_cpp = 0

    barra_py = "█" * blocos_py
    barra_cpp = "█" * blocos_cpp
    
    tabela.add_row("Base de dados", "nomes.txt")
    tabela.add_row("Tamanho", f"{tamanho_base} elementos")
    tabela.add_row("", "") 
    
    tabela.add_row("Tempo Python", f"[{COR_VERDE}]{tempo_python:.6f} s[/{COR_VERDE}]")
    tabela.add_row("Gráfico Python", f"[{COR_VERDE}]{barra_py}[/{COR_VERDE}]")
    tabela.add_row("", "") 
    
    tabela.add_row("Tempo C++", f"[{COR_BRANCA}]{tempo_cpp:.6f} s[/{COR_BRANCA}]")
    tabela.add_row("Gráfico C++", f"[{COR_BRANCA}]{barra_cpp}[/{COR_BRANCA}]")
    tabela.add_row("", "") 
    
    tabela.add_row("Veredito", f"{mais_rapido} foi [{COR_VERDE}]{fator:.1f}x mais rápido[/{COR_VERDE}]")

    painel_resultados = Panel(
        tabela,
        title=titulo,
        title_align="left",
        box=box.SQUARE,
        border_style="white",
        expand=False
    )
    
    console.print(painel_resultados)