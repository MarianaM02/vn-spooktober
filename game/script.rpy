﻿label splashscreen:
    scene black
    with Pause(1)

    show jam at truecenter with dissolve
    with Pause(2)

    scene black with fade
    with Pause(0.2)

    show text "Onda Dinamita presenta..." with dissolve
    with Pause(2.5)

    scene black with fade
    with Pause(1)

    return

define mm = Character("????", color="#2a7f62")
define pom = Character("????", color="#89909f")
define cal = Character("????", color="#538083")
define sil = Character("????", color="#ade1e5")
define abu = Character("????", color="#5a80d3")

define flash = Fade(0.9, 0.0, 0.5, color="#fff")

label start:
    stop music fadeout 2.5

    $ playerName = renpy.input("Mi nombre es..", default = "Alba", length=12)
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "Alba"
    define p = Character("[playerName]", color="#c3acce")
    jump intro

label intro:
    centered "30 de Octubre\n4:00pm"
    p "¡Phew! ¡Ya era hora!"
    p "Después de un viaje tan largo..."
    p "...finalmente estoy de vuelta."
    
    play music "audio/intro-loop.wav" fadein 1
    scene fondo pueblo frente with dissolve
    show player feliz with moveinbottom
    "No había visitado el pueblo de mamá desde hace dos veranos, justo cuando el abuelo cayó enfermo."
    show player triste with dissolve
    "Han sido unos meses muy tristes, y mamá no ha sido la misma desde que se enteró."
    show player feliz with dissolve
    "Pero estoy segura que venir le hará bien."

    show player pensativa with dissolve
    p "Ahora... La casa del abuelo estaba al final de la calle..."
    scene fondo casa lejos with fade
    show player feliz at right with easeinright
    "Mis padres estaban muy ocupados para venir hoy, pero yo no puedo perderme el festival de Halloween."
    "¡Siempre fue mi preferida!"
    scene fondo casa frente with fade
    p "¡Whoa! Siempre olvido lo grande que es."
    "Mamá me dijo que pidió que la limpiaran antes que llegáramos, ¡Cuánto trabajo!"
    "Todavía es un poco temprano, así que podría investigar un poco antes de volver a salir."
    stop music fadeout 3.0
    pause
    # p "¿Dónde voy?"
    # menu:
    #     "Examinar cocina":
    #         # TODO cross fade musica
    #         pass
    scene fondo sala with fade
    show player feliz at right with easeinright
    play music ["audio/ambiente-lento-loop.wav"] fadein 3.0
    p "Está mucho más limpia de lo que recuerdo..."
    show alfajores at truecenter with dissolve
    "Cuando era pequeña, solía ayudar al abuelo a hacer alfajores."
    "Hacíamos un desastre, ¡pero quedaban deliciosos!"
    hide alfajores with dissolve
    # menu:
    #     "Examinar sala":
    #         pass
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
    #play sound "audio/bostezo.ogg"
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
    centered "\"{cps=10}[playerName!q]...{/cps}\""
    centered "\"No le creas.\""
    centered "\"No lo busques.\""
    centered "\"Está aquí.\""
    centered "\"{cps=5}Esperándote...{/cps}\""
    pause
    jump festival

label festival:
    centered "30 de Octubre.\n8:00pm"
    #Fade in
    scene fondo sala with fade
    play music "audio/intro-loop.wav" fadein 1
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
    play music "audio/intro-loop.wav" fadein 1
    p "¡Vamos al pueblo!"
    scene fondo pueblo decorado with fade
    play music "audio/intro-loop.wav" if_changed fadein 1
    show player feliz at left with moveinbottom
    p "¡Wow! Hay muchísima más gente de la que recordaba."
    "Todos los años, el pueblo hace un gran festival por Halloween. Los preparativos empiezan muchas semanas antes, y dura dos días."
    "Pero siempre lo mejor es durante la noche del 31:\nhay danzas, disfraces y muchísima comida."
    show player at right with move
    "El abuelo me contó que cuando mamá era adolescente, ponía a coserse la ropa desde un mes antes, y salía a las calles con sus amigos cantando."
    "Siempre se maquillaba de maneras espeluznantes y todo el mundo quedaba encantado. Es la fiesta turística del pueblo."
    "Mamá siempre contaba que desde hacía siglos, el pueblo tenía una gran conexión con el Otro Mundo"
    "...y mientras conociéramos nuestras raíces y quienes éramos, nada podía hacernos daño."
    "Ella dice que se sentía más cómoda como un monstruo entre humanos. Me encantaría volverla a ver así."
    jump grampasBox

label grampasBox:
    scene black with fade
    stop music fadeout 3.0
    centered "30 de Octubre.\n11:55pm"
    scene fondo casa lejos with fade
    show player bostezo at right with easeinright
    p "Phew... Estoy agotada, ha sido realmente divertido!"
    show player feliz with dissolve
    p "Que suerte que aquí la celebración es hasta mañana, seguro mamá lo disfrut--"
    show player triste with dissolve
    p "¿Eh?"
    play music "audio/ambiente-lento-loop.wav" fadein 2
    show player asustada with dissolve
    "Veo la luz saliendo de la puerta entreabierta, las luces del resto de la casa se encuentran apagadas"
    p "¿Qué... Es eso...?"
    "Viene de la habitación de mi abuelo... No he estado allí desde hace años."
    show player triste with dissolve
    menu:
        "Acercarse":
            pass
    stop music fadeout 2.0
    scene fondo escaleras with fade
    p "¿Hola?"
    p ". . ."
    "Que extraño, nadie me dijo que habría alguien aquí, ¿Será una broma?"
    # [Empiezan a oirse susurros, la luz se ve saliendo desde la puerta entreabierta
    menu:
        "Entrar":
            pass
    play sound "audio/puerta.ogg"
    scene fondo dormitorio with fade
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
    play sound "audio/cofre.ogg"
    show cofre abierto with dissolve
    # Pantalla toda en blanco.
    scene white with flash
    p "AGHHH!"

