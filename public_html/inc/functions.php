<?php
$pages = array(
    'witam' => 'Aplikacja w PHP',
    'sqlcmd' => 'SQL',
    'formularz' => 'Formularz'
) // słownik, definicja trzech stron

function get_menu($id){ // funkcja generująca linki w menu
    global $pages;
    foreach ($pages as $klucz => $wartosc){
        echo
        '<li class="nav-item">
            <a class=\"nav-link js-scroll-trigger" href="?id='.$klucz.'">.$wartosc.</a>
        </li>' // ?id zmienne przekazywane za pomocą GET
    }
}
?>
