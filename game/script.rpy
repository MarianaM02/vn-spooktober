label splashscreen:
    scene black
    with Pause(1)

    show text "Onda Dinamita presenta..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

define mm = Character("????", color="#2a7f62")
define pom = Character("????", color="#89909f")
define cal = Character("????", color="#538083")
define sil = Character("????", color="#ade1e5")
# $ pomberoName = "Har"
# $ silbonName = "Wiija"
define flash = Fade(0.9, 0.0, 0.5, color="#fff")

label start:

    $ playerName = renpy.input("Mi nombre es..", default = "Alba", length=12)
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "Alba"
    define p = Character("[playerName]", color="#c3acce")
    jump intro

label intro:
    centered "{cps=10}30 de Octubre\n4:00pm{/cps}"
    p "¡Phew! ¡Ya era hora!"
    p "Después de un viaje tan largo..."
    p "...finalmente estoy de vuelta."
    
    play music "audio/introv2.mp3" fadein 1
    scene pueblo with dissolve
    show player feliz with moveinbottom
    "No había visitado el pueblo de mamá desde hace dos veranos, justo cuando el abuelo cayó enfermo."
    show player triste with dissolve
    "Han sido unos meses muy tristes, y mamá no ha sido la misma desde que se enteró."
    show player feliz with dissolve
    "Pero estoy segura que venir le hará bien."

    show player pensativa with dissolve
    p "Ahora... La casa del abuelo estaba al final de la calle..."
    scene casa with fade
    p "¡Whoa! Siempre olvido lo grande que es."
    "Mamá me dijo que pidió que la limpiaran antes que llegáramos, ¡Cuanto trabajo!"
    "Mis padres estaban muy ocupados para venir hoy, pero yo no puedo perderme el festival de Halloween."
    "¡Siempre fue mi preferida!"
    "Todavía es un poco temprano, así que podría investigar un poco antes de volver a salir."
    p "¿Dónde voy?"
    menu:
        "Examinar cocina":
            # TODO cross fade musica
            pass
    scene cocina with fade
    play music "audio/ambiente-lento-001.mp3" fadein 2
    show player feliz at right with easeinright
    p "Está mucho más limpia de lo que recuerdo..."
    show alfajores at truecenter with dissolve
    "Cuando era pequeña, solía ayudar al abuelo a hacer alfajores. "
    "Hacíamos un desastre, ¡pero quedaban deliciosos!"
    hide alfajores with dissolve
    menu:
        "Examinar sala":
            pass
    scene sala with fade
    show player feliz at left with easeinleft
    show retrato at truecenter with dissolve
    "Está lleno de fotos de nosotros. Mamá y el abuelo siempre habían sido muy compañeros."
    "Pero mamá dejó el pueblo a los 18 para irse a estudiar y jamás volvió."
    "El abuelo nunca dijo nada, y siempre que volvían a verse era como si el tiempo no hubiera pasado."
    show player triste with dissolve
    "Me pregunto si realmente eso fue difícil para ellos..."
    hide retrato with dissolve
    menu:
        "No quiero investigar mas":
            pass
    #play sound "audio/bostezo.wav"
    show player bostezo with dissolve
    p "Yaaawwwwnn..."
    p "Creo que mejor voy a descansar un poco."
    hide player with dissolve
    "Esta casa posee muchos recuerdos... Tanto para mí como para mi mamá."
    "Me pregunto como reaccionará ella cuando venga mañana..."
    jump dream

label dream:
    # TODO Fade out
    stop music fadeout 3.0
    scene black with fade
    pause
    scene dream with dissolve
    centered "\"{cps=10}[playerName!q]...{/cps}\""
    centered "\"No le creas.\""
    centered "\"No lo busques.\""
    centered "\"Está aquí.\""
    centered "\"{cps=5}Esperándote...{/cps}\""
    scene black with fade
    pause
    jump festival

