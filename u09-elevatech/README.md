# 🏢 ElevaTech - E-commerce de Elevadores

Este é o projeto final da disciplina de **Programação em Python (UC3)** do **Senac RJ**. A aplicação simula uma empresa B2B de engenharia, oferecendo um catálogo completo e um sistema de vendas de elevadores residenciais, comerciais e hospitalares.

O projeto foi construído do zero com **Django**, aplicando conceitos de back-end, arquitetura MVT, segurança e responsividade.

---

## 🚀 Funcionalidades

- **Catálogo Inteligente:** Listagem de produtos com paginação visual, filtros por categoria e barra de busca.
- **Carrinho de Compras:** Adição de itens e controle de quantidade utilizando **Sessões do Django**.
- **Checkout Transacional:** Finalização de pedido com baixa automática de estoque.
- **Autenticação:** Sistema de Login, Logout e Cadastro de novos clientes.
- **Painel de Gestão (CRUD):** Área restrita para funcionários cadastrarem e editarem elevadores.
- **Admin Django:** Gestão nativa de pedidos e usuários.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.14**
- **Django 6.1**
- **SQLite**
- **Bootstrap 5.3** e **Bootstrap Icons**
- **Pillow** (Processamento de imagens)

---

## ⚙️ Como Executar o Projeto Localmente

### 1. Clonar o repositório e criar o ambiente virtual

    git clone https://github.com/seu-usuario/elevatech.git
    cd elevatech
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Linux / macOS:
    source .venv/bin/activate

### 2. Instalar dependências

    pip install -r requirements.txt

### 3. Configurar o Banco de Dados

    python manage.py migrate

### 4. Criar um Superusuário (Admin)

    python manage.py createsuperuser

### 5. Popular o Banco (Opcional)

    python manage.py seed

### 6. Rodar o Servidor

    python manage.py runserver

Acesse o site em: **http://127.0.0.1:8000/**

---

## 📝 Declaração de Uso de Inteligência Artificial

Em respeito à ética acadêmica e à transparência, declaro que este projeto utilizou recursos de Inteligência Artificial durante o seu desenvolvimento.

**Ferramenta utilizada:**
- **DeepSeek** (desenvolvido pela DeepSeek)
- **Gemini** (desenvolvido pelo Google)

**Como a IA foi utilizada:**
A IA foi empregada estritamente como uma **ferramenta de mentoria técnica e apoio ao aprendizado** (Pair Programming), atuando nos seguintes aspectos:
1. **Explicação de conceitos:** Aprofundamento teórico sobre o framework Django (Models, Sessões, Transações e ORM).
2. **Arquitetura de Software:** Sugestões de boas práticas de estruturação de pastas e separação de responsabilidades (apps).
3. **Depuração (Debug):** Auxílio na leitura de tracebacks de erros e identificação de falhas de sintaxe em templates.
4. **Design System:** Apoio na criação de variáveis CSS e adaptação de componentes do Bootstrap para o tema personalizado.

**O que NÃO foi feito pela IA:**
- Todo o código foi **digitado, testado e validado** pelo aluno no ambiente local.
- A modelagem do banco de dados e as regras de negócio foram **compreendidas e definidas** pelo desenvolvedor.
- A IA não gerou o projeto de forma automatizada; ele atuou como um "professor particular" ao lado do aluno durante o processo de construção.

---

## 👨‍💻 Autor

Desenvolvido por **Rodrigo**  
Senac RJ - 2026