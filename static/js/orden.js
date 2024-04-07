function borrarProducto(index){
    delete productos[index]
    cant_productos-=2
    ordenarProductos()
    listarProductos()
    Sumatoria()
};

function borrarServicio(a){
    delete servicios[a]
    cant_servicio-=2
    ordenarServicios()
    listarServicios()
    Sumatoria()
};

function borrarCausa(a){
    delete causas[a]
    cant_causas-=2
    ordenarCausas()
    listarCausas()
};

function ordenarProductos(){
    for (let i = 0; i <= cant_productos; i++) {
        if(productos[i] == null){
            productos[i] = productos[i+1];
            delete productos[i+1]}
    }
}

function ordenarServicios(){
    for (let i = 0; i <= cant_servicio; i++) {
        if(servicios[i] == null){
            servicios[i] = servicios[i+1];
            delete servicios[i+1]}
    }
}

function ordenarCausas(){
    for (let i = 0; i <= cant_causas; i++) {
        if(causas[i] == null){
            causas[i] = causas[i+1];
            delete causas[i+1]}
    }
}

function recalcularServicio(a){
    servicio = servicios[parseInt(a)];
    servicio.cantidad = parseInt($(`#cant_serv_${a}`).val())
    cant_servicio--
    listarServicios()
    Sumatoria()
}

function recalcularProducto(a){
    producto = productos[parseInt(a)];
    console.log(producto);
    if(parseInt($(`#cant_prod_${a}`).val()) <= parseInt(producto.cantidadMax)){
        producto.cantidad = parseInt($(`#cant_prod_${a}`).val())
    }else{
        mensajeError(`La cantidad excede la cantidad máxima de ${producto.cantidadMax} ${producto.unidad}`)
        producto.cantidad = 1
    }

    cant_productos--
        listarProductos()
        Sumatoria()
}

function listarServicios(){
    detalles_factura['total_servicios'] = 0.0
    $('#detalle-servicio tbody').html("");
    for(let i = 0; i <= cant_servicio; i++){
        let fila = '<tr>';
        fila +=  '<td>' + (servicios[i]['nombre']) + '</td>';
        fila +=  '<td>' + (servicios[i]['categoria']) + '</td>';
        fila +=  '<td>' + (servicios[i]['precio']) + '</td>';
        fila +=  '<td>' + `<input class="input-table" id="cant_serv_${i}" type="number" onchange="recalcularServicio(${i})" value= "${servicios[i]['cantidad']}" `  + '</td>';
        fila +=  '<td>' + (servicios[i]['precio']*servicios[i]['cantidad']).toFixed(2) + '</td>';
        fila +=  `<td><button class="btn-sm btn-danger" type="button" onclick="borrarServicio(${i})"><i class="bi bi-trash-fill"></button></td>`;
        fila +=  '</tr>';
        $('#detalle-servicio tbody').append(fila);
        detalles_factura['total_servicios'] += (servicios[i]['precio']*servicios[i]['cantidad'])
    }
    cant_servicio ++;
}

function listarCausas(){
    $('#detalle-causas tbody').html("");
    for(let i = 0; i <= cant_causas; i++){
        let fila = '<tr>';
        fila +=  '<td>' + (causas[i]['nombre']) + '</td>';
        fila +=  `<td><button class="btn-sm btn-danger" type="button" onclick="borrarCausa(${i})"><i class="bi bi-trash-fill"></button></td>`;
        fila +=  '</tr>';
        $('#detalle-causas tbody').append(fila);
    }
    cant_causas ++;
}

function listarProductos(){
    detalles_factura['total_productos'] = 0.0 
    $('#detalle-producto tbody').html("");
    for(let i = 0; i <= cant_productos; i++){
        let fila = '<tr>';
        fila +=  '<td>' + (productos[i]['nombre']) + '</td>';
        fila +=  '<td>' + (productos[i]['precio']) + '</td>';
        fila +=  '<td>' + `<input class="input-table" id="cant_prod_${i}" type="number" onchange="recalcularProducto(${i})" value= "${productos[i]['cantidad']}" ` + '</td>';
        fila +=  '<td>' + (productos[i]['unidad']) + '</td>';
        fila +=  '<td>' + (productos[i]['precio']*productos[i]['cantidad']).toFixed(2) + '</td>';
        fila +=  `<td><button class="btn-sm btn-danger" type="button" onclick="borrarProducto(${i})"><i class="bi bi-trash-fill"></button></td>`;
        fila +=  '</tr>';
        $('#detalle-producto tbody').append(fila);
        detalles_factura['total_productos'] += (productos[i]['precio']*productos[i]['cantidad'])
    }
    cant_productos ++;
}

function Sumatoria(){
    detalles_factura['subtotal'] = detalles_factura['total_productos'] + detalles_factura['total_servicios'] 
    detalles_factura['iva'] = detalles_factura['subtotal'] * 0.12
    detalles_factura['total'] = detalles_factura['subtotal'] + detalles_factura['iva']

    $('#id_subtotal').val(detalles_factura['subtotal'])
    $('#id_iva').val(detalles_factura['iva'])
    $('#id_total').val(detalles_factura['total'])
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        $('#myTable').DataTable();
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