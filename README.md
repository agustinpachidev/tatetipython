# 🕹️​👾​ <b>Juego TATETI</b> 🕹️​👾​
Descripción del Juego <b>TA-TE-TI</b> en equipos
El juego comienza cargando los nombres de los jugadores de 2
equipos.
Luego se lanza un dado para determinar si el equipo <b>CRUZ</b> o el equipo <b>CIRCULO</b> empieza la partida.
Para cada equipo se debe generar una estructura que sirva para mantener el puntaje obtenido por cada jugador en las jugadas.

<b>De los equipos:<br>
● Id Jugador: número entero de 3 cifras<br>
● Nombre o Apodo del Jugador: no debe ser vacío<br>
● Puntaje Total: número entero mayor o igual a 0<br>
De las jugadas:<br>
● Nro de Partida: número entero mayor a 0<br>
● Id del Jugador 1: no debe ser vacío<br>
● Id del Jugador 2: no debe ser vacío<br>
● Ganador: no debe ser vacío<br>
● Cantidad de movimientos: número entero mayor a 0<br>

Reglas del Juego
1. Juegan 2 equipos (equipo Cruz y equipo Círculo) de entre 2 y 10 integrantes
cada uno. Los equipos deben tener la misma cantidad de integrantes.<br>
2. Una vez definidos los equipos, se determina aleatoriamente el enfrentamiento
entre todos los miembros de los equipos.<br>
3. Se tira un dado para ver qué equipo comienza.<br>
   
Partida
1. Se presenta el tablero que consiste en un cuadro de 3x3 vacío.
2. Cada jugador en su turno solo debe colocar su símbolo una vez y no debe ser
sobre una casilla ya jugada.
3. Gana, quien logre colocar 3 símbolos seguidos en cualquier dirección.
4. El ganador se lleva como puntaje la cantidad de movimientos que hizo para
ganar.
5. En caso de empate, se repite la jugada con los mismos jugadores. Si empatan 3
veces seguidas, cada jugador se lleva un punto.

<br>Ganador</br>
1. Una vez que se enfrentaron todos los jugadores, el equipo que más puntos tiene,
se proclama Ganador.
<br> Informe Ganador </br>
Luego de que termine la partida en el menu principal se puede consultar los puntajes:
| Jugadas       | Equipo Cruz | Equipo Círculo |
|---------------|-------------|----------------|
| Juan          | 3           | 4              |
| María         | 1           | 1              |
| Total:        | 4           | 5              |
| Ganador:      |             | Equipo Círculo |