label meetMadreMonte:
    # personaje ???
    play music "audio/madre-monte-loop.wav" fadein 0.5
    scene fondo dormitorio with fade
    show mmonte neutra with dissolve
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
    mm "¿¡Qué hiciste!? ¿¡Fuíste tú!?" with vpunch
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
    mm "Tu familia usó un hechizo para encerrarlos, si escaparon, es porque éste se ha debilitado, pero aún tienes la oportunidad de volver a darle fuerza."
    show player triste with dissolve
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
        "Inaru":
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
            mm "El Silbón es un espectro con la forma de un joven, le encanta silbar y tiene un particular odio hacia los hombres."
            pause
            jump info
        "Calchona":
            mm "La Calchona solía ser una bruja, pero sufrió una maldición por sus actos. Ahora es condenada a vagar el mundo sin poder volver a su forma humana."
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
    "Dentro mío, estaba segura que Inaru no me mentía, y que mi abuelo estaba fuertemente conectado a esto."
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
    "Inaru me mira impaciente. Yo tardo unos momentos antes de hablar de nuevo."
    p "¿De verdad no hay nadie más que pueda resolver esto? Mamá vendrá mañana y-"
    mm "Mañana ya será demasiado tarde. No, lo siento, si tú no lo haces, nadie podrá."
    p "¿Por qué no podemos llamar a la policía?"
    mm "Nada de lo que hagan podrá resultar. Solo puedes tú. Solo tú tienes la sangre de tu abuelo."
    p "¿Cómo?"
    "En un instante, Inaru sujetó mi mano."
    mm "Cierra los ojos."
    "En un reflejo, cerré los ojos justo cuando sentí la piel de mi palma abrirse."
    show player asustada with dissolve
    p "Agh!" with vpunch
    "El líquido comenzó a brotar, mojando mi mano."
    "Sus dedos rígidos pasaron sobre mi palma."
    "Cuando abrí los ojos, mi mano estaba seca y las yemas de Inaru brillaban de un color carmesí."
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
    show player asustada with dissolve
    p "!!!!" with vpunch 
    hide player with dissolve
    show mmonte at center with move
    "No llegué a voltear, mi cuerpo entumecido solo atisbó a mirar hacia abajo, donde las ramas salían de mi estómago."
    scene black with fade
    "Luego... Oscuridad."

    pause
    "Bad Ending :("
    # Finaliza el juego:
    return

label missionAccepted:
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

