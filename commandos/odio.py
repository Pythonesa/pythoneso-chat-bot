import random

def odio_sin_blanco(nombre):
    frases_odio = [
        f"{nombre} odia... ¡espera! ¿Qué odias exactamente?",
        f"¡Vamos {nombre}! No puedes odiar al aire, dime qué es.",
        f"{nombre} odia... ¿el vacío? ¡Especifica!",
        f"¡Hey {nombre}! Odias tan fuerte que se te olvidó decir qué.",
        f"{nombre} odia... ¡el suspenso!",
        f"{nombre}, necesito más detalles. ¿Qué es eso que odias?",
        f"¡Ups! Parece que {nombre} olvidó lo que odia.",
        f"{nombre} odia no recordar lo que odia.",
        f"¡Vaya {nombre}! Tienes tanto odio que no sabes ni por dónde empezar.",
        f"{nombre} odia... ¡ayuda! Se me olvidó.",
        f"¿Odias el silencio, {nombre}? Porque no has dicho nada.",
        f"{nombre}, tu odio es tan misterioso que ni yo sé a qué te refieres.",
        f"{nombre} odia la indecisión. ¿Es eso?",
        f"Odiar sin objeto es como un café sin cafeína, {nombre}.",
        f"Si el odio fuera un deporte, {nombre} olvidó decirnos qué posición juega.",
        f"{nombre} odia cuando el bot no entiende.",
        f"{nombre}, ¿odias el misterio? Porque estás siendo muy misterioso.",
        f"{nombre}, estás siendo tan enigmático que hasta los acertijos están celosos.",
        f"{nombre} odia... ¡Dime rápido antes de que me de un cortocircuito!",
        f"El odio sin dirección es como {nombre} olvidando especificar.",
        f"{nombre}, tu odio está en modo incógnito.",
        f"{nombre} odia tanto que su odio se evaporó.",
        f"¿Eres un ninja del odio, {nombre}? Porque no veo nada.",
        f"{nombre} odia el suspense. ¡Oh, espera!",
        f"¡Cuidado {nombre}! Tu odio es tan silencioso que es casi inexistente.",
        f"{nombre} odia no terminar lo que empieza... como su frase.",
        f"{nombre}, tu odio está en stand-by.",
        f"{nombre} odia... ¡el cliffhanger!",
        f"Si tu odio fuera música, {nombre}, sería una nota sostenida... indefinidamente.",
        f"¡Oh no! {nombre} olvidó especificar y ahora está en el limbo del odio.",
        f"{nombre} odia... ¿esperar? Porque eso es lo que estoy haciendo.",
        f"Tu odio es un enigma, {nombre}.",
        f"{nombre} odia las interrupciones, justo como esta.",
        f"{nombre}, ¿tu odio es un juego de adivinanzas?",
        f"El odio de {nombre} es tan abstracto que podría ser una obra de arte.",
        f"{nombre} odia las listas interminables... como esta.",
        f"{nombre} odia los silencios incómodos.",
        f"Odio decirlo, {nombre}, pero te olvidaste de especificar.",
        f"{nombre} odia... ¡Oops! Error 404, odio no encontrado.",
        f"{nombre}, tu odio está en modo invisible.",
        f"¡Atención! {nombre} ha dejado su odio en blanco.",
        f"{nombre} odia las sorpresas... ¿es eso?",
        f"{nombre}, ¡termina tu frase! ¡No nos dejes con el suspenso!",
        f"El odio de {nombre} es tan profundo que no tiene palabras.",
        f"{nombre} odia los finales abiertos.",
        f"{nombre}, ¿estás jugando a las adivinanzas con tu odio?",
        f"{nombre} odia... ¡qué intriga!",
        f"El odio sin especificar de {nombre} es el nuevo misterio sin resolver.",
        f"{nombre} odia los puntos suspensivos...",
        f"Tu odio es como una caja de chocolates, {nombre}, nunca sabes qué te va a tocar.",
        f"{nombre} odia que su odio sea tan ambiguo.",
        f"¿Jugamos al juego del odio escondido, {nombre}?",
        f"{nombre}, tu odio es tan misterioso como el tesoro perdido.",
        f"{nombre} odia el drama... ¿o no?",
        f"El odio de {nombre} tiene más giros que una telenovela.",
        f"{nombre} odia los vacíos... en su frase.",
        f"{nombre}, tu odio es un thriller sin final.",
        f"Tu odio es tan enigmático, {nombre}, que necesitaríamos a Sherlock para descifrarlo.",
        f"{nombre}, ¿tu odio está jugando al escondite?",
        f"El odio de {nombre} es como una película muda: no dice nada.",
        f"{nombre} odia... inserte aquí.",
        f"Esperando las especificaciones de odio de {nombre}...",
        f"{nombre} odia... ¿el misterio?",
        f"{nombre}, ¿tu odio está en pausa?",
        f"{nombre} odia las frases a medias.",
        f"{nombre} odia la ambigüedad... creo.",
        f"Tu odio es una novela sin final, {nombre}.",
        f"{nombre} odia... ¿el desconcierto?",
        f"{nombre}, ¿tu odio es una ecuación sin resolver?",
        f"{nombre} odia las frases incompletas, justo como",
        f"¿Estás probando mi paciencia, {nombre}? ¡Especifica tu odio!",
        f"{nombre} odia... ¡termina la frase, por favor!",
        f"¿Estás jugando a ser misterioso con tu odio, {nombre}?",
        f"{nombre}, tu odio es una historia sin desenlace.",
        f"{nombre} odia... algo. ¡Eso es seguro!",
        f"El odio de {nombre} está en modo misterio.",
        f"{nombre}, ¡dinos qué odias antes de que estalle la curiosidad!",
        f"{nombre} odia... la intriga.",
        f"Tu odio es un laberinto, {nombre}.",
        f"{nombre}, tu odio se perdió en el camino.",
        f"{nombre} odia... ¿la incertidumbre?",
        f"¡Esperando instrucciones de odio de {nombre}!",
        f"{nombre} odia... las frases sin final.",
        f"{nombre}, ¿odias las preguntas sin respuesta?",
        f"{nombre} odia los misterios... como su propia frase.",
        f"{nombre}, ¿tu odio está de vacaciones?",
        f"{nombre}, ¿tu odio es un rompecabezas?",
        f"{nombre} odia... ¿las sorpresas?",
        f"{nombre}, completa el siguiente espacio: odia _______.",
        f"{nombre} odia... ¡déjanos adivinar! ¿El enigma?",
        f"{nombre}, ¿tu odio es un cliffhanger?",
        f"{nombre}, ¿odias los espacios en blanco?",
        f"{nombre} odia... ¡qué curioso! No nos lo ha dicho.",
        f"{nombre}, tu odio es un libro sin última página.",
        f"{nombre} odia... ¿dejarnos en vilo?",
        f"{nombre}, ¿estás probando un nuevo juego de odio?",
        f"El odio de {nombre} es como una serie sin temporada final.",
        f"{nombre}, ¿odias dejarnos con la duda?",
        f"{nombre} odia... ¡espera! Se perdió la señal.",
        f"{nombre} odia la indefinición.",
        f"{nombre}, tu odio es una novela de misterio.",
        f"{nombre} odia... ¡la sorpresa viene después!",
        f"¡{nombre}, lanza el dado y descubre qué odias!",
        f"El odio de {nombre} es un bestseller sin conclusión.",
        f"{nombre}, ¡tu odio es el mejor misterio de todos!"
    ]

    return random.choice(frases_odio)

