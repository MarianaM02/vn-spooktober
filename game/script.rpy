# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define player = Character(["playerName"], color="#c3acce")
define grandpa = Character("Abuelo", color="#dfd9e2")
define madreMonte = Character("Inaru", color="#2a7f62")
define pombero = Character("Har", color="#89909f")
define calchona = Character("Fisa", color="#538083")
define silbon = Character("Wiija", color="#ade1e5")


# El juego comienza aquí.

label start:

    $ playerName = renpy.input("Mi nombre es..", default = "Alba", length=12)
    $ playerName = playerName.strip()

    if playerName == "":
        $ playerName = "Alba"


    centered "30 de Octubre\n4:00pm"
    playerName "¡Phew! ¡Ya era hora!"
    playerName "Después de un viaje tan largo..."
    playerName "...finalmente estoy de vuelta."
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.
    scene bg room
    "No había visitado el pueblo de mamá desde hace dos veranos, justo cuando el abuelo cayó enfermo."
    "Han sido unos meses muy tristes, y mamá no ha sido la misma desde que se enteró."
    "Pero estoy segura que venir le hará bien."

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.
    # show eileen happy
    playerName "Ahora... La casa del abuelo estaba al final de la calle..."
    playerName "¡Whoa! Siempre olvido lo grande que es."
    "Mamá me dijo que pidió que la limpiaran antes que llegáramos, ¡Cuanto trabajo!"
    "Mis padres estaban muy ocupados para venir hoy, pero yo no puedo perderme el festival de Halloween."
    "¡Siempre fue mi preferida!"
    "Todavía es un poco temprano, así que podría investigar un poco antes de volver a salir."
    playerName "¿Dónde voy?"
    menu:
        "Examinar cocina":
            pass

    playerName "Está mucho más limpia de lo que recuerdo..."
    "Cuando era pequeña, solía ayudar al abuelo a hacer alfajores. Hacíamos un desastre, ¡pero quedaban deliciosos!"
    menu:
        "Examinar sala":
            pass

    "Está lleno de fotos de nosotros. Mamá y el abuelo siempre habían sido muy compañeros."
    "Pero mamá dejó el pueblo a los 18 para irse a estudiar y jamás volvió."
    "El abuelo nunca dijo nada, y siempre que volvían a verse era como si el tiempo no hubiera pasado."
    "Me pregunto si realmente eso fue difícil para ellos..."
    menu:
        "No quiero investigar mas":
            pass

    playerName "Yaaawwwwnn..."
    playerName "Creo que mejor voy a descansar un poco."
    "Esta casa posee muchos recuerdos... Tanto para mí como para mi mamá."
    "Me pregunto como reaccionará ella cuando venga mañana..."

    # Fade out
    centered "\"[playerName]...\""
    centered "\"No le creas.\""
    centered "\"No lo busques.\""
    centered "\"Está aquí.\""
    centered "\"Esperándote...\""
    #Fade in

    pause
    centered "30 de Octubre.\n8:00pm"
    playerName "¡Esa fue una gran siesta!"
    playerName "¡Será mejor que ya vuelva a salir antes de que se haga muy tarde."
    playerName ". . ."
    "Que frío hace aquí dentro..."
    "Debo recordar prender la calefacción cuando vuelva."

    playerName "Vamos al pueblo!"
    playerName "¡Wow! Hay muchísima más gente de la que recordaba."
    "Todos los años, el pueblo hace un gran festival por Halloween. Los preparativos empiezan muchas semanas antes, y dura dos días."
    "Pero siempre lo mejor es durante la noche del 31: hay danzas, disfraces y muchísima comida."
    "El abuelo me contó que cuando mamá era adolescente, ponía a coserse la ropa desde un mes antes, y salía a las calles con sus amigos cantando."
    "Siempre se maquillaba de maneras espeluznantes y todo el mundo quedaba encantado. Es la fiesta turística del pueblo."
    "Mamá siempre contaba que desde hacía siglos, el pueblo tenía una gran conexión con el Otro Mundo"
    "...y mientras conociéramos nuestras raíces y quienes éramos, nada podía hacernos daño."
    "Ella dice que se sentía más cómoda como un monstruo entre humanos. Me encantaría volverla a ver así."


    centered "30 de Octubre.\n11:55pm"
    playerName "Phew... Estoy agotada, ha sido realmente divertido!"
    playerName "Que suerte que aquí la celebración es hasta mañana, seguro mamá lo disfrut--"
    playerName "¿Eh?"
    "Veo la luz saliendo de la puerta entreabierta, las luces del resto de la casa se encuentran apagadas"
    playerName "¿Que... Es eso...?"
    "Viene de la habitación de mi abuelo... No he estado allí desde hace años."
    menu:
        "Acercarse":
            pass

    playerName "¿Hola?"
    playerName ". . ."
    "Que extraño, nadie me dijo que habría alguien aquí, ¿Será una broma?"
    # [Empiezan a oirse susurros, la luz se ve saliendo desde la puerta entreabierta
    menu:
        "Entrar":
            pass

    # "Se abre la puerta, la habitación está vacía, se ve la cama, y junto a ella, la caja de donde sale esa luz."
    # "Hay más susurros, el ambiente es cada vez más tenso"
    "Tal y como recordaba este lugar... Es como si el abuelo jamás se hubiese ido. Pero... Esa caja..."
    menu:
        "Acercarse":
            pass

    playerName ". . ."
    # "Ambiente más y más abrumador, desconectando a player del exterior"
    "La recuerdo, mi abuelo nunca me dejaba tocarla. Me pregunto..."
    menu:
        "Abrir":
            pass

    # Se abre la caja, se ven luces salir
    # Siguiente

    # Pantalla toda en blanco.
    playerName "AGHHH!"
    # Tinnitus?
    # Siguiente

    # personaje ???
    madreMonte "Vaya..."
    menu:
        "\"¿Quien eres?\"":
            pass

    madreMonte "¿Quien soy yo? ¿Que no te han enseñado nada?"
    # Cambia a Inaru
    madreMonte "Me llamo Inaru, soy una protectora de los bosques, por supuesto!"
    madreMonte "O lo era, hasta que quedé bajo las órdenes del Maestro, he vivido en esta caja por cuarenta largos años!"
    playerName "¿¡Cómo!? ¿¡Mi abuelo es tu maestro!?"
    madreMonte "Pues parece que sí, tanto yo como los otros estábamos bajo sus ord-"
    madreMonte ". . ."
    madreMonte "¿¡Qué hiciste!? ¿¡Fuíste tú!?"
    madreMonte "¡No debiste haber hecho eso, niña tonta!"
    madreMonte "... Si yo estoy afuera, quiere decir que los demás también."
    menu:
        "\"¿¡Que está pasando!?\"":
            pass

    madreMonte "Miralo tu misma"
    # ((Paneo a la caja, con los cuatro objetos inanimados, sin luz))
    madreMonte "Estos son Vestigios."
    madreMonte "Reliquias que tu abuelo perfeccionó para capturar a las Leyendas que habitan este mundo."
    madreMonte "Una Leyenda puede ser cualquier cosa: un espíritu, un monstruo, un objeto poseído, cualquier criatura atrapada en una época que no le pertenezca."
    madreMonte "Tu abuelo ha dedicado su vida a capturar y atrapar sus Leyendas, al igual que su padre antes que él."
    madreMonte "Hasta ahora, tu familia ha podido capturar a tres Leyendas: Ellos son el Silbón, la Calchona y el Pombero." 
    madreMonte "Criaturas que vagaban el mundo causando terror antes de que tú las liberaras nuevamente." 
    madreMonte "Ahora es tu responsabilidad encontrarlas y capturarlas de nuevo dentro de los Vestigios."
    menu:
        "\"¿Y cómo voy a hacer eso?\"":
            pass

    madreMonte "Tendrás que convencerlos, por supuesto!"
    madreMonte "No estoy esperando que puedas derrotarlos y forzarlos dentro del Vestigio, no pareces muy fuerte."
    madreMonte "Las Leyendas son criaturas suspicaces, si sienten que eres una amenaza, será más difícil encontrarlos."
    madreMonte "Ahí tu corres ventaja, van a subestimarte."
    playerName ". . ."
    madreMonte "Tu familia usó un hechizo para encerrarlos, si escaparon, es porque éste se ha debilitado, pero aún tienes la oportunidad de volver a darle fuerza."
    madreMonte "Cada Leyenda tiene una marca, si tienes la sangre de tu abuelo, usar un poco de tu sangre sobre la marca será suficiente para devolver su alma a los Vestigios."
    playerName "Mi sangre..." 
    playerName "Nada tiene sentido, ¿por qué mi abuelo nunca nos lo diría?"
    madreMonte "Te veo preocupada"
    menu:
        "\". . .\"":
            jump info
   