label festival:
    centered "{cps=10}30 de Octubre.\n8:00pm{/cps}"
    #Fade in
    scene sala with fade
    play music "audio/introv2.mp3" fadein 1
    show player feliz with moveinbottom
    p "¡Esa fue una gran siesta!"
    p "¡Será mejor que ya vuelva a salir antes de que se haga muy tarde!"
    stop music fadeout 1.0
    show player pensativa with dissolve
    p ". . ."
    show player triste with dissolve
    "Que frío hace aquí dentro..."
    show player feliz with dissolve
    "Debo recordar prender la calefacción cuando vuelva."
    play music "audio/introv2.mp3" fadein 1
    p "Vamos al pueblo!"
    hide player with fade
    scene festival with fade
    play music "audio/introv2.mp3" if_changed fadein 1
    show player feliz with moveinbottom
    p "¡Wow! Hay muchísima más gente de la que recordaba."
    "Todos los años, el pueblo hace un gran festival por Halloween. Los preparativos empiezan muchas semanas antes, y dura dos días."
    "Pero siempre lo mejor es durante la noche del 31:\nhay danzas, disfraces y muchísima comida."
    "El abuelo me contó que cuando mamá era adolescente, ponía a coserse la ropa desde un mes antes, y salía a las calles con sus amigos cantando."
    "Siempre se maquillaba de maneras espeluznantes y todo el mundo quedaba encantado. Es la fiesta turística del pueblo."
    "Mamá siempre contaba que desde hacía siglos, el pueblo tenía una gran conexión con el Otro Mundo"
    "...y mientras conociéramos nuestras raíces y quienes éramos, nada podía hacernos daño."
    "Ella dice que se sentía más cómoda como un monstruo entre humanos. Me encantaría volverla a ver así."
    jump grampasBox

label grampasBox:
    scene black with fade
    stop music fadeout 3.0
    centered "{cps=10}30 de Octubre.\n11:55pm{/cps}"
    scene sala with fade
    show player bostezo at left with easeinleft
    p "Phew... Estoy agotada, ha sido realmente divertido!"
    show player feliz with dissolve
    p "Que suerte que aquí la celebración es hasta mañana, seguro mamá lo disfrut--"
    show player triste at center with move
    p "¿Eh?"
    play music "audio/ambiente-lento-001.mp3" fadein 2
    show player asustada with dissolve
    "Veo la luz saliendo de la puerta entreabierta, las luces del resto de la casa se encuentran apagadas"
    p "¿Qué... Es eso...?"
    "Viene de la habitación de mi abuelo... No he estado allí desde hace años."
    show player triste with dissolve
    menu:
        "Acercarse":
            pass
    stop music fadeout 2.0
    scene puerta with fade
    p "¿Hola?"
    p ". . ."
    "Que extraño, nadie me dijo que habría alguien aquí, ¿Será una broma?"
    # [Empiezan a oirse susurros, la luz se ve saliendo desde la puerta entreabierta
    menu:
        "Entrar":
            pass
    play sound "audio/puerta.wav"
    scene dormitorio with fade
    # "Se abre la puerta, la habitación está vacía, se ve la cama, y junto a ella, la caja de donde sale esa luz."
    # "Hay más susurros, el ambiente es cada vez más tenso"
    "Tal y como recordaba este lugar... Es como si el abuelo jamás se hubiese ido. Pero... Esa caja..."
    menu:
        "Acercarse":
            pass
    show cofre cerrado at truecenter with dissolve
    p ". . ."
    # "Ambiente más y más abrumador, desconectando a p del exterior"
    "La recuerdo, mi abuelo nunca me dejaba tocarla. Me pregunto..."
    menu:
        "Abrir":
            pass

    # Se abre la caja, se ven luces salir
    # Siguiente
    play sound "audio/cofre.wav"
    show cofre abierto with dissolve
    # Pantalla toda en blanco.
    scene white with flash
    p "AGHHH!"
    play sound "audio/tinnitus2.wav"
    # Tinnitus?
    # Siguiente

