"""Exercício 5 (CRUD Básico em Lista: Create & Read)
Crie uma classe Pet (nome, especie).
• Monte um menu com while True permitindo Cadastrar (Create) e Listar
(Read) os pets da lista."""

class Pet:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        