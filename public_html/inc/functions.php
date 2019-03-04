<?php
$kom = []; // tablica komunikatów
$pages = array(
    'witam' => 'Aplikacja w PHP',
    'sqlcmd' => 'SQL',
    'csssel' => 'Selektory CSS',
    'formularz' => 'Formularz'
); // słownik, definicja trzech stron

function get_page_title($id){
    global $pages;
    if (array_key_exists($id, $pages))
        echo $pages[$id];
    else
        echo 'Aplikacja w PHP';
}

function get_kom(){
    global $kom;
    foreach ($kom as $k) // wydobadz wartosci po kolei i zapisuj w zmiennej k
        echo '<p>'.$k.'</p>';
}

function get_page_content($id){
    global $pages, $kom;
    if (file_exists($id.'.html')) // za pomocą tej fnkcji sprawdzamy czy plik istnieje na dysku
        include($id.'.html');
    else
        $kom[]='Brak strony: '.$id;
}

function get_menu($id){ // funkcja generująca linki w menu
    global $pages;
    foreach ($pages as $klucz => $wartosc){
        echo
        '<li class="nav-item">
            <a class=\"nav-link js-scroll-trigger" href="?id='.$klucz.'">'.$wartosc.'</a>
        </li>'; // ?id zmienne przekazywane za pomocą GET
    }
}

function clrtxt(&$el, $maxdl=20) {
    if(is_array($el)) {
        return array_map('clrtxt', $el);
    } else {
        $el = trim($el); // usuwanie niepotrzebnych spacji
        $el =substr($el, 0, $maxdl); // obcina ilość znaków
        if(get_magic_quotes_gpc()) $el=stripsslashes($el);
        $el=htmlspecialchars($el, ENT_QUOTES);
        return $el;
    }
}

?>
