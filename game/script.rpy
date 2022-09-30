label splashscreen:
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
    #centered "Casa del abuelo.\n30 de Octubre\n4:00pm"
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
    p "Ahora... La casa del abuelo estaba hacia el final de la calle..."
    "Recordaba que estaba alejada del pueblo. Esa era una de las mejores cosas."
    "Está cercana a los campos, por lo que hay mucho espacio."
    "Mamá siempre me contaba que el abuelo adoraba eso."
    "Que desde pequeño siempre salía a explorar y se internaba en los bosques."
    show player asustada with dissolve
    "Una vez, el abuelo me mostró su colección de insectos, ¡Guacala!"
    show player feliz with dissolve
    p "Será mejor que me de prisa."
    scene black with fade
    centered "Casa del abuelo. \n30 de Octubre. \n4:00pm."
    scene fondo casa lejos with fade
    show player feliz at right with easeinright
    "Mis padres estaban muy ocupados para venir hoy, pero yo no puedo perderme el festival de Halloween."
    "¡Siempre fue mi preferida!"
    
    scene fondo casa frente with fade
    p "¡Whoa! Siempre olvido lo grande que es."
    "Sé que mamá pidió que la limpiaran antes que llegáramos, ¡Cuánto trabajo!"
    "El abuelo nunca la cuidaba demasiado. Sé que era la abuela quien le gustaba quedarse en casa."
    "Yo no la conocí. Así que me crié solo con las historias del abuelo y sus aventuras."
    "Mamá siempre se enfadaba porque cada vez que veníamos había algo que reparar."
    "Pero siempre las cosas de la abuela las mantenía pulidas con mucho cariño."
    "Supongo que era una una relación de mucho afecto."
    "Él cuidaba de los jardines y los campos. Ella del hogar. Ambos parecían ser un gran equipo." 
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
    p "La cocina está en mejor estado de lo que recuerdo..."
    show alfajores at truecenter with dissolve
    "Cuando era pequeña, solía ayudar al abuelo a hacer alfajores."
    "Hacíamos un desastre, ¡pero quedaban deliciosos!"
    hide alfajores with dissolve
    # menu:
    #     "Examinar sala":
    #         pass
    show retrato at truecenter with dissolve
    "La sala está llena de fotos de nosotros. Mamá y el abuelo solían ser muy compañeros."
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
    play sound "audio/yawn-002.wav"
    p "Yaaawwwwnn..."
    p "El viaje ha sido realmente agotador."
    p "Creo que mejor voy a descansar un poco."
    hide player with dissolve
    "Esta casa posee muchos recuerdos... Tanto para mí como para mi mamá."
    "Ya quiero ver su reacción cuando venga..."
    jump dream

label dream:
    # TODO Fade out
    stop music fadeout 3.0
    scene black with fade
    pause
    centered "\"{cps=10}[playerName!q]...{/cps}\""
    centered "\"No le creas.\""
    centered "\"Ten cuidado.\""
    centered "\"Está aquí.\""
    centered "\"{cps=5}Esperándote...{/cps}\""
    pause
    jump festival

label festival:
    #centered "Casa del Abuelo.\n 30 de Octubre.\n8:00pm."
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
    centered "Pueblo Liwen. \n30 de Octubre. \n8:00pm."
    scene fondo pueblo decorado with fade
    play music "audio/intro-loop.wav" if_changed fadein 1
    show player feliz at left with moveinbottom
    p "¡Wow! Hay muchísima más gente de la que recordaba."
    "Todos los años, el pueblo hace un gran festival por Halloween. Los preparativos empiezan muchas semanas antes, y el evento dura dos días."
    "Pero siempre lo mejor es durante la noche del 31:\nhay danzas, disfraces y muchísima comida."
    show player at right with move
    "El abuelo me contó que cuando mamá era adolescente, ella ponía a coserse la ropa desde un mes antes, y salía a las calles con sus amigos."
    "Siempre se maquillaba de maneras espeluznantes y todo el mundo quedaba encantado. Es la fiesta turística del pueblo."
    "Mamá siempre contaba que desde hacía siglos, el pueblo tenía una gran conexión con el Otro Mundo"
    "...y mientras conociéramos nuestras raíces y quienes éramos, nada podía hacernos daño."
    "Ella dice que se sentía más cómoda como un monstruo entre humanos. Me encantaría volver a verla así."
    jump grampasBox

label grampasBox:
    scene black with fade
    stop music fadeout 3.0
    centered "Casa del Abuelo. \n30 de Octubre. \n11:55pm"
    scene fondo casa lejos with fade
    show player bostezo at right with easeinright
    p "Phew... Estoy agotada, pero ha sido realmente divertido!"
    show player feliz with dissolve
    p "Que suerte que aquí la celebración es hasta mañana, seguro mamá lo disfrut-"
    show player triste with dissolve
    p "¿Eh?"
    play music "audio/ambiente-lento-loop.wav" fadein 2
    show player asustada with dissolve
    "Veo luz saliendo de la puerta entreabierta, las luces del resto de la casa se encuentran apagadas"
    p "¿Quién anda ahí...?"
    "Viene de la habitación del abuelo... No he estado allí desde hace años."
    show player triste with dissolve
    menu:
        "Acercarse":
            pass
    stop music fadeout 2.0
    scene fondo escaleras with fade
    p "¿Hola?"
    p ". . ."
    "Que extraño, nadie me dijo que alguien vendría hoy, ¿Será una broma?"
    # [Empiezan a oirse susurros, la luz se ve saliendo desde la puerta entreabierta
    menu:
        "Entrar":
            pass
    play sound "audio/puerta.ogg"
    scene fondo dormitorio with fade
    # "Se abre la puerta, la habitación está vacía, se ve la cama, y junto a ella, la caja de donde sale esa luz."
    # "Hay más susurros, el ambiente es cada vez más tenso"
    "Este lugar está tal y como recordaba... Es como si el abuelo jamás se hubiese ido. {w}Pero... {w}Esa caja..."
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
    p "¡AGHHH!"

label meetMadreMonte:
    # personaje ???
    play music "audio/madre-monte-loop.wav" fadein 0.5
    scene fondo dormitorio with fade
    show mmonte neutra with dissolve
    mm "Vaya..."
    menu:
        "\"¿Quién eres?\"":
            pass

    mm "¿Quién soy yo? ¿Qué no te han enseñado nada?"
    # Cambia a Inaru
    $ mm = Character("Inaru", color="#2a7f62")
    mm "Vaya, ese fue un descanso largo..."
    show mmonte at right with move
    show player asustada at left with easeinleft
    p "Pero... ¿¡De dónde has salido!?"
    p "Yo abrí esa caja... Y de pronto estabas aquí."
    mm "... No sabes nada, ¿verdad?"
    mm "Me llamo Inaru. Soy una protectora de los bosques, ¡por supuesto!"
    mm "O lo era, hasta que quedé bajo las órdenes del Maestro, he vivido en esta caja por cuarenta largos años!"
    p "¿¡Cómo!? ¿¡Mi abuelo es tu maestro!?"
    mm "Pues parece que sí, tanto yo como los otros estábamos bajo sus ord-"
    mm "..."
    "Inaru se volteó a ver la caja.{w} Se quedó mirándola en silencio antes de voltear a verme."
    mm "¿¡Qué hiciste!? ¿¡Fuíste tú!?" with vpunch
    mm "¡No debiste haber hecho eso, niña tonta!"
    mm "... Si yo estoy afuera, quiere decir que los demás también."
    menu:
        "\"¿¡Los demás!?\"":
            pass
    mm "..."
    mm "Realmente no sabes nada."
    mm "Míralo tu misma"
    show player triste with dissolve
    # ((Paneo a la caja, con los cuatro objetos inanimados, sin luz))
    mm "Estos son Vestigios."
    mm "Reliquias que tu abuelo perfeccionó para capturar a las Leyendas que habitan este mundo."
    mm "Una Leyenda puede ser cualquier cosa: un espíritu, un monstruo, un objeto poseído, cualquier criatura atrapada en una época que no le pertenezca."
    mm "Tu abuelo ha dedicado su vida a capturar y atrapar Leyendas, al igual que su padre antes que él."
    mm "Aparte de mí, ha podido capturar a tres Leyendas: {w}el Silbón, {w}la Calchona {w}y el Pombero." 
    mm "Criaturas que vagaban el mundo causando terror antes de que tú las liberaras nuevamente." 
    mm "Ahora es tu responsabilidad encontrarlas y capturarlas de nuevo dentro de los Vestigios."
    "Estaba bromando... Debía ser una broma."
    show player asustada with dissolve
    menu:
        "\"¿Y cómo voy a hacer eso?\"":
            pass

    mm "Tendrás que convencerlos, por supuesto!"
    mm "No estoy esperando que puedas derrotarlos y forzarlos dentro del Vestigio, no pareces muy fuerte."
    show player triste with dissolve
    mm "Las Leyendas son criaturas suspicaces, si sienten que eres una amenaza, será más difícil atraparlos."
    mm "Ahí tu corres ventaja, van a subestimarte."
    show player enojada with dissolve
    p ". . ."
    mm "Tu familia usó un hechizo para encerrarlos.{w} Si escaparon, es porque éste se ha debilitado, pero aún tienes la oportunidad de volver a darle fuerza."
    show player triste with dissolve
    mm "Cada Leyenda tiene una marca, si tienes la sangre de tu abuelo, usar un poco de tu sangre sobre la marca será suficiente para devolver su alma a los Vestigios."
    p "Mi sangre..." 
    p "Esto no tiene sentido, ¿por qué mi abuelo nunca nos lo diría?"
    mm "No lo sé. Pero ahora no tienes elección."
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
            mm "El Pombero es un duende, del color de la noche. Con los humanos es el más impredecible, pero posee un gran cariño y respeto por los bosques."
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
    "Estaba segura de que tenía una fuerte conexión con lo que estaba ocurriendo."
    mm "Se que es mucha información, y no tenemos mucho tiempo."
    p "Hoy es el festival, y hay mucha gente aquí que podría correr peligro, ¿No causarán el caos?"
    mm "Los humanos no ven nada que no quieren ver, y las Leyendas no se hacen notar a menos que quieran ser vistas."
    mm "Ahora, ellos también están recobrando sus fuerzas, pero no les llevará mucho hasta que empiecen a moverse nuevamente."
    "Me pregunto si realmente puedo confiar en Inaru de la manera que ella espera que lo haga..."
    mm "Oye..."
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
    mm "Nada de lo que hagan podrá resultar. Solo tú tienes la sangre de tu abuelo."
    p "Pero, ¿Cómo puedo usar mi sangre?"
    "En un instante, Inaru sujetó mi mano."
    mm "Cierra los ojos."
    "En un reflejo, obedecí justo cuando sentí la piel de mi palma abrirse."
    show player asustada with dissolve
    p "Agh!" with vpunch
    "El líquido comenzó a brotar, humedeciendo mi mano."
    "Sus dedos rígidos pasaron sobre mi palma."
    "Cuando abrí los ojos, mi mano estaba seca y las yemas de Inaru brillaban de un color carmesí.{w} La herida de mi mano rapidamente comenzó a cicatrizar."
    mm "Para encerrar nuevamente a las Leyendas, necesitas encontrar el lugar donde tu abuelo ha puesto el hechizo y debes marcarlo con tu sangre."
    show player triste with dissolve
    mm "Yo puedo forzar a dos de las Leyendas de nuevo dentro de su Vestigio usándola tambien, pero enfrentarme a los tres podría matarme."
    "Su mano se posó sobre mi mejilla, podía sentir el calor a través de su palma."
    mm "Lo siento, hubiera querido que las cosas fueran diferentes. Aún así, la última decisión la tienes tú."
    mm "¿Deseas ayudarme a salvar lo que tu abuelo ha intentado proteger?"
    menu:
        "\"Sí, voy a ayudarte.\"":
            jump missionAccepted
        "\"¡No! ¡De ninguna manera!\"":
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
    "Bad Ending."
    # Finaliza el juego:
    return

label missionAccepted:
    show player feliz with dissolve
    mm "Gracias... Sé que esto no es fácil."
    mm "Entonces ya está decidido."
    mm "Luego de vivir tantas décadas con ellos, puedo sentirlos."
    "Inaru camina hacia un mapa del pueblo colgado en la pared."
    # Paneo al mapa con tres marcas
    show mapa at truecenter with dissolve
    mm "Al Silbón le gusta estar entre la gente, así que es probable que lo encuentres caminando en el pueblo. "
    mm "Si hay un lugar donde seguro el Pombero iría primero, es en el bosque Suas Agascuana."
    mm "Y la Calchona... Debe estar buscando algo que comer, así que seguramente la encontrarás en los campos Lania."
    hide mapa with dissolve
    mm "Hay mucho terreno por cubrir y poco tiempo-"
    mm "Prometo ayudarte en todo lo que pueda. Nombra una Leyenda y yo me encargaré de lo demás."
    show player pensativa with dissolve
    "Debo tomar una decisión, ¿Tras de quién iré?"
    p "Elijo a..."
    #Hay alguna chance de que estas dos lineas vayan LUEGO de elegir la opción y antes de hacer el salto?

    menu:
        "Calchona":
            show player feliz with dissolve
            mm "Buena suerte. Te estaré esperando aquí al amanecer"
            "Sin más, Inaru desapareció. Nuevamente sola, me dirigí hacia la puerta."
            jump calchonaRoute
        "Pombero":
            show player feliz with dissolve
            mm "Buena suerte. Te estaré esperando aquí al amanecer"
            "Sin más, Inaru desapareció. Nuevamente sola, me dirigí hacia la puerta."
            jump pomberoRoute
        "Silbón":
            show player feliz with dissolve
            mm "Buena suerte. Te estaré esperando aquí al amanecer"
            "Sin más, Inaru desapareció. Nuevamente sola, me dirigí hacia la puerta."
            jump silbonRoute
##########################################################
label calchonaRoute:
    default goodAnswersCalchona = 0
    stop music fadeout 2.5
    scene black with fade
    centered "Campos Liwen. \n31 de Octubre. \n00:30am."
    scene campo with fade
    show player feliz at left with easeinleft
    "Me encantaba venir aquí... De pequeña, los vecinos me dejaban acariciar a los animales y darles de comer."
    show player triste with dissolve
    "Ahora estoy buscando a una bruja, y parece ser el peor lugar del mundo."
    "El viento soplaba con suavidad, y con él, lograba escuchar los susurros de las ovejas que dormían dentro de sus corrales. Parecía que cotilleaban entre ellas en sueños."
    show player asustada with dissolve
    cal "Nghh.."
    p "!!!"
    "Unos gemidos forzaron que me detuviera. Mi cuerpo se tensó, mientras escaneaba cerca de los corrales."
    "Allí la vi, una figura encorvada que forcejeaba para entrar a uno de los corrales"
    show player pensativa with dissolve
    "Pobre oveja, no debieron darse cuenta que quedó afuera."
    p ". . ."
    show player asustada with dissolve
    p "!!!"
    "Al ser iluminada bajo la luz de la Luna, pude ver un rostro humano, el cual se inclinaba para pasar la cabeza entre los postes del corral y alcanzar el bebedero."
    p "¡AH!"
    hide player with dissolve
    # personaje ???
    show calchona neutra with fade
    cal "?"
    "Apenas me oyó, la oveja volteó a verme. Su espalda comenzó a erguirse para levantarse en las patas traseras. Un par de ojos brillantes se posaron en mí, dorados y muertos."
    "¿Qué hago?{w} ¿Qué hago?{w} ¿Qué hago?"
    "Puedo verla tensar sus manos, sus ojos se mueven lejos de mí. Si se escapa, podría estar perdiendo la única oportunidad que tengo de ayudar al abuelo."

    show calchona at right with move 
    show player asustada at left with easeinleft
    p "¡AGUA!"
    cal "..."
    "La criatura se volvió a verme."
    show player triste with dissolve
    p "Te puedo ayudar..."
    "Me fui acercando despacio, mis ojos sobre la criatura. Ella me observaba de regreso, dando unos pasos atrás. Pero no se alejaba."
    "Una vez llegué a la valla, puse las dos manos sobre ella y le trepé para llegar al otro lado. Las ovejas seguían dormidas. La criatura me miraba expectante."
    "Mi mano se extendió para abrir el grifo y el agua empezó a correr. En un instante, la criatura puso ambas manos dentro del corral, bajo el agua, y luego se las llevó al hocico, bebiendo desesperadamente."
    "Sus mirada nunca me abandonaba."
    show player feliz with dissolve
    cal "Gracias."
    cal "¿Qué estás haciendo aquí?"
    show player triste with dissolve
    "Vaya, no me lo esperaba."
    "Aún así, sabía que estaba desconfiada. No puedo decirle la completa verdad, o sino se irá. Me pregunto si se dará cuenta que le estoy mintiendo..."

    show player pensativa with dissolve
    p "Yo..."
    menu:
        "\"Te estaba buscando.\"":
            $ goodAnswersCalchona += 1
            show player feliz with dissolve
            p "Te estaba buscando. {w}En el pueblo se oyen historias sobre leyendas que vagan en la noche. {w}Pensé que si comenzaba a explorar podría encontrar alguna."
            show player triste with dissolve
            p "Lamento haberte asustado."
            cal "Los campesinos no hablan conmigo. Pero siempre me dejan algo de beber."
            cal "Jamás había estado aquí antes."
            show player feliz with dissolve
            "Pude ver como comienza a relajarse, y en respuesta, sentí mis hombros bajando a la par."
        "\"Me escapé del festival.\"":
            show player feliz with dissolve
            p "Me escapé del festival. {w}Había mucho ruido, y quería ver como se encontraban los animales." 
            p "Vengo a este pueblo desde que soy pequeña y siempre he tenido una conexión con ellos. {w}Cuando me acerqué, pensé que eras una oveja que se había escapado del corral."
            cal "No serías la primera. Es normal teniendo en cuenta como... Luzco."
            "Pude notar que aún me mira con desconfianza, pero no hizo ningún intento de salir corriendo. En respuesta, siento como mis músculos se relajan."
   
    p "Si tienes hambre, ¡puedo ayudarte a buscar algo para comer!"
    cal "..."
    p "Soy [playerName!q] ¿cuál es tu nombre?"
    cal "..."
    # Cambia a Fisa
    $ cal = Character("Fisa", color="#538083")
    cal "Fisa."
    p "Bueno, ¡es un placer conocerte, Fisa! Ven, vamos a buscar algo para comer."
    "Mientras me alejaba, me puse a pensar acerca de como le estaba yendo a Inaru..."
    "Mi mano comenzaba escocer al recordar todo lo que conllevaba esto, y en el problema en que me había metido."
    show player triste with dissolve
    "¿Por qué abrí esa caja?"
    # (recuerdo)
    show black at truecenter with dissolve
    centered "No le veas."
    centered "Ten cuidado."
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
    "En un instante, Fisa tomó la pera de mis manos y a pesar de mantener la apariencia hasta ahora, la devoró en un instante."
    "La lana de sus mejillas se llenó del líquido de la pera y se volvió pegajosa."
    "Me senté en el suelo con varias peras entre mis brazos, y esparcí la mayoría sobre el cesped. {w}Precavida, Fisa se sentó frente a mí."
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
            cal "Mi esposo y yo trabajábamos en los campos. Él no sabía que yo era una bruja. {w}Por las noches, me sentía libre, tomaba mis pociones y vagaba por los campos como una oveja."
            show player triste with dissolve
            cal "Un día volví y no había nada. {w}Ni mi esposo, ni mis hijos. {w}Y todas mis pociones habían sido destruidas. Solo pude tomar los restos de una."
            cal "Y quedé... Así."
            cal "La pena, o vaya a saber que, me ató a este mundo desde ese entonces, condenada a caminar solo por el borde. Ni humana, ni animal."
            cal "Y simplemente, la gente empezó a morir y a olvidarse de mí."
            cal "Me volví nada más que una Leyenda..."
        "\"Me inspiras confianza\"":
            show player feliz with dissolve
            "Me encogí de hombros, tratando de poner el rostro más impasible que podía."
            p "Supongo que me inspiras confianza."
            p "Desde que te vi, no has hecho nada más que tratar de alejarte."
            p "Si algo parecía, era que tú tenías más miedo de mí que yo."
            "Fisa parpadeó varias veces, usando el revés de su mano para limpiarse los restos de pera."
            cal "Eres valiente. {w} Pero he visto gente intrépida como tú cometer errores muy graves."
            cal "Hay muchas otras criaturas... Más grandes, fuertes y crueles que yo."
            show player triste with dissolve
            "La manera en que Fisa perdía la vista en la comida me hacía pensar que ella también tenía algo de aquella fuerza y crueldad de la que hablaba."
    
    cal "Hace mucho conocí a un hombre no muy distinto a tí. {w}Fue el primer humano que me trató como una persona."
    cal "Era amable. Y me miraba a los ojos con una sonrisa."
    cal "Un día, me ofreció ir con él."
    cal "Y luego... Solo sentí calor."
    "Está hablando del abuelo..."
    menu:
        "Hablar sobre mamá":
            $ goodAnswersCalchona += 1
            p "Estar sola... Suena difícil."
            p "Yo no sé que haría si no pudiera volver a ver mi mamá..."
            p "Cuando era pequeña, tuve una pesadilla. Estaba sola en el mundo... {w}No había absolutamente nada, como si alguien hubiera puesto un lienzo y solo me puso a mí, y allí me dejó."
            p "Cuando desperté me di cuenta que no le temía a estar sola, {w}sino a la posibilidad de que hubiera algo más allí lo cual no me podría enfrentar."
            "Fisa hizo silencio, pero luego, sujetó mi mano."
            cal "Siempre cuando uno de mis hijos tenía miedo, yo les decía que cerrara el puño fuertemente e imaginara que estaba apretando mi mano."
            "Con sus palabras, podía sentir como su agarre se hacía más firme, y en un reflejo, hice lo mismo."
            cal "Cuando haces mucha fuerza, no sientes si en verdad hay o no alguien contigo. {w}Eso... Nos hace sentir menos solos."
            show player feliz with dissolve
            "Así, nos quedamos hablando por horas."
            pause
        "Hablar de su pasado":
            p "Cometer un error no nos hace menos humanos. Lamento mucho lo que te ocurrió."
            "Fisa volteó su mirada, y en el reflejo de aquellos ojos pude ver... Compasión."
            cal "No lo hagas. No era una buena persona. Los humanos pueden guardar muchos buenos sentimientos.."
            cal "Pero ser un animal significaba que podía hacer lo que quisiera, sin consecuencias. Podía robar, podía matar sin mirar atrás."
            cal "Eso era la verdadera libertad."
            cal "Pero al final, tenemos que enfrentar que no estamos solos, y lo que hacemos, repercute a todo nuestro alrededor."
            "El silencio volvió a caer entre nosotras."
            "Por un largo rato, me quedé pensando en lo que había dicho..."
            pause

    scene black with fade
    centered "Campos Lania. \n31 de Octubre. \n6:00am."
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
    "Me levanté del cesped, sacudí un poco mi pantalón y la seguí. Era ahora o nunca, tenía que sellarla."
    "Fisa se detuvo a campo abierto, justo donde el Sol empezaría a alumbrar."
    show player triste at left with dissolve
    show calchona neutra at right with dissolve
    cal "He vivido oculta por cientos de años, ya había olvidado lo que se siente el calor."
    cal "No puedo culpar a mi Vestigio, he vivido fuera del Sol mucho antes que estar en él."
    "Lentamente, se sentó, sus manos acariciando el rocío del cesped."
    cal "¿Tú lo tienes, verdad?"
    show player asustada with dissolve
    "Al oir esas palabras, pude sentir como mi cuerpo se tensaba. Ella sabía."
    cal "Ven, siéntate. Correr de mí sería inútil."
    "Lentamente, me aproximé a ella. Mi corazón estaba latiendo cada vez más fuerte."
    cal "Eres una buena niña, ..."
    show player triste at left with dissolve
    "Al sentarme junto a ella, todos mis miedos resurgieron. Podía dejarla ir. Podía ignorar que la había visto, quizá Inaru podría lidiar con ella."
    "Su lana, tan pálida bajo la luna, comenzaba a verse del blanco más hermoso que había visto.{w} Fisa cerró los ojos."
    cal "Desearía... Poder llorar. Por mi familia, por mi pasado."
    cal "Por las cosas que vas a pasar de ahora en más."
    "Llorar..."
    "Quizá... La marca estaba..."
    "Fisa se giró hacia mí, sus ojos reluciendo con cada palabra."
    cal "¿Debe doler, no? Ser una buena persona, forzada a hacer cosas malas..."
    "Si no lo hacía ahora... No llegaría a tiempo."
    "Mis uñas arrancaron la cáscara que contenían la sangre en mi palma. {w}Y sin más, apreté la mano contra los brillantes ojos de Fisa."
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
    "Antes de que me diera cuenta, caí hacia adelante. {w}El sol estaba iluminando el campo por completo."
    show player triste with dissolve
    "Estaba sola."
    "De mi bolsillo, cayó el vestigio, reluciente y lleno de vida."
    "Pero yo... Sentía que una parte mía se había desvanecido."
    "Lo que sea que había hecho mi abuelo, esperaba que haya valido la pena."
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
    "Bad Ending."
    # Finaliza el juego:
    return

##########################################################
label pomberoRoute:
    default goodAnswersPombero = 0
    stop music fadeout 2.5
    scene black with fade
    centered "Bosque Suas Agascuana. \n31 de Octubre. \n00:30am."
    scene campo with fade
    show player feliz at left with easeinleft
    "Una vez salí de la casa, tomé el camino más corto para llegar al bosque. "
    "Había oído historias de niños como yo que entraban al bosque a jugar por la noche. {w}Nunca pensé que sería yo quien se metiera voluntariamente alguna vez."
    "..."
    "Las copas de los árboles se mecían sobre mí, danzando con el viento en un arruyo. Y aún así, podía sentir como un gran peso caía sobre mí."
    show player triste with dissolve
    pom "Mh mh mh~!"
    "Un tarareo sonó en eco contra los troncos de los árboles. {w} Luego pude verlo. "
    "Unos metros más adelante, una figura oscura se acercaba a un arroyo, cantando para sí."
    show player pensativa with dissolve
    p "¿Está... {w}Alegre?"
    hide player with dissolve
    "Antes de ser descubierta, me escondí detrás de un árbol, observando." 
    "Parecía un duende, pero no era como nada que haya visto antes en cuentos."
    show pombero neutro with fade
    pom "De los montes vengo...{w} A los montes voy...{w} A hablar con la niña que me ha visto hoy~"
    "!!!!"
    "Un escalofrío corrió por mi espalda. Sentía que estaban por cazarme."
    "Me di vuelta."
    scene campo with fade
    show player triste at center 
    show pombero neutro at right with easeinright
    pom "¡Ho-laa~!"
    show player asustada with dissolve
    p "¡Ah!"
    show player at left with move
    "Mis piernas se movieron por sí solas, y en un instante, me moví hacia un lado antes de quedar acorralada."
    "El duende bajó del árbol, una gran sonrisa adornando su rostro. {w}Cada paso que daba hacia adelante, yo lo retrodecía."
    pom "Jaja... Ja. ¡La niña tiene miedo!"
    "¡Necesito reaccionar rápido antes de que se acerque!"
    "¿Qué hago?"
    menu:
        "Enfrentarlo":
            "Sentía que mi corazón iba a salirse de mi pecho. Aún así, di un paso hacia adelante."
            show player enojada with dissolve
            p "¡No! ¡No le tengo miedo a criaturas como tú!"
            "El Pombero dejó de reírse. Sentía que aquel silencio me iba a devorar."
            "Luego, empezó a reir de nuevo."
            pom "¡Niña tonta~!"
            hide pombero with dissolve
            "... Desapareció."
            show player asustada with dissolve
            p "¿Qué? ¡Espera!"
            scene campo with fade
            "Salí a perseguirlo, las ramas tan cerca de mi rostro que sentía me golpearían en cualquier momento."
            "Cuando me quedé sin aire, tuve que detenerme, las manos descansando sobre mis rodillas."
            show player triste at left with moveinleft
            p "¿Dónde... {w}Dónde se metió?"
            pom "Niña tonta"
            show pombero neutro at right with dissolve
            "El duende se apareció frente a mí."
            pom "Eres como un toro, corres hacia adelante lista para atacar. {w}No puedes atravesar una montaña yendo hacia adelante~!"
        "Correr":
            $ goodAnswersPombero += 1
            scene campo with fade
            "Sin pensarlo dos veces, me giré y eché a correr, internándome en los bosques."
            show player triste at left with moveinleft
            "Corrí entre los árboles, escuchando los ecos de la risa del Pombero. {w}No sabía si estaba lejos o cerca de él, pero estaba segura de que se estaba aproximando."
            "De pronto, la risa se desvaneció. {w}Esos instantes fueron los únicos que necesite para determe a recuperar el aliento."
            pom "Niña lista, muy lista."
            show player asustada with dissolve
            "!!!"
            show pombero neutro at right with dissolve
            "Levanté la mirada, y estaba en cuclillas frente a mí. Incluso en la oscuridad, podía ver brillando su enorme sonrisa."
            pom "Para encontrarse, uno debe perdese. Si si si.{w} Niña lista, muy lista."

    show player enojada with dissolve
    p "Deja de llamarme así."
    pom "Mh?"
    p "Me llamo [playerName]."
    pom "Ugh, los humanos y sus nombres pretenciosos. {w}Ustedes me llaman de mil maneras, ¿por qué no podría hacer lo mismo?"
    p "¿Cómo te gusta a tí que te llamen?"
    $ pom = Character("Har", color="#89909f")
    pom "Har! Es fuerte, intrépido, y solemne, si si si. ¡Digno nombre para mi persona!"
    "¿Y eso no es pretencioso?"
    pom "Niñas como tú no deberían estar vagando solas en el bosque, ¡hay monstruos, y cazadores, y hombres malos dando vueltas."
    p "¿Y qué haces tú aquí?"
    "Har ladeó la cabeza, y luego se echó hacia atrás, la mirada fija en sus alrededores."
    pom "Busco divertirme, los humanos son MUY divertidos, ¿sabes?"
    show player triste with dissolve
    "El aire comenzó a sentirse dneso, como si los árboles estuvieran a punto de caer sobre nosotros."
    pom "¡Se creen realmente ingeniosos cuando en realidad son"
    pom "Torpes"
    pom "Egoístas"
    pom "Y débiles."
    pom "Piden, piden, piden, y no saben que uno es más inteligente que ellos, ¡jaja~!"
    "Incluso entre sus risas, podía ver lo enojado que estaba. {w}Era aterrador."
    show player feliz with dissolve
    p "Quizá podemos hacer algo juntos."
    pom "¿Quieres jugar conmigo? Niña tonta, ¡pero valiente!"
    "De un salto, Har comenzo a alejarse."
    hide pombero with dissolve
    pom "¡Ven, niña lenta!"
    show player asustada with dissolve
    p "¡Espérame!"
    hide player with dissolve
    "Salí corriendo tras él, de nuevo. Solo unos minutos más tarde, llegamos a una pequeña laguna."
    show pombero neutro at right with easeinright
    show player triste at left with easeinleft
    p "¿Un lago? ¿Quieres jugar en un lago?"
    pom "¡Sip, tú eliges! ¿Qué quieres hacer?"
    p ". . ."
    "Si esto era lo que necesitaba para que él confiara en mí..."
    p "Vamos a..."
    menu:       
        "Pescar":
            show player feliz with dissolve
            p "Podemos pescar aquí, ¿o no?"
            pom "¿Hm?"
            "Me acerqué a uno de los árboles donde sobresalía una rama larga y delgada."
            p "Podemos usar esto y mis cordones para hacer una caña!"
            "Ambas manos sujetaron la rama para tratar de romperla, cuando Har puso una mano en mi hombro y con mucha fuerza me arrojó al agua."
            scene campo with fade
            "Logré patalear de nuevo a la superficie, solo para ver a Har nadando hacia mí."
            pom "¡Sorpresa! Niña tonta necesita prestar más atención~"
            p "{i}Cof, cof{/i} ¡Eso no fue nada amable!"
            pom "Tú tampoco has querido ser amable con los peces."
            "Con una pequeña risa, Har empezó a nadar en círculos a mi alrededor. {w}Me recordaba a los tiburones."
        "Nadar":
            $ goodAnswersPombero += 1
            show player feliz with dissolve
            p "Quiero ir a nadar."
            pom "¿Hm?"
            "Me di vuelta y observé la laguna. No me había dado cuenta, pero los árboles daban paso a la luz de la Luna para caer sobre el agua, haciendo del agua un espejo reluciente."
            p "¡A que llego primero!"
            scene campo with fade
            "Luego de gritar, eché a correr hacia el lago. {w}Detrás mío, los pies de Har trastabillaban antes de salir corriendo tras de mí."
            "De un salto me metí en el agua, dejando que me cubriera por completo por un momento antes de sacar la cabeza."
            pom "¡Niña astuta, cree que puede ganarme!"
            "A diferencia de antes, Har parecía entretenido dentro del agua."
            pom "Sígueme."
            "Tomando una gran bocanada de aire, que parecía más pretendida que otra cosa, él se sumergió."
            "Nadamos hacia el fondo, donde pude ver los peces que allí habitaban."
            pom "Mira bien."
            p "?!"
            "Las manos de Har en mis hombros me forzaron a parpadear varias veces {w}. De pronto, las formas de los peces y las algas se veían más claramente. ¡Era increíble!"
            "A pesar de que las criaturas en el bosque aún dormían, las del agua estaban llenas de vida."
            "Volví a la superficie para recobrar el aliento, y Har ya estaba allí, flotando boca arriba, admirando la Luna."
            p "Es hermoso."
            pom "Lo sé. No en todos lados es así."
            pom "Los bosques son fuertes, pero se mueven muy lentamente. {w}Los humanos son rápidos. {w}Quitan sin pensar."
            pom "No ven lo que hay a su alrededor."
            pom "¡Pero yo soy más rápido!"
            "En un instante, lo pude ver moverse cerca mío."
            pom "Nadie es más rápido, o más fuerte que yo en los bosques. {w}Si estoy aquí, nadie sería lastimado por un humano. {w}Ningún árbol, o pez, ni nadie."
            "No estaba segura si era un comentario, o una amenaza. Sin embargo, no pude evitar sentir la fuerte conexión que Har tenía con los bosques."
            p "Entonces es bueno que estés aquí."
            "Har volteó la mirada."
            pom ". . ."
            pom "Niña lista."

    "Eventualmente, salimos del agua, y me tiré en el cesped."
    show player feliz at left with dissolve
    show pombero neutro at right with dissolve
    "La noche era calurosa, así que la ropa mojada no me molestaba en lo absoluto. {w}Al mismo tiempo, Har se sentó contra un árbol."
    "Por el rabillo del ojo, pude ver que desenterraba un cigarro de entre las raíces y se lo ponía entre los labios. {w}¿Hace cuanto que tenía eso ahí?"
    show player pensativa with dissolve
    p "Quiero preguntarte algo."
    pom "Bien por ti."
    show player triste with dissolve
    p "¿Qué haces aquí?"
    "Del suelo, levantaba una hoja seca, y con un chasquido de sus dedos, causó un chispazo que la encendió."
    "Lentamente la guió al cigarro, sacudiendo los restos quemados una vez éste estaba encendido."
    pom "Me recuerda a mi hogar. Vengo de un lugar parecido a éste."
    "Har exhaló el humo de su cigarro, perdiéndose en sus palabras."
    pom "¿Qué hay de tí? ¿Por qué estás aquí?"
    "Por un largo rato, me quedé en silencio."
    show player feliz with dissolve
    p "Quiero hacer un trato."
    pom ". . ."
    pom "¿Ah sí?"
    "Volvió a dar una calada. Mi corazón se encogió."
    pom "Que... Coincidencia. {w}Parece que estás en el lugar ideal."
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
            pom "No ofrecerías eso si supieras todo lo que dicen de mí en mi pueblo, niña tonta."
            pom "Soy un protector del bosque, no un humano."
            p "¿Por qué odias tanto a los humanos?"
            pom "¿Odiarlos? {w}No no no, niña tonta, no es así. {w}Los humanos son quienes me odian a mí."
            pom "Cazadores, pescadores, leñadores..."
            pom "A mí no me interesa lo que los humanos hagan, pero cuando destrozan, matan, corrompen... {w}Me enfurecen."
            "Otra exhalación, y dejó que el rastro de humo se desvanezca en el aire."
            pom "Podría decirse que me convertí en el conveniente monstruo.{w} Dicen que huyas porque yo podría atacar en los pastizales. {w}Les dicen a las mujeres que no salgan de sus casas."
            pom "Algunos humanos son listos. {w}Hábiles cuando se trata de desviar la atención de sus monstruosas acciones."
            pom "Ya no quedan criaturas como yo. {w}Casi todas están muertas. Y las que no, como yo, se vuelven antagónicas."
            pom "Hacia el final, sólo somos leyendas destinadas a olvidarse."
            p "..."
            show player feliz with dissolve
            p "Yo no voy a olvidarte."
            pom "Ja..."
            pom "Niña inocente."
            "Luego de ello, nos quedamos hablando por horas. {w}Har me contó sobre las selvas donde vivía. {w}Antes de darme cuenta, comenzó a amanecer."
        "Cuida de este bosque.":
            p "A tí te preocupan los bosques, ¿verdad?. No quisiera que lastimes a nadie. Pero me gustaría que siguieras cuidando de los bosques."
            "Har exhaló el humo de su cigarro, y giró la cabeza hacia mí."
            pom "Dime, ¿por qué las vidas humanas valen más que las de cualquier otra criatura?"
            show player triste with dissolve
            p ". . ."
            pom "Los humanos matan a sus propios niños, arrancan las plumas de las aves para descansar cómodamente."
            pom "Desollan mamíferos vivos para ir bien vestidos. {w}Torturan en vida. {w}Queman. {w}Ahogan. {w}Electrocutan. {w}Dime, ¿por qué no puedo devolverles la gentileza?"
            pom "¿Quien te da la autoridad y el poder de decirme que sería o no correcto?"
            "Me quedé en silencio. {w}Con cada palabra, podía sentir la tierra temblar a través de las raíces."
            p "Lo siento."
            pom "No tienes que disculparte. {w}Eres solo una niña."
            "Seguimos hablando el resto de la noche... De a poco, podía entender la relación de Har con los humanos."

    scene black with fade
    centered "Campos Suas Aguascana. \n31 de Octubre. \n6:00am."
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
    pom "¿Sabes? Hace años, conocí a este hombre."
    pom "Era astuto, pero también tenía esto... {w}Humanos siempre le dicen \'corazón\', pero todos tienen uno."
    pom "Era algo distinto. Algo como tú lo tienes."
    pom "Luz."
    pom "Si... {w}Eso es lo que era... {w}Luz."
    p "..."
    pom "Jamás lo resentí por encerrarme. Sabía que cuando el tiempo sea el correcto, volvería a este mundo y aún habría mucho por hacer."
    pom "Él me decía 'el mundo no puede depender de tí. Si tiene que morir, morirá y no habrá nada que podrás hacer'."
    pom "Y tenía razón. {w]Este mundo ya no es para criaturas como yo."
    pom "Si algo me da tranquilidad, es que aún hay criaturas como tú."
    pom "Este mundo... {w}Es más tuyo que mío. {w}Ahora es tu responsabilidad."
    p "Har..."
    pom "Mis condiciones."
    pom "Escucha lo que el mundo tiene que decir. {w}Hay voces que merecen ser oídas."
    pom "Yo no soy de dar regalos. {w}Así que toma esto y no lo cuestiones."
    pom "No creas en las intenciones de nadie. {w}Todo el mundo tiene una razón para hacer algo. {w}Escucha sus acciones más que su palabras."
    "Sabía que no respondería ninguna de mis preguntas, no importa cuanto me gustaría hacerlas... {w}Y me estaba quedando sin tiempo."
    p "¿Qué quieres a cambio?"
    "Otra vez, sonrió.{w} Una mano sujeto la mía y rasgó la piel de mi palma. {w}Luego se la llevó al oído."
    show player asustada with dissolve
    pom "Ah, sí... Justo lo que imaginaba..."
    show player triste with dissolve
    pom "Hasta Luego [playerName]."
    hide pombero with flash
    "En cuestión de segundos, en lugar de ver el rostro de Har, estaba viendo mi mano ensangrentada."
    "!!"
    "De mi bolsillo el Vestigio cayó contra el suelo, brillante, pesado y lleno de vida. {w}Har sabía de mi abuelo, estoy segura. {w}Me hubiera gustado saber más."
    "Si tan solo supiera que haría él en este momento."
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
    p "No de nuevo.. {w}¡Har, espera!"
    "Salí tras él. {w}Corriendo entre los árboles, persiguiendo el aire."
    "Me detuve de pronto, y miré para todos lados."
    show player triste at center with moveinleft
    p "¡Har!"
    pom "Esa bruja realmente se cree lista, ¿no?"
    "Giré la mirada, pero no podía verlo. {w}Su voz hacía eco por todas partes."
    pom "Pobre, pobre niña, cayó en los encantos de una bruja y pensó que podía ser amiga de todas las criaturitas del bosque."
    "El aire dejó mis pulmones."
    pom "Pobrecilla~ "
    pom "Pero no te preocupes, puedo hacer lo que me pides. {w}Este bosque estará a salvo y tú y yo podremos seguir jugando."
    pom "Te quedarás aquí."
    pom "Para siempre."
    show pombero neutro at right with dissolve
    show player asustada with dissolve
    "De golpe, sentí un fuerte empujón, y las hojas detrás mío desaparecieron." with vpunch
    "Estaba cayendo... {w}La sonrisa del duende alejándose."
    hide player with dissolve
    show pombero at center with move
    pom "Adios, niña tonta~!"
    "!!!" with vpunch
    scene black with fade
    pause
    "Bad Ending."
    # Finaliza el juego:
    return

##########################################################
label silbonRoute:
    default goodAnswersSilbon = 0
    stop music fadeout 2.5
    scene black with fade
    centered "Pueblo Liwen. \n31 de Octubre. \n00:30am."
    scene fondo pueblo decorado with fade
    show player feliz at left with easeinleft
    "Si había un lugar donde podía sentirme en mi elemento, era éste. {w}Las festividades ya comenzaron y hay muchísima gente caminando alrededor, niños y adultos por igual..."
    "Me hubiera gustado poder disfrutarlo..."
    "Al caminar a través de los puestos de comida, vi una figura que escondía su rostro bajo su sombrero, una mano sujetaba una gran bolsa sobre su hombro."
    hide player with dissolve
    show silbon neutro with dissolve
    sil "Ciervo ciervo... {w}Si si si... {w}En tiras, en cubos, en rebanadas..."
    sil "Aguardiente, ohhh, aguardiente, calienta los huesos. {w}El polvo de hueso que se rompe, {w}y se rompe {w}y se rompe."
    p "Ese es...?"
    "Aquel joven caminaba encorvado, murmurando para sí mismo. Con cada palabra, podía sentir como su lengua se pegaba a los dientes y dejaba pasar el aire. {w}Como un silbido."
    "Se veía... {w}Horripilante."
    "Caminé hacia él, fijando la mirada en los puestos cercanos. {w}Nadie parece prestarle atención, como si no existiera."
    "{i}Fiu...{/i}"
    "El silbido chirrió junto a mi oído, y mis ojos se abrieron de par en par."
    show silbon at right with move
    show player asustada at left with easeinleft
    sil "¿Qué crees que haces?"
    "Me giré hacia él."
    p "¿Eh?"
    sil "Miras, miras y miras, {w}¿Qué buscas, que quieres?"
    "Bajo el sombrero, podía ver el destello de unos ojos llenos de odio."
    show player pensativa with dissolve
    "¿Qué hago? Necesitaba pensar rápido."

    menu:
        "\"Quiero comer lo que veías.\"":
            show player feliz with dissolve
            p "Quiero comer lo que veías, ¡se veía delicioso!"
            sil "..."
            p "Es ciervo, ¿verdad?"
            sil "Ciervo."
            show player triste with dissolve
            sil "¡Ciervos engañosos, {w}mentirosos, {w}traicioneros! Corren, y corren, y no se dejan atrapar."
            sil "Estos... {w}Ya... {w}No... {w}Corren."
            p "..."
        "\"Quiero saber sobre tí.\"":
            $ goodAnswersSilbon += 1
            show player feliz with dissolve
            p "Quería saber sobre tí."
            sil "?"
            show player asustada with dissolve
            p "!!"
            p "Eh... ¡Tu disfraz! Es muy bonito."
            sil "Dis...{w}Fraz."
            sil " ..."
            p "..."
            sil "Si si. {w}Mi disfraz. Colorido, de fiesta, todos están con disfraces."
            show player feliz with dissolve
            p "¡Aja, exacto!"
    
    show player feliz with dissolve 
    p "¡No me has dicho tu nombre! Yo me llamo [playerName], vengo aquí de visita."
    sil "Nadie me llama por mi nombre. Todos gritan, todos huyen. {w}No muy rápido."
    $ sil = Character("Wiija", color="#ade1e5")
    sil "Pero cuando tenía nombre... {w}Era Wiija."
    p "Wiija..."
    show player triste with dissolve 
    "Su rostro estaba cubierto bajo aquella máscara. {w}Era imposible saber como reaccionaba a mis palabras."
    "Su tono de voz siseante apenas dejaba entrever una agresividad internalizada."
    "Estar en el festival era lo único que me daba un poco de alivio. {w}Había mucha gente a nuestro alrededor."
    show player feliz with dissolve 
    "Al oir ese nombre, sonreí."
    p "¡Es un placer conocerte, Wiija!"
    p "Sé que no eres de por aquí, ya que no sabías mucho del festival. Si quieres puedo mostrarte un poco del lugar."
    sil "..."
    "Se había quedado callado."
    "¿Lo está pensando?"
    sil "¿Qué tiene esto de especial?"
    menu:
        "\"Puedes hacer nuevos amigos.\"":
            $ goodAnswersSilbon += 1
            p "¡Puedes hacer nuevos amigos!"
            sil "..."
            "Se ha quedado en silencio."
            sil "Amigos."
            sil "Nunca tuve amigos."
            show player triste with dissolve
            p "¿No?"
            sil "Siempre solo. {w}Siempre en casa. {w}Sin amigos."
            sil "Siempre en casa. {w}Con mamá y papá. {w}Ellos temían. {w}Así que no salía."
            sil "Con el abuelo a veces... {w}Salía con el abuelo."
            p "¿Tu abuelo?"
            "Wiija asintió, una mano moviendo su saco. En su interior, el contenido se movía chocando entre sí."
            show player feliz with dissolve
            p "Si quieres... {w}Podríamos ser amigos."
            sil "No."
            show player triste with dissolve
            p "!"
            p "?"
            sil "No podríamos. {w}No, no. Mala. No. Terrible idea."
            p "... ¿Por qué no?"
            sil "No tengo amigos, nunca los tuve. {w}Solo eran mamá y papá."
            sil "Y el abuelo."
            p "..."
            sil "El Maestro... {w}Me recordaba a mi abuelo."
            # Flashback? dale Gracias uwu
            scene black with fade
            show mmonte neutra with dissolve
            mm "Quedé bajo las órdenes del Maestro, he vivido en esta caja por cuarenta largos años"
            scene fondo pueblo decorado with fade
            show player triste at left with dissolve
            show silbon neutro at right with dissolve
            # Fin del Flashback?
            "Inaru llamaba a mi abuelo Maestro. Estaba segura que Wiija también estaba hablando de él."
            sil "Fuerte. {w}Listo. {w}Severo. {w}Si si, severo era él."
            sil "Menos severo que mi abuelo."
            sil "Un día hice algo... Malo."
            sil "Si si, era malo. Lo recuerdo. {w}Era divertido, entretenido, pero también malo."
            sil "A mamá no le gustó, y al abuelo mucho menos."
            sil "Con látigos y perros me hizo escarmentar y ahora no puedo volver."
            sil "Quería odiarlo. {w}ODIARLO. {w}ODIARLO. {w}Me convirtió en esto."
            sil "Pero no pude, no puedo."
            sil "Odio a papá. {w}Siempre odié a papá."
            sil "Apestaba a aguardiente."
            sil "¡Lo odiaba, lo odiaba!"
        "\"Puedes pasarla bien en familia.\"":
            p "Puedes pasarla bien en familia."
            sil "..."
            p "Recuerdo que mi mamá adoraba este lugar y-"
            sil "No tengo familia."
            p "¿Eh? ¿Y tus padres?"
            sil "..."
            "Sus puños se apretaron fuertemente."
            sil "No {w}tengo."
            p "...?"
            "Con cada palabra, se empezó a proximar hacia mí. {w}Estando tan cerca, pude ver sus ojos a través de la máscara. {w}Poseían tanto odio que me hizo retroceder varios pasos. {w}Wiija siguió avanzando, arrastrando su bolsa."
            sil "Mi madre no está. {w}Se ha ido. {w}No existe."
            sil "Mi padre..."
            "Hizo silencio, su cabeza torciéndose hacia un lado."
            sil "Aún me acompaña."
    
    show player triste with dissolve
    p "Wiija..."
    show player feliz with dissolve
    p "Ven conmigo."
    "Me di media vuelta y me acerqué a unos puestos a comprar helado."
    p "¿Has probado alguna vez?"
    "Wiija negó con la cabeza."
    "Una vez el vendedor me los entregó. Me di vuelta y caminé fuera del area principal. La feria aún estaba visible. Pero menos gente pasaba cerca de nosotros."
    p "Ten."
    "Le ofrecí el helado."
    "Podía ver que estaba desconfiado. {w}Pero aún así, se sentó junto a mí, llevándose el helado en la abertura de la boca."
    sil "Está frío."
    p "¡Es la idea! ¡Es dulce! ¿Te gusta lo dulce?"
    sil "Es extraño. Raro. {w}No es carne."
    p "No lo es, no."
    "Por un largo rato, seguimos disfrutando del helado. {w}A veces, Wiija hacia preguntas, y yo hacia lo mejor para contestarla."
    "Con cada respuesta, él silbaba en una tonada particular."
    "Otras veces llevaba su mano al saco que descansaba junto a nuestra banca. {w}Hacia tintinear su interior y luego volvía a su helado."
    show player pensativa with dissolve
    "La curiosidad me invadió. Quizá esa era la forma de acercarme a él."
    menu:       
        "\"¿Qué hay en la bolsa?\"":
            p "Wiija..."
            show player feliz with dissolve
            p "¿Qué hay en la bolsa?"
            sil "Ja... Jaja." with vpunch
            "Una mano palmó el costado de la bolsa."
            sil "Cosas malas."
            show player triste with dissolve
            sil "La gente es mala. Hace cosas malas."
            sil "Miente, engaña. Bebe, bebe mucho."
            sil "yY es tonta."
            sil "Odio a la gente mala."
            sil "Y odio a la gente tonta."
            "Su cabeza se giró hacia mi, el helado chorrendo entre sus dedos."
            sil "Eres mala, [playerName]"
            show player asustada with dissolve
            p "!!"
            "Mi nombre en su boca... Se oía como si lo estuviera masticando. Saboreando..."
            sil "No. Nono. No eres mala."
            show player triste with dissolve
            sil "Pero eres tonta."
            sil "¿Qué has hecho para merecer esto?"
            sil "Nunca lo sabré. Nunca lo sabrás."
            "Luego, volvió a su helado, murmurando para sí."
            sil "La bolsa... {w}Apesta a aguardiente."
        "\"¿Quién te enseñó a silbar?\"":
            $ goodAnswersSilbon += 1
            show player feliz with dissolve
            p "¿Quién te enseñó a silbar?"
            sil "¿Hm?"
            "Wiija se quedó pensativo. {w}Por un largo momento hubo silencio, como si él se hubiera ido a otro lugar. {w}Muy lejos de aquí."
            sil "Mi abuelo me enseñó."
            show player triste with dissolve
            sil "Era un niño, era débil, asustaba a los demás cuando silbaba."
            sil "Lo oían lejos, y creían que no había peligro."
            sil "Lo oían cerca, y el miedo los invadía"
            sil "Yo era listo. Muy, muy listo."
            sil "Mi abuelo era severo."
            sil "Pero era bueno conmigo."
            sil "Por eso..."
            "Giró la cabeza de lado a lado, una mano se la llevó a su hombro."
            sil "Duele..."
            sil "El cuero. {w}Chocando contra la piel."
            sil "Y los perros."
            sil "Perros malos. {w}Odio a los perros."
            sil "El abuelo..."
            p "..."with vpunch
            "Mi mano se posó sobre su brazo."
            sil "!!"
            "Wiija se movió sobresaltado."
            sil "La familia tendría que ser algo imporante. Sí sí."
            sil "Yo no era familia."
            sil "Mi abuelo me traicionó"
            sil "Y yo lo traicioné a él."
            p "Te ha causado mucho dolor, ¿verdad?"
            sil "No fueron los latigazos. Ni los perros."
            sil "Ni las heridas."
            sil "Él no me sacó a tiempo. {w}No hubo amigos. No hubo abrazos."
            sil "Yo les hice pagar. Le hice pagar a él."
            sil "Y él me hizo pagar a mi."
            sil "Él me hizo desaparecer."
            sil "Puff."
            sil "Él murió con su pena."
            sil "Y yo vivo cargando con la mía."
            sil "Vago..."
            sil "Como Leyenda."

    p "..."with vpunch
    "Luego de eso, busqué cambiar el tema. {w}Seguimos hablando de trivialidades del pueblo. La gente, las costumbres."
    scene black with fade
    centered "Pueblo Liwen. \n31 de Octubre. \n6:00am."
    scene fondo pueblo temprano with fade
    "Wiija era... {w}Una criatura como ninguna otra."
    "Hablamos y hablamos hasta que el Sol comenzó a aparecer entre los edificios. {w}Para ese entonces, la mayoría de la gente se había marchado."
    "De pronto, Wiija se levantó."
    show player triste at left with dissolve
    show silbon neutro at right with dissolve
    p "Wiija?"
    "Me levanté con él. {w}Aún no sabía como sellarlo y él parecía que estaba a punto de marcharse."
    if goodAnswersSilbon == 3:
        jump silbonGoodEnding
    else:
        jump silbonBadEnding

label silbonGoodEnding:
    $ persistent.silbonEnding = True
    sil "¿Por qué haces esto?"
    p "¿Eh?"
    "De pronto, comenzó a alejarse."
    hide silbon with dissolve
    p "¡Espera!"
    hide player with dissolve
    "Lo empecé a seguir. {w}Se metía cada vez más entre los edificios. {w}Ya no había nadie en las calles. Solo los restos del festival."
    show silbon neutro at right with dissolve
    show player triste at left with easeinleft
    sil "¿Vas a castigarme, verdad? ¿Cómo él me castigó?"
    "Lo sabe..."
    p "..."with vpunch
    p "No."
    p "No voy a castigarte."
    sil "Sí lo harás. {w}Eres como mi abuelo."
    sil "Eres igual al Maestro también."
    p "Wiija."
    p "Necesito ayudar a mi abuelo."
    p "Él... Es importante para mí."
    sil "¿Importante?"
    p "Si pudieras volver atrás, ¿No querrías hacer lo mismo?"
    p "Huir con tu abuelo, protegerlo. Tener amigos."
    "Wiija miró al suelo. {w}Sumido en sus pensamientos. Dí un paso adelante. Y luego otro."
    show player feliz with dissolve
    p "Seamos amigos."
    sil "Te iras. {w}Me abandonarás."
    show player triste with dissolve
    sil "Las personas buenas se cansan de personas como yo. Merecen más. Mucho más."
    p "..."
    "Comencé a dudar. {w}Wiija... Tenía miedo. Y yo no sabía que decir. {w}Era cierto, ¿Qué haría con los Vestigios una vez los sellara nuevamente? {w}¿Abandonaría la caja para siempre?"
    "..."
    "No. No podía hacer eso."
    show player feliz with dissolve
    p "No te voy abandonar."
    p "Estaremos juntos. {w}E iremos a otros festivales."
    p "Lo prometo."
    p "Solo... Déjame hacer esto, dejame salvar a mi abuelo. Ayúdame a salvar a mi abuelo"
    sil "..."
    sil "A tu abuelo."
    sil "..."
    sil "Tu abuelo. Era bueno."
    
    show player asustada with dissolve
    "Su mano tomó la mía, y se llevó mi dedo a su boca."
    "En un lento movimiento, sus dientes presionaron contra la piel, cortando en ella. Luego, sus labios se posaron contra la yema. Allí se quedó un rato."
    p "..." with vpunch
    sil "Ja... Jaja."
    sil "Amigos..."
    hide silbon with flash
    "Un parpadeo, y Wiija desapareció. Bajé la mano, y vi solo el costal que venía cargando desde que lo vi la primera vez."
    show player triste with dissolve
    "Jamás había visto a alguien cargar con sus pecados así. Y no podía armarme de valor para juzgarlo."
    "Sin su dueño, la bolsa comenzó a hacerse polvo, envejeciendo frente a mis ojos."
    hide player with dissolve
    "Ya no había más que hacer aquí. Así que di la vuelta, y volví a casa."

    jump normalEnding

label silbonBadEnding:
    sil "Niña tonta. Mentirosa..."
    show player asustada with dissolve
    p "¿Eh?"
    "!!" with vpunch
    "Una fuerte mano se apretó contra mi cuello. Sus dedos apretando. Apretando..."
    show silbon at center with move
    p "AGH-!" with vpunch
    hide player with dissolve
    sil "¿Me ibas a entregar a ella, verdad?"
    sil "Niña tonta. Niña mala."
    sil "¡No me vas a encerrar! ¡NO ERES MI PADRE, NO PUEDES DECIRME QUE HACER!"
    p "Unghh-!" with vpunch
    sil "Tu abuelo. Es tu abuelo. Yo lo sé. Yo lo sé."
    sil "Era como el mío. Bueno y malo. Malo y bueno."
    sil "No te preocupes."
    sil "Te voy a ayudar."
    "Mis pies abandonaron el suelo cuando él me levantó, haciendo presión. No podía pelear, me estaba debilitando."
    "Y luego, sentí mi cuerpo chocar. ¿La banca, la pared? No lo sabía..."
    "{i}CRACK{/i}" with vpunch
    "Me siento... {w}Cansada..."
    scene black with fade
    "... Negro"
    "Todo negro"
    p "..."
    "No puedo hablar. No puedo moverme."
    "Ayuda... {w}Auxilio."
    "Siento movimiento, mi cuerpo está..."
    "..."
    "Una bolsa..."
    "¿Qué- Qué es esto?"
    "..."
    "Huesos."
    "Son huesos."
    sil "Somos amigos ahora. {w}Sí sí sí. {w}Tú cuida de papá allí."
    sil "Es hora de ir a hacer más amigos."with vpunch
    pause

    "Bad Ending."
    # Finaliza el juego:
    return

##########################################################
label normalEnding:
    scene black with fade
    centered "Casa del Abuelo. \n31 de Octubre. \n6:00am."

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
    $ cal = Character("Fisa", color="#538083")
    $ sil = Character("Wiija", color="#ade1e5")
    $ pom = Character("Har", color="#89909f")
    scene black with fade
    show calchona neutra with dissolve
    cal "Cuando haces mucha fuerza, no sientes si en verdad hay o no alguien contigo."
    scene black with fade
    show pombero neutro with dissolve
    pom "Si algo me da tranquilidad, es que aún hay criaturas como tú."
    scene black with fade
    show silbon neutro with dissolve
    sil "Las personas buenas se cansan de personas como yo. Merecen más. Mucho más."
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
    abu "Tú eres mi Vestigio."
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