function mensajeSuccess (mensaje){
    Swal.fire({
        title: 'Felicitaciones',
        text: mensaje,
        icon: 'success',
        confirmButtonText: 'Aceptar'
    })
}


function mensajeError (mensaje){
    Swal.fire({
        title: 'Error',
        text: mensaje,
        icon: 'error',
        confirmButtonText: 'Aceptar'
    })
}

function abrir_modal_eliminacion(url){
    $('#addModal').load(url, function(){
        $(this).modal('show');
    });
}

function cerrar_modal_eliminacion(){
    $('#addModal').modal('hide');
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}