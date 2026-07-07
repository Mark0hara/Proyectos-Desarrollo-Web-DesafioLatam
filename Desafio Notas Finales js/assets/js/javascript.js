// NOTAS HTML
let htmlNota1 = prompt("Ingrese nota 1 [HTML]:");
let htmlNota2 = prompt("Ingrese nota 2 [HTML]:");
let htmlNota3 = prompt("Ingrese nota 3 [HTML]:");
// NOTAS CSS
let cssNota1 = prompt("Ingrese nota 1 [CSS]:");
let cssNota2 = prompt("Ingrese nota 2 [CSS]:");
let cssNota3 = prompt("Ingrese nota 3 [CSS]:");
// NOTAS JAVASCRIPT
let jsNota1 = prompt("Ingrese nota 1 [JavaScript]:");
let jsNota2 = prompt("Ingrese nota 2 [JavaScript]:");
let jsNota3 = prompt("Ingrese nota 3 [JavaScript]:");
// Fórmula del promedio: (nota1 + nota2 + nota3) / 3
let htmlPromedio = (parseFloat(htmlNota1) + parseFloat(htmlNota2) + parseFloat(htmlNota3)) / 3;
let cssPromedio = (parseFloat(cssNota1) + parseFloat(cssNota2) + parseFloat(cssNota3)) / 3;
let jsPromedio = (parseFloat(jsNota1) + parseFloat(jsNota2) + parseFloat(jsNota3)) / 3;

// MOSTRAR NOTAS EN LA TABLA:
// HTML
document.getElementById("html-nota1").textContent = htmlNota1;
document.getElementById("html-nota2").textContent = htmlNota2;
document.getElementById("html-nota3").textContent = htmlNota3;
document.getElementById("html-promedio").textContent = htmlPromedio.toFixed(2);
// CSS
document.getElementById("css-nota1").textContent = cssNota1;
document.getElementById("css-nota2").textContent = cssNota2;
document.getElementById("css-nota3").textContent = cssNota3;
document.getElementById("css-promedio").textContent = cssPromedio.toFixed(2);
// JavaScript
document.getElementById("js-nota1").textContent = jsNota1;
document.getElementById("js-nota2").textContent = jsNota2;
document.getElementById("js-nota3").textContent = jsNota3;
document.getElementById("js-promedio").textContent = jsPromedio.toFixed(2);