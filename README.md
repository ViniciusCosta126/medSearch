# MedicSearch

## Rodando localmente

Primeiro clone o repositorio

```bash
    git clone https://github.com/ViniciusCosta126/medSearch
```

Depois de clonado entre na pasta

```bash
    cd medSearch
```

Crie a virtualenv para instalar as libs

```bash
    python3 -m venv env
```

Instale as libs
```bash
    pip install -r requirements.txt
``` 

Ative a venv

windows
```bash
    .\nome_da_virtualenv\Scripts\activate
``` 

linux ou macOS
```bash
    source nome_da_virtualenv/bin/activate 
``` 

Para iniciar o servidor rode:
```bash
    python3 manage.py runserver
```
Faça as migrations para o banco de dados
```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
```
