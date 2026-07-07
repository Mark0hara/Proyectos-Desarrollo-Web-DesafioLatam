$(document).ready(function () {

    $("#enviarCorreo").click(function () {
        alert("El correo fue enviado correctamente...");
    });

    $("h2").on("dblclick", function () {
        if ($(this).text() === "INGREDIENTES" || $(this).text() === "PREPARACIÓN") {
            $(this).css("color", "red");
        }
    });
     // Doble clic en recetas relacionadas para que desaparezca y aparezca con 7 seg de duracion
    $(".card-title").click(function () {
        $(this).closest(".card").find(".card-body").slideToggle(750);
    });
});