function comprar(nomeProduto, preco){
    console.log("Produto: ", nomeProduto);
    console.log("Preço: ", preco);

    alert(
        "Você selecionou: " + nomeProduto + "Preço: R$" + preco
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


    let estiloSelecionado = document.querySelector(
        'input[name="estilo"]:checked'
    );
    
    let estilo;
    if (estiloSelecionado) {
        estilo = estiloSelecionado.value;
    } else {
        estilo = "Não informado";
    }


    let tiposTenis = [];

    if (document.getElementById("tenisCorrida").checked) {
        tiposTenis.push("Corrida");
    }
    if (document.getElementById("tenisCasual").checked) {
        tiposTenis.push("Casual");
    }
    if (document.getElementById("tenisBasquete").checked) {
        tiposTenis.push("Basquete");
    }
    if (document.getElementById("tenisTrilha").checked) {
        tiposTenis.push("Trilha");
    }

    let cliente = {
        nome,
        email,
        telefone,
        idade,
        numeracao,
        cor,
        estilo,
        tiposTenis,
        mensagem
    };

    alert(
        "Nome: " + nome + "\n" +
        "E-mail: " + email + "\n" +
        "Telefone: " + telefone + "\n" +
        "Idade: " + idade + "\n" +
        "Numeração: " + numeracao + "\n" +
        "Cor: " + cor + "\n" +
        "Estilo: " + estilo + "\n" +
        "Interesses: " + tiposTenis.join(", ") + "\n" +
        "Mensagem: " + mensagem
    );

    console.log(cliente);
}

function calcularFrete(){

    let valorCompra = document.getElementById("valorCompra").value;
    let regiao = document.getElementById("regiao").value;

    valor = parseFloat(valorCompra);

    let frete = 0;

    if (regiao == "sudeste") {
        frete = 19.90;

    }

    if (regiao == "sul") {
        frete = 24.90;

    }

    if (regiao == "nordeste") {
        frete = 29.90;

    }

    if (valor >= 299) {
        frete = 0;
    }

    document.getElementById("resultado").textContent = 
    "Frete: R$ " + frete.toFixed(2);

    console.log(valorCompra)
    console.log(regiao)
    console.log(frete)
}