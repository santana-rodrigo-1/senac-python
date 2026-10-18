# -*- coding: utf-8 -*-
"""SISTEMA DE RECURSOS HUMANOS - MÓDULO DE SNE/FOLHA DE PAGAMENTO.

Este sistema realiza a validação de entradas cadastrais e financeiras
para emissão e renderização de demonstrativos de pagamento (holerites).
"""

import sys
from typing import Final

# Definição de Constantes Globais de Negócio (Configuráveis)
ALIQUOTA_MINIMA: Final[float] = 0.0
ALIQUOTA_MAXIMA: Final[float] = 20.0
LARGURA_INTERNA_CONTEUDO: Final[int] = 38


def obter_nome_funcionario() -> str:
    """Solicita e valida o nome do colaborador, garantindo que não seja vazio."""
    while True:
        nome = input("Digite o nome do funcionário: ").strip()
        if nome:
            return nome.title()
        print(" [ERRO] O nome corporativo não pode ser vazio. Tente novamente.")


def obter_salario_bruto() -> float:
    """Solicita e valida o salário bruto, tratando divergências de pontuação."""
    while True:
        entrada = input("Digite o salário bruto (R$): ").strip()
        entrada_higienizada = entrada.replace(",", ".")
        try:
            salario = float(entrada_higienizada)
            if salario > 0:
                return salario
            print(" [ERRO] O salário bruto deve ser um valor positivo superior a zero.")
        except ValueError:
            print(" [ERRO] Caracteres inválidos. Insira apenas números (ex: 2500.00).")


def obter_aliquota_inss() -> float:
    """Valida a alíquota de desconto dentro das regras paramétricas do RH."""
    while True:
        entrada = input("Digite a alíquota do INSS (%): ").strip()
        entrada_higienizada = entrada.replace(",", ".")
        try:
            aliquota = float(entrada_higienizada)
            if ALIQUOTA_MINIMA <= aliquota <= ALIQUOTA_MAXIMA:
                return aliquota
            print(
                f" [ERRO] Alíquota fora do limite legal ({ALIQUOTA_MINIMA}% a {ALIQUOTA_MAXIMA}%)."
            )
        except ValueError:
            print(
                " [ERRO] Entrada inválida. Utilize formato numérico (ex: 11 ou 11.5)."
            )


def renderizar_holerite(nome: str, bruto: float, aliquota: float) -> None:
    """Realiza o processamento contábil e renderiza o layout final do holerite.

    A largura interna é controlada rigidamente por constantes para prevenir
    erros de denteamento causados pela interpretação de caracteres Unicode.
    """
    # Regras de Negócio / Cálculos Contábeis
    desconto_inss = bruto * aliquota / 100
    salario_liquido = bruto - desconto_inss

    # Engenharia de Layout - Strings Internas com Largura Fixa Estrita (38 caracteres)
    string_titulo = f"{'DEMONSTRATIVO DE PAGAMENTO':^{LARGURA_INTERNA_CONTEUDO}}"
    string_nome = f" Colaborador: {nome:<25}"[:LARGURA_INTERNA_CONTEUDO].ljust(
        LARGURA_INTERNA_CONTEUDO
    )
    string_bruto = f" Vencimentos (Bruto):    R$ {bruto:>10.2f}"
    string_inss = f" Desconto INSS ({aliquota:>4.1f}%):  R$ {desconto_inss:>10.2f}"
    string_liq = f" SALÁRIO LÍQUIDO:        R$ {salario_liquido:>10.2f}"

    # Construção da Estrutura de Contorno (Unicode Box-Drawing)
    linha_horizontal = "─" * (LARGURA_INTERNA_CONTEUDO + 2)
    linha_topo = "╭" + linha_horizontal + "╮"
    linha_meio = "├" + linha_horizontal + "┤"
    linha_base = "╰" + linha_horizontal + "╯"

    # Saída Gráfica do Demonstrativo no Terminal
    print("\n" + linha_topo)
    print(f"│ {string_titulo} │")
    print(linha_meio)
    print(f"│ {string_nome} │")
    print(linha_meio)
    print(f"│ {string_bruto} │")
    print(f"│ {string_inss} │")
    print(linha_meio)
    print(f"│ {string_liq} │")
    print(linha_base + "\n")


def main() -> None:
    """Ponto de entrada principal da aplicação (Application Lifecycle)."""
    try:
        # Coleta de Dados Cadastrais e Financeiros
        nome = obter_nome_funcionario()
        salario_bruto = obter_salario_bruto()
        aliquota_inss = obter_aliquota_inss()

        # Geração do Artefato de Saída
        renderizar_holerite(nome, salario_bruto, aliquota_inss)

    except KeyboardInterrupt:
        # Tratamento do encerramento forçado via terminal (Ctrl+C)
        print("\n\n [SISTEMA] Processo finalizado pelo operador. Desconectando...")
        sys.exit(0)


if __name__ == "__main__":
    main()
