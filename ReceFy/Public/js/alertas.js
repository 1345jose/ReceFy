//Alertas plan nutricional

function borrarPlan(event, element) {
    event.preventDefault(); 
    const url = element.getAttribute('data-url');

    Swal.fire({
        title: "Estas seguro ?",
        text: "Si la eliminas no la podras recuperar !",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, Eliminar!"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Plan Eliminado!",
                text: "Tu plan ha sido eliminado con exito",
                icon: "success"
            }).then(() => {
                // Redirige a la URL obtenida
                window.location.href = url;
            });
        }
    });
}
