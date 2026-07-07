
document.addEventListener('DOMContentLoaded', function () {

    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    const contactForm = document.getElementById('contactForm');
    const toastEl = document.getElementById('liveToast');
    const toast = new bootstrap.Toast(toastEl, {
        autohide: true,
        delay: 3000 // Se oculta solo después de 3 segundos
    });
    contactForm.addEventListener('submit', function (event) {
        event.preventDefault(); 
        toast.show();
        contactForm.reset();
    });
    const scrollSpy = new bootstrap.ScrollSpy(document.body, {
        target: '.navbar',       
        offset: 56,              
        smoothScroll: true       
    });
});