label meetMadreMonte:
    # personaje ???
    play music "audio/madre-monte-002.mp3" fadein 0.5
    scene dormitorio with fade
    show mmonte full with dissolve
    mm "Vaya..."
    menu:
        "\"¿Quien eres?\"":
            pass

    mm "¿Quien soy yo? ¿Que no te han enseñado nada?"
    # Cambia a Inaru
    $ mm = Character("Inaru", color="#2a7f62")
    mm "Me llamo Inaru, soy una protectora de los bosques, por supuesto!"
    mm "O lo era, hasta que quedé bajo las órdenes del Maestro, he vivido en esta caja por cuarenta largos años!"
    show mmonte at right with move
    show player asustada at left with easeinleft
    p "¿¡Cómo!? ¿¡Mi abuelo es tu maestro!?"
    mm "Pues parece que sí, tanto yo como los otros estábamos bajo sus ord-"
    mm ". . ."
    mm "¿¡Qué hiciste!? ¿¡Fuíste tú!?"
    mm "¡No debiste haber hecho eso, niña tonta!"
    mm "... Si yo estoy afuera, quiere decir que los demás también."
    menu:
        "\"¿¡Que está pasando!?\"":
            pass
    mm "Míralo tu misma"
    show player triste with dissolve
    # ((Paneo a la caja, con los cuatro objetos inanimados, sin luz))
    mm "Estos son Vestigios."
    mm "Reliquias que tu abuelo perfeccionó para capturar a las Leyendas que habitan este mundo."
    mm "Una Leyenda puede ser cualquier cosa: un espíritu, un monstruo, un objeto poseído, cualquier criatura atrapada en una época que no le pertenezca."
    mm "Tu abuelo ha dedicado su vida a capturar y atrapar sus Leyendas, al igual que su padre antes que él."
    mm "Hasta ahora, tu familia ha podido capturar a tres Leyendas: Ellos son el Silbón, la Calchona y el Pombero." 
    mm "Criaturas que vagaban el mundo causando terror antes de que tú las liberaras nuevamente." 
    mm "Ahora es tu responsabilidad encontrarlas y capturarlas de nuevo dentro de los Vestigios."
    show player asustada with dissolve
    menu:
        "\"¿Y cómo voy a hacer eso?\"":
            pass

    mm "Tendrás que convencerlos, por supuesto!"
    mm "No estoy esperando que puedas derrotarlos y forzarlos dentro del Vestigio, no pareces muy fuerte."
    show player triste with dissolve
    mm "Las Leyendas son criaturas suspicaces, si sienten que eres una amenaza, será más difícil encontrarlos."
    mm "Ahí tu corres ventaja, van a subestimarte."
    show player enojada with dissolve
    p ". . ."
    show player triste with dissolve
    mm "Tu familia usó un hechizo para encerrarlos, si escaparon, es porque éste se ha debilitado, pero aún tienes la oportunidad de volver a darle fuerza."
    mm "Cada Leyenda tiene una marca, si tienes la sangre de tu abuelo, usar un poco de tu sangre sobre la marca será suficiente para devolver su alma a los Vestigios."
    p "Mi sangre..." 
    p "Nada tiene sentido, ¿por qué mi abuelo nunca nos lo diría?"
    mm "Te veo preocupada"
    menu:
        "\". . .\"":
            jump info
   
label info:
    mm "¿Qué quieres saber?"
    menu:
        "Madre Monte":
            mm "Yo soy un espíritu protector de los bosques. Estaba perdida hasta que tu abuelo me encontró."
            mm "Él me salvó de morir cegada por la ira y el rencor, y desde entonces, juré estar siempre a su lado."
            mm "Es por eso que tienes que conseguir que las otras Leyendas vuelvan a sus Vestigios."
            pause
            jump info
        "Pombero":
            mm "El Pombero es un duende, muy peludo y del color de la noche. Con los humanos es el más impredecible, pero posee un gran cariño y respeto por los bosques."
            pause
            jump info
        "Silbón":
            mm "El silbón es un espectro con la forma de un joven, le encanta silbar y tiene un particular odio hacia los hombres."
            pause
            jump info
        "Calchona":
            mm "La cal solía ser una bruja, pero sufrió una maldición por sus actos. Ahora es condenada a vagar el mundo sin poder volver a su forma humana."
            pause
            jump info
        "Abuelo":
            mm "Tu abuelo fue un hombre muy hábil e inteligente, ha dedicado su vida entera a buscar y capturar Leyendas que podrían ser dañinas para los humanos."
            mm "Él solía hablar con nosotros, lo hizo hasta sus últimos días..."
            pause
            jump info
        "Estoy bien":
            jump preMission

