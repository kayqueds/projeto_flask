// script.js
document.addEventListener("DOMContentLoaded", function() {
    var loadingSpinner = document.getElementById('loading-spinner');
    var content = document.getElementById('content');

    // Simula um tempo de carregamento
    setTimeout(function() {
        loadingSpinner.style.display = 'none';
        content.style.display = 'block';
    }, 2000); // 2 segundos de carregamento simulado
});
