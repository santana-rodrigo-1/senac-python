
# 🏢 ElevaTech - E-commerce de Elevadores

Este é o projeto final da disciplina de **Programação em Python (UC3)** do SENAC Rio. A aplicação simula uma empresa B2B de engenharia, oferecendo um catálogo completo e um sistema de vendas de elevadores residenciais, comerciais e hospitalares.

O projeto foi construído do zero com **Django**, aplicando conceitos de back-end, arquitetura MVT, segurança e responsividade.

---

## 🚀 Funcionalidades

* **Catálogo Inteligente:** Listagem de produtos com paginação visual, filtros por categoria (Residencial, Comercial, Hospitalar) e barra de busca.
* **Carrinho de Compras:** Adição de itens e controle de quantidade utilizando **Sessões do Django** (sem sobrecarregar o banco de dados).
* **Checkout Transacional:** Finalização de pedido com baixa automática de estoque, garantida por transações atômicas (`transaction.atomic`).
* **Autenticação:** Sistema de Login, Logout e Cadastro de novos clientes.
* **Painel de Gestão (CRUD):** Área restrita para funcionários (Staff) cadastrarem e editarem elevadores pelo próprio site, incluindo **upload de imagens**.
* **Admin Django:** Gestão nativa de pedidos e usuários.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.14**
* **Django 6.1** (Framework Web)
* **SQLite** (Banco de dados relacional)
* **Bootstrap 5.3** e **Bootstrap Icons** (Front-end)
* **Pillow** (Processamento de imagens)
* **CSS3 Customizado** (Design System próprio com variáveis)

---

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação na sua máquina.

### 1. Clonar o repositório e criar o ambiente virtual

```bash
# Clone o projeto
git clone https://github.com/seu-usuario/elevatech.git
cd elevatech

# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate
```
