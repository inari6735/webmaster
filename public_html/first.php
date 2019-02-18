<!DOCTYPE html>
<html lang="en">
<!--
   first.php
-->

<head>
<meta charset="utf-8" />
<title>bez nazwy</title>
<meta name="generator" content="Geany 1.32" />
</head>

<body>

<?php
echo "Witaj";
// zmienne globalne
$x = 5 * 5;
$txt = "działania";

function myTest(){
    global $x, $txt;
    if ($x > 20)
        echo "<p>Wynik ".$txt.": $x</p>";    
}

myTest();

?>

</body>

</html>