label info:
    madreMonte "¿Qué quieres saber?"
    menu:
        "Madre Monte":
            madreMonte "Yo soy un espíritu protector de los bosques. Estaba perdida hasta que tu abuelo me encontró."
            madreMonte "Él me salvó de morir cegada por la ira y el rencor, y desde entonces, juré estar siempre a su lado."
            madreMonte "Es por eso que tienes que conseguir que las otras Leyendas vuelvan a sus Vestigios."
            madreMonte ""
            jump info
        "Pombero":
            madreMonte "El Pombero es un duende, muy peludo y del color de la noche. Con los humanos es el más impredecible, pero posee un gran cariño y respeto por los bosques."
            madreMonte ""
            jump info
        "Silbón":
            madreMonte "El silbón es un espectro con la forma de un joven, le encanta silbar y tiene un particular odio hacia los hombres."
            madreMonte ""
            jump info
        "Calchona":
            madreMonte "La calchona solía ser una bruja, pero sufrió una maldición por sus actos. Ahora es condenada a vagar el mundo sin poder volver a su forma humana."
            madreMonte ""
            jump info
        "Abuelo":
            madreMonte "Tu abuelo fue un hombre muy hábil e inteligente, ha dedicado su vida entera a buscar y capturar Leyendas que podrían ser dañinas para los humanos."
            madreMonte "Él solía hablar con nosotros, lo hizo hasta sus últimos días..."
            madreMonte ""
            jump info
        "Estoy bien":
            jump preMission

