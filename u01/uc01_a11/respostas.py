class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print(f"Au au! Meu nome é {self.nome}!")

    def __str__(self):
        return f"Cachorro: {self.nome} (Raça: {self.raca})"


meu_dog = Cachorro("Rex", "Labrador")
meu_dog.latir()
print(meu_dog)


class Lampada:
    def __init__(self):
        self.ligada = False

    def ligar(self):
        self.ligada = True
        print("A lâmpada foi LIGADA.")

    def desligar(self):
        self.ligada = False
        print("A lâmpada foi DESLIGADA.")

    def status(self):
        if self.ligada:
            print("Status: Lâmpada ACESA 💡")
        else:
            print("Status: Lâmpada APAGADA 🔌")


l = Lampada()
l.status()
l.ligar()
l.status()
l.desligar()


class Termostato:
    def __init__(self):
        self.temperatura = 20.0

    def aumentar(self, qtd):
        if self.temperatura + qtd <= 40.0:
            self.temperatura += qtd
            print(f"Temperatura aumentada para {self.temperatura:.1f}°C")
        else:
            print("ERRO: A temperatura máxima permitida é de 40.0°C!")

    def diminuir(self, qtd):
        if self.temperatura - qtd >= 0.0:
            self.temperatura -= qtd
            print(f"Temperatura reduzida para {self.temperatura:.1f}°C")
        else:
            print("ERRO: A temperatura mínima permitida é de 0.0°C!")


t = Termostato()
t.aumentar(15.0)
t.aumentar(10.0)
t.diminuir(40.0)


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20


f = Funcionario("Carlos", 3000.0)
g = Gerente("Ana", 5000.0)

print(f"Bônus do Funcionário {f.nome}: R${f.calcular_bonus():.2f}")
print(f"Bônus da Gerente {g.nome}: R${g.calcular_bonus():.2f}")


class Pet:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def __str__(self):
        return f"Pet: {self.nome:<12} | Espécie: {self.especie}"


lista_pets = []

while True:
    print("\n--- SISTEMA PETSHOP (CRUD BÁSICO) ---")
    print("1 - Cadastrar Pet (Create)")
    print("2 - Listar Pets (Read)")
    print("0 - Sair")
    
    op = input("Escolha uma opção: ")
    
    if op == "1":
        nome = input("Digite o nome do Pet: ")
        especie = input("Digite a espécie (ex: Cão, Gato): ")
        novo_pet = Pet(nome, especie)
        lista_pets.append(novo_pet)
        print(f"✓ Pet '{nome}' cadastrado com sucesso!")
        
    elif op == "2":
        print("\n--- LISTA DE PETS CADASTRADOS ---")
        if not lista_pets:
            print("Nenhum pet cadastrado no momento.")
        else:
            for idx, pet in enumerate(lista_pets, 1):
                print(f"{idx}. {pet}")
                
    elif op == "0":
        print("Saindo do sistema de pets. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.paginas_lidas = 0

    def ler(self, paginas):
        if paginas > 0:
            self.paginas_lidas += paginas
            print(f"Você leu {paginas} páginas do livro '{self.titulo}'.")

    def __str__(self):
        return f"Livro: '{self.titulo}' ({self.autor}) | Páginas lidas até agora: {self.paginas_lidas}"


meu_livro = Livro("O Hobbit", "J.R.R. Tolkien")
meu_livro.ler(30)
meu_livro.ler(25)
print(meu_livro)


class Produto:
    def __init__(self, nome, preco, estoque_inicial):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque_inicial

    def adicionar_estoque(self, qtd):
        if qtd > 0:
            self.estoque += qtd
            print(f"✓ {qtd} unidades de '{self.nome}' adicionadas ao estoque.")

    def vender(self, qtd):
        if qtd <= 0:
            print("Quantidade de venda inválida.")
        elif qtd <= self.estoque:
            self.estoque -= qtd
            valor_total = qtd * self.preco
            print(f"✓ Venda de {qtd}x '{self.nome}' realizada! Total: R${valor_total:.2f}")
        else:
            print(f"❌ Estoque insuficiente! Você tentou vender {qtd}, mas só tem {self.estoque} em estoque.")


p = Produto("Smartphone", 1500.0, 5)
p.vender(3)
p.vender(4)
p.adicionar_estoque(10)
p.vender(4)


class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Moto(Veiculo):
    def empinar(self):
        print(f"A moto {self.marca} {self.modelo} empinou a roda da frente! VRUMMM 🏍️💨")


m = Moto("Yamaha", "MT-07")
print(f"Moto cadastrada: {m.marca} {m.modelo}")
m.empinar()


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome:<15} | Nota Final: {self.nota:.1f}"


turma = []

