var lista_usuario = [];
//Busca as informações contidas dentro do banco de dados.
async function carregarUsuario(){
    
    const response = await axios.get('http://localhost:8000/usuarios');

    const usuarios = response.data

    const lista = document.getElementById('usuarios_cadastrados');
    
    
    lista.innerHTML = ""
    
    //O laço abaixo cria as linhas e as celulas para cada atributo e
    //seguida coloca os dados vindos do formulario cadastrar na lista.
    usuarios.forEach(usuario => {
        const linha = document.createElement('tr')
        const linha_nome = document.createElement('td')
        const linha_idade = document.createElement('td')
        const linha_cpf = document.createElement('td')
        const linha_telefone = document.createElement('td')
        
        var btEditar = document.createElement('a')
        var btRemover = document.createElement('a')
                
        linha_nome.innerText = usuario.nome
        linha_idade.innerText = usuario.idade
        linha_cpf.innerText = usuario.cpf
        linha_telefone.innerText = usuario.telefone 
        btEditar.innerHTML = '<a a class="fa fa-edit" onclick="openModal()" id="btnEditar"></a>'
        btRemover.innerHTML = '<a class="fa fa-trash" id="btnRemover"></a>'
        

        linha.appendChild(linha_nome)
        linha.appendChild(linha_idade)
        linha.appendChild(linha_cpf)
        linha.appendChild(linha_telefone)
        linha.appendChild(btEditar)
        linha.appendChild(btRemover)
        

        lista.appendChild(linha)
        
        btEditar.onclick = () => openModal(usuario.id)
        btRemover.onclick = () => openModalConfirmacao(usuario.codigo)
        lista_usuario.push([usuario.id, usuario.codigo, usuario.nome, usuario.idade, usuario.cpf, usuario.telefone])
    });    
    //-------------------------------------------------------------------------------------------------------------
    //-------------------------------------------------------------------------------------------------------------
    var tabela = document.getElementById('tdUsuario');
    var linhas = tabela.getElementsByTagName('tr');

    //Evento Click
    for(var i = 0; i < linhas.length; i++){
        var linha = linhas[i];
        linha.addEventListener("click", function(){
            selLinha(this, false); //Selecione apenas um
            //selLinha(this, true); //Selecione quantos quiser
        });
    }

    /**
    A função selLinha() vai ser responsável por adicionar ou remover a class “selecionado” do nó. Passamos também um parâmetro que vai determinar se poderá selecionar mais que uma linha ou apenas uma. O primeiro laço, caso múltiplos seja falso, irá apenas desmarcar todos as linhas antes de marcar a linha clicada
    Caso passe true, você pode selecionar multiplas linhas.
    Caso passe false, você só pode selecionar uma linha por vez.
    **/
    function selLinha(linha, multiplos){
        if(!multiplos){
            var linhas = linha.parentElement.getElementsByTagName("tr");
            for(var i = 0; i <linhas.length; i++){
                var linha_ = linhas[i];
                linha_.classList.remove("selecionado");
            }
        }
        linha.classList.toggle("selecionado");
    }
};


//A função faz com que o icone de editar seja aberto com os dados para serem atualizados.
async function openModal(id_usuario){
    const modal = document.getElementById('dv-modal')
    if(typeof modal == 'undefined' || modal == null)
        return;
        modal.style.display = 'Block';
  
    for(var n = 0; n < lista_usuario.length; n++)
    {
        if(lista_usuario[n].includes(id_usuario) == true)
        {
            lin_nome = document.getElementById('nome');
            lin_idade = document.getElementById('idade')
            lin_cpf = document.getElementById('cpf')
            lin_telefone = document.getElementById('telefone')
            
            lin_nome.value = lista_usuario[n][1]
            lin_idade.value = lista_usuario[n][2]
            lin_cpf.value = lista_usuario[n][3]
            lin_telefone.value = lista_usuario[n][4]        
        }  
    } 
    AtualizarDados(id_usuario)
}

//Fecha o formulario de edição.
function closeModal(){
    let modal = document.getElementById('dv-modal')

    if(typeof modal == 'undefined' || modal == null)
        return;
    modal.style.display = 'none';
}


//Atualiza as informações no formulario de editar, através da roa PUT.
function AtualizarDados(id_usuario){
    const form_editar = document.getElementById('form-editar');
    const input_nome = document.getElementById('nome');
    const input_idade = document.getElementById('idade');
    const input_cpf = document.getElementById('cpf');
    const input_telefone = document.getElementById('telefone');

    form_editar.onsubmit = async (event) =>{
        event.preventDefault()
        const nome = input_nome.value
        const idade = input_idade.value
        const cpf = input_cpf.value
        const telefone = input_telefone.value


        await axios.put('http://localhost:8000/usuarios/'+ id_usuario,{
            nome: codigo,
            idade: produto,
            cpf: preco,
            telefone: quantidade,
        });
        alert(" Usuário Atualizado!")
    }
}


//A função faz com que o icone de deletar seja aberto com a confirmação se deseja excluir ou não.
function openModalConfirmacao(usuario_codigo){
    const modal = document.getElementById('dv-modal_confirmacao')
    if(typeof modal == 'undefined' || modal == null)
        return;
    modal.style.display = 'Block';

    const btSim = document.getElementById('botao-sim')

    btSim.onclick = async () =>{
        await axios.delete('http://localhost:8000/usuarios/' + produto_codigo);  
        alert("Usuário Deletado com sucesso!") 
    }
    
}


//Fecha o o botão de confirmação.
function closeModalConfirmacao(){
    let modal = document.getElementById('dv-modal_confirmacao')

    if(typeof modal == 'undefined' || modal == null)
        return;
    modal.style.display = 'none';
}


//Afunção serve para inicializar e chamar as outras funções.
function App(){
    console.log('App Iniciada')
    carregarUsuario()
    AtualizarDados()
}
App()