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
# Removemos a largura interna fixa global, pois agora ela será dinâmica.


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
            print(f" [ERRO] Alíquota fora do limite legal ({ALIQUOTA_MINIMA}% a {ALIQUOTA_MAXIMA}%).")
        except ValueError:
            print(" [ERRO] Entrada inválida. Utilize formato numérico (ex: 11 ou 11.5).")


def renderizar_holerite(nome: str, bruto: float, aliquota: float) -> None:
    """Realiza o processamento contábil e renderiza o layout autoexpansível do holerite.
    
    A largura se adapta dinamicamente ao tamanho do nome do colaborador.
    """
    # Regras de Negócio / Cálculos Contábeis
    desconto_inss = bruto * aliquota / 100
    salario_liquido = bruto - desconto_inss

    # Base de strings para os cálculos financeiros
    str_bruto_valores = f"R$ {bruto:>10.2f}"
    str_inss_valores  = f"R$ {desconto_inss:>10.2f}"
    str_liq_valores   = f"R$ {salario_liquido:>10.2f}"

    # Define uma largura mínima baseada no tamanho padrão dos campos financeiros ou título
    # " Desconto INSS (00.0%):   " tem 26 caracteres + 13 do valor = 39. É a nossa base segura.
    largura_base_financeira = 39 
    largura_nome_real = len(f" Colaborador: {nome} ")

    # A largura interna final será o maior valor entre o tamanho do nome ou a base financeira
    largura_dinamica = max(largura_base_financeira, largura_nome_real)

    # Engenharia de Layout Adaptativa
    string_titulo = f"{'DEMONSTRATIVO DE PAGAMENTO':^{largura_dinamica}}"
    string_nome   = f" Colaborador: {nome}".ljust(largura_dinamica)
    
    # Alinhamento dos valores financeiros ajustados à nova largura dinâmica
    string_bruto  = f" Vencimentos (Bruto):".ljust(largura_dinamica - len(str_bruto_valores)) + str_bruto_valores
    string_inss   = f" Desconto INSS ({aliquota:>4.1f}%):".ljust(largura_dinamica - len(str_inss_valores)) + str_inss_valores
    string_liq    = f" SALÁRIO LÍQUIDO:".ljust(largura_dinamica - len(str_liq_valores)) + str_liq_valores

    # Construção da Estrutura de Contorno (Unicode Box-Drawing)
    linha_horizontal = "─" * (largura_dinamica + 2)
    linha_topo  = "╭" + linha_horizontal + "╮"
    linha_meio  = "├" + linha_horizontal + "┤"
    linha_base  = "╰" + linha_horizontal + "╯"

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