##########################################################
label calchonaRoute:
    default goodAnswersCalchona = 0
    stop music fadeout 2.5
    scene black with fade
    centered "31 de Octubre.\n00:30am\nLos Campos"
    scene campo with fade
    show player feliz at left with easeinleft
    "Siempre me gustó venir aquí... De pequeña, los vecinos me dejaban acariciar a los animales y darles de comer."
    show player triste with dissolve
    "Ahora, estoy buscando a una bruja, y parece ser el peor lugar del mundo."
    "El viento soplaba con suavidad, y con él, lograba escuchar los susurros de las ovejas que dormían dentro de sus corrales. Parecía que cotilleaban entre ellas en sueños."
    show player asustada with dissolve
    p "Nghh.."
    p "!!!"
    "Unos gemidos forzaron que me detuviera. Mi cuerpo se tensó, mientras escaneaba cerca de los corrales."
    "Allí la vi, una figura encorvada que forcejeaba para entrar a uno de los corrales"
    show player pensativa with dissolve
    "Pobre oveja, no debieron notar que quedó afuera."
    p ". . ."
    show player asustada with dissolve
    p "!!!"
    "Al ser iluminada bajo la luz de la Luna, pude ver un rostro humano, el cual se inclinaba para pasar la cabeza entre los postes del corral y alcanzar el bebedero."
    p "AH!"
    hide player with dissolve
    # personaje ???
    show calchona neutra with fade
    cal "?"
    "Apenas me oyó, la oveja volteó a verme, y su espalda se irguió para levantarse en las patas traseras. Sus ojos brillantes se posaron en mí, dorados y muertos."
    "¿Qué hago?{w} ¿Qué hago?{w} ¿Qué hago?"
    "Puedo verla tensar sus manos, y sus ojos se mueven lejos de mí. Si se escapa, podría estar perdiendo la única oportunidad que tengo de ayudar al abuelo."

    show calchona at right with move 
    show player asustada at left with easeinleft
    p "AGUA!"
    cal "..."
    "La criatura se volvió a verme"
    show player triste with dissolve
    p "Te puedo ayudar..."
    "Me fui acercando despacio, mis ojos en la criatura. Ella me observaba de regreso, dando unos pasos atrás. Pero no se alejaba."
    "Una vez llegué a la valla, puse las dos manos sobre ella y le trepé para llegar al otro lado. Las ovejas seguían dormidas. La criatura me miraba expectante."
    "Mi mano se extendió para abrir el grifo y el agua empezó a correr. En un instante, la criatura puso ambas manos dentro del corral y bajo el agua y luego se las llevó al hocico, bebiendo desesperadamente."
    "Sus ojos nunca me abandonaban."
    show player feliz with dissolve
    cal "Gracias."
    cal "¿Qué estás haciendo aquí?"
    show player triste with dissolve
    "Vaya, no me lo esperaba."
    "Aún así, me miraba con desconfianza. No puedo decirle la completa verdad, o sino se irá. Me pregunto si se dará cuenta que le estoy mintiendo..."

    show player pensativa with dissolve
    p "Yo..."
    menu:
        "\"Te estaba buscando.\"":
            $ goodAnswersCalchona += 1
            show player feliz with dissolve
            p "Te estaba buscando. En el pueblo, se oyen historias sobre leyendas que vagan en esta noche, pensé que si comenzaba a explorar, podría encontrar alguna. Lamento haberte asustado."
            cal "Los campesinos jamás hablan conmigo. Pero siempre me dejan algo de beber. Jamás había estado aquí antes."
            "Puedo ver como comienza a relajarse, y en respuesta, siento como mis hombros bajan a la par."
        "\"Me escapé del festival.\"":
            show player feliz with dissolve
            p "Me escapé del festival. Había mucho estruendo, y quería ver como se encontraban los animales." 
            p "Vengo a este pueblo desde que soy pequeña y siempre he tenido una conexión con ellos. Cuando me acerqué, pensé que eras una oveja que se había escapado del corral."
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
    show player triste with dissolve
    "¿Por qué abrí esa caja?"
    # (recuerdo)
    show black at truecenter with dissolve
    centered "No lo veas"
    centered "No lo escuches"
    hide black with fade
    "¿Quién era esa voz?"
    cal "No tendrías que haber venido."
    p "?!"
    cal "Los campos son peligrosos, en especial por la noche. No sabes lo que puede haber aquí."
    p "Podría decir lo mismo de tí."
    cal "..."
    cal "Peras."
    p "?"
    "Fisa levanta un brazo, señalando a los árboles que contenían una gran cantidad de peras maduras."
    show player feliz with dissolve
    p "¡Bingo!"
    "Poniéndome en puntas de pie, logré alcanzar varias frutas. Sin pensarlo, le extendí una a Fisa."
    p "Buen provecho."
    "En un instante, Fisa tomó la pera de mis manos y a pesar de mantener la apariencia hasta ahora, la devoró en un instante. La lana de sus mejillas se llenó del líquido de la pera y se volvió pegajosa."
    "Me senté en el suelo con varias peras entre mis brazos, y esparcí la mayoría sobre el cesped."
    "Precavida, Fisa se sentó frente a mí."
    cal "¿Por qué eres buena conmigo?"
    show player pensativa with dissolve
    p "¿Mh?"
    show player triste with dissolve
    cal "¿No me estás viendo? ¿Cómo estás tan tranquila?"
    
    menu:
        "\"No lo estoy\"":
            $ goodAnswersCalchona += 1
            p "No lo estoy."
            p "No realmente al menos."
            p "Estar asustada de algo que no conozco no me va a llevar a ningún sitio."
            show player feliz with dissolve
            p "¿No es eso la vida? ¿Tomar riesgos?"
            cal "... Eres valiente, me recuerdas a mis hijos."
            p "¿Hijos?"
            "Me giré a observarla, sus ojos moribundos parecían brillar como el fuego de las hogueras mientras se llevaba otra pera a la boca."
            cal "Mi esposo y yo trabajábamos en los campos. Él no sabía que yo era una bruja. Por las noches, me sentía libre, tomaba mis pociones y vagaba por las afueras, como una oveja."
            show player triste with dissolve
            cal "Un día, volví, y no había nada. Ni mi esposo, ni mis hijos, y todas mis pociones habían sido destruidas. Solo pude tomar los restos de una."
            cal "Y quedé... Así."
            cal "La pena, o vaya a saber que, me ató a este mundo desde ese entonces, condenada a caminar solo por el borde. Ni humana, ni animal."
            cal "Y simplemente, la gente empezó a morir, y a olvidarse de mí."
            cal "Me volví nada más que una Leyenda..."
        "\"Me inspiras confianza\"":
            show player feliz with dissolve
            "Me encogí de hombros, tratando de poner el rostro más impasible que podía."
            p "Supongo que me inspiras confianza."
            p "Desde que te vi, no has hecho nada más que tratado de alejarse."
            p "Si algo parecía, era que tú tenías más miedo de mí que yo."
            "Fisa parpadeó varias veces, usando el revés de su mano para limpiarse los restos de pera."
            cal "Eres valiente. He visto gente intrépida como tú cometer errores muy graves."
            cal "Hay muchas otras criaturas... Más grandes, fuertes, y crueles que yo."
            show player triste with dissolve
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
            show player feliz with dissolve
            "Así, nos quedamos hablando por horas."
            pause
        "Consolarla":
            p "Cometer un error no nos hace menos humanos. Lamento mucho lo que te ha pasado."
            "Fisa volteó su mirada, y en el reflejo de aquellos ojos pude ver... Compasión."
            cal "No lo hagas. No era una buena persona. Los humanos pueden guardar muchos buenos sentimientos y a su vez ser un animal..."
            cal "Significaba que podía hacer lo que quisiera, sin consecuencias. Podía robar, podía matar... Y no tenía que mirar atrás."
            cal "Eso era la verdadera libertad."
            cal "Pero al final, tenemos que enfrentar que no estamos solos, y lo que hacemos, repercute a todo nuestro alrededor."
            "El silencio volvió a caer entre nosotras, mientras me quedé pensando en lo que había dicho..."
            pause

    scene black with fade
    centered "31 de Octubre.\n5:00am\nLos Campos"
    scene campo with fade
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
    show player feliz at left with dissolve
    show calchona neutra at right with dissolve
    cal "He vivido oculta por cientos de años, ya había olvidado lo que se siente el calor."
    p "... Pero-"
    cal "No puedo culpar a mi Vestigio, he vivido fuera del Sol mucho antes que estar en él."
    cal "¿Tú lo tienes, verdad?"
    show player triste with dissolve
    "Al oir esas palabras, pude sentir como mi cuerpo se tensaba. Ella sabía."
    cal "Ven, siéntate. Correr de mí será inútil."
    "Lentamente, me acerqué a ella. Mi corazón estaba latiendo cada vez más fuerte."
    cal "Eres una buena niña, ..."
    cal "Veamos el amanecer juntas."
    "Al sentarme junto a ella, todos mis miedos resurgieron. Podía dejarla ir. Podía ignorar que la había visto, quizá Inaru pueda lidiar con ella."
    "Su lana, tan pálida bajo la luna, comenzaba a verse del blanco más hermoso que había visto. Fisa cerró los ojos."
    cal "Desearía... Poder llorar. Por mi familia, por mi pasado."
    cal "Por las cosas que vas a pasar de ahora en más."
    "Llorar..."
    "La marca está..."
    "Fisa se giró hacia mí, sus ojos reluciendo con cada palabra."
    cal "¿Debe doler, no? Ser una buena persona, forzada a hacer cosas malas..."
    "Si no lo hacía ahora... No llegaría a tiempo."
    "Mis uñas arrancaron las cáscaras que contenían la sangre de mi palma. Y sin más, apreté la mano contra los brillantes ojos de Fisa."
    "Podía ver como dos hilos carmesí caían por sus mejillas, tiñiendo la suave lana. Sus ojos quemaban sobre mi mano."
    cal "Nghhh--!!" with vpunch
    show player asustada with dissolve
    p "¡Lo siento! ¡Tengo que hacerlo por mi abuelo!"
    "Ambas manos sujetaron mi brazo con fuerza."
    hide player with dissolve
    show calchona at center with move
    cal "Tu abuelo es parte de tí."
    cal "Y..."
    cal "Ahora..."
    cal "Yo también."
    hide calchona with flash
    "Antes de que me diera cuenta, caí hacia adelante. El sol estaba iluminando el campo. Estaba sola. De mi bolsillo, cayó el vestigio, reluciente y lleno de vida."
    "Pero yo... Sentía que una parte mía se había desvanecido."
    "Lo que sea que haya hecho mi abuelo, espero haya valido la pena."
    "Por ahora, me levanté, volví a guardar el Vestigio y caminé de regreso a casa."
    jump normalEnding

label calchonaBadEnding:
    show player feliz at left with dissolve
    show calchona neutra at right with dissolve
    p "Quizá debamos descansar, no era mi intención quedarnos toda la noche."
    cal "Lo sé."
    cal "Quieres encerrarme de nuevo, verdad...?"
    show player asustada with dissolve
    "!!!"
    cal "Te envió ella. Dejaste que te convenciera de que esto era por tu bien."
    cal "Ojalá... No tuviera que ser así."
    p "No, espera. Escuchame, mi abuel-"
    "Antes de terminar, Fisa se abalanzó sobre mi, una mano me sujetó la cabeza con fuerza y la empujó contra el cesped." with vpunch
    hide player with dissolve
    show calchona at center with move
    cal "¡Lo siento, no puedo dejar que me entregues!"
    "Por favor..." with vpunch 
    cal "¿¡Que has hecho!?"
    "Basta..." with vpunch
    cal "¡Todo por lo que él ha peleado, ahora ha valido nada!"
    "No..." with vpunch
    cal "Lo arruinaste... {cps=4}Todo.{/cps}"

    scene black with fade
    pause
    "Bad Ending :("
    # Finaliza el juego:
    return