label preMission:
    "Sabía que había un gran peligro por delante. Al mismo tiempo, sentía que algo me empujaba hacia ello." 
    "Dentro mío, estaba segura que la Madre Monte no me mentía, y que mi abuelo estaba fuertemente conectado a esto."
    mm "Se que es mucha información, y no tenemos mucho tiempo."
    p "Hay mucha gente que corre peligro, ¿No causarán el caos?"
    mm "Los humanos no ven nada que no quieran ver, y las Leyendas no se hacen notar a menos que quieran ser vistas."
    mm "Ahora, ellos también están recobrando sus fuerzas, pero no les llevará mucho hasta que empiecen a moverse nuevamente."
    "Me pregunto si realmente puedo confiar en ella de la manera que ella espera que lo haga..."
    mm "¿Estás segura?"
    show player asustada with dissolve
    p "!!"
    "Su voz me saca de mis pensamientos, y un fuerte sentimiento de inseguridad me invade de repente."
    "Algo que no estaba allí un momento antes."
    show player triste with dissolve
    "¿Es esto lo que pueden causar las Leyendas solo con su voz? ¿Miedo, dudas?"
    "O quizá también... Protección y seguridad."
    "La Madre Monte me mira impaciente. Yo tardo unos momentos antes de hablar de nuevo."
    p "¿De verdad no hay nadie más que pueda resolver esto? Mamá vendrá mañana y-"
    mm "Mañana ya será demasiado tarde. No, lo siento, si tú no lo haces, nadie podrá."
    p "¿Por qué no podemos llamar a la policía?"
    mm "Nada de lo que hagan podrá resultar. Solo puedes tú. Solo tú tienes la sangre de tu abuelo."
    p "¿Cómo?"
    "En un instante, la Madre Monte sujetó mi mano."
    mm "Cierra los ojos."
    "En un reflejo, cerré los ojos justo cuando sentí la piel de mi palma abrirse."
    show player asustada with dissolve
    p "Agh!"
    "El líquido comenzó a brotar, mojando mi mano."
    "Los dedos rígidos de la Madre Monte pasaron sobre la palma."
    "Cuando abrí los ojos, mi mano estaba seca y las yemas de la madre monte brillaban de un color carmesí."
    mm "Para encerrar nuevamente a las Leyendas, necesitas encontrar el lugar donde tu abuelo ha puesto el hechizo y debes marcarlo con tu sangre."
    show player triste with dissolve
    mm "Yo puedo forzar a dos de las Leyendas de nuevo dentro de su Vestigio usándola tambien, pero enfrentarme a los tres podría matarme."
    "Su mano se posó sobre mi mejilla, podía sentir el calor a través de su palma."
    mm "Lo siento, hubiera querido que las cosas fueran diferentes. Aún así, la última decisión la tienes tú."
    mm "¿Deseas ayudarme a salvar lo que tu abuelo ha intentado proteger?"
    menu:
        "\"Sí, voy a ayudarte.\"":
            jump missionAccepted
        "\"No! De ninguna manera!\"":
            jump missionDenied

label missionDenied:
    stop music fadeout 3.0
    p "No puedo... No soy la persona que buscas."
    mm "Vaya, que decepción."
    mm "Pero supongo que no te puedo forzar."
    "Me di vuelta, y caminé hacia la puerta."
    mm "Pero aún así {cps=7}puedo usarte.{/cps}"
    p "!!!!"
    "No llegué a voltear, mi cuerpo entumecido solo atisbó a mirar hacia abajo, donde las ramas salían de mi estómago."
    "Luego... Oscuridad."
    "F en el chat"
    "Bad Ending :("
    # Finaliza el juego:
    return

