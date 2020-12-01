const empresa = document.querySelector('#empresa')
const vaga = document.querySelector('#vaga')
const btn = document.querySelector('#send')
const text = document.querySelector('#log')

// Mostrar na tela
eel.expose(output)
text.innerHTML = ``
function output(texto){
    text.innerHTML += `Bot: ${texto} <br>`
}


// Enviar ao backend
btn.addEventListener('click',() => {
    text.innerHTML = `Carregando... <br>`
    eel.send(empresa.value, vaga.value)
})