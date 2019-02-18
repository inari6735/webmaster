<?php
setlocale(LC_ALL, "pl_PL.UTF-8"); //LC_ALL - wszystkie komunikaty mają być wyświetlane i interpretowane jako komunikaty w jez polskim
date_default_timezone_set('Europe/Warsaw'); // strefa czasowa
error_reporting(E_All); // w jaki sposob php sie zachowuje w sposob wykrycia błędów E_All - wyswietla wszystkie bledy
ini_set('display_errors', 1); // wyswietla bledy 1 - wyswietla 0 - nie wyswietla
ini_set('log_errors', 1); // zapisuj błędy
ini_set('error_log', 'errorlog.txt'); // zapisuje błędy do pliku errorlog.txt
define('DINC', 'inc/'); // zadeklarowanie zmiennej ze ścieżką
require_once(DINC.'functions.php'); // requie - musisz dolaczyc inaczej aplikacja nie bedzie dzialac
include_once(DINC.'template.php'); // wgranie szablonu strony DINC - stała określająca ścieżkę do pliku
?>
