
    let busca_cod = document.querySelector('.busca_cod');
    let result = document.querySelector('.prod_info');
    let codigo = Number(document.querySelector(".cod_prod").value);
    let btnSearch = document.querySelector('.btn-search');

    async function getData(codigo) {
        let response = await fetch(`/busca_prod/?busca_prod=${codigo}`);
        
        if (response.status == 200) {
            let data = await response.json();
            result.innerHTML = `<div class="nome_produto">
                                    <h2>Produto:</h2>
                                    <p class="nome_prod">${data.nome}</p>
                                </div>
                                <div class="valor_produto">
                                    <h2>Valor do Produto:</h2>
                                    <p class="val_prod">${data.valor}</p>
                                </div>`;
        }
    }

    btnSearch.addEventListener("click", (event) => {
        event.preventDefault();
        getData(codigo);
        console.log(data);
    });






// let busca_cod = document.querySelector('.busca_cod');
// let result = document.querySelector('.prod_info');
// let codigo = Number(document.querySelector(".cod_prod").value);
// let btnSearch = document.querySelector('.btn-search');



// async function getData(codigo){
    
//     let response = await fetch(`busca_prod/${codigo}`)
    
//     if (response.status == 200) {
//         let data = await response.json()
//         result.innerHTML = `<div class="nome_produto">
//                                 <h2>Produto:</h2>
//                                 <p class="nome_prod">${data.nome}</p>
//                             </div>
//                             <div class="valor_produto">
//                                 <h2>Valor do Produto:</h2>
//                                 <p class="val_prod">${data.valor}</p>
//                             </div>`;
//     }else{
//         result.innerHTML = `Código não encontrado`;
//     }
// }

// btnSearch.addEventListener("submit", (event) => {
//   event.preventDefault();
//   getData(codigo);
//   console.log(data);
// });


// document.querySelector(".btn-search").addEventListener('click', function() {
//     ;

//     async function busca_produto(){
//     let response = await fetch('busca_prod/')
//     let data = await response.json()
//     }

//     busca_produto();

//     for(i in data){
//         if(data.id = id){
//             nome_prod.value = data.nome;
//             valor_prod.value = data.valor;
//         }
//     }


// })


