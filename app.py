import streamlit as st

# 1. EL ARCHIVADOR (Nuestra base de datos de preguntas)
# Cada bloque entre { } es una pregunta distinta. Cada pregunta es un diccionario de 3 entradas (texto, opciones, correcta).
# Creamos la lista de preguntas: 
preguntas = [

    {
        "texto": "¿Cuál es la capital de Francia?",
        "opciones": [" ", "Madrid", "Tokyo", "Londres", "París"],
        "correcta": "París"
    },
    {
        "texto": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": [" ", "Saturno", "Júpiter", "Venus", "Urano"],
        "correcta": "Júpiter"
    },
    {
        "texto": "¿Qué científico formuló la teoría de la relatividad?",
        "opciones": [" ", "Albert Einstein", "Marie Curie", "Charles Darwin", "Nikola Tesla"],
        "correcta": "Albert Einstein"
    },
    {
        "texto": "¿Qué elemento químico tiene el símbolo “Au”?",
        "opciones": [" ", "Platino", "Mercurio", "Oro", "Astato"],
        "correcta": "Oro"
    },
    {
        "texto": "¿Qué artista pintó “La noche estrellada”?",
        "opciones": [" ", "Salvador Dalí", "Vincent van Gogh", "Leonardo da Vinci", "Joan Miró"],
        "correcta": "Vincent van Gogh"
    },  
    {
        "texto": "¿Qué empresa desarrolla el iPhone?",
        "opciones": [" ", "Apple", "Samsung", "Amazon", "Microsoft"],
        "correcta": "Apple"
    },
    {
        "texto": "¿En qué año llegó el hombre a la Luna por primera vez?",
        "opciones": [" ", "1956", "1969", "1986", "2000"],
        "correcta": "1969"
    },
    {
        "texto": "¿Qué emperador francés fue derrotado en la batalla de Waterloo?",
        "opciones": [" ", "Carlos II", "Luis XVI", "Felipe IV", "Napoleón Bonaparte"],
        "correcta": "Napoleón Bonaparte"
    },
    {
        "texto": "¿Qué país alberga el monte Everest?",
        "opciones": [" ", "Rusia", "Nepal", "Kiribati", "Mongolia"],
        "correcta": "Nepal"
    },

]

# Configuración visual de la página
st.title("🎓 Mi Primer Examen Interactivo")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")

# 2. EL FORMULARIO (Agrupamos todo para que no se recargue la web a cada clic)
# Eso se consigue con el comando with

with st.form("quiz_form"):

    # Aquí guardaremos las respuestas que elija el alumno. Será una lista.
    respuestas_usuario = []
    
    # Recorremos el archivador usando un bucle 'for' para crear las preguntas
    for pregunta in preguntas:
        st.subheader(pregunta["texto"]) # Ponemos el texto de la pregunta

        # Creamos los botones de opción (radio)
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])

        # Guardamos la elección en nuestra lista usando append ()
        respuestas_usuario.append(eleccion)
        st.write("---") # Una línea para separar preguntas

    # Botón obligatorio para cerrar el formulario
    boton_enviar = st.form_submit_button("Entregar Examen")

# 3. LA CORRECCIÓN (Solo ocurre cuando pulsamos el botón)
if boton_enviar:
    aciertos = 0
    # Total es número de preguntas (usa el método len)
    total = len(preguntas)

    # Comparamos las respuestas del usuario con las 'correctas' del archivador
    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1
        
        if respuestas_usuario[i] == " ":
            continue
            
        else:
            aciertos - 1
            
    # Calculamos la nota sobre 10
    nota = round((aciertos / total) * 10, 2)
    
    # Mostramos el resultado con colores
    st.divider()
    st.header(f"Resultado final: {nota} / 10")

    if nota <= 2.99:
        st.error(f"muy insuficiente Has suspendido con {aciertos} aciertos.")
        
    elif 3 <= nota < 4.99:
        st.error(f"insuficiente Has suspendido con {aciertos} aciertos.")

    elif 5 <= nota < 6:
        st.success(f"suficiente Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!

    elif 6.1 <= nota < 7:
        st.success(f"bien Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!

    elif 7.1 <= nota < 8:
        st.success(f"notable Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!
 
    elif 8.1 <= nota < 9:
        st.success(f"sobresaliente Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!
 
    else:
        st.success(f"EXCELENTE Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!



import streamlit as st

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(
        ["1","2","3","4","5","6","7","8","9"])

with tab1:
    st.header("París")
    st.image("https://cdn2.civitatis.com/francia/paris/galeria/torre-eiffel-altura.jpg", width=200)
with tab2:
    st.header("Júpiter")
    st.image("https://content.nationalgeographic.com.es/medio/2022/08/02/el-planeta-jupiter_b107cb4f_1280x1280.jpg", width=200)
with tab3:
    st.header("Albert Einstein")
    st.image("https://www.recoleta.edu.pe/blog/wp-content/uploads/2025/04/PORTADA-6.jpg", width=200)
with tab4:
    st.header("Oro")
    st.image("https://i.pinimg.com/736x/14/98/bb/1498bbcbcf79ca739e5bf59b338a64b0.jpg", width=200)
with tab5:
    st.header("Vicent van Gogh")
    st.image("https://historia-arte.com/_/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpbSI6WyJcL2FydHdvcmtcL2ltYWdlRmlsZVwvbm9jaGUtZXN0cmVsbGFkYS12YW4tZ29naC5qcGciLCJyZXNpemUsMjAwMCwyMDAwIl19.3mkWyHY4L_z-nPKgFPQik1jxy3GXcxNc0ShLGcVAlRg.jpg", width=200)
with tab6:
    st.header("Apple")
    st.image("https://www.apple.com/v/iphone/home/cj/images/overview/consider_modals/environment/modal_packaging__bscmhs9fjdhy_large.jpg", width=200)
with tab7:
    st.header("1969")
    st.image("https://www.etsit.upm.es/fileadmin/documentos/biblioteca/biblioteca/imagenes/dia_del_libro/2020/Hitos/Hitos_imagenes/Hito10_Hombre_en_la_Luna_300x203.jpg", width=200)
with tab8:
    st.header("Napoleón Bonaparte")
    st.image("https://static.wikia.nocookie.net/memes-pedia/images/c/c9/Cee4133a4556c093b1f2ae27ee6d2ea0.jpg/revision/latest?cb=20230927152508&path-prefix=es", width=200)
with tab9:
    st.header("Nepal")
    st.image("https://imagenes2.eltiempo.com/files/og_thumbnail/uploads/2020/10/20/5f8f119570285.jpeg", width=200)