def odio_auto(nombre):
    frases_autoodio = [
        f"{nombre}, ¡deja de ser tan duro contigo mismo!",
        f"{nombre}, todos tenemos días en los que somos nuestros peores críticos.",
        f"¡Hey {nombre}! Todos cometemos errores. ¡Relájate y sigue adelante!",
        f"El peor enemigo de {nombre} parece ser... {nombre}.",
        f"{nombre}, ¡eres increíble! Deja de dudar de ti mismo.",
        f"Todos tienen días malos, {nombre}, ¡pero tú eres genial!",
        f"{nombre}, recuerda que el autodesprecio no está de moda.",
        f"¡Vamos {nombre}! ¡Eres mejor de lo que piensas!",
        f"{nombre}, no hay necesidad de ser tan duro contigo mismo.",
        f"{nombre}, ¡dale un respiro a ese corazón grande que tienes!",
        f"¡Hey {nombre}! Tómate un momento para apreciar todas las cosas buenas que has hecho.",
        f"{nombre}, cada vez que dudas de ti mismo, piensa en todos tus logros.",
        f"Es difícil ser perfecto, {nombre}. ¡Pero estás haciendo un trabajo fantástico intentándolo!",
        f"{nombre}, recuerda: ¡Todos somos humanos y cometemos errores!",
        f"¡A todos nos pasa, {nombre}! Pero tú tienes la fortaleza para superarlo.",
        f"{nombre}, ¡dale un descanso a esa mente crítica y date un aplauso!",
        f"{nombre}, sé tu propio héroe y deja de ser tu propio crítico.",
        f"¡Eres más fuerte de lo que piensas, {nombre}!",
        f"{nombre}, cada vez que pienses en autocríticarte, piensa en todo lo que has superado.",
        f"El peor juez de {nombre} es {nombre}. ¡Deja de juzgarte tanto!",
        f"{nombre}, no te tomes tan en serio. ¡Eres increíble!",
        f"¡Hey {nombre}! Deja ese pensamiento negativo y abraza todo lo bueno en ti.",
        f"Todos tenemos inseguridades, {nombre}, pero tú eres más que ellas.",
        f"{nombre}, ¡enfoca esa energía en amarte más!",
        f"¡Tú puedes con esto y más, {nombre}!",
        f"{nombre}, cada vez que te sientas mal contigo mismo, piensa en todas las personas que te aprecian.",
        f"¡Tienes un gran potencial, {nombre}! ¡No lo olvides!",
        f"{nombre}, ¡eres una persona asombrosa!",
        f"{nombre}, sé amable contigo mismo. ¡Te lo mereces!",
        f"La vida está llena de altibajos, {nombre}, pero tú siempre brillas.",
        f"{nombre}, ¡déjame decirte algo! Eres una persona increíblemente valiosa.",
        f"El mayor desafío de {nombre} es {nombre}. ¡Pero sabemos que puedes superarlo!",
        f"¡Nadie es perfecto, {nombre}! ¡Y eso está bien!",
        f"{nombre}, deja de ser tu peor enemigo y conviértete en tu mejor aliado.",
        f"¡Hey {nombre}! Recuerda siempre ser amable contigo mismo.",
        f"{nombre}, ¿sabías que eres increíble? ¡Porque lo eres!",
        f"¡Deja la autocrítica a un lado y brilla, {nombre}!",
        f"{nombre}, no hay nadie como tú, ¡y eso es asombroso!",
        f"¡Eres capaz de lograr cosas increíbles, {nombre}!",
        f"{nombre}, la única opinión que importa es la que tienes de ti mismo. ¡Asegúrate de que sea positiva!",
        f"{nombre}, cada vez que dudes de ti mismo, recuerda todas las veces que superaste obstáculos.",
        f"El mundo es un lugar mejor con {nombre} en él.",
        f"{nombre}, eres fuerte, valiente y capaz. ¡Recuérdalo!",
        f"¡Tú eres tu activo más valioso, {nombre}!",
        f"Todos cometemos errores, {nombre}, pero eso no define quién eres.",
        f"{nombre}, eres más que tus inseguridades.",
        f"{nombre}, sé amable contigo mismo y el mundo te será amable.",
        f"Recuerda todas las veces que te levantaste y seguiste adelante, {nombre}.",
        f"{nombre}, ¡eres una estrella brillando en el universo!",
        f"Deja de dudar de ti mismo, {nombre}. ¡Confía en tu proceso!",
        f"{nombre}, cada desafío te hace más fuerte. ¡No te rindas!",
        f"¡Nunca dejes que una mala situación te haga dudar de ti mismo, {nombre}!",
        f"{nombre}, ¡creemos en ti y tú deberías hacerlo también!",
        f"Siempre hay un nuevo día para ser una mejor versión de ti mismo, {nombre}.",
        f"{nombre}, eres asombroso. ¡No lo olvides!",
        f"El viaje es largo, pero {nombre} tiene la fuerza para superarlo.",
        f"¡Nadie puede hacerte sentir inferior sin tu consentimiento, {nombre}!",
        f"Las palabras pueden herir, pero {nombre} tiene la resistencia para superarlo.",
        f"{nombre}, tú defines tu propio valor. ¡Y vales mucho!",
        f"¡El cielo es el límite, {nombre}! ¡No te pongas límites!",
        f"{nombre}, recuerda que eres amado y apreciado.",
        f"Cada día es una nueva oportunidad para amarte más, {nombre}.",
        f"{nombre}, la autocrítica puede ser útil, pero no te sumerjas en ella.",
        f"{nombre}, ¡tu luz brilla incluso en los días más oscuros!",
        f"¡Sigue adelante, {nombre}! ¡El mundo necesita tu brillo!",
        f"La vida puede ser difícil, pero {nombre} tiene la fortaleza para superar cualquier obstáculo.",
        f"{nombre}, confía en ti mismo y en tu viaje.",
        f"¡No te rindas, {nombre}! Eres más fuerte de lo que piensas.",
        f"¡Tú tienes el poder de cambiar y crecer, {nombre}!",
        f"{nombre}, cada desafío es una oportunidad para aprender y crecer.",
        f"{nombre}, eres una fuerza a tener en cuenta. ¡No lo olvides!",
        f"¡Afronta cada día con confianza y amor propio, {nombre}!",
        f"Las opiniones de los demás no definen tu valor, {nombre}.",
        f"{nombre}, cada vez que mires al espejo, ve la persona asombrosa que eres.",
        f"Tu viaje es único, {nombre}. ¡Valora cada paso!",
        f"{nombre}, eres más que suficiente. ¡Recuérdalo siempre!",
        f"El autodesprecio es temporal, pero tu esencia es eterna, {nombre}.",
        f"{nombre}, no hay nadie en el mundo exactamente como tú. ¡Eso es especial!",
        f"¡Cree en ti mismo y todo es posible, {nombre}!",
        f"{nombre}, eres valioso y mereces todo lo bueno que viene en tu camino.",
        f"¡Tú eres el héroe de tu propia historia, {nombre}!",
        f"{nombre}, la vida es un viaje, no un destino. ¡Disfruta cada momento!",
        f"El camino puede ser rocoso, pero {nombre} tiene el calzado adecuado para recorrerlo.",
        f"{nombre}, eres una inspiración para muchos. ¡Recuérdalo!",
        f"{nombre}, cada desafío es una oportunidad para mostrar tu fortaleza.",
        f"¡Tú tienes el poder de cambiar cualquier situación, {nombre}!",
        f"¡Recuerda siempre lo lejos que has llegado, {nombre}!",
        f"{nombre}, la vida es un desafío, pero tienes la habilidad para superar cualquier obstáculo.",
        f"{nombre}, el mundo es un lugar mejor gracias a ti."
    ]

    return random.choice(frases_autoodio)

