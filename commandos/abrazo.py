import random

def obtener_abrazo_nadie(nombre):
    MENSAJES_SIN_NICK = [
        f"No puedes abrazar al aire, {nombre}. ¿Lo sabes, verdad?",
        f"¡Oye, {nombre}! No puedes simplemente abrazar a la nada. ¡Elige a alguien!",
        f"¿A quién intentas abrazar, {nombre}? ¡Dímelo!",
        f"Parece que {nombre} está practicando abrazos imaginarios.",
        f"¡Vamos, {nombre}! Elige a alguien real para ese abrazo.",
        f"{nombre} está intentando abrazar su imaginación.",
        f"Si intentas abrazar al aire, {nombre}, al menos hazlo con estilo.",
        f"{nombre}, ¡la nada también necesita abrazos!",
        f"¿Practicando tus técnicas de abrazo, {nombre}?",
        f"{nombre} intentó abrazar a alguien, pero parece que se volvió invisible.",
        f"¡Es un abrazo fantasma, {nombre}!",
        f"{nombre}, ¿estás abrazando a tus amigos imaginarios?",
        f"Creo que {nombre} está intentando inventar el abrazo aéreo.",
        f"¡Ups! Parece que {nombre} se olvidó de elegir a alguien para abrazar.",
        f"¿Estás bien, {nombre}? Pareces estar abrazando a un fantasma.",
        f"¡Abrazos invisibles cortesía de {nombre}!",
        f"{nombre}, ese abrazo parece un poco... vacío.",
        f"¿Un abrazo al aire, {nombre}? ¡Eso es nuevo!",
        f"Parece que {nombre} quiere abrazar a todo el chat de una vez.",
        f"¡Tal vez {nombre} vio algo que nosotros no vimos!"
    ]
    
    return random.choice(MENSAJES_SIN_NICK)

def obtener_abrazo_auto(nombre):
    MENSAJES_A_SI_MISMO = [
        f"Eh, {nombre}, es raro que te abraces a ti mism@. ¿Estás bien?",
        f"¿Necesitas un abrazo, {nombre}? ¡Aquí estamos para apoyarte!",
        f"¡A veces, todos necesitamos auto-abrazarnos, verdad {nombre}?",
        f"Parece que {nombre} necesita un poco de amor propio. ¡Eso está bien!",
        f"{nombre}, ¡darte un auto-abrazo es una gran forma de mostrarte amor propio!",
        f"¡Es bueno amarse a uno mismo, {nombre}!",
        f"¡Vaya! {nombre} se está dando un poco de cariño propio.",
        f"Todos necesitamos un abrazo de vez en cuando, ¿verdad {nombre}?",
        f"{nombre} está mostrando cómo amarse a uno mismo.",
        f"Un poco de amor propio nunca viene mal, ¿eh {nombre}?",
        f"¡Eso es un poco solitario, {nombre}! ¿Quieres que te demos un abrazo grupal?",
        f"{nombre}, recuerda que siempre puedes contar con el chat para recibir abrazos.",
        f"¡No te preocupes, {nombre}! Aquí todos te queremos y te abrazamos virtualmente.",
        f"¿Todo está bien, {nombre}? ¡Estamos aquí para ti!",
        f"Parece que {nombre} está practicando el arte del auto-abrazo.",
        f"{nombre} muestra que a veces, todo lo que necesitas es darte un poco de cariño a ti mism@.",
        f"¡Hey, {nombre}! Siempre puedes pedir un abrazo aquí.",
        f"{nombre}, abrazarte a ti mism@ es un recordatorio de que eres amado.",
        f"¡Eso es amor propio, {nombre}!",
        f"{nombre} sabe que a veces, tienes que ser tu propio héroe."
    ]

    return random.choice(MENSAJES_A_SI_MISMO)