label preMission:
    madreMonte "Bueno, entonces ya está decidido."
    madreMonte "Luego de vivir tantas décadas con ellos, puedo sentirlos."
    "La Madremonte camina hacia un mapa del Pueblo colgado en la pared."
    # Paneo al mapa con tres marcas
    madreMonte "Al Silbón le gusta estar entre gente, así que es probable que lo encuentres caminando en el pueblo. "
    madreMonte "Si hay un lugar donde seguro el Pombero iría primero, son los bosques."
    madreMonte "Y la Calchona... Debe estar buscando algo que comer, así que seguramente la encontrarás en los campos."
    madreMonte "Hay mucho terreno por cubrir y poco tiempo-"
    "Sabía que había un gran peligro por delante."
    "Al mismo tiempo, sentía que algo me empujaba hacia ello. Dentro mío, estaba segura que la Madre Monte no me mentía, y que mi abuelo estaba fuertemente conectado a esto."
    madreMonte "Se que es mucha información, y no tenemos mucho tiempo."
    playerName "Hay mucha gente que corre peligro, ¿No causarán el caos?"
    madreMonte "Los humanos no ven nada que no quieran ver, y las Leyendas no se hacen notar a menos que quieran ser vistas."
    madreMonte "Ahora, ellos también están recobrando sus fuerzas, pero no les llevará mucho hasta que empiecen a moverse nuevamente."
    "Me pregunto si realmente puedo confiar en ella de la manera que ella espera que lo haga..."
    madreMonte "¿Estás segura?"
    playerName "!!"
    "Su voz me saca de mis pensamientos, y un fuerte sentimiento de inseguridad me invade de repente."
    "Algo que no estaba allí un momento antes."
    "¿Es esto lo que pueden causar las Leyendas solo con su voz? ¿Miedo, dudas?"
    "O quizá también... Protección y seguridad."
    "La Madre Monte me mira impaciente. Yo tardo unos momentos antes de hablar de nuevo."
    playerName "¿De verdad no hay nadie más que pueda resolver esto? Mamá vendrá mañana y-"
    madreMonte "Mañana ya será demasiado tarde. No, lo siento, si tú no lo haces, nadie podrá."
    playerName "¿Por qué no podemos llamar a la policía?"
    madreMonte "Nada de lo que hagan podrá resultar. Solo puedes tú. Solo tú tienes la sangre de tu abuelo."
    playerName "¿Cómo?"
    "En un instante, la Madre Monte sujetó mi mano."
    madreMonte "Cierra los ojos."
    "En un reflejo, cerré los ojos justo cuando sentí la piel de mi palma abrirse."
    playerName "Agh!"
    "El líquido comenzó a brotar, mojando mi mano."
    "Los dedos rígidos de la Madre Monte pasaron sobre la palma."
    "Cuando abrí los ojos, mi mano estaba seca, y las yemas de la madre monte brillaban de un color carmesí."
    madreMonte "Para encerrar nuevamente a las Leyendas, necesitas encontrar el lugar donde tu abuelo ha puesto el hechizo y debes marcarlo con tu sangre."
    madreMonte "Yo puedo forzar a dos de las Leyendas de nuevo dentro de su Vestigio usandola tambien, pero enfrentarme a los tres podría matarme."
    "Su mano se posó sobre mi mejilla, podía sentir el calor a través de su palma."
    madreMonte "Lo siento, hubiera querido que las cosas fueran diferentes. Aún así, la última decisión la tienes tú."
    madreMonte "¿Deseas ayudarme a salvar lo que tu abuelo ha intentado proteger?"
    menu:
        "\"Sí, voy a ayudarte.\"":
            jump missionAccepted
        "\"No! De ninguna manera!\"":
            jump missionDenied

