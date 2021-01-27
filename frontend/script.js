const empresa = document.querySelector('#empresa')
const vaga = document.querySelector('#vaga')
const btn = document.querySelector('#send')
const text = document.querySelector('#log')
const stopBtn = document.querySelector('#stop')
const credentails = document.querySelectorAll('#modelId input[type=text], input[type=password]')
let loadSpin

// Mostrar na tela
eel.expose(output)
text.innerHTML = ``
function output(texto){
    if(texto){
        console.log(loadSpin)
        loadSpin.innerHTML = ''
    }

    text.innerHTML += `${texto} </br>`
}

// Reativar botão
eel.expose(enableButton)
function enableButton(){
    btn.disabled = false
}

// Enviar ao backend
btn.addEventListener('click',() => {
    const [email_infojobs, password_infojobs, email_vagas, password_vagas] = credentails

    btn.disabled = true
    
    text.innerHTML = `<div id="load" class="d-flex align-items-center">
    <strong>Carregando...</strong>
    <div class="spinner-border ml-auto text-primary" role="status" aria-hidden="true"></div>
    </div></br>`

    eel.send(empresa.value, vaga.value, email_infojobs.value, password_infojobs.value, email_vagas.value, password_vagas.value)
    loadSpin = document.querySelector('#load')
})

// Parar busca de empregos
// btn.addEventListener('click', () => {
//     eel.stop()
// })