##########################################################
label pomberoRoute:
    default goodAnswersPombero = 0
    stop music fadeout 2.5
    scene black with fade
    centered "31 de Octubre.\n00:30am\nBosque de Suas Agascuana"
    scene campo with fade
    show player feliz at left with easeinleft
    "Una vez salí de la casa, tomé el camino más corto para llegar al bosque. "
    "Había oído historias de como niños como yo entraban al bosque a jugar por la noche, nunca pensé que sería yo quien entrara voluntariamente alguna vez."
    "..."
    "Las copas de los árboles se mecían sobre mí, danzando con el viento en un arruyo. Y aún así, puedo sentir como un peso caía sobre mí."
    show player triste with dissolve
    pom "Mh mh mh~!"
    "Un tarareo sonó en eco contra los troncos de los árboles, y luego pude verlo. "
    "Unos metros más adelante, una figura oscura se acercaba a un arroyo, cantando para sí."
    show player pensativa with dissolve
    p "Está... Alegre?"
    hide player with dissolve
    "Antes de ser descubierta, me escondí atrás de un árbol, observando." 
    "Era un duende, pero no se parece a nada que haya visto antes."
    show pombero neutro with fade
    pom "De los montes vengo...{w} A los montes voy...{w} A conocer a la niña que me ha visto hoy~"
    "!!!!"
    "Un escalofrío corrió por mi espalda. Sentía que estaban por cazarme. Me di vuelta al instante."
    scene campo with fade
    show player triste at center 
    show pombero neutro at right with easeinright
    pom "Ho-laa~!"
    show player asustada with dissolve
    p "¡Ah!"
    show player at left with move
    "Mis piernas se movieron por sí solas, y en un instante, me moví hacia un lado antes de quedar acorralada."
    "El duende bajó del árbol, una gran sonrisa adornando su rostro. Cada paso que daba hacia adelante, yo lo retrodecía."
    pom "Jaja... Ja. La niña tiene miedo!"
    "¡Necesito reaccionar rápido antes de que se acerque!"
    "¿Qué hago?"
    menu:
        "Correr":
            $ goodAnswersPombero += 1
            scene campo with fade
            "Sin pensarlo dos veces, me giré y eché a correr, internándome así en los bosques. Según Inaru, el lugar preferido de esta criatura."
            show player triste at left with moveinleft
            "Corrí entre los árboles, escuchando los ecos de la risa del Pombero. No sabía si estaba lejos o cerca de él, pero sabía que estaba cerca mío."
            "De pronto, la risa se desvaneció. Esos instantes fueron los únicos que necesite para determe a recuperar el aliento."
            pom "Niña lista, muy lista."
            show player asustada with dissolve
            "!!!"
            show pombero neutro at right with dissolve
            "Levanté la mirada, y estaba en cuclillas frente a mí! Incluso en la oscuridad, podía ver una enorme sonrisa, brillando frente a mí."
            pom "Para encontrarse, uno debe perdese, si si si. Niña lista, muy lista."
        "Enfrentarlo":
            "Sentía que mi corazón iba a salirse de mi pecho. Aún así, di un paso hacia adelante."
            show player enojada with dissolve
            p "¡No! ¡No le tengo miedo a criaturas como tú!"
            "De pronto, el Pombero dejó de reírse. Por unos segundos, aquel silencio sentía que me iba a devorar."
            "Finalmente, empezó a reir de nuevo."
            pom "Niña tontaa~!"
            hide pombero with dissolve
            "Con eso, desapareció entre los árboles."
            show player asustada with dissolve
            p "¿Qué? ¡Espera!"
            scene campo with fade
            "Salí a perseguirlo, las ramas tan cerca de mi rostro que sentía me golpearían en cualquier momento."
            "Cuando me quede sin aire, tuve que detenerme, con las manos descansando sobre mis rodillas."
            show player triste at left with moveinleft
            p "¿Donde... Donde se metió?"
            pom "Niña tonta"
            show pombero neutro at right with dissolve
            "El duende se apareció frente a mí."
            pom "Eres como un toro, corres hacia adelante lista para atacar, no puedes atravesar una montaña yendo hacia adelante~!"
    
    show player enojada with dissolve
    p "Deja de llamarme sí."
    pom "Mh?"
    p "Me llamo [playerName]."
    pom "Ugh, los humanos y sus nombres pretenciosos. Ustedes me llaman de mil maneras, ¿por qué no podría hacer lo mismo?"
    p "¿Cómo te gusta a tí que te llamen?"
    $ pom = Character("Har", color="#89909f")
    pom "Har! Es fuerte, intrépido, y solemne, si si si. ¡Digno nombre para mi persona!"
    "¿Y eso no es pretencioso?"
    pom "Niñas como tú no deberían estar vagando solas en el bosque, ¡hay monstruos, y cazadores, y hombres malos dando vueltas."
    p "¿Y qué haces tú aquí?"
    "Har ladeó la cabeza, y luego se echó hacia atrás, mirando a su alrededor."
    pom "Busco divertirme, los humanos son MUY divertidos, ¿sabes?"
    show player triste with dissolve
    "De pronto, sentí como el aire empezaba a volverse denso, como si los árboles estuvieran a punto de caer sobre nosotros."
    pom "¡Se creen realmente ingeniosos cuando en realidad son"
    pom "Torpes"
    pom "Egoístas"
    pom "Y débiles"
    pom "piden, piden, piden, y no saben que uno es más inteligente que ellos, jaja~!"
    "Incluso entre sus risas, podía ver lo enojado que estaba. Era aterrador."
    show player feliz with dissolve
    p "¿Quizá podemos hacer algo juntos?"
    pom "¿Quieres jugar conmigo? Niña tonta, pero valiente!"
    "De un salto, Har comenzo a alejarse."
    hide pombero with dissolve
    pom "Ven, niña lenta!"
    show player asustada with dissolve
    p "¡Espérame!"
    hide player with dissolve
    "Salí corriendo tras él, de nuevo. Solo unos minutos más tarde, llegamos a una pequeña laguna."
    show pombero neutro at right with easeinright
    show player triste at left with easeinleft
    pom "¡Tú eliges! ¿Qué quieres hacer?"
    p ". . ."
    p "Vamos a..."
    menu:
        "Nadar":
            $ goodAnswersPombero += 1
            show player feliz with dissolve
            p "Quiero ir a nadar."
            pom "¿Hm?"
            "Me di vuelta y observé la laguna, no había notado hasta ahora, pero los árboles daban completo paso a la luz de la luna para caer sobre el agua, haciendo del agua un espejo brillante."
            p "¡A que llego primero!"
            scene campo with fade
            "Luego de gritar, eché a correr hacia el lago, y pude oir como los pies de Har trastabillaban antes de salir corriendo tras de mí."
            "De un salto me metí en el agua, dejando que me cubriera por completo por un momento antes de sacar la cabeza."
            pom "¡Niña astuta, cree que puede ganarme!"
            "A diferencia de antes, Har parecía realmente entretenido dentro del agua."
            pom "Sígueme."
            "Tomando una gran bocanada de aire , que parecía más pretendida que otra cosa, él se sumergió en el agua."
            "Una vez de nuevo, nadamos un poco hacia el fondo, donde pude ver la forma de los peces que habitaban el lago."
            pom "Mira bien."
            p "?!"
            "Las manos de Har en mis hombros, me forzaron a parpadear varias veces, y las formas de los peces y las algas se veían más claramente. ¡Era increíble!"
            "A pesar de que las criaturas en el bosque aún dormían, las del agua estaban llenas de energía."
            "Volvimos a la superficie para recobrar el aliento, y Har ya estaba allí, flotando boca arriba, admirando a la Luna."
            p "Es hermoso."
            pom "Lo sé. No en todos lados es así."
            pom "Los bosques son fuertes, pero se mueven muy lentamente. Los humanos son rápidos. Quitan sin pensar."
            pom "No ven lo que hay a su alrededor."
            pom "¡Peeero yo soy más rápido!"
            "En un instante, lo pude ver moverse cerca mío."
            pom "Nadie es más rápido, o más fuerte que yo en los bosques. Si estoy aquí, nadie sería lastimado por un humano. Ningún árbol, o pez, ni nadie."
            "No estaba segura si era un comentario, o una amenaza. Sin embargo, no pude evitar sentir la fuerte conexión que Har tenía con los bosques."
            p "Entonces es bueno que estés aquí."
            "Har volteó la mirada."
            pom ". . ."
            pom "Niña lista."
        "Pescar":
            show player feliz with dissolve
            p "Podemos pescar aquí, o no?"
            pom "¿Hm?"
            "Me acerqué a uno de los árboles, de la cual sobresalía una rama larga y delgada."
            p "Podemos usar esto y mis cordones para hacer una caña!"
            "Ambas manos estaban sujetando la rama para tratar de romperla, cuando Har puso una mano en mi hombro y con mucha fuerza me arrojó al agua."
            scene campo with fade
            "Logré pedalear de nuevo a la superficie, solo para ver a Har nadando hacia mí."
            pom "¡Sorpresa! Niña tonta necesita prestar más atención~"
            p "{i}cof cof{/i} ¡Eso no fue nada amable!"
            pom "Tú no has querido ser amable con los peces tampoco"
            "Con una pequeña risa, Har empezó a nadar en círculos a mi alrededor. Me recordaba a los tiburones."
    
    "Eventualmente, salimos del agua, y me tiré en el cesped."
    show player feliz at left with dissolve
    show pombero neutro at right with dissolve
    "La noche se sentía aún bastante calurosa, así que la ropa mojada no me molestaba en lo absoluto. Al mismo tiempo, Har se sentó contra un árbol."
    "Por el rabillo del ojo, pude ver como desenterraba un cigarro de entre las raíces y se lo ponía entre los labios. ¿Hace cuanto que tenía eso ahí?"
    show player pensativa with dissolve
    p "Quiero preguntarte algo."
    pom "Bien por ti."
    show player triste with dissolve
    p "¿Qué haces aquí?"
    "Del suelo, levantaba una hoja seca, y con un chasquido de sus dedos, causó un chispazo que encendió la hoja."
    "Lentamente la guió al cigarro, sacudiendo los restos de la hoja una vez éste estaba encendido."
    pom "Me recuerda a mi hogar. Vengo de un lugar parecido a éste."
    "Har exhaló el humo de su cigarro, como si hubiera estado perdido en sus pensamienos."
    pom "¿Qué hay de tí? ¿Por qué estás aquí?"
    "Por un largo rato, me quedé en silencio."
    show player feliz with dissolve
    p "Quiero hacer un trato."
    pom ". . ."
    pom "¿Ah sí?"
    "Volvió a dar una calada. Mi corazón se encogió."
    pom "Que... Coincidencia. Parece que estás en el lugar ideal."
    pom "¿Y qué podría querer una niña como tú de mi?"
    menu:
        "Seamos amigos.":
            $ goodAnswersPombero += 1
            p "Seamos amigos."
            pom ". . ."
            pom "Ja... Jaja"
            pom "Jajajajajajajaja!"
            "Sacándose el cigarro de la boca, Har lanzó una carcajada al cielo."
            show player triste with dissolve
            p "¿Q-Qué? ¡¿Qué dije?!"
            pom "¿Tú quieres que seamos amigos? Eso sí que es nuevo."
            pom "Ciertamente no dirías eso si supieras todo lo que dicen de mí en mi pueblo, niña tonta."
            pom "Soy un protector del bosque, no un humano."
            p "¿Por qué odias tanto a los humanos?"
            pom "¿Odiarlos? No no no, niña tonta, no es así. Los humanos son quienes me detestan a mí."
            pom "Cazadores, pescadores, leñadores..."
            pom "A mí no me interesa lo que los humanos hagan, pero cuando destrozan, matan, corrompen... Me enfurecen."
            "Otra exhalación, dejó el rastro de humo desvanecerse en el aire."
            pom "Podría decirse que me convertí en el monstruo que les convenía a ellos. Dicen que huyas porque podría atacar en los pastizales, les dicen a las mujeres que no salgan de sus casas."
            pom "Algunos humanos son listos. Y hábiles cuando se trata de desviar la atención de sus monstruosas acciones."
            pom "Ya no quedan criaturas como yo. Casi todas están muertas, y las que no, como yo, son antagonizadas."
            pom "Sólo somos leyendas destinadas a olvidarse."
            p "..."
            show player feliz with dissolve
            p "Yo no voy a olvidarte."
            pom "Ja..."
            pom "Niña inocente."
            "Luego de ello, nos quedamos hablando por horas. Har me contó sobre las selvas donde vivía. Y antes de darme cuenta, comenzó a amanecer."
        "Cuida de este bosque.":
            p "A tí te preocupan los bosques, ¿verdad? No quisiera que lastimes a nadie. Pero me gustaría que siguieras cuidando de los bosques."
            "Har exhaló el humo de su cigarro, y giró la cabeza hacia mí."
            pom "Dime, ¿por qué las vidas humanas valen más que las de cualquier otra criatura?"
            show player triste with dissolve
            p ". . ."
            pom "Humanos matan a sus propios niños, arrancan las plumas de las aves para descansar cómodamente."
            pom "Desuellan mamíferos vivos por moda. Torturan en vida. Queman. Ahogan. Electrocutan. Dime, ¿por qué no puedo devolverles la gentileza?"
            pom "¿Quien te da la autoridad y el poder de decirme que sería o no correcto?"
            "Me quedé en silencio. Con cada palabra, podía sentir la tierra temblar a través de las raíces."
            p "Lo siento."
            pom "No tienes que disculparte. Eres solo una niña."
            "Seguimos hablando el resto de la noche... Y pude entender un poco más de la relación de Har con los humanos."

    scene black with fade
    centered "31 de Octubre\n5:00am"
    scene campo with fade
    show player feliz at left with dissolve
    show pombero neutro at right with dissolve
    "Cuando los primeros haces de luz empezaron a aparecer entre los árboles, Har volvió a hablar."
    pom "Creo recordar que tú querías hacer un trato."
    show player triste with dissolve
    p "¿Eh?"
    "No pensé que hubiera estado dispuesto a aceptar..."
    pom "Quizá es momento de discutir mis condiciones."
    if goodAnswersPombero == 3:
        jump pomberoGoodEnding
    else:
        jump pomberoBadEnding