label missionDenied:
    playerName "No puedo... No soy la persona que buscas."
    madreMonte "Vaya, que decepción."
    madreMonte "Pero supongo que no te puedo forzar."
    "Me di vuelta, y caminé hacia la puerta."
    madreMonte "Pero aún así puedo usarte."
    playerName "!!!!"
    "No llegué a voltear, mi cuerpo entumecido solo atisbó a mirar hacia abajo, donde las ramas salían de mi estómago."
    "Luego... Oscuridad."
    "F en el chat"
    "THE END (Gracias por nada)"
    "Bad Ending :("
    # Finaliza el juego:
    return

label missionAccepted:
    madreMonte "Gracias... Sé que esto no es fácil. Prometo ayudarte en todo lo que pueda. Nombra una Leyenda y yo me encargaré de lo demás."
    menu:
        "Calchona":
            jump calchonaRoute
        "Pombero":
            jump pomberoRoute
        "Silbón":
            jump silbonRoute

            
label calchonaRoute:
    default goodAnswersCalchona = 0
    
    centered "00:30am\nLos Campos"
    "Siempre me gustó venir aquí... De pequeña, los vecinos me dejaban acariciar a los animales y darles de comer."
    "Ahora, estoy buscando a una bruja, y parece ser el peor lugar del mundo."
    "El viento soplaba con suavidad, y con él, lograba escuchar los susurros de las ovejas que dormían dentro de sus corrales. Parecía que cotilleaban entre ellas en sueños."
    playerName "Nghh.."
    playerName "!!!"
    "Unos gemidos forzaron que me detuviera. Mi cuerpo se tensó, mientras escaneaba cerca de los corrales."
    "Allí la vi, una figura encorvada que forcejeaba para entrar a uno de los corrales"
    "Pobre oveja, no debieron notar que quedó afuera."
    playerName ". . ."
    playerName "!!!"
    "Al ser iluminada bajo la luz de la Luna, pude ver un rostro humano, el cual se inclinaba para pasar la cabeza entre los postes del corral y alcanzar el bebedero."
    playerName "AH!"
    # personaje ???
    calchona "?"
    "Apenas me oyó, la oveja volteó a verme, y su espalda se irguió para levantarse en las patas traseras. Sus ojos brillantes se posaron en mí, dorados y muertos."
    "¿Qué hago?"
    "¿Qué hago?"
    "¿Qué hago?"
    "Puedo verla tensar sus manos, y sus ojos se mueven lejos de mí. Si se escapa, podría estar perdiendo la única oportunidad que tengo de ayudar al abuelo."
    playerName "AGUA!"
    calchona "..."
    "La criatura se volvió a verme"
    playerName "Te puedo ayudar..."
    "Me fui acercando despacio, mis ojos en la criatura. Ella me observaba de regreso, dando unos pasos atrás. Pero no se alejaba."
    "Una vez llegué a la valla, puse las dos manos sobre ella y le trepé para llegar al otro lado. Las ovejas seguían dormidas. La criatura me miraba expectante."
    "Mi mano se extendió para abrir el grifo y el agua empezó a correr. En un instante, la criatura puso ambas manos dentro del corral y bajo el agua y luego se las llevó al hocico, bebiendo desesperadamente."
    "Sus ojos nunca me abandonaban."
    calchona "Gracias."
    calchona "¿Qué estás haciendo aquí?"
    "Vaya, no me lo esperaba."
    "Aún así, me miraba con desconfianza. No puedo decirle la completa verdad, o sino se irá. Me pregunto si se dará cuenta que le estoy mintiendo..."
    # Siguiente

    playerName "Yo..."
    menu:
        "\"Te estaba buscando.\"":
            $ goodAnswersCalchona += 1
            playerName "Te estaba buscando. En el pueblo, se oyen historias sobre leyendas que vagan en esta noche, pensé que si comenzaba a explorar, podría encontrar alguna. Lamento haberte asustado."
            calchona "Los campesinos jamás hablan conmigo. Pero siempre me dejan algo de beber. Jamás había estado aquí antes."
            "Puedo ver como comienza a relajarse, y en respuesta, siento como mis hombros bajan a la par."
        "\"Me escapé del festival.\"":
            playerName "Me escapé del festival. Había mucho estruendo, y quería ver como se encontraban los animales." 
            playerName"Vengo a este pueblo desde que soy pequeña y siempre he tenido una conexión con ellos. Cuando me acerqué, pensé que eras una oveja que se había escapado del corral."
            calchona "No serías la primera. Es normal teniendo en cuenta como... Luzco."
            "Puedo notar que aún me mira con desconfianza, pero no hace ningún intento de salir corriendo. En respuesta, siento como mis músculos se relajan."
 
    
    playerName "Si tienes hambre, puedo ayudarte a buscar algo para comer!"
    calchona "..."
    playerName "Soy [playerName] ¿cuál es tu nombre?"
    calchona "..."
    # Cambia a Fisa
    calchona "Fisa."
    playerName "Bueno, entonces es un placer conocerte! Ven, vamos a buscar algo para comer."
    "Mientras me alejaba, me puse a pensar acerca de como le estaba yendo a Inaru..."
    "Mi mano comenzaba escocer al recordar todo lo que conllevaba esto, y en el problema en que me había metido."
    "¿Por qué abrí esa caja?"
    # (recuerdo)
    centered "No lo veas"
    centered "No lo escuches"
    "¿Quién era esa voz?"
    calchona "No tendrías que haber venido."
    playerName "?!"
    calchona "Los campos son peligrosos, en especial por la noche. No sabes lo que puede haber aquí."
    playerName "Podría decir lo mismo de tí."
    calchona "..."
    calchona "Peras."
    playerName "?"
    "Fisa levanta un brazo, señalando a los árboles que contenían una gran cantidad de peras maduras."
    playerName "¡Bingo!"
    "Poniéndome en puntas de pie, logré alcanzar varias frutas. Sin pensarlo, le extendí una a Fisa."
    playerName "Buen provecho."
    "En un instante, Fisa tomó la pera de mis manos y a pesar de mantener la apariencia hasta ahora, la devoró en un instante. La lana de sus mejillas se llenó del líquido de la pera y se volvió pegajosa."
    "Me senté en el suelo con varias peras entre mis brazos, y esparcí la mayoría sobre el cesped."
    "Precavida, Fisa se sentó frente a mí."
    calchona "¿Por qué eres buena conmigo?"
    playerName "¿Mh?"
    calchona "¿No me estás viendo? ¿Cómo estás tan tranquila?"
    
    menu:
        "\"No lo estoy\"":
            $ goodAnswersCalchona += 1
            playerName "No lo estoy."
            playerName "No realmente al menos."
            playerName "Estar asustada de algo que no conozco no me va a llevar a ningún sitio."
            playerName "¿No es eso la vida? ¿Tomar riesgos?"
            calchona "... Eres valiente, me recuerdas a mis hijos."
            playerName "¿Hijos?"
            "Me giré a observarla, sus ojos moribundos parecían brillar como el fuego de las hogueras mientras se llevaba otra pera a la boca."
            calchona "Mi esposo y yo trabajábamos en los campos. Él no sabía que yo era una bruja. Por las noches, me sentía libre, tomaba mis pociones y vagaba por las afueras, como una oveja."
            calchona "Un día, volví, y no había nada. Ni mi esposo, ni mis hijos, y todas mis pociones habían sido destruidas. Solo pude tomar los restos de una."
            calchona "Y quedé... Así."
            calchona "La pena, o vaya a saber que, me ató a este mundo desde ese entonces, condenada a caminar solo por el borde. Ni humana, ni animal."
            calchona "Y simplemente, la gente empezó a morir, y a olvidarse de mí."
            calchona "Me volví nada más que una Leyenda..."
        "\"Me inspiras confianza\"":
            "Me encogí de hombros, tratando de poner el rostro más impasible que podía."
            playerName "Supongo que me inspiras confianza."
            playerName "Desde que te vi, no has hecho nada más que tratado de alejarse."
            playerName "Si algo parecía, era que tú tenías más miedo de mí que yo."
            "Fisa parpadeó varias veces, usando el revés de su mano para limpiarse los restos de pera."
            calchona "Eres valiente. He visto gente intrépida como tú cometer errores muy graves."
            calchona "Hay muchas otras criaturas... Más grandes, fuertes, y crueles que yo."
            "La manera en que Fisa perdía la vista en la comida, me hacía pensar que ella también tenía algo de aquella fuerza y crueldad de la que hablaba."
    
    calchona "Hace mucho conocí a un hombre, no muy distinto a tí. Fue el primer humano que me trató como una persona."
    calchona "Y luego... Solo sentí calor."
    "Está hablando del abuelo..."
    menu:
        "Hablar sobre mamá":
            $ goodAnswersCalchona += 1
            playerName "Yo no sé que haría si no pudiera volver a ver mi mamá..."
            playerName "Cuando era pequeña, tuve una pesadilla. Estaba sola en el mundo... No había absolutamente nada, como si alguien hubiera puesto un lienzo y solo me puso a mí, y allí me dejó."
            playerName "Cuando desperté me di cuenta que no le temía a estar sola, sino a la posibilidad de que hubiera algo más allí lo cual no me podría enfrentar."
            "Fisa hizo silencio, pero luego, sujetó mi mano."
            calchona "Siempre cuando uno de mis hijos tenía miedo, yo les decía, que cerrara el puño fuertemente e imaginara que estaba apretando mi mano."
            "Con sus palabras, podía sentir como su agarre se hacía más firme, y en un reflejo, hice lo mismo."
            calchona "Cuando haces mucha fuerza, no sientes si en verdad hay o no alguien contigo. Eso... Nos hace sentir menos solos."
            "Así, nos quedamos hablando por horas."
            pause
        "Consolarla":
            playerName "Cometer un error no nos hace menos humanos. Lamento mucho lo que te ha pasado."
            "Fisa volteó su mirada, y en el reflejo de aquellos ojos pude ver... Compasión."
            calchona "No lo hagas. No era una buena persona. Los humanos pueden guardar muchos buenos sentimientos y a su vez
            ser un animal..."
            calchona "Significaba que podía hacer lo que quisiera, sin consecuencias. Podía robar, podía matar... Y no tenía que mirar atrás."
            calchona "Eso era la verdadera libertad."
            calchona "Pero al final, tenemos que enfrentar que no estamos solos, y lo que hacemos, repercute a todo nuestro alrededor."
            "El silencio volvió a caer entre nosotras, mientras me quedé pensando en lo que había dicho..."
            pause

    centered "5:00am\nLos Campos"
    "La noche comenzaba a desaparecer."
    calchona "Yaaaawn"
    "Al fin, pude ver que Fisa estaba agotada..."

    if goodAnswersCalchona == 3:
        jump calchonaGoodEnding
    else:
        jump calchonaBadEnding

