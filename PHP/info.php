<h1>Pierwsza strona w PHP</h1>
<h2>Informacje na temat wersji PHP</h2>

<?php // znacznik otwierający skrypt php
  // phpinfo();
  print_r($_GET);
?>
<!-- znacznik zamykający skrypt -->

<form name="formularz" id="formularz">
  <table class="table">
    <tr>
      <td><label for="imie">Imię:</label></td>
      <td><input type="text" name="imie" value=""><br></td>
    </tr>
    <tr>
      <td><label for="nazwisko">Nazwisko:</label></td>
      <td><input type="text" name="nazwisko" value=""></td>
    </tr>
  </table>

  <fieldset>
    <legend>Wybierz płeć</legend>
    <input type="radio" name="gender" value="m" checked>Male<br>
    <input type="radio" name="gender" value="k">Female<br>
    <input type="radio" name="gender" value="i">Other
  </fieldset>

  <fieldset>
    <legend>Wybierz pojazd</legend>
    <input type="checkbox" name="vehicle1" value="Bike"> I have a bike<br>
    <input type="checkbox" name="vehicle2" value="Car"> I have a car
  </fieldset>

  <select name="cars">
   <option value="volvo">Volvo</option>
   <option value="saab">Saab</option>
   <option value="fiat">Fiat</option>
   <option value="audi" selected>Audi</option>
  </select>

  <select name="cars2" multiple>
   <option value="volvo">Volvo</option>
   <option value="saab">Saab</option>
   <option value="fiat">Fiat</option>
   <option value="audi" selected>Audi</option>
  </select>
  <br>
  <textarea name="message" rows="10" cols="30">Mój kod</textarea>
  <br>
  <input type="submit" name="" value="Prześlij">
  <input type="reset" name="" value="Reset">
</form>