label missionAccepted:
    stop music fadeout 3.0
    show player feliz with dissolve
    mm "Gracias... Sé que esto no es fácil."
    mm "Bueno, entonces ya está decidido."
    mm "Luego de vivir tantas décadas con ellos, puedo sentirlos."
    "Inaru camina hacia un mapa del Pueblo colgado en la pared."
    # Paneo al mapa con tres marcas
    show mapa at truecenter with dissolve
    mm "Al Silbón le gusta estar entre gente, así que es probable que lo encuentres caminando en el pueblo. "
    mm "Si hay un lugar donde seguro el Pombero iría primero, son los bosques."
    mm "Y la Calchona... Debe estar buscando algo que comer, así que seguramente la encontrarás en los campos."
    hide mapa with dissolve
    mm "Hay mucho terreno por cubrir y poco tiempo-"
    mm "Prometo ayudarte en todo lo que pueda. Nombra una Leyenda y yo me encargaré de lo demás."

    menu:
        "Calchona":
            jump calchonaRoute
        "Pombero":
            jump pomberoRoute
        "Silbón":
            jump silbonRoute
            
label calchonaRoute:
    default goodAnswersCalchona = 0
    
    scene black with fade
    centered "{cps=10}31 de Octubre.\n00:30am\nLos Campos{/cps}"
    scene white with fade
    "Siempre me gustó venir aquí... De pequeña, los vecinos me dejaban acariciar a los animales y darles de comer."
    "Ahora, estoy buscando a una bruja, y parece ser el peor lugar del mundo."
    "El viento soplaba con suavidad, y con él, lograba escuchar los susurros de las ovejas que dormían dentro de sus corrales. Parecía que cotilleaban entre ellas en sueños."
    p "Nghh.."
    p "!!!"
    "Unos gemidos forzaron que me detuviera. Mi cuerpo se tensó, mientras escaneaba cerca de los corrales."
    "Allí la vi, una figura encorvada que forcejeaba para entrar a uno de los corrales"
    "Pobre oveja, no debieron notar que quedó afuera."
    p ". . ."
    p "!!!"
    "Al ser iluminada bajo la luz de la Luna, pude ver un rostro humano, el cual se inclinaba para pasar la cabeza entre los postes del corral y alcanzar el bebedero."
    p "AH!"
    # personaje ???
    show cal 1 with fade
    cal "?"
    "Apenas me oyó, la oveja volteó a verme, y su espalda se irguió para levantarse en las patas traseras. Sus ojos brillantes se posaron en mí, dorados y muertos."
    "¿Qué hago?"
    "¿Qué hago?"
    "¿Qué hago?"
    "Puedo verla tensar sus manos, y sus ojos se mueven lejos de mí. Si se escapa, podría estar perdiendo la única oportunidad que tengo de ayudar al abuelo."
    p "AGUA!"
    cal "..."
    "La criatura se volvió a verme"
    p "Te puedo ayudar..."
    "Me fui acercando despacio, mis ojos en la criatura. Ella me observaba de regreso, dando unos pasos atrás. Pero no se alejaba."
    "Una vez llegué a la valla, puse las dos manos sobre ella y le trepé para llegar al otro lado. Las ovejas seguían dormidas. La criatura me miraba expectante."
    "Mi mano se extendió para abrir el grifo y el agua empezó a correr. En un instante, la criatura puso ambas manos dentro del corral y bajo el agua y luego se las llevó al hocico, bebiendo desesperadamente."
    "Sus ojos nunca me abandonaban."
    cal "Gracias."
    cal "¿Qué estás haciendo aquí?"
    "Vaya, no me lo esperaba."
    "Aún así, me miraba con desconfianza. No puedo decirle la completa verdad, o sino se irá. Me pregunto si se dará cuenta que le estoy mintiendo..."
    # Siguiente

    p "Yo..."
    menu:
        "\"Te estaba buscando.\"":
            $ goodAnswersCalchona += 1
            p "Te estaba buscando. En el pueblo, se oyen historias sobre leyendas que vagan en esta noche, pensé que si comenzaba a explorar, podría encontrar alguna. Lamento haberte asustado."
            cal "Los campesinos jamás hablan conmigo. Pero siempre me dejan algo de beber. Jamás había estado aquí antes."
            "Puedo ver como comienza a relajarse, y en respuesta, siento como mis hombros bajan a la par."
        "\"Me escapé del festival.\"":
            p "Me escapé del festival. Había mucho estruendo, y quería ver como se encontraban los animales." 
            p"Vengo a este pueblo desde que soy pequeña y siempre he tenido una conexión con ellos. Cuando me acerqué, pensé que eras una oveja que se había escapado del corral."
            cal "No serías la primera. Es normal teniendo en cuenta como... Luzco."
            "Puedo notar que aún me mira con desconfianza, pero no hace ningún intento de salir corriendo. En respuesta, siento como mis músculos se relajan."
 
    
    p "Si tienes hambre, puedo ayudarte a buscar algo para comer!"
    cal "..."
    p "Soy [playerName!q] ¿cuál es tu nombre?"
    cal "..."
    # Cambia a Fisa
    $ cal = Character("Fisa", color="#538083")
    cal "Fisa."
    p "Bueno, entonces es un placer conocerte! Ven, vamos a buscar algo para comer."
    "Mientras me alejaba, me puse a pensar acerca de como le estaba yendo a Inaru..."
    "Mi mano comenzaba escocer al recordar todo lo que conllevaba esto, y en el problema en que me había metido."
    "¿Por qué abrí esa caja?"
    # (recuerdo)
    centered "No lo veas"
    centered "No lo escuches"
    "¿Quién era esa voz?"
    cal "No tendrías que haber venido."
    p "?!"
    cal "Los campos son peligrosos, en especial por la noche. No sabes lo que puede haber aquí."
    p "Podría decir lo mismo de tí."
    cal "..."
    cal "Peras."
    p "?"
    "Fisa levanta un brazo, señalando a los árboles que contenían una gran cantidad de peras maduras."
    p "¡Bingo!"
    "Poniéndome en puntas de pie, logré alcanzar varias frutas. Sin pensarlo, le extendí una a Fisa."
    p "Buen provecho."
    "En un instante, Fisa tomó la pera de mis manos y a pesar de mantener la apariencia hasta ahora, la devoró en un instante. La lana de sus mejillas se llenó del líquido de la pera y se volvió pegajosa."
    "Me senté en el suelo con varias peras entre mis brazos, y esparcí la mayoría sobre el cesped."
    "Precavida, Fisa se sentó frente a mí."
    cal "¿Por qué eres buena conmigo?"
    p "¿Mh?"
    cal "¿No me estás viendo? ¿Cómo estás tan tranquila?"
    
    menu:
        "\"No lo estoy\"":
            $ goodAnswersCalchona += 1
            p "No lo estoy."
            p "No realmente al menos."
            p "Estar asustada de algo que no conozco no me va a llevar a ningún sitio."
            p "¿No es eso la vida? ¿Tomar riesgos?"
            cal "... Eres valiente, me recuerdas a mis hijos."
            p "¿Hijos?"
            "Me giré a observarla, sus ojos moribundos parecían brillar como el fuego de las hogueras mientras se llevaba otra pera a la boca."
            cal "Mi esposo y yo trabajábamos en los campos. Él no sabía que yo era una bruja. Por las noches, me sentía libre, tomaba mis pociones y vagaba por las afueras, como una oveja."
            cal "Un día, volví, y no había nada. Ni mi esposo, ni mis hijos, y todas mis pociones habían sido destruidas. Solo pude tomar los restos de una."
            cal "Y quedé... Así."
            cal "La pena, o vaya a saber que, me ató a este mundo desde ese entonces, condenada a caminar solo por el borde. Ni humana, ni animal."
            cal "Y simplemente, la gente empezó a morir, y a olvidarse de mí."
            cal "Me volví nada más que una Leyenda..."
        "\"Me inspiras confianza\"":
            "Me encogí de hombros, tratando de poner el rostro más impasible que podía."
            p "Supongo que me inspiras confianza."
            p "Desde que te vi, no has hecho nada más que tratado de alejarse."
            p "Si algo parecía, era que tú tenías más miedo de mí que yo."
            "Fisa parpadeó varias veces, usando el revés de su mano para limpiarse los restos de pera."
            cal "Eres valiente. He visto gente intrépida como tú cometer errores muy graves."
            cal "Hay muchas otras criaturas... Más grandes, fuertes, y crueles que yo."
            "La manera en que Fisa perdía la vista en la comida, me hacía pensar que ella también tenía algo de aquella fuerza y crueldad de la que hablaba."
    
    cal "Hace mucho conocí a un hombre, no muy distinto a tí. Fue el primer humano que me trató como una persona."
    cal "Y luego... Solo sentí calor."
    "Está hablando del abuelo..."
    menu:
        "Hablar sobre mamá":
            $ goodAnswersCalchona += 1
            p "Yo no sé que haría si no pudiera volver a ver mi mamá..."
            p "Cuando era pequeña, tuve una pesadilla. Estaba sola en el mundo... No había absolutamente nada, como si alguien hubiera puesto un lienzo y solo me puso a mí, y allí me dejó."
            p "Cuando desperté me di cuenta que no le temía a estar sola, sino a la posibilidad de que hubiera algo más allí lo cual no me podría enfrentar."
            "Fisa hizo silencio, pero luego, sujetó mi mano."
            cal "Siempre cuando uno de mis hijos tenía miedo, yo les decía, que cerrara el puño fuertemente e imaginara que estaba apretando mi mano."
            "Con sus palabras, podía sentir como su agarre se hacía más firme, y en un reflejo, hice lo mismo."
            cal "Cuando haces mucha fuerza, no sientes si en verdad hay o no alguien contigo. Eso... Nos hace sentir menos solos."
            "Así, nos quedamos hablando por horas."
            pause
        "Consolarla":
            p "Cometer un error no nos hace menos humanos. Lamento mucho lo que te ha pasado."
            "Fisa volteó su mirada, y en el reflejo de aquellos ojos pude ver... Compasión."
            cal "No lo hagas. No era una buena persona. Los humanos pueden guardar muchos buenos sentimientos y a su vez
            ser un animal..."
            cal "Significaba que podía hacer lo que quisiera, sin consecuencias. Podía robar, podía matar... Y no tenía que mirar atrás."
            cal "Eso era la verdadera libertad."
            cal "Pero al final, tenemos que enfrentar que no estamos solos, y lo que hacemos, repercute a todo nuestro alrededor."
            "El silencio volvió a caer entre nosotras, mientras me quedé pensando en lo que había dicho..."
            pause

    scene black with fade
    centered "{cps=10}31 de Octubre.\n5:00am\nLos Campos{/cps}"
    scene white with fade
    "La noche comenzaba a desaparecer."
    cal "Yaaaawn"
    "Al fin, pude ver que Fisa estaba agotada..."

    if goodAnswersCalchona == 3:
        jump calchonaGoodEnding
    else:
        jump calchonaBadEnding

