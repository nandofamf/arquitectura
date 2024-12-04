// Selecciona todas las tarjetas en la página
document.querySelectorAll('.card').forEach((card) => {
    // Agrega un evento al hacer clic en cada tarjeta
    card.addEventListener('click', () => {
        // Cambia el contenido de la tarjeta cuando se hace clic
        const content = card.querySelector('.content');
        content.textContent = '¡Tarjeta clickeada!';

        // Opcional: Agregar un efecto visual extra al hacer clic
        card.classList.add('clicked');
        setTimeout(() => {
            card.classList.remove('clicked');
        }, 500); // Elimina la clase después de 500ms

        // También puedes redirigir a otra página
        if (content.textContent.includes('Ver Gastos')) {
            window.location.href = '/ver_gastos/';
        } else if (content.textContent.includes('Generar Gasto')) {
            window.location.href = '/generar_gasto/';
        } else if (content.textContent.includes('Registrar Pago')) {
            window.location.href = '/registrar_pago/';
        }
    });
});