label pomberoGoodEnding:
    $ persistent.pomberoEnding = True
    pom "Sabes, hace años, conocí a este hombre."
    pom "Era astuto, pero también tenía esto... Humanos siempre le dicen \'corazón\', pero todos tienen uno."
    pom "Era algo distinto. Algo como tú lo tienes."
    pom "Luz."
    pom "Si... Eso es lo que era... Luz."
    p "..."
    pom "Jamás lo resentí por encerrarme, sabía que cuando el tiempo sea el correcto, volvería a este mundo, y aún habría mucho por hacer."
    pom "Él me decía 'el mundo no puede depender de tí. Si tiene que morir, morirá y no habrá nada que podrás hacer'."
    pom "Y él tenía razón, este mundo ya no es para criaturas como yo."
    pom "Si algo me da tranquilidad, es que aún hay criaturas como tú."
    pom "Este mundo... Es más tuyo que mío."
    p "Har..."
    pom "Mis condiciones."
    pom "Escucha lo que el mundo tiene que decir. Hay voces que merecen ser oídas."
    pom "Yo no soy de dar regalos. Así que toma esto y no lo cuestiones."
    pom "No creas en las intenciones de nadie. Nadie es altruista, y todo el mundo tiene una razón para hacer algo. Escucha a sus acciones más que su palabras."
    "Sabía que no respondería ninguna de mis preguntas, no importa cuanto me gustaría hacerlas... Y me estaba quedando sin tiempo."
    p "¿Qué quieres a cambio?"
    "Otra vez, sonrió. Una mano sujeto la mía y rasgó la piel de mi palma. Luego se la llevó al oído."
    show player asustada with dissolve
    pom "Ah, sí... Justo lo que imaginaba..."
    show player triste with dissolve
    pom "Hasta Luego [playerName]."
    hide pombero with flash
    "En cuestión de segundos, en lugar de ver el rostro de Har, estaba viendo mi mano ensangrentada."
    "!!"
    "De mi bolsillo el Vestigio cayó contra el suelo, brillante, pesado y lleno de vida. Har sabía de mi abuelo, estoy segura. Me hubiera gustado saber más de lo que hacía."
    "Me gustaría saber... Que hubiera hecho él en este momento."
    "Tomé el Vestigio y volví a guardarmelo en el bolsillo."
    p "Hasta luego, Har."
    hide player with dissolve
    "Es hora de volver a casa..."

    jump normalEnding

