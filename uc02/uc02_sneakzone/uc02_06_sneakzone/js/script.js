let carrinho = [];
let produtoSelecionado = null;

function formatarMoeda(valor) {
    return valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
}

function comprar(nomeProduto, preco, imagem) {
    produtoSelecionado = { nome: nomeProduto, preco: preco, imagem: imagem };

    document.getElementById('modalProdutoNome').textContent = nomeProduto;
    document.getElementById('modalProdutoPreco').textContent = formatarMoeda(preco);
    document.getElementById('modalProdutoImagem').src = imagem;
    document.getElementById('modalProdutoImagem').alt = nomeProduto;

    const modal = bootstrap.Modal.getOrCreateInstance(document.getElementById('modalProduto'));
    modal.show();
}

function confirmarCompra() {
    if (!produtoSelecionado) return;

    carrinho.push({ ...produtoSelecionado });
    atualizarCarrinho();

    const modal = bootstrap.Modal.getInstance(document.getElementById('modalProduto'));
    if (modal) modal.hide();

    document.getElementById('carrinho').scrollIntoView({ behavior: 'smooth' });
}

function atualizarCarrinho() {
    const lista = document.getElementById('listaCarrinho');
    const contador = document.getElementById('contadorCarrinho');
    const totalElemento = document.getElementById('totalCarrinho');

    contador.textContent = carrinho.length;

    if (carrinho.length === 0) {
        lista.innerHTML = '<p class="text-secondary mb-0">Seu carrinho está vazio.</p>';
        totalElemento.textContent = formatarMoeda(0);
        return;
    }

    let total = 0;
    lista.innerHTML = carrinho.map((produto, index) => {
        total += produto.preco;
        return `
            <div class="d-flex justify-content-between align-items-center border-bottom py-2 gap-3">
                <div class="d-flex align-items-center gap-2">
                    <img src="${produto.imagem}" alt="${produto.nome}" width="55" height="55" class="rounded object-fit-cover">
                    <span>${produto.nome}</span>
                </div>
                <div class="d-flex align-items-center gap-2">
                    <strong>${formatarMoeda(produto.preco)}</strong>
                    <button class="btn btn-sm btn-outline-danger" onclick="removerDoCarrinho(${index})" aria-label="Remover ${produto.nome}"><i class="bi bi-trash"></i></button>
                </div>
            </div>`;
    }).join('');

    totalElemento.textContent = formatarMoeda(total);
}

function removerDoCarrinho(index) {
    carrinho.splice(index, 1);
    atualizarCarrinho();
}

function finalizarCarrinho() {
    if (carrinho.length === 0) {
        alert('Seu carrinho está vazio.');
        return;
    }

    const total = carrinho.reduce((soma, produto) => soma + produto.preco, 0);
    alert(`Pedido pronto!\nItens: ${carrinho.length}\nTotal: ${formatarMoeda(total)}`);
}

function cadastrar() {
    const form = document.getElementById('formCadastro');

    if (!form.checkValidity()) {
        form.classList.add('was-validated');
        return;
    }

    let nome = document.getElementById('nome').value;
    let email = document.getElementById('email').value;
    let telefone = document.getElementById('telefone').value;
    let idade = document.getElementById('idade').value;
    let numeracao = document.getElementById('numeracao').value;
    let cor = document.getElementById('cor').value;
    let mensagem = document.getElementById('mensagem').value;

    let estiloSelecionado = document.querySelector('input[name="estilo"]:checked');
    let estilo = estiloSelecionado ? estiloSelecionado.value : 'Não informado';

    let tiposTenis = [];
    if (document.getElementById('tenisCorrida').checked) tiposTenis.push('Corrida');
    if (document.getElementById('tenisCasual').checked) tiposTenis.push('Casual');
    if (document.getElementById('tenisBasquete').checked) tiposTenis.push('Basquete');
    if (document.getElementById('tenisTrilha').checked) tiposTenis.push('Trilha');

    let cliente = { nome, email, telefone, idade, numeracao, cor, estilo, tiposTenis, mensagem };

    document.getElementById('mensagemSucesso').innerHTML =
        '<div class="alert alert-success" role="alert"><i class="bi bi-check-circle"></i> Cadastro realizado com sucesso!</div>';

    console.log(cliente);
}

function calcularFrete() {
    const valor = parseFloat(document.getElementById('valorCompra').value);
    const regiao = document.getElementById('regiao').value;
    const resultado = document.getElementById('resultado');

    if (isNaN(valor) || valor < 0 || !regiao) {
        resultado.className = 'alert alert-danger mb-0';
        resultado.textContent = 'Informe um valor de compra e uma região válida.';
        return;
    }

    let frete = 0;
    let limiteGratis = 299;

    if (regiao === 'sudeste') frete = 19.90;
    if (regiao === 'sul') frete = 24.90;
    if (regiao === 'nordeste') {
        frete = 29.90;
        limiteGratis = 349;
    }

    if (valor >= limiteGratis) frete = 0;

    const total = valor + frete;
    const mensagemFrete = frete === 0 ? 'Frete grátis!' : formatarMoeda(frete);

    resultado.className = 'alert alert-info mb-0';
    resultado.innerHTML = `
        <strong>Resumo do pedido</strong><br>
        Subtotal: ${formatarMoeda(valor)}<br>
        Frete: ${mensagemFrete}<br>
        <strong>Total: ${formatarMoeda(total)}</strong>`;
}

atualizarCarrinho();