while True:
    print("\n--- SISTEMA DE ALUNOS (CRUD + BUSCA) ---")
    print("1 - Cadastrar Aluno (Create)")
    print("2 - Listar Todos os Alunos (Read)")
    print("3 - Buscar Aluno pelo Nome (Search)")
    print("0 - Sair")
    
    op = input("Opção: ")
    
    if op == "1":
        nome = input("Digite o nome do aluno: ").strip()
        try:
            nota = float(input("Digite a nota do aluno (0 a 10): "))
            turma.append(Aluno(nome, nota))
            print(f"✓ Aluno '{nome}' cadastrado com sucesso!")
        except ValueError:
            print("❌ Erro: Digite apenas valores numéricos para a nota.")
            
    elif op == "2":
        print("\n--- ALUNOS CADASTRADOS ---")
        if not turma:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in turma:
                print(aluno)
                
    elif op == "3":
        busca = input("Digite o nome do aluno que deseja buscar: ").strip()
        encontrado = False
        
        for aluno in turma:
            if aluno.nome.lower() == busca.lower():
                print(f"\n✓ ALUNO ENCONTRADO:\n{aluno}")
                encontrado = True
                break
                
        if not encontrado:
            print(f"\n❌ O aluno '{busca}' não foi encontrado na turma.")
            
    elif op == "0":
        print("Encerrando o programa de alunos...")
        break
    else:
        print("Opção inválida.")


class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"✓ Depósito de R${valor:.2f} realizado!")
        else:
            print("❌ Valor inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("❌ Valor inválido.")
        elif valor <= self.saldo:
            self.saldo -= valor
            print(f"✓ Saque de R${valor:.2f} realizado!")
        else:
            print(f"❌ Saldo insuficiente! Saldo atual: R${self.saldo:.2f}")

    def __str__(self):
        return f"Titular: {self.titular:<15} | Saldo: R${self.saldo:.2f}"


lista_contas = []

while True:
    print("\n=== BANCO DIGITAL JWC TECH (CRUD COMPLETO EM MEMÓRIA) ===")
    print("1 - [C] Create  ➔ Cadastrar Nova Conta")
    print("2 - [R] Read    ➔ Listar Todas as Contas")
    print("3 - [U] Update  ➔ Depositar em uma Conta")
    print("4 - [U] Update  ➔ Sacar de uma Conta")
    print("5 - [D] Delete  ➔ Encerrar/Excluir Conta")
    print("0 - Sair do Sistema")
    
    op = input("Escolha uma opção: ")

    if op == "1":
        nome = input("Digite o nome do Titular: ").strip()
        if nome:
            nova_conta = ContaBancaria(nome)
            lista_contas.append(nova_conta)
            print(f"✓ Conta de '{nome}' criada com sucesso!")
        else:
            print("❌ O nome do titular não pode ser vazio.")

    elif op == "2":
        print("\n--- TODAS AS CONTAS DO BANCO ---")
        if not lista_contas:
            print("Nenhuma conta cadastrada no banco.")
        else:
            for idx, conta in enumerate(lista_contas, 1):
                print(f"{idx}. {conta}")

    elif op == "3":
        nome_busca = input("Digite o nome do titular para depósito: ").strip()
        conta_encontrada = None
        
        for c in lista_contas:
            if c.titular.lower() == nome_busca.lower():
                conta_encontrada = c
                break
                
        if conta_encontrada:
            try:
                val = float(input("Digite o valor para depósito: R$ "))
                conta_encontrada.depositar(val)
            except ValueError:
                print("❌ Digite um valor numérico válido.")
        else:
            print(f"❌ Conta de '{nome_busca}' não encontrada.")

    elif op == "4":
        nome_busca = input("Digite o nome do titular para saque: ").strip()
        conta_encontrada = None
        
        for c in lista_contas:
            if c.titular.lower() == nome_busca.lower():
                conta_encontrada = c
                break
                
        if conta_encontrada:
            try:
                val = float(input("Digite o valor para saque: R$ "))
                conta_encontrada.sacar(val)
            except ValueError:
                print("❌ Digite um valor numérico válido.")
        else:
            print(f"❌ Conta de '{nome_busca}' não encontrada.")

    elif op == "5":
        nome_busca = input("Digite o nome do titular da conta que deseja EXCLUIR: ").strip()
        conta_encontrada = None
        
        for c in lista_contas:
            if c.titular.lower() == nome_busca.lower():
                conta_encontrada = c
                break
                
        if conta_encontrada:
            lista_contas.remove(conta_encontrada)
            print(f"✓ A conta de '{conta_encontrada.titular}' foi ENCERRADA e excluída do banco.")
        else:
            print(f"❌ Conta de '{nome_busca}' não encontrada.")

    elif op == "0":
        print("Encerrando o Sistema Bancário JWC Tech. Até logo!")
        break
    else:
        print("❌ Opção inválida! Tente novamente.")