label pomberoBadEnding:
    p "Uhm, de acuerdo."
    p "¿Qué quieres a cambio?"
    "Una sonrisa se dibujó en sus labios antes de salir corriendo."
    scene campo with fade
    p "No de nuevo.. ¡Har, espera!"
    "Salí tras él una vez más. Corriendo entre los árboles, como persiguiendo el aire."
    "Me detuve de pronto, y miré para todos lados."
    show player triste at center with moveinleft
    p "¡Har!"
    pom "Esa bruja realmente se cree lista, ¿no?"
    "Giré la mirada, pero no podía verlo. Su voz hacía eco por todas partes."
    pom "Pobre, pobre niña, cayó en los encantos de una bruja del bosque y pensó que podía ser amiga de todas las criaturitas del bosque."
    "El aire dejó mis pulmones."
    pom "Pobrecilla~ "
    pom "Pero no te preocupes, puedo hacer lo que me pides. Este bosque estará a salvo y tú y yo seremos amigos."
    pom "Te quedarás aquí."
    pom "Para siempre."
    show pombero neutro at right with dissolve
    show player asustada with dissolve
    "De golpe, sentí un fuerte empujón, y las hojas detrás mío desaparecieron." with vpunch
    "Estaba cayendo... La sonrisa del duende alejándose."
    hide player with dissolve
    show pombero at center with move
    pom "Adios, niña tonta~!"
    "!!!" with vpunch
    scene black with fade
    pause
    "Bad Ending :("
    # Finaliza el juego:
    return