def obtener_abrazo(abrazador, abrazado):
    MENSAJES_DE_ABRAZO = [
        f"¡{abrazador} da un fuerte abrazo a {abrazado}!",
        f"{abrazador} envuelve a {abrazado} en un cálido abrazo.",
        f"{abrazado}, ¡{abrazador} te ha dado un abrazo sorpresa!",
        f"{abrazador} y {abrazado} comparten un tierno momento de abrazo.",
        f"¡Qué lindo ver a {abrazador} abrazando a {abrazado}!",
        f"{abrazador} abraza a {abrazado} como si no hubiera un mañana.",
        f"¡Abrazo alerta! {abrazador} ha atrapado a {abrazado} en un abrazo.",
        f"¡{abrazado}! {abrazador} te ha dado un abrazo especial.",
        f"¡Es un abrazo de oso de {abrazador} a {abrazado}!",
        f"{abrazador} corre hacia {abrazado} y le da un abrazo épico.",
        f"{abrazador} y {abrazado} están en modo abrazo total.",
        f"¡Es un abrazo en equipo entre {abrazador} y {abrazado}!",
        f"{abrazador} se acerca sigilosamente y... ¡abraza a {abrazado}!",
        f"{abrazador} da un abrazo cariñoso a {abrazado}. ¡Qué dulce!",
        f"{abrazado}, parece que {abrazador} te extrañaba. ¡Abrazo!",
        f"¡Momento de abrazo! {abrazador} y {abrazado} están en ello.",
        f"¡{abrazador} ha elegido a {abrazado} para su abrazo del día!",
        f"{abrazador} y {abrazado}, demostrando que los abrazos son la mejor medicina.",
        f"¡Alerta de ternura! {abrazador} está abrazando a {abrazado}.",
        f"Es un abrazo de amistad entre {abrazador} y {abrazado}. ¡Hermoso!",
        f"¡{abrazador} lanza un abrazo aéreo a {abrazado}!",
        f"¡{abrazado}, {abrazador} ha decidido que mereces un super abrazo!",
        f"¡Nada como un abrazo entre amigos! Bien hecho, {abrazador} y {abrazado}.",
        f"¡Es un abrazo mágico de {abrazador} a {abrazado}!",
        f"{abrazador} ha atrapado a {abrazado} en un abrazo inesperado.",
        f"{abrazador} da un abrazo de osito a {abrazado}. ¡Tan reconfortante!",
        f"{abrazador} y {abrazado} demuestran que los abrazos hacen el día mejor.",
        f"¡{abrazador} abraza a {abrazado} en un momento perfecto!",
        f"{abrazador} le da a {abrazado} el abrazo que tanto necesitaba.",
        f"¡Momento épico! {abrazador} da un abrazo poderoso a {abrazado}.",
        f"¡Qué momento! {abrazador} ha dado el abrazo perfecto a {abrazado}.",
        f"{abrazador} y {abrazado}, compartiendo un momento abrazo.",
        f"¡Es un abrazo lleno de energía de {abrazador} a {abrazado}!",
        f"{abrazador} abraza a {abrazado} con toda su fuerza. ¡Qué pasión!",
        f"¡{abrazador} sorprende a {abrazado} con un abrazo desde atrás!",
        f"¡Es un abrazo lleno de sonrisas entre {abrazador} y {abrazado}!",
        f"{abrazador} da un abrazo super especial a {abrazado}.",
        f"¡Abrazo a la vista! {abrazador} y {abrazado} están en ello.",
        f"¡{abrazador} abraza a {abrazado} levantando el espíritu del chat!",
        f"{abrazador} le da un abrazo reconfortante a {abrazado}.",
        f"¡{abrazado}, parece que {abrazador} realmente quería darte un abrazo!",
        f"{abrazador} ha decidido que {abrazado} merece un gran abrazo.",
        f"¡Momento especial! {abrazador} y {abrazado} comparten un abrazo mágico.",
        f"{abrazador} se lanza en un abrazo aventurero hacia {abrazado}.",
        f"El amor está en el aire: ¡{abrazador} abraza a {abrazado}!",
        f"{abrazador} da un abrazo relajante a {abrazado}. ¡Justo lo que necesitaban!",
        f"¡Qué tierno! {abrazador} da un abrazo suave a {abrazado}.",
        f"{abrazado}, ¡siente el calor del abrazo de {abrazador}!",
        f"Es un abrazo lleno de felicidad entre {abrazador} y {abrazado}.",
        f"¡{abrazador} ha dado un abrazo inolvidable a {abrazado}!",
        f"¡Alerta de amistad! {abrazador} y {abrazado} están compartiendo un abrazo.",
        f"{abrazador} da un abrazo lleno de amor a {abrazado}. ¡Qué dulce!",
        f"¡Momento memorable! {abrazador} abrazando a {abrazado}.",
        f"¡Es un abrazo lleno de risas entre {abrazador} y {abrazado}!",
        f"{abrazador} y {abrazado} comparten un abrazo lleno de alegría.",
        f"¡{abrazador} le da a {abrazado} un abrazo que ilumina el día!",
        f"¡Es un abrazo encantador de {abrazador} a {abrazado}!",
        f"{abrazador} da un abrazo a {abrazado} lleno de buenas vibras.",
        f"{abrazador} y {abrazado}, ¡compartiendo un abrazo que vale oro!",
        f"¡{abrazador} da un abrazo sorpresa a {abrazado}!",
        f"{abrazador} y {abrazado}, ¡celebrando con un gran abrazo!",
        f"¡{abrazador} da un abrazo que dura una eternidad a {abrazado}!",
        f"{abrazador} y {abrazado}, ¡demostrando que un abrazo dice más que mil palabras!",
        f"¡Es un abrazo legendario entre {abrazador} y {abrazado}!",
        f"{abrazador} da el abrazo perfecto a {abrazado}. ¡Bella conexión!",
        f"¡{abrazador} abraza a {abrazado} como nunca antes!",
        f"{abrazador} y {abrazado}, ¡el dúo dinámico del abrazo!",
        f"¡{abrazador} lanza un abrazo cariñoso a {abrazado}!",
        f"¡{abrazador} y {abrazado} crean el momento abrazo perfecto!",
        f"{abrazador} y {abrazado}, ¡abrazándose como campeones!",
        f"¡{abrazador} da un abrazo que podría derretir corazones a {abrazado}!",
        f"{abrazador} y {abrazado} compartiendo un abrazo que todos envidiarían.",
        f"¡Es un abrazo maratón entre {abrazador} y {abrazado}!",
        f"{abrazador} abraza a {abrazado} con toda la felicidad del mundo.",
        f"¡{abrazador} da un abrazo a {abrazado} que se siente como una suave brisa!",
        f"¡{abrazador} y {abrazado}, haciendo del chat un lugar más cálido con ese abrazo!",
        f"Es un abrazo lleno de risas y alegría entre {abrazador} y {abrazado}.",
        f"{abrazador} da un abrazo a {abrazado} que siente como un rayo de sol.",
        f"¡{abrazador} y {abrazado}, compartiendo un abrazo que dura toda una vida!",
        f"{abrazador} y {abrazado}, demostrando que un abrazo puede cambiar el día.",
        f"¡{abrazador} da un abrazo a {abrazado} que siente como una suave melodía!",
        f"¡Es un abrazo que todos querrían! Bien hecho, {abrazador} y {abrazado}.",
        f"{abrazador} y {abrazado}, ¡el dúo perfecto para un abrazo!",
        f"¡Es un abrazo que se siente como un abrazo! {abrazador} a {abrazado}.",
        f"{abrazador} da un abrazo a {abrazado} que todos recordarán.",
        f"¡{abrazador} y {abrazado}, creando recuerdos con ese abrazo!",
        f"¡{abrazador} da un abrazo a {abrazado} que ilumina el chat!",
        f"{abrazador} y {abrazado}, unidos por un abrazo inquebrantable.",
        f"¡{abrazador} da un abrazo a {abrazado} que siente como un cuento de hadas!",
        f"{abrazador} y {abrazado}, ¡la combinación perfecta para un abrazo perfecto!",
        f"¡Es un abrazo que vale la pena recordar entre {abrazador} y {abrazado}!"
    ]
    
    return random.choice(MENSAJES_DE_ABRAZO)
