const boton = document.getElementById("btn-frase");
const resultado = document.getElementById("resultado");

boton.addEventListener("click", () => {
    fetch("/frase")
        .then(respuesta => respuesta.json())
        .then(data => {
            resultado.textContent = data.frase;
        });
});