##########################################################
label silbonRoute:
    default goodAnswersSilbon = 0
    stop music fadeout 2.5
    scene black with fade
    centered "31 de Octubre.\n00:30am\nPueblo"
    scene fondo pueblo decorado with fade
    show player feliz at left with easeinleft
    "Si había un lugar donde podía sentirme en mi elemento, era el pueblo.. Los festivales ya comenzaron y hay muchísima gente caminando alrededor, niños y adultos por igual..."
    "Me hubiera gustado poder disfrutarlos mejor..."
    "Al caminar a través de los puestos de comida, vi una figura que escondía su rostro bajo su sombrero, una mano sujetando una gran bolsa sobre su hombro."
    hide player with dissolve
    show silbon neutro with dissolve
    sil "Ciervo ciervo... Si si si... En tiras, en cubos, en rebanadas..."
    sil "Aguardiente, ohhh, aguardiente, calienta los huesos. El polvo de hueso que se rompe, y se rompe y se rompe."
    p "Ese es...?"
    "Aquel joven caminaba encorvado, murmurando para sí mismo, con cada palabra, podía sentir como su lengua se pegaba a sus dientes y dejaba pasar un leve silbido."
    "Se veía... Horripilante."
    "Lentamente caminé hacia él, fijando la mirada en los puestos cercanos. Nadie parece prestarle atención, como si no existiera."
    "{i}Fiu...{/i}"
    "El silbido chirrió junto a mi oído, y mis ojos se abrieron de par en par."
    show silbon at right with move
    show player asustada at left with easeinleft
    sil "¿Qué crees que haces?"
    "Me giré hacia él."
    p "¿Eh?"
    show player triste with dissolve
    sil "Miras, miras y miras, ¿Qué buscas, que quieres?"
    "Bajo el sombrero, podía ver el destello de unos ojos llenos de odio. Nunca había visto algo así."
    show player pensativa with dissolve
    "¿Que hago? Necesito pensar rápido."

    "Decisión 1"
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
    scene black with fade
    centered "31 de Octubre\n6:00am"

    scene fondo casa lejos with fade
    show player triste at right with easeinright
    "A esta hora, ya apenas podía oírse el festival, ya no había gente en la calle y la música estaba apagada."
    "Siento que todo el peso de una larga noche caía sobre mí y no estaba pensando en nada más que dormir."
    # Entra a la casa
    scene fondo sala with fade
    show player triste at right with dissolve
    "Veo este lugar, y es como si no hubiera estado esta mañana."
    "Sólo espero que Inaru haya tenido suerte..."
    # Entra a la habitación del abuelo
    scene fondo dormitorio with fade
    show player triste at left with easeinleft
    "..."
    # Aparece la Madre Monte
    play music "audio/madre-monte-loop.wav" fadein 1
    show mmonte neutra at right with dissolve
    mm "Vaya, al fin llegas, ¿cómo te fue?"
    "Sin decir mucho, saqué el Vestigio de mi bolsillo, y lo puse en la caja."
    "Los otros dos lucen preciosos..."
    "..."
    "Se sienten... Tan familiares."
    mm "¿Cómo te sientes?"
    p "Estoy... Muy cansada."
    mm "Lo has hecho bien. Superaste mis expectativas."
    p "Hm?"
    mm "Quizá debería habertelo dicho antes."
    mm "Estos Vestigios...{w} Usaron algo más que la sangre de tu abuelo."
    mm "Se necesita un gran poder para mantener a una Leyenda dentro de ellas."
    mm "Es por eso que su alma era necesaria."
    # Madre Monte se transforma y se vuelve OP
    show mmonte ulti with flash
    show player asustada with dissolve
    p "!!!!"
    mm "O una porción de su alma, para ser precisa."
    mm "Usando tu sangre, pude sellar parte de tu alma en dos de las Leyendas."
    mm "Y tú me ayudaste con el tercero."
    "Su mano se apoyó contra su pecho."
    mm "Ahora parte del alma de Lucio vive aquí. Y tú tienes la otra parte."
    mm "No por mucho."
    stop music fadeout 5
    show mmonte at center with easeoutright
    p "¿Qué? ¡AGH!" with vpunch
    "Mi cabeza... Duele."
    "Sí que caíste, niña tonta."
    "Pobrecilla."
    "No no no, ¡dejame salir!"
    "Son demasiadas voces. Gritando. Gritando."
    p "¡Aghh! ¡Basta!" with vpunch
    mm "¿Duele verdad? Imagino que tu abuelo habrá lidiado con algo similar con años. Merece ser liberado de esa tortura."
    mm "Que suerte que apareciste. Ahora es tu alma la que las mantendrá a raya."
    "Las ramas de sus manos todavía estaban enrojecidas. Esa era... Mi sangre."
    "Un dedo presionó en mi frente."
    p "AHHH!" with vpunch
    mm "Ah... Lucio... Allí estás."
    mm "No te preocupes, pequeña [playerName]. No te dejaré pasar por lo que tu querido abuelo tuvo que pasar."
    mm "Cuando te suelte... Ya no sentirás tanto dolor. Guardaré lo que quede tu alma en mi Vestigio."
    p ". . ."
    mm "Hasta siempre, [playerName]. Descansa sabiendo que has liberado a tu abuelo."
    p "¡No! ¡Espera!"
    scene white with flash
    "Todo se vuelve blanco"
    "Ya no estoy en la casa del abuelo... Inaru no está."
    "Realmente... ¿estoy encerrada en su Vestigio?"
    p ". . ."
    p "No..."
    p "No, no, no..."
    p "¿Qué hice?"
    p "¿¡Alguien me escucha!?"
    "No veo a nadie a mi alrededor. Y las voces en mi cabeza desaparecieron."
    "Estoy sola..."
    p "No, por favor..."
    p "Por favor, mamá... Ayúdame."
    abu "[playerName]..."
    p "!!!"
    p "¿¡ABUELO!?"
    if persistent.calchonaEnding == True and persistent.pomberoEnding == True and persistent.silbonEnding == True:
        jump trueEnding
    else: 
        "Normal Ending."
        # Finaliza el juego:
        return

