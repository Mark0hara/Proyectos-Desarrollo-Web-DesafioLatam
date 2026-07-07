$(document).ready(function () {
    console.log("jQuery cargado correctamente");
});

// 1. Hide/Show/Toggle
function hideEffect() {
    $("#hideTarget").hide(1000);
}
function showEffect() {
    $("#hideTarget").show("slow");
}
function toggleEffect() {
    $("#hideTarget").toggle(500);
}
function resetHide() {
    $("#hideTarget").show();
}

// 2. Fade Effects
function fadeInEffect() {
    $("#fadeTarget").fadeIn(1000);
}
function fadeOutEffect() {
    $("#fadeTarget").fadeOut("slow");
}
function fadeToggleEffect() {
    $("#fadeTarget").fadeToggle(800);
}
function fadeToEffect() {
    $("#fadeTarget").fadeTo(1000, 0.3);
}
function resetFade() {
    $("#fadeTarget").stop().css("opacity", 1).show();
}

// 3. Slide Effects
function slideUpEffect() {
    $("#slideTarget").slideUp(1000);
}
function slideDownEffect() {
    $("#slideTarget").slideDown("fast");
}
function slideToggleEffect() {
    $("#slideTarget").slideToggle(800);
}
function resetSlide() {
    $("#slideTarget").stop().show();
}

// 4. Animate Effects
function animateRight() {
    $("#animateBox").animate({ left: "+=200px" }, 1000);
}
function animateLeft() {
    $("#animateBox").animate({ left: "-=200px" }, 1000);
}
function animateGrow() {
    $("#animateBox").animate({
        width: "150px",
        height: "150px",
        fontSize: "20px"
    }, 1000);
}
function animateComplex() {
    $("#animateBox").animate({
        left: "300px",
        opacity: 0.5,
        borderRadius: "50%"
    }, 1500);
}
function resetAnimate() {
    $("#animateBox").stop().css({
        left: "0",
        width: "100px",
        height: "100px",
        opacity: 1,
        borderRadius: "10px",
        fontSize: "14px"
    });
}

// 5. Delay Effect
function delayEffect() {
    $("#delayTarget")
        .slideUp(500)
        .delay(2000)
        .slideDown(500)
        .delay(1000)
        .fadeOut(500)
        .delay(1000)
        .fadeIn(500);
}
function resetDelay() {
    $("#delayTarget").stop().show();
}

// 6. Toggle Class
function toggleClassEffect() {
    $("#classTarget").toggleClass("active");
}
function addClassEffect() {
    $("#classTarget").addClass("highlight");
}
function removeClassEffect() {
    $("#classTarget").removeClass("highlight");
}
function resetClass() {
    $("#classTarget").removeClass("active highlight");
}

// 7. Callback
function callbackEffect() {
    $("#callbackTarget").fadeOut(1000, function () {
        alert("¡El efecto fadeOut terminó! Ahora voy a aparecer de nuevo.");
        $(this).fadeIn(1000);
    });
}

// 8. Chain
function chainEffect() {
    $("#chainTarget")
        .slideUp(300)
        .delay(500)
        .slideDown(300)
        .css({ background: "#764ba2" })
        .animate({ width: "150px" }, 500)
        .delay(500)
        .animate({ width: "100px" }, 500);
}
function resetChain() {
    $("#chainTarget").stop().css({
        background: "linear-gradient(135deg, #667eea, #764ba2)",
        width: "100px"
    }).show();
}