label calchonaGoodEnding:
    $ persistent.calchonaEnding = True
    "De pronto, se levantó, y se alejó caminando."
    playerName "?!"
    calchona "Ven, quiero ver el amanecer."
    "Me levanté del cesped, sacudí un poco mi pantalón, y la seguí. Era ahora o nunca, tenía que sellarla."
    "Finalmente, Fisa se detuvo a campo abierto, justo donde el Sol empezaría a caer con toda su fuerza."
    calchona "He vivido oculta por cientos de años, ya había olvidado lo que se siente el calor."
    playerName "... Pero-"
    calchona "No puedo culpar a mi Vestigio, he vivido fuera del Sol mucho antes que estar en él."
    calchona "¿Tú lo tienes, verdad?"
    "Al oir esas palabras, pude sentir como mi cuerpo se tensaba. Ella sabía."
    calchona "Ven, siéntate. Correr de mí será inútil."
    "Lentamente, me acerqué a ella. Mi corazón estaba latiendo cada vez más fuerte."
    calchona "Eres una buena niña, ..."
    calchona "Veamos el amanecer juntas."
    "Al sentarme junto a ella, todos mis miedos resurgieron. Podía dejarla ir. Podía ignorar que la había visto, quizá la Madre Monte pueda lidiar con ella."
    "Su lana, tan pálida bajo la luna, comenzaba a verse del blanco más hermoso que había visto. Fisa cerró los ojos."
    calchona "Desearía... Poder llorar. Por mi familia, por mi pasado."
    calchona "Por las cosas que vas a pasar de ahora en más."
    "Llorar..."
    "La marca está..."
    "Fisa se giró hacia mí, sus ojos reluciendo con cada palabra."
    calchona "¿Debe doler, no? Ser una buena persona, forzada a hacer cosas malas..."
    "Si no lo hacía ahora... No llegaría a tiempo. Mis uñas arrancaron las cáscaras que contenían la sangre de mi palma. Y sin más, apreté la mano contra los brillantes ojos de Fisa. Podía ver como dos hilos carmesí caían por sus mejillas, tiñiendo la suave lana. Sus ojos quemaban sobre mi mano."
    calchona "Nghhh--!!"
    playerName "¡Lo siento! ¡Tengo que hacerlo por mi abuelo!"
    "Ambas manos sujetaron mi brazo con fuerza."
    calchona "Tu abuelo es parte de tí."
    calchona "Y..."
    calchona "Ahora..."
    calchona "Yo también."
    "Antes de que me diera cuenta, caí hacia adelante. El sol estaba iluminando el campo. Estaba sola. De mi bolsillo, cayó el vestigio, reluciente y lleno de vida."
    "Pero yo... Sentía que una parte mía se había desvanecido."
    "Lo que sea que haya hecho mi abuelo, espero haya valido la pena."
    "Por ahora, me levanté, volví a guardar el Vestigio y caminé de regreso a casa."
    jump normalEnding