##########################################################
label trueEnding:
    $ abu = Character("Lucio", color="#5a80d3")
    show abuelo neutro with dissolve
    abu "Hola, ..."
    p "ABUELO."
    "No sé si realmente es parte de un sueño, apenas puedo verlo."
    "Mi vista empieza a volverse borrosa, pero yo me muevo para adelante. Cuando lo abrazo, puedo sentir allí, es real..."
    "Mi abuelo..."
    "Estaba conmigo."
    show abuelo at right with move
    show player feliz at left with dissolve
    abu "Lo siento mucho, calabaza.. Hay tanto de que hablar..."
    abu "Lamento todo lo que has tenido que pasar por mí."
    show player triste with dissolve
    p "Pero abuelo... Me atrapó. Inaru... Todo esto lo hizo para..."
    abu "Lo sé."
    p "..."
    abu "Inaru solo es un eco de mis sentimientos y mis recuerdos, igual que todos los demás."
    p "?!"
    abu "Verás, .... Hay algo especial en las Leyendas."
    abu "Algunas son temidas, otras son admiradas."
    abu "Las historias corren a través de los años. Pero son eso. Historias."
    abu "Una Leyenda no puede ser buena, ni mala. No conoce de eso. Nosotros, los humanos, somos quienes juzgamos su valor."
    abu "Una leyenda, no es más que energía. Y como tal, se alimenta de lo que absorbe a su alrededor."
    abu "Es lo que solía hacer, otorgaba mi energía a las Leyendas que encontraba. Les daba un poco de mi ser."
    abu "Así, dentro tuyo, puedes sentir como si ya los conocieras."
    show player pensativa with dissolve
    p "¿Como si los conociera...?"
    # Recuerdo
    scene black with fade
    show calchona neutra with dissolve
    cal "Cuando haces mucha fuerza, no sientes si en verdad hay o no alguien contigo."
    scene black with fade
    show pombero neutro with dissolve
    pom "Si algo me da tranquilidad, es que aún hay criaturas como tú."
    scene black with fade
    show silbon neutro with dissolve
    sil "(Frase)"
    scene black with fade
    scene white with flash
    # Fin Recuerdo
    show player feliz at left with dissolve
    show abuelo neutro at right with dissolve
    p "!!!!"
    p "¡Los escucho!"
    p "Entonces las... Las leyendas."
    abu "Eran parte mi alma."
    abu "Y ahora son parte de la tuya. Son un reflejo de lo que eres. Lo bueno, y lo malo."
    p "..."
    "Fisa... Har... Wiija..."
    "Ahora son parte de mí. De pronto, eso me causa mucha tranquilidad. Como si aquel miedo comenzara a desvanecerse por completo."
    "Lo único que queda... Es un cabo suelto."
    show player triste with dissolve
    p "Abuelo..."
    p "¿Cómo es que estás aquí?"
    abu "¿Hm?"
    abu "Oh, claro."
    abu "Bueno siempre he estado aquí."
    "Su mano se apoya en su esternón."
    abu "Siempre he estado contigo, ..."
    abu "Tú eres mi vestigio."
    p "..."
    p "¿Eh?"
    abu "Quizá haya mucho que explicar."
    abu "Tu madre... Amaba a este lugar, y era igual a tí. Intrépida, aventurera. Pero ella no quería capturar a las leyendas, creía que era un precio alto que pagar."
    abu "Ella decía, que eso les quitaba su libertad de decidir, de ser su propio ser, para bien o para mal."
    abu "Y temía por mí, por lo que ocurriría con mi alma una vez ésta abandonase mi cuerpo."
    abu "Así que... Selló una parte de mí en sí misma antes de irse."
    abu "Creía que así podría protegerme y ella nunca se volvería a acercar a los Vestigios."
    abu "Pero luego, tú naciste. Creo que ninguno de nosotros sabía realmente que ahora tú llevabas mi alma."
    abu "Cuando me di cuenta, ya era demasiado tarde y con una conexión tan débil, no pude advertirte."
    p "Entonces esa voz que oí..."
    abu "Era yo."
    abu "Sabía que Inaru intentaría recuperar los fragmentos de mi alma."
    abu "Pero ella, al igual que yo, no contaba con que tú fueras el último Vestigio."
    abu "Eso nos da una esperanza."
    abu "Y lamento que haya llegado a esto."
    p "Lo sé."
    abu "..."
    show player feliz with dissolve
    p "Está bien, abuelo. Mamá, papá y tú... Son mi familia. Haría lo que sea por ustedes."
    p "Inaru me pidió que selle a las Leyendas, usando mi sangre. Eso hizo que las Leyendas volvieran a quedar encerradas en los Vestigios."
    abu "Todas las Leyendas. Menos una."
    p "Significa que ahora..."
    abu "Debes sellar a Inaru. Si."
    show player triste with dissolve
    p "..."
    show player asustada with dissolve
    p "¿Cómo haré eso?"
    abu "A través de mí. Por supuesto."
    show player triste with dissolve
    abu "Tú tienes la última parte de mi alma. Ella tiene las demás, pero es tu sangre la que mantiene la conexión."
    abu "Si lo haces-"
    p "Los sello a ambos."
    p "..."
    show player pensativa with dissolve
    p "¿Qué pasará contigo?"
    abu "Yo no tengo un Vestigio. Este lugar le pertenece a Inaru. Así que mi alma desaparecerá."
    show player triste with dissolve
    p "Abuelo..."
    abu "Lo siento, calabaza."
    p "No puedo dejarte desaparecer."
    abu "¿Desaparecer?"
    abu "Por supuesto que no."
    abu "Seré libre. Podré ser lo que yo quiera."
    abu "Tu madre... Ella tenía razón."
    abu "Yo ya hice todo lo que pude. El resto, te lo encargo."
    "Bajé la mirada. Podía sentir aún la cicatriz de mi palma, aún no terminaba de sanar. Cuando la otra mano la cubrió, pude sentir a mi abuelo abrazándome nuevamente. Cerré los ojos con fuerza."
    abu "Lo hiciste muy bien... Cuidate mucho, calabaza."
    show player feliz with dissolve
    "Podía sentir su corazón latiendo. Cuando era pequeña, eso siempre me calmaba. Me hacía sentir protegida. Ahora, mi mano se apoyaba sobre él."
    p "Adios, abuelo"
    # Volvemos a la habitación del abuelo
    scene fondo dormitorio with flash 
    show player feliz with dissolve
    p "He vuelto..."
    show player at left with move
    show mmonte ulti at right with dissolve
    mm "Ngh-!" with vpunch
    show player asustada with dissolve
    p "!!!!"
    "Al voltear, pude ver a Inaru de rodillas, su cuerpo templaba, como si estuviera resistiendo el desaparecer."
    show player triste with dissolve
    "Mi pecho se encogió. Debería estar furiosa. Había hecho tanto mal. A mí, a las otras Leyendas."
    "Pero lo hizo por mi abuelo... Y ahora estaba desvaneciendose nuevamente en el Vestigio."
    mm "No, Lucio, él..."
    "Me arrodillé frente a ella. Inaru de regreso, me miró a los ojos."
    mm "Lo estoy perdiendo."
    "Una mano se apoyó en su brazo. Era quizá una de las decisiones más difíciles que tuve que tomar."
    p "Está bien..."
    p "Yo tampoco quiero perderlo..."
    p "Pero él decidió hacer con su tiempo lo que más deseaba."
    show player feliz with dissolve
    p "Creemos algo nuevo a partir de lo que nos dejó."
    mm "..."
    "Sus ramas sujeron mi mano. Su agarre tenso y su cuerpo aún temblando."
    mm "Lo has dejado morir... No puedo perdonarte por eso."
    mm "Pero no puedo sostenerlo cuando se escapa de mis manos."
    mm "...."
    mm "Una vez eso ocurra, será tu alma la que esté dentro mío, y lentamente, olvidaré al Maestro."
    mm "Sólo las Leyendas perduran en el tiempo. Los humanos desaparecen, y uno a uno, serán olvidados."
    show player triste with dissolve
    "Con sus palabras, podía sentir su profunda tristeza. Quedar en el olvido podría ser una de las cosas más terroríficas que un alma podría vivir. Podía entender lo que Inaru estaba sintiendo."
    show player feliz with dissolve
    "Pero no podía aceptarlo."
    p "Entonces te hablaré sobre él."
    p "Te contaré sobre todo lo que aprendí y ni tú ni yo lo vamos a olvidar."
    "Inaru me observó, y casi derrotada, la pude ver sonreir."
    mm "Vaya..."
    mm "Si que eres..."
    mm "Su nieta..."
    hide mmonte with flash
    # Se desvanece, wooo, F
    show player triste with dissolve
    pause
    show player at center with move
    "..."
    pause
    "Inaru..."
    "Ahora entiendo."
    "He pasado una noche tan larga, y he descubierto tanto sobre el abuelo"
    "Nuevamente todos los Vestigios volvieron a su caja. Pero... Lo que dijo el abuelo..."
    "..."
    "Los Vestigios."
    "Quizá... Quizá ella tenga razón"
    # Puerta abriéndose
    play sound "audio/puerta.ogg" volume 0.5
    "???" "[playerName]! ¿Estás ahí?"
    p "..."
    show player feliz with dissolve
    p "Mamá!!"
    pause
    scene black with fade
    centered "Fin"
    # Finaliza el juego:
    return