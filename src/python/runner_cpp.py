import os
import subprocess

def executar_cpp(path_arquivo):
    """
    ### Compila e executa o C++
    - Recebe um caminho de arquivo (.txt)
    - Retorna uma tupla: [tempo de execução (float), mensagem de erro - se houver (string)]
    """
    # Evitar erros de diretorio
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    dir_cpp = os.path.abspath(os.path.join(diretorio_atual, "..", "cpp"))
    bin_dir = os.path.abspath(os.path.join(diretorio_atual, "..", "bin"))
    executavel_cpp = os.path.join(bin_dir, "engine_sort")
    os.makedirs(bin_dir, exist_ok=True)

    try:
        subprocess.run([
            "g++", 
            os.path.join(dir_cpp, "main.cpp"), 
            os.path.join(dir_cpp, "LinkedList.cpp"), 
            "-o", executavel_cpp,
            # -O3 garante otimizacao de performance pelo g++
            "-O3"
        ], check=True, capture_output=True, text=True)
        
        resultado_cpp = subprocess.run(
            [executavel_cpp, path_arquivo], 
            capture_output=True, 
            text=True,           
            check=True
        )
        
        tempo = float(resultado_cpp.stdout.strip())
        return tempo, None
        
    except subprocess.CalledProcessError as e:
        # Captura erros de compilacao (g++)
        erro_msg = e.stderr if e.stderr else str(e)
        return 0.0, erro_msg
    except ValueError:
        return 0.0, "Erro: O programa C++ não retornou um número válido."