label calchonaBadEnding:
    playerName "Quizá debamos descansar, no era mi intención quedarnos toda la noche."
    calchona "Lo sé."
    calchona "Quieres encerrarme de nuevo, verdad...?"
    "!!!"
    calchona "Te envió ella. Dejaste que te convenciera de que esto era por tu bien."
    calchona "Ojalá... No tuviera que ser así."
    playerName "No, espera. Escuchame, mi abuel-"
    "Antes de terminar, Fisa se abalanzó sobre mi, una mano me sujetó la cabeza con fuerza y la empujó contra el cesped."
    calchona "¡Lo siento, no puedo dejar que me entregues!"
    "Por favor..." #(Golpe)
    calchona "¿¡Que has hecho!?"
    "Basta..." #(Golpe)
    calchona "¡Todo por lo que él ha peleado, ahora ha valido nada!"
    "No..." #(Golpe)
    calchona "Lo arruinaste... Todo."
    #(Golpe)
    "BAD ENDING."
    # Finaliza el juego:
    return

##########################################################
label pomberoRoute:
    default goodAnswersPombero = 0
    "Ruta del Pombero"
    pombero "Decisión 1"
    menu:
        "Elección Buena":
            $ goodAnswersPombero += 1
            pombero "Respuesta Positiva"
        "Elección Mala":
            pombero "Respuesta Negativa"
    pombero "Decisión 2"
    menu:
        "Elección Buena":
            $ goodAnswersPombero += 1
            pombero "Respuesta Positiva"
        "Elección Mala":
            pombero "Respuesta Negativa"
    pombero "Decisión 3"
    menu:
        "Elección Buena":
            $ goodAnswersPombero += 1
            pombero "Respuesta Positiva"
        "Elección Mala":
            pombero "Respuesta Negativa"

    if goodAnswersPombero == 3:
        jump pomberoGoodEnding
    else:
        jump pomberoBadEnding

