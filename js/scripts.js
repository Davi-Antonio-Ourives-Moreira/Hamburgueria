icone_menubar = document.getElementById("icone-menu-bar");

botao_scroll_top = document.getElementById("botao-scroll-top");

botao_scroll_top_div = document.querySelector(".botao-scroll-top");

menu_bar = document.querySelector(".menu-bar");

icone_menubar.onclick = () => {
    if (icone_menubar.classList.contains('bi-list')) {
        icone_menubar.classList.remove('bi-list');
        icone_menubar.classList.add('bi-x');

        menu_bar.style.display = "block";
    } else {
        icone_menubar.classList.remove('bi-x');
        icone_menubar.classList.add('bi-list');

        menu_bar.style.display = "none";
    }
}

botao_scroll_top.onclick = () => {
    window.location.href = "#home";
}

window.onscroll = function() {
    if (document.body.scrollTop > 0 || document.documentElement.scrollTop > 0) {
        botao_scroll_top_div.style.display = "block"; 
    } else {
        botao_scroll_top_div.style.display = "none"; 
    }
};