label calchonaGoodEnding:
    $ persistent.calchonaEnding = True
    "De pronto, se levantó, y se alejó caminando."
    p "?!"
    cal "Ven, quiero ver el amanecer."
    "Me levanté del cesped, sacudí un poco mi pantalón, y la seguí. Era ahora o nunca, tenía que sellarla."
    "Finalmente, Fisa se detuvo a campo abierto, justo donde el Sol empezaría a caer con toda su fuerza."
    cal "He vivido oculta por cientos de años, ya había olvidado lo que se siente el calor."
    p "... Pero-"
    cal "No puedo culpar a mi Vestigio, he vivido fuera del Sol mucho antes que estar en él."
    cal "¿Tú lo tienes, verdad?"
    "Al oir esas palabras, pude sentir como mi cuerpo se tensaba. Ella sabía."
    cal "Ven, siéntate. Correr de mí será inútil."
    "Lentamente, me acerqué a ella. Mi corazón estaba latiendo cada vez más fuerte."
    cal "Eres una buena niña, ..."
    cal "Veamos el amanecer juntas."
    "Al sentarme junto a ella, todos mis miedos resurgieron. Podía dejarla ir. Podía ignorar que la había visto, quizá la Madre Monte pueda lidiar con ella."
    "Su lana, tan pálida bajo la luna, comenzaba a verse del blanco más hermoso que había visto. Fisa cerró los ojos."
    cal "Desearía... Poder llorar. Por mi familia, por mi pasado."
    cal "Por las cosas que vas a pasar de ahora en más."
    "Llorar..."
    "La marca está..."
    "Fisa se giró hacia mí, sus ojos reluciendo con cada palabra."
    cal "¿Debe doler, no? Ser una buena persona, forzada a hacer cosas malas..."
    "Si no lo hacía ahora... No llegaría a tiempo. Mis uñas arrancaron las cáscaras que contenían la sangre de mi palma. Y sin más, apreté la mano contra los brillantes ojos de Fisa. Podía ver como dos hilos carmesí caían por sus mejillas, tiñiendo la suave lana. Sus ojos quemaban sobre mi mano."
    cal "Nghhh--!!"
    p "¡Lo siento! ¡Tengo que hacerlo por mi abuelo!"
    "Ambas manos sujetaron mi brazo con fuerza."
    cal "Tu abuelo es parte de tí."
    cal "Y..."
    cal "Ahora..."
    cal "Yo también."
    "Antes de que me diera cuenta, caí hacia adelante. El sol estaba iluminando el campo. Estaba sola. De mi bolsillo, cayó el vestigio, reluciente y lleno de vida."
    "Pero yo... Sentía que una parte mía se había desvanecido."
    "Lo que sea que haya hecho mi abuelo, espero haya valido la pena."
    "Por ahora, me levanté, volví a guardar el Vestigio y caminé de regreso a casa."
    jump normalEnding