def odio_dirigido(emisor, receptor):
    frases_hacia_otro = [
        f"{emisor} piensa que si {receptor} tuviera un poco más de cerebro, sería peligroso. Bueno, para sí mismo.",
        f"Según {emisor}, {receptor} es la prueba viviente de que se puede vivir sin cerebro.",
        f"{emisor} a veces se pregunta cómo {receptor} puede respirar y pensar al mismo tiempo.",
        f"{emisor} cree que {receptor} lleva una linterna solo para encontrar su propia sombra.",
        f"Si se pagara por no pensar, {emisor} dice que {receptor} sería millonario.",
        f"Para {emisor}, {receptor} es tan brillante que podría confundirse con un eclipse.",
        f"{emisor} piensa que si las ideas fueran rayos, {receptor} sería un desierto.",
        f"{emisor} dice que cada vez que {receptor} habla, demuestra que incluso la evolución tiene días malos.",
        f"En la opinión de {emisor}, {receptor} es el tipo de persona que vendería su coche por gasolina.",
        f"{emisor} cree que el zoo ha llamado, buscan a {receptor}.",
        f"{emisor} piensa que el genio se perdió en la familia de {receptor}.",
        f"{emisor} dice que si {receptor} estuviera dos veces más listo, seguiría siendo estúpido.",
        f"Para {emisor}, {receptor} es el tipo de persona que buscaría 'Google' en Bing.",
        f"{emisor} cree que el eco en la cabeza de {receptor} debe ser ensordecedor.",
        f"Según {emisor}, si la estupidez fuera crimen, {receptor} estaría cumpliendo cadena perpetua.",
        f"Para {emisor}, {receptor} es el regalo que sigue sin dar.",
        f"{emisor} piensa que si la ignorancia fuera una virtud, {receptor} sería canonizado.",
        f"{emisor} se pregunta si {receptor} siempre ha sido así o si ha tomado clases.",
        f"{emisor} dice que {receptor} tiene el toque mágico para complicar lo simple.",
        f"En la mente de {emisor}, {receptor} es la respuesta a '¿Qué pasaría si?... No, mejor no'.",
        f"{emisor} cree que si las tonterías fueran música, {receptor} sería una orquesta.",
        f"Para {emisor}, {receptor} es la razón por la que hay instrucciones en el champú.",
        f"{emisor} piensa que la rueda gira, pero el hámster ya murió en la cabeza de {receptor}.",
        f"{emisor} se pregunta si {receptor} ha sido siempre así de torpe o si es un talento adquirido.",
        f"Para {emisor}, el día que {receptor} nació, la naturaleza estaba de humor.",
        f"{emisor} piensa que {receptor} es el tipo de persona que necesita instrucciones para un libro de instrucciones.",
        f"{emisor} sospecha que {receptor} es la prueba de que los extraterrestres han experimentado con humanos.",
        f"Según {emisor}, el árbol genealógico de {receptor} es un círculo.",
        f"{emisor} dice que si la ignorancia tuviera voz, sonaría como {receptor}.",
        f"{emisor} cree que {receptor} ha sido dejado atrás por la evolución.",
        f"{emisor} dice que si la tontería fuera un superpoder, {receptor} sería invencible.",
        f"Según {emisor}, {receptor} ha estado a dieta toda su vida... pero sólo de conocimiento.",
        f"{emisor} piensa que {receptor} tiene menos contenido que un paquete de patatas fritas al vacío.",
        f"Para {emisor}, {receptor} es el tipo de persona que se ahogaría en una ducha.",
        f"{emisor} sospecha que si la estupidez tuviera calor, {receptor} sería el sol.",
        f"Si hubiera un concurso de ignorancia, {emisor} está seguro de que {receptor} ya se habría olvidado de inscribirse.",
        f"{emisor} dice que cada vez que {receptor} dice algo, una enciclopedia llora.",
        f"En el juego de la vida, {emisor} piensa que {receptor} aún está tratando de desembalar la caja.",
        f"{emisor} cree que si {receptor} tuviera un cerebro más, sería un simpleton.",
        f"Para {emisor}, {receptor} es la prueba de que se puede vivir sin cerebro.",
        f"{emisor} piensa que {receptor} podría olvidarse de respirar si no fuera un reflejo.",
        f"Según {emisor}, {receptor} es el único que necesita instrucciones para jugar a piedra, papel o tijera.",
        f"Para {emisor}, el sistema operativo de {receptor} claramente necesita una actualización.",
        f"{emisor} dice que si el sarcasmo fuera un lenguaje, {receptor} aún estaría aprendiendo el alfabeto.",
        f"{emisor} piensa que cada vez que {receptor} habla, un profesor pierde la esperanza.",
        f"Para {emisor}, la historia de la vida de {receptor} sería la guía perfecta de 'qué no hacer'.",
        f"{emisor} sospecha que {receptor} es el tipo de persona que necesita un manual para usar un lápiz.",
        f"{emisor} piensa que si la estupidez fuera combustible, {receptor} podría alimentar una ciudad entera.",
        f"Según {emisor}, {receptor} tiene el toque inverso de Midas: todo lo que toca se convierte en un desastre.",
        f"{emisor} dice que {receptor} es la razón por la que no podemos tener cosas bonitas.",
        f"Para {emisor}, {receptor} es como una nube gris en un día soleado: siempre aparece en el momento menos oportuno.",
        f"{emisor} cree que si {receptor} tuviera un punto válido, aún estaría tratando de sacarlo del embalaje.",
        f"{emisor} piensa que {receptor} podría ser superado en un debate por un tomate.",
        f"Según {emisor}, la única forma de que {receptor} se meta en un libro es si alguien lo dibuja allí.",
        f"{emisor} sospecha que {receptor} es el tipo de persona que pide una cita para ir al auto-servicio.",
        f"{emisor} dice que el único desafío que {receptor} podría ganar es uno de torpeza.",
        f"Para {emisor}, {receptor} es tan lento que podría competir con una tortuga en una carrera... y perder.",
        f"{emisor} piensa que {receptor} tiene más probabilidad de entender una conversación en un idioma inventado que una charla normal.",
        f"Si la falta de sentido común fuera un talento, {emisor} cree que {receptor} sería un prodigio.",
        f"Para {emisor}, {receptor} es la prueba viviente de que a veces el árbol genealógico no crece, simplemente se pudre.",
        f"{emisor} piensa que {receptor} es la razón por la que algunos animales se comen a sus crías.",
        f"Si la inteligencia fuera una enfermedad, {emisor} dice que {receptor} estaría inmune.",
        f"{emisor} cree que {receptor} es tan profundo como un charco en una acera.",
        f"Para {emisor}, {receptor} es la definición viviente de 'necesita supervisión'.",
        f"{emisor} piensa que {receptor} es el tipo de persona que lleva un salvavidas a la piscina de pelotas.",
        f"{emisor} se pregunta si {receptor} tiene su cerebro en modo avión todo el tiempo.",
        f"Si se hiciera una competencia de 'quién se olvida más rápido de algo', {emisor} está seguro de que {receptor} ya lo ha olvidado.",
        f"{emisor} piensa que si la inteligencia fuera azúcar, {receptor} sería una dieta.",
        f"Para {emisor}, cada vez que {receptor} da un paso adelante, de alguna manera termina cinco pasos atrás.",
        f"{emisor} dice que {receptor} es la persona que se pregunta por qué el televisor no funciona, solo para descubrir que nunca lo encendió.",
        f"Si fueran a hacer una película sobre errores, {emisor} está seguro de que {receptor} sería el protagonista.",
        f"{emisor} piensa que {receptor} tiene más oportunidad de volar al espacio con una mochila que de ganar un argumento lógico.",
        f"{emisor} dice que si la vida fuera un videojuego, {receptor} aún estaría tratando de pasar el tutorial.",
        f"Según {emisor}, {receptor} es el tipo de persona que necesitaría un manual para atarse los zapatos.",
        f"{emisor} piensa que {receptor} podría quedarse atascado en un columpio.",
        f"{emisor} se pregunta si {receptor} fue dejado atrás por extraterrestres como experimento con humanos.",
        f"Para {emisor}, {receptor} es como una señal de Wi-Fi: todos saben que está ahí, pero nunca funciona cuando se necesita.",
        f"{emisor} dice que {receptor} es el tipo de persona que se quedaría atrapado en un videojuego de escape."
    ]
    return random.choice(frases_hacia_otro)