<?php
setlocale(LC_ALL, "pl_PL.UTF-8"); //LC_ALL - wszystkie komunikaty mają być wyświetlane i interpretowane jako komunikaty w jez polskim
date_default_timezone_set('Europe/Warsaw'); // strefa czasowa
error_reporting(E_ALL); // w jaki sposob php sie zachowuje w sposob wykrycia błędów E_All - wyswietla wszystkie bledy
ini_set('display_errors', 1); // wyswietla bledy 1 - wyswietla 0 - nie wyswietla
ini_set('log_errors', 1); // zapisuj błędy
ini_set('error_log', 'errorlog.txt'); // zapisuje błędy do pliku errorlog.txt
define('DINC', 'inc/'); // zadeklarowanie zmiennej ze ścieżką
define('DBASE', 'db/');
require_once(DINC.'functions.php'); // require - musisz dolaczyc inaczej aplikacja nie bedzie dzialac
require_once(DBASE.'db.php');
$dbfile=DBASE.'db.sqlite';
$db=null;
$mode=PDO::FETCH_ASSOC;
init_baza($dbfile);
// db_exec($initstr);

$id='witam';
if (isset($_GET['id']))
    $id=trim($_GET['id']); // yta się czy w tablicy GET jest jakis klucz id, trim usuwa spacje - oczyszcza

include_once(DINC.'template.php'); // wgranie szablonu strony DINC - stała określająca ścieżkę do pliku
?>
