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

## def Find_Folder
   
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
- Se path estiver vazio (ou seja, não existe um diretório com esse nome), o código constrói o caminho completo usando os.path.join e cria o diretório usando os.makedirs, que cria todos os diretórios intermediários se necessário.
- "exist_ok=True" evita um erro se o diretório já existir

## def move_files

A função recebe dois parâmetros:
- file_types: Uma lista de extensões de arquivo que devem ser movidas.
- directory: O nome do diretório para o qual os arquivos devem ser movidos.

  ```bash
   def move_files(file_types, directory):
    destination = os.path.join(downloads_path, directory)
    
    for file_type in file_types:
        section = [f for f in files if f.endswith(file_type)]
        
        for file_name in section:
            source_path = os.path.join(downloads_path, file_name)
            shutil.move(source_path, destination)
   ```
- O código constrói o caminho de destino onde os arquivos devem ser movidos.

- Para cada tipo de arquivo na lista file_types, ele filtra os arquivos na pasta de Downloads para encontrar aqueles que terminam com a extensão correspondente.

- Para cada arquivo encontrado, ele constrói o caminho de origem e usa shutil.move para mover o arquivo para o diretório de destino.

## Definição do Caminho de Downloads

- os.path.expanduser("~") obtém o diretório home do usuário atual. O caminho completo para a pasta de Downloads é então construído usando os.path.join.
  ```bash
  downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
  ```
## Listagem dos Arquivos na Pasta de Downloads

- os.listdir retorna uma lista de todos os arquivos e diretórios contidos na pasta especificada.
  ```bash
  files = os.listdir(downloads_path)
  ```

## Criação de Pastas para Organização

- Para cada tipo de pasta (Documents, Images, etc.), o código verifica se já existe uma pasta correspondente na lista de arquivos.
- Se não existir, a função find_folder é chamada para criar a pasta.

  ```bash
  find_folder(next((f for f in files if f == "Documents"), None), 'Documents')
  find_folder(next((f for f in files if f == "Images"), None), 'Images')
  find_folder(next((f for f in files if f == "Sheets"), None), 'Sheets')
  find_folder(next((f for f in files if f == "Compact"), None), 'Compact')
  find_folder(next((f for f in files if f == "Executable"), None), 'Executable')
  find_folder(next((f for f in files if f == "Others"), None), 'Others')
  ```

## Definição das Extensões de Arquivos

- Cada lista (documents_, images_, sheets_, compacted_, executable_) contém as extensões que são relevantes para a categoria correspondente.
- Essas listas serão usadas posteriormente para filtrar e mover os arquivos adequadamente.

  ```bash
  documents_ = [".pdf", ".docx", ".doc", ".txt", ".ofx", ".rtf", ".odt", ".ppt",     ".pptx", ".epub", ".mobi", ".html", ".htm"]
  images_ = [".jpg", ".jpeg", ".png", ".webp", ".gif", ".tiff", ".tif", ".bmp",     ".svg", ".heic"]
  sheets_ = [".xlsx", ".xls", ".ods", ".csv", ".tsv", ".dbf"]
  compacted_ = [".zip", ".gz", ".rar", ".7z", ".tar", ".bz2", ".xz"]
  executable_ = [".exe", ".msi", ".bat", ".sh", ".apk", ".dll"]
  ```

## Movimentação dos Arquivos para as Pastas Correspondentes

- Para cada lista de extensões (documentos, imagens, planilhas, etc.), a função move_files é chamada, passando a lista de extensões e o nome da pasta de destino.

- A função move_files faz a filtragem dos arquivos na pasta de Downloads e os move para as pastas apropriadas, conforme já explicado.

  ```bash
  move_files(documents_, 'Documents')
  move_files(images_, 'Images')
  move_files(sheets_, 'Sheets')
  move_files(compacted_, 'Compact')
  move_files(executable_, 'Executable')
  ```

## Identificar e Mover Arquivos que Não se Encaixam nas Categorias

- Uma lista chamada management_folders é criada, contendo os nomes das pastas que foram criadas anteriormente.
- O código lista novamente os arquivos na pasta de Downloads.
- A lista other_files é construída filtrando os arquivos que não estão na lista management_folders.
- Um loop percorre cada arquivo na lista other_files.
- Para cada arquivo, o caminho de origem é construído e o caminho de destino é definido como a pasta "Others".
- O arquivo é movido para a pasta "Others" usando shutil.move.

  ```bash
  management_folders = ["Documents", "Images", "Sheets", "Compact", "Executable",   "Others"]
  files = os.listdir(downloads_path)

  other_files = [f for f in files if f not in management_folders]

  for file_name in other_files:
    source_path = os.path.join(downloads_path, file_name)
    destination_path = os.path.join(downloads_path, 'Others')
    shutil.move(source_path, destination_path)
  ```

# Resumo da Lógica Geral
- Criação de Pastas: O script verifica se as pastas necessárias existem e as cria, se necessário.

- Filtragem de Arquivos: Para cada tipo de arquivo (documentos, imagens, etc.), o script filtra os arquivos na pasta de Downloads com base nas extensões definidas.

- Movimentação de Arquivos: Os arquivos filtrados são movidos para suas respectivas pastas.

- Classificação de Arquivos Não Identificados: Arquivos que não se encaixam em nenhuma das categorias são movidos para uma pasta "Others".  
