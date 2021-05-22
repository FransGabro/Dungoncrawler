# __Dungeon Crawler__
---

Ett sidoprojekt som inte är helt klart än.

* * *

># __HowTo__:
* Starta [Meny](/Menu.exe)
* Välj Skapa ny hjälte [[1]](####Menyval-1:-Skapa-ny-hjälte) eller Ladda sparat äventyr [[2]](####Menyval-2:-Ladda-sparat-äventyr)
* * *
>#### __Menyval 1: Skapa ny hjälte__
\
Skapa och namnge en ny [spelkaraktär](#Spelkaraktärer). \
Valbara karaktärer är: 

* [Riddaren](####Riddare)
* [Trollkarlen](####Trollkarl)
* [Tjuven](####Tjuv)\
\
Klicka på karaktären för en detaljerad beskrivning.

\
Efter att karaktären namngivits får du välja [storlek på fängelsehålan](#Fängelsehåla---Storlek-och-symboler).


* * *

>#### __Menyval 2: Ladda sparat äventyr__
\
Visa en lista över tidigare sparade spelkaraktärer.\
Välj en karaktär att fortsätta äventyret med!\
Därefter återvänder du till menyn och får välja [storlek på fängelsehålan](#Fängelsehåla---Storlek-och-symboler).
***
>### __Spelkaraktärer__
***

>#### __Riddare__
<table>
<thead>
<tr>
  <th>Attribut</th>
  <th>Värde</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Initiativ</td>
  <td>5</td>
</tr>
<tr>
  <td>Tålighet</td>
  <td>9</td>
</tr>
<tr>
  <td>Attack</td>
  <td>6</td>
</tr>
<tr>
  <td>Smidighet</td>
  <td>4</td>
</tr>
<tr>
  <td>Specialförmåga</td>
  <td>Sköldblock</td>
</tr>
</tbody>
</table>

__Sköldblock -__  Riddaren blockerar alltid första attacken
per strid med sin sköld, och behöver därför varken undvika eller ta någon skada.
>#### __Trollkarl__
<table>
<thead>
<tr>
  <th>Attribut</th>
  <th>Värde</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Initiativ</td>
  <td>6</td>
</tr>
<tr>
  <td>Tålighet</td>
  <td>4</td>
</tr>
<tr>
  <td>Attack</td>
  <td>9</td>
</tr>
<tr>
  <td>Smidighet</td>
  <td>5</td>
</tr>
<tr>
  <td>Specialförmåga</td>
  <td>Ljussken</td>
</tr>
</tbody>
</table>

__Ljussken -__ Trollkarlen kan göra monster blinda och har
därför alltid 80% chans att fly från strider.

>#### __Tjuv__

<table>
<thead>
<tr>
  <th>Attribut</th>
  <th>Värde</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Initiativ</td>
  <td>7</td>
</tr>
<tr>
  <td>Tålighet</td>
  <td>5</td>
</tr>
<tr>
  <td>Attack</td>
  <td>5</td>
</tr>
<tr>
  <td>Smidighet</td>
  <td>7</td>
</tr>
<tr>
  <td>Specialförmåga</td>
  <td>Kritisk träff</td>
</tr>
</tbody>
</table>

__Kritisk träff -__ Tjuven har 25% chans att göra dubbel skada varje gång
tjuven attackerar.

***
>### __Fängelsehåla -__ Storlek och symboler
\
Fängelsehålorna finns i tre olika storlekar:
<table>
<thead>
<tr>
  <th>Namn</th>
  <th>Storlek</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Liten</td>
  <td>4x4 rutor</td>
</tr>
<tr>
  <td>Mellan</td>
  <td>5x5 rutor</td>
</tr>
<tr>
  <td>Stor</td>
  <td>8x8 rutor</td>
</tr>
</tbody>
</table>

 \
Symboler:
* Spelaren = [P](Player)
* Väggar = [[#]](Wall)
* Ingången till fängelsehålan = [[>]](Entrence)
* Utgången från fängelsehålan = [[<]](Exit)
* Outforskat rum = [[.]](New_room)
* Uforskat rum =[X](Visited_room)
