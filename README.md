# Organizador de Downloads

Este projeto é um script em Python que organiza automaticamente os arquivos na pasta de Downloads do usuário em subpastas específicas, com base nas extensões dos arquivos. O script cria pastas para documentos, imagens, planilhas, arquivos compactados, executáveis e outros arquivos.

## Funcionalidades

- Criação de pastas para diferentes tipos de arquivos:
  - **Documents**: arquivos de texto e documentos (ex: .pdf, .docx, .txt)
  - **Images**: arquivos de imagem (ex: .jpg, .png, .gif)
  - **Sheets**: planilhas (ex: .xlsx, .csv)
  - **Compact**: arquivos compactados (ex: .zip, .rar)
  - **Executable**: arquivos executáveis (ex: .exe, .msi)
  - **Others**: qualquer outro arquivo que não se enquadre nas categorias acima

- Movimentação automática de arquivos para as pastas apropriadas.

## Pré-requisitos

- Python 3.x instalado no seu sistema.
- Permissões adequadas para acessar e modificar a pasta de Downloads.

## Instalação

1. Clone este repositório ou baixe o arquivo `main.py`.

   ```bash
   git clone https://github.com/lmfrozza/DownloadManagementPython.git
   cd DownloadManagementPython
   ```
2. (Opcional) Crie um ambiente virtual:

   ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate     # Para Windows
   ```
## Uso
- Navegue até o diretório onde o script está localizado.

- Execute o script:
   ```bash
   python main.py
   ```
# Explicação do código

## def Finda_Folder
   
A função recebe dois parâmetros:
- path: O caminho do diretório que está sendo verificado.
- name: O nome do diretório a ser criado.
   
   ```bash
   def find_folder(path, name):
    if not path:
        folder_path = os.path.join(downloads_path, name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"{folder_path} Diretório criado...")
   ```
