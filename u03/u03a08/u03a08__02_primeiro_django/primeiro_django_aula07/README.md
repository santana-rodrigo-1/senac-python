# Primeiro Django — Aula 07

Projeto didático para a Aula 07 — Início do Django.

## Objetivo

Construir uma aplicação web simples mostrando o fluxo:

Navegador → URL → View → Template → HTML → Navegador

## Executar

### 1. Criar e ativar o ambiente virtual

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
python -m venv venv
venv\Scripts\activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Aplicar migrações

```bash
python manage.py migrate
```

### 4. Iniciar o servidor

```bash
python manage.py runserver
```

Abra:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/produtos/
- http://127.0.0.1:8000/sobre/

### 5. Outra porta

Se a porta 8000 estiver ocupada:

```bash
python manage.py runserver 8080
```

Depois acesse:

http://127.0.0.1:8080/

## Estrutura

```text
primeiro_django_aula07/
├── manage.py
├── requirements.txt
├── README.md
├── primeiroprojeto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── core/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    └── templates/
        └── core/
            ├── home.html
            ├── produtos.html
            └── sobre.html
```

## Exercício em sala

Altere os templates e crie uma nova página `/contato/`.
