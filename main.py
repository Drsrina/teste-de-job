import os
import time

def task():
    """Simula uma tarefa de processamento de dados."""
    print("--- INICIANDO JOB ---")
    
    # Simula leitura de variáveis de ambiente (útil para automação)
    env = os.getenv('AMBIENTE', 'Desenvolvimento')
    print(f"Ambiente detectado: {env}")
    
    # Simula um processamento
    print("Processando dados...", end="", flush=True)
    for i in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\nProcessamento concluído.")
    
    print("--- JOB FINALIZADO COM SUCESSO ---")

if __name__ == "__main__":
    task()