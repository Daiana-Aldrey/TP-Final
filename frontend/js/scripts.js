function mostrarFormulario(categoria) {
    document.getElementById('seleccion-inicial').style.display = 'none';
    document.getElementById('formulario-compra').style.display = 'block';

    fetch(`http://localhost:5000/categorias/${categoria}`)
        .then(response => response.json())
        .then(data => {
            const marcaSelect = document.getElementById('marca');
            marcaSelect.innerHTML = ''; 
            data.marcas.forEach(marca => {
                const option = document.createElement('option');
                option.value = marca;
                option.textContent = marca;
                marcaSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error al obtener marcas:', error));
}

function mostrarMensaje() {
    document.getElementById('mensaje-exito').style.display = 'block';
    document.getElementById('comprar_form').reset();
    return false;
}
