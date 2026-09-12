function comprar(nomeProduto, preco) {
    console.log("Produto: ", nomeProduto);
    console.log("Preço: ", preco);
    alert(
        "Você selecionou: " + nomeProduto + " preço: R$ " + preco
    )
}

function cadastrar() {

    let nome = document.getElementById("nome").value;
    let email = document.getElementById("email").value;
    let telefone = document.getElementById("telefone").value;
    let idade = document.getElementById("idade").value;
    let numeracao = document.getElementById("numeracao").value;
    let cor = document.getElementById("cor").value;
    let mensagem = document.getElementById("mensagem").value;

    let estilo = document.querySelector(
        'input[name= "estilo"]:checked'
    ).value
    let cliente = {
        nome: nome,
        email: email,
        telefone: telefone,
        idade: idade,
        numeracao: numeracao,
        cor: cor,
        mensagem: mensagem
    }

    console.log(nome)
}

function calcularFrete() {
    let valor = do.getElementById("valor").value;
    let regiao = document.getElementById(regiao).value;

    valor = parseFloat(valor);

    let frete;

    if (regiao == "sudeste") {
        frete = 19, 90;
    }
    else if (true) {

    }
    if (regiao == "sul") {
        frete = 24, 90;
    }
    if (regiao == "nordeste") {
        frete = 29, 90;
    }
    if (valor >= 299) {
        frete = 0;
    }

    document.getElementById("resultado").textContent =
        "frete: R$ " + frete.toFixed(2);
}