label calchonaBadEnding:
    p "Quizá debamos descansar, no era mi intención quedarnos toda la noche."
    cal "Lo sé."
    cal "Quieres encerrarme de nuevo, verdad...?"
    "!!!"
    cal "Te envió ella. Dejaste que te convenciera de que esto era por tu bien."
    cal "Ojalá... No tuviera que ser así."
    p "No, espera. Escuchame, mi abuel-"
    "Antes de terminar, Fisa se abalanzó sobre mi, una mano me sujetó la cabeza con fuerza y la empujó contra el cesped."
    cal "¡Lo siento, no puedo dejar que me entregues!"
    "Por favor..." #(Golpe)
    cal "¿¡Que has hecho!?"
    "Basta..." #(Golpe)
    cal "¡Todo por lo que él ha peleado, ahora ha valido nada!"
    "No..." #(Golpe)
    cal "Lo arruinaste... {cps=4}Todo.{/cps}"
    #(Golpe)
    "BAD ENDING."
    # Finaliza el juego:
    return

##########################################################
label pomberoRoute:
    default goodAnswersPombero = 0
    "Ruta del Pombero"
    pom "Decisión 1"
    menu:
        "Elección Buena":
            $ goodAnswersPombero += 1
            pom "Respuesta Positiva"
        "Elección Mala":
            pom "Respuesta Negativa"
    pom "Decisión 2"
    menu:
        "Elección Buena":
            $ goodAnswersPombero += 1
            pom "Respuesta Positiva"
        "Elección Mala":
            pom "Respuesta Negativa"
    pom "Decisión 3"
    menu:
        "Elección Buena":
            $ goodAnswersPombero += 1
            pom "Respuesta Positiva"
        "Elección Mala":
            pom "Respuesta Negativa"

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
    sil "Decisión 1"
    menu:
        "Elección Buena":
            $ goodAnswersSilbon += 1
            sil "Respuesta Positiva"
        "Elección Mala":
            sil "Respuesta Negativa"
    sil "Decisión 2"
    menu:
        "Elección Buena":
            $ goodAnswersSilbon += 1
            sil "Respuesta Positiva"
        "Elección Mala":
            sil "Respuesta Negativa"
    sil "Decisión 3"
    menu:
        "Elección Buena":
            $ goodAnswersSilbon += 1
            sil "Respuesta Positiva"
        "Elección Mala":
            sil "Respuesta Negativa"

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

##########################################################
label normalEnding:
    "Normal Ending :)"
    if persistent.calchonaEnding == True and persistent.pomberoEnding == True and persistent.silbonEnding == True:
        jump trueEnding
    else: 
        # Finaliza el juego:
        return

##########################################################
label trueEnding:
    "True Ending!!!! :D"
    # Finaliza el juego:
    return
    