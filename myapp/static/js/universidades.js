/*
    1. Meter en una variable el dato que el usuario selecciona (varCA = "País Vasco")
    2. Buscar ese valor en la base de datos dentro de la ccaa
            varCA = Universidad.ccaa("País Vasco");
    3. Modificar la tabla y mostrar solo las universidades con esa ccaa
*/

//ordenarTabla() - función para ordenar la tabla ordenado alfabéticamente por el nombre de la universidad

function ordenarTabla() {
    var table, i, x, y;
    tabla = document.getElementById("tabla");
    var switching = true;

    // Se recorre el switchin entre las diferentes filas hasta que no haga falta hacer más cambios
    while (switching) {
        switching = false;
        var filas = tabla.rows;

        // Bucle para recorrer cada fila de la tabla
        for (i = 1; i < (filas.length - 1); i++) {
            var Switch = false;

            // Selecciona dos filas para comparar
            x = filas[i].getElementsByTagName("TD")[0];
            y = filas[i + 1].getElementsByTagName("TD")[0];

            // Comprueba si las dos filas seleccionadas tienen que cambiarse de orden
            if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {

                // Si hay que cambiar el ordeen de las dos filas, se cambia el estado see Switch a true y se para el bucle
                Switch = true;
                break;
            }
        }
        //Si se ha roto el bucle = si el estado de Switch = true
        if (Switch) {
            // cambiamos el orden de las filas y cambiamos el estado de switching a true, para marcarlo como finalizadoFunction to switch rows and mark switch as completed
            filas[i].parentNode.insertBefore(filas[i + 1], filas[i]);
            switching = true;
        }
    }
}