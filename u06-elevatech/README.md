# 🏢 ElevaTech - E-commerce de Elevadores

Aplicação web completa desenvolvida em **Python + Django** que simula uma empresa de soluções em mobilidade vertical. O sistema conta com um catálogo interativo de elevadores residenciais, comerciais e hospitalares, oferecendo dois fluxos de negócio distintos: **venda direta via carrinho** e **solicitação de orçamentos customizados**.

_Projeto final do curso de Programação em Python (UC3) - SENAC Rio._

---

## 🚀 Funcionalidades Principais

- **Catálogo Inteligente:** Filtros combinados por tipo, categoria e busca por modelo.
- **Dois Fluxos de Compra:**
  - _Carrinho:_ Para compra direta de modelos padrão (com controle de quantidade).
  - _Orçamento:_ Para projetos específicos que exigem negociação técnica.
- **Autenticação e Área do Cliente:** Cadastro, login e histórico de pedidos e orçamentos próprios.
- **Painel Administrativo (CRUD):** Área restrita para a equipe (staff) gerenciar elevadores, preços e imagens pelo próprio site.
- **Django Admin Customizado:** Gestão completa de usuários, produtos, pedidos e status de orçamentos.
- **Notificações de E-mail (Console):** Simulação de envio de e-mails para a equipe de vendas ao receber pedidos/orçamentos, visível em tempo real no terminal (ideal para testes em desenvolvimento).
- **Design Responsivo:** Interface moderna, escura e adaptada para dispositivos móveis.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.14
- **Framework:** Django 6.x
- **Banco de Dados:** SQLite (padrão de desenvolvimento)
- **Front-end:** HTML5, CSS3, Bootstrap 5.3, Bootstrap Icons
- **Bibliotecas:** Pillow (upload de imagens)

---

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação na sua máquina.

### 1. Clonar o repositório e criar o ambiente virtual

```bash
# Clone o projeto
git clone https://github.com/seu-usuario/elevatech.git
cd elevatech

# Crie e ative o ambiente virtual
python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```