label pomberoGoodEnding:
    $ persistent.pomberoEnding = True
    "Good Ending Pombero :)"
    jump normalEnding

label pomberoBadEnding:
    "Bad Ending :("
    # Finaliza el juego:
    return

##########################################################

label silbonRoute:
    default goodAnswersSilbon = 0
    "Ruta del Silbón"
    silbon "Decisión 1"
    menu:
        "Elección Buena":
            $ goodAnswersSilbon += 1
            silbon "Respuesta Positiva"
        "Elección Mala":
            silbon "Respuesta Negativa"
    silbon "Decisión 2"
    menu:
        "Elección Buena":
            $ goodAnswersSilbon += 1
            silbon "Respuesta Positiva"
        "Elección Mala":
            silbon "Respuesta Negativa"
    silbon "Decisión 3"
    menu:
        "Elección Buena":
            $ goodAnswersSilbon += 1
            silbon "Respuesta Positiva"
        "Elección Mala":
            silbon "Respuesta Negativa"

    if goodAnswersSilbon == 3:
        jump silbonGoodEnding
    else:
        jump silbonBadEnding


label silbonGoodEnding:
    $ persistent.silbonEnding = True
    "Good Ending Silbón :)"
    jump normalEnding

label silbonBadEnding:
    "Bad Ending :("
    # Finaliza el juego:
    return

############################################

label normalEnding:
    "Normal Ending :)"
    if persistent.calchonaEnding == True and persistent.pomberoEnding == True and persistent.silbonEnding == True:
        jump trueEnding
    else: 
        # Finaliza el juego:
        return

label trueEnding:
    "True Ending!!!! :D"
    # Finaliza el juego:
    return
    