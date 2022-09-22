# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define player = Character(["playerName"], color="#c3acce")
define grandpa = Character("Abuelo", color="#dfd9e2")
define madreMonte = Character("Madre Monte", color="#2a7f62")
define pombero = Character("Pombero", color="#89909f")
define calchona = Character("Calchona", color="#538083")
define silbon = Character("Silbón", color="#ade1e5")


# El juego comienza aquí.

label start:

    $ playerName = renpy.input("Mi nombre es..", default = "Alba", length=12)
    $ playerName = playerName.strip()

    if playerName == "":
        $ playerName = "Alba"


    "30 de Octubre. 4.00pm"
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
    "\"[playerName]...\""
    "\"No le creas.\""
    "\"No lo busques.\""
    "\"Está aquí.\""
    "\"Esperándote...\""
    #Fade in

    "30 de Octubre. 8pm"
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


    "23.55"
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

    madreMonte "Vaya..."
    menu:
        "\"¿Quien eres?\"":
            pass

    madreMonte "¿Quien soy yo? ¿Que no te han enseñado nada?"
    madreMonte "Me llamo *, soy una protectora de los bosques, por supuesto!"
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
    madreMonte "\". . .\""
    madreMonte "Chicuela egoista!! Nos condenarás a todos!!"
    "Y así el mundo se acercó a su destrucción..."
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
    "Ruta de la Calchona"
    calchona "Decisión 1"
    menu:
        "Elección Buena":
            $ goodAnswersCalchona += 1
            calchona "Respuesta Positiva"
        "Elección Mala":
            calchona "Respuesta Negativa"
    calchona "Decisión 2"
    menu:
        "Elección Buena":
            $ goodAnswersCalchona += 1
            calchona "Respuesta Positiva"
        "Elección Mala":
            calchona "Respuesta Negativa"
    calchona "Decisión 3"
    menu:
        "Elección Buena":
            $ goodAnswersCalchona += 1
            calchona "Respuesta Positiva"
        "Elección Mala":
            calchona "Respuesta Negativa"

    if goodAnswersCalchona == 3:
        jump calchonaGoodEnding
    else:
        jump calchonaBadEnding


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


label calchonaGoodEnding:
    $ persistent.calchonaEnding = True
    "Good Ending Calchona :)"
    jump normalEnding

label calchonaBadEnding:
    "Bad Ending Calchona :("
    # Finaliza el juego:
    return

label pomberoGoodEnding:
    $ persistent.pomberoEnding = True
    "Good Ending Pombero :)"
    jump normalEnding

label pomberoBadEnding:
    "Bad Ending :("
    # Finaliza el juego:
    return

label silbonGoodEnding:
    $ persistent.silbonEnding = True
    "Good Ending Silbón :)"
    jump normalEnding

label silbonBadEnding:
    "Bad Ending :("
    # Finaliza el juego:
    return

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
    