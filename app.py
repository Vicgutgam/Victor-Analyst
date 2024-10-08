import streamlit as st
import pandas as pd
import numpy as np

#El request me va a ayudar a importar el archivo de la URL y así permitirme descargarme el archivo una vez pulse el botón
import requests



## Para arracan streamlit hay que escribir en la terminal : streamlit run app.py

# Pasos para conseguir el botón de descarga del CV:
    # 1º Crear una referencia del la url
    
link_cv = 'blob:null/a565714e-faae-4df4-b61b-7dc2ba1e8385'

    # 2º Crear el botón de descarga en la zona deseada.

    #3º Configurar el botón 

response = requests.get(link_cv)
pdf_data = response.content



# Configuración de la página
st.set_page_config(
    page_title='VictorAnalyst',
    page_icon="🤖",
    layout='wide', )





# sidebar



top_sidebar_placeholder = st.sidebar.empty()
top_sidebar_placeholder.markdown('''
<p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Victor-Analyst/refs/heads/main/bilder/portada.jpg?token=GHSAT0AAAAAACXPZG5MLQWWR4XXNVGV4HDUZXVVP2A" width="100%" alt="Akkurat">
  <br>
</p>
''', unsafe_allow_html=True)
st.sidebar.title('Index')


page = st.sidebar.radio('', ['How Am I?','Night at the museum', 'King of the Pirates', 'Machine Learning', 'Visualization','Python', 'SQL'])
about_selection = ''



with st.spinner('Creando un mundo mejor...'):
    
    
### PÁGINA  PRINCIPAL
    if page == 'How Am I?':
        st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Victor-Analyst/refs/heads/main/bilder/jeg.jpeg?token=GHSAT0AAAAAACXPZG5NORLLY6HD74Z7A7IYZXVVNTA" width="30%" alt="Víctor Gutiérrez Data Analyst">
  <br>
</p>
''', unsafe_allow_html=True)
        st.subheader('How Am I?')
        st.markdown("####  👨‍🏫 I am a data analyst with more than ten years of experience in the field of teaching and culture. Now I am working on improving my knowledge in Machine Learning and advanced data visualization. If you´re wondering where I am, I´m probably taking a walk in the nearby mountains or participating in some cultural activity.")

        st.markdown('### Why did I create this?')
        st.markdown('#### I recently had a job interview and I had a bit of a hard time figuring out what my skills are or what projects I have created.')

        st.markdown('### My CV:')
        st.markdown('#### Here is my CV in case you are interested in getting to know me a little better.')

#Creación del botón de descarga:

        st.download_button(
    label="Descargar PDF",
    data=pdf_data,
    file_name="archivo.pdf",
    mime="application/pdf")
        

### perfil


# Página 'Tu Perfil'
    elif page == 'Night at the museum':
    # Title and logo   
        st.markdown('''
                     <p align="center">
  <img src="https://raw.githubusercontent.com/Vicgutgam/Victor-Analyst/refs/heads/main/bilder/museum.jpg?token=GHSAT0AAAAAACXPZG5M4IXSVPZVNKWGH6ZOZXVWW4A" width="30%" alt="Akkurat">
  <br>
</p>
''', unsafe_allow_html=True)     
        st.markdown("## Introduction:")
        st.markdown('#### This project has its origins in the practices of a data analysis Bootcamp. It is inspired by the typical "create your own story" notebooks where the journey of the adventure is the adventure itself, with the outcome being unimportant.')

        st.markdown('## What does the code currently do?')
        st.markdown('#### It is currently in a very primitive state and only includes a few functions related to the responses that the user can give. The code is developed in a very linear way, following the initial inspiration, but it already has some dictionaries introduced that I hope can be completed over time.')
        
        
### PROYECTOS EN CASA
    elif page == 'Proyectos en casa':
        # Title and logo
        st.markdown("# ¿Cómo reducir tu huella de carbono en casa?")
              # Select organ sample using selectbox
        organ_sample = st.selectbox('', ['Tu jardín', 'Gestión de Residuos', 'Energía','Alimentación', 'Agua'])
        # Image upload
        if organ_sample == 'Agua':
            st.markdown('### Reduciendo tu Huella de Carbono en Casa: El Papel del Agua')
            texto_columna, imagen_columna = st.columns([2, 1])
            with texto_columna:
                st.write('##### La reducción de la huella de carbono en casa es esencial para mitigar el cambio climático y promover la sostenibilidad. Una de las áreas clave para lograr esto es gestionar el uso del agua de manera eficiente y consciente. Aquí hay algunas estrategias simples pero efectivas para reducir tu huella de carbono relacionada con el agua en casa:', '\n', '##### 1. Reparar fugas y mejorar la eficiencia: Las fugas de agua pueden representar un desperdicio significativo de recursos y energía. Revisa regularmente las tuberías, grifos y accesorios en busca de fugas y repáralas de inmediato. Además, considera instalar dispositivos de ahorro de agua, como cabezales de ducha de bajo flujo y grifos con sensor, para reducir el consumo de agua sin sacrificar la comodidad.', '\n', '##### 2. Reducir el consumo de agua caliente: El calentamiento del agua requiere una cantidad considerable de energía, lo que contribuye a las emisiones de carbono. Limita el uso del agua caliente siempre que sea posible, como lavar la ropa con agua fría y tomar duchas más cortas. Además, asegúrate de que tu calentador de agua esté bien aislado para minimizar la pérdida de calor y considera la posibilidad de instalar un calentador de agua solar para reducir aún más tu dependencia de fuentes de energía no renovables.','\n', '##### 3. Captura y reutiliza el agua de lluvia: La recolección de agua de lluvia es una forma efectiva de conservar agua potable y reducir la demanda de agua de la red municipal. Instala barriles de lluvia en tu propiedad para capturar el agua de lluvia y úsala para regar el jardín, lavar el coche y otras tareas no potables. Esto no solo reduce tu huella de carbono al disminuir la energía necesaria para purificar y distribuir agua potable, sino que también ayuda a prevenir la escasez de agua en tu comunidad.',  '\n', '##### 4. Adopta prácticas de jardinería sostenible: El riego del jardín puede representar una parte significativa del consumo de agua en el hogar. Opta por plantas nativas y adaptables que requieran menos agua y establece un horario de riego eficiente, preferiblemente durante las horas más frescas del día para reducir la evaporación. Además, utiliza métodos de riego más precisos, como el riego por goteo, para maximizar la eficiencia y minimizar el desperdicio de agua.',  '\n','##### 5. Conciencia y educación: Finalmente, educa a tu familia sobre la importancia de conservar el agua y reducir la huella de carbono en casa. Involúcralos en la implementación de prácticas de conservación del agua y hábitos sostenibles, como cerrar el grifo mientras se cepillan los dientes o tomar duchas más cortas. A través de la conciencia y la acción colectiva, podemos hacer una diferencia significativa en la reducción de nuestra huella de carbono relacionada con el agua y contribuir a un futuro más sostenible para todos.',  '\n','##### Adoptar estas prácticas en casa no solo puede ayudar a reducir tu huella de carbono, sino que también puede ahorrarte dinero a largo plazo y mejorar la calidad de vida de tu hogar. Con pequeños cambios en nuestros hábitos diarios, podemos marcar una gran diferencia en la conservación de este recurso vital y en la protección del medio ambiente.')
            with imagen_columna:
                st.image('https://raw.githubusercontent.com/Vicgutgam/Final-proyect/main/Im%C3%A1genes/Energ%C3%ADa.png')

        if organ_sample == 'Tu jardín':
            st.markdown('### ¿Quiéres tener un jardín casero y ecológicamente responsable?')
            texto_columna, imagen_columna = st.columns([2, 1])
            with texto_columna:
                st.write('### Cultivar un Jardín Casero y Ecológico: ¡Una Opción Sostenible!', '\n', '##### Crear un jardín en casa que sea ecológicamente responsable es posible y gratificante. Optar por plantas nativas y adaptadas a tu región no solo fomenta la biodiversidad, sino que también reduce la necesidad de agua y fertilizantes. Además, prácticas como el compostaje y el uso de fertilizantes orgánicos enriquecen el suelo de forma natural y sostenible.','\n', '##### Conservar el agua es esencial, por lo que instalar sistemas de riego por goteo y recolectar agua de lluvia para el riego son estrategias efectivas. Mantener el jardín sin pesticidas tóxicos es clave para proteger la vida del suelo, los polinizadores y la salud humana. En su lugar, puedes recurrir a métodos naturales de control de plagas y malas hierbas, así como promover un equilibrio natural en el jardín.', '\n', '##### La educación y la conciencia ambiental también desempeñan un papel crucial. Participar en actividades educativas sobre jardinería sostenible y compartir conocimientos con otros puede ayudarte a mejorar continuamente tus prácticas y contribuir a un futuro más verde.', '\n', '##### Cultivar un jardín casero y ecológicamente responsable no solo embellece tu entorno, sino que también te permite ser parte de la solución para cuidar nuestro planeta. Con prácticas conscientes y un compromiso continuo, puedes disfrutar de un jardín vibrante y saludable mientras contribuyes positivamente al medio ambiente.')

            with imagen_columna:
                st.image("https://raw.githubusercontent.com/Vicgutgam/Final-proyect/main/Im%C3%A1genes/Houseplants.jpg?token=GHSAT0AAAAAACNF6SMVFCTXH6V464RL2IWUZPPQONQ")                
                
        if organ_sample == 'Alimentación':
            st.markdown('### Reduciendo tu Huella de Carbono en Casa a través de la Alimentación')
            
            texto_columna, imagen_columna = st.columns([2, 1])
            with texto_columna:
                st.write("##### En un mundo cada vez más consciente del impacto ambiental de nuestras acciones, la reducción de la huella de carbono se ha convertido en una prioridad. Una de las áreas clave donde podemos hacer cambios significativos es en nuestra alimentación. La producción de alimentos contribuye de manera significativa a las emisiones de gases de efecto invernadero, desde la deforestación para la agricultura hasta las emisiones de metano de la ganadería. Aquí hay algunas formas prácticas de reducir tu huella de carbono en casa a través de tus elecciones alimentarias:", "\n", "##### Opta por una dieta basada en plantas: Reducir el consumo de productos de origen animal es una de las formas más efectivas de reducir tu huella de carbono. Las dietas basadas en plantas requieren menos recursos naturales y emiten menos gases de efecto invernadero en comparación con las dietas ricas en carne y lácteos.", "\n", "##### Compra alimentos locales y de temporada: Al reducir la distancia que viajan los alimentos desde el lugar de producción hasta tu plato, se reduce la cantidad de energía necesaria para transportarlos. Además, apoyar a los agricultores locales fomenta prácticas agrícolas sostenibles y ayuda a mantener vivas las economías locales. ", "\n", "##### Reduce el desperdicio de alimentos: Una gran cantidad de alimentos se desperdicia cada año, lo que contribuye significativamente a las emisiones de gases de efecto invernadero. Planificar las comidas, almacenar los alimentos adecuadamente y utilizar sobras creativamente puede ayudar a reducir este desperdicio y, por lo tanto, tu huella de carbono.", "\n", "##### Elige productos orgánicos y de comercio justo: Los productos orgánicos suelen tener una huella de carbono más baja porque no se utilizan productos químicos sintéticos en su producción, lo que reduce las emisiones asociadas con la fabricación y el uso de estos productos. Además, el apoyo al comercio justo garantiza que los agricultores y trabajadores agrícolas reciban un salario justo por su trabajo.", "\n", "##### Minimiza el consumo de alimentos procesados: Los alimentos procesados a menudo requieren una gran cantidad de energía y recursos para su producción y envasado. Optar por alimentos frescos y minimamente procesados no solo es más saludable, sino que también puede reducir tu huella de carbono.", "\n", "##### Al hacer cambios conscientes en tus elecciones alimentarias, puedes contribuir significativamente a la reducción de tu huella de carbono en casa. Cada pequeña acción cuenta en la lucha contra el cambio climático, y la alimentación es un área donde todos podemos hacer una diferencia tangible.")          
                    
            with imagen_columna:
                st.image("https://raw.githubusercontent.com/Vicgutgam/Final-proyect/main/Im%C3%A1genes/alimentaci%C3%B3n.jpg", caption="Descripción de la imagen")                
             
            
        if organ_sample == 'Gestión de Residuos':
            st.markdown('### Algo huele mal: La Gestión de Residuos')
            
            texto_columna, imagen_columna = st.columns([2,1])
            with texto_columna:
                st.write("##### Reducir la huella de carbono en casa es un objetivo alcanzable mediante la adopción de prácticas sostenibles de gestión de residuos. Aquí hay algunas formas prácticas de minimizar tu impacto ambiental relacionado con la basura:", "\n", "##### 1. Reducir, Reutilizar, Reciclar: Esta tríada es fundamental para la gestión de residuos sostenible. Reduce el consumo de productos de un solo uso y opta por opciones reutilizables siempre que sea posible. Separa adecuadamente los materiales reciclables y asegúrate de seguir las pautas de reciclaje de tu comunidad para maximizar la cantidad de residuos que se desvían de los vertederos.", "\n", "##### 2. Compostaje: El compostaje es una forma efectiva de reducir la cantidad de residuos orgánicos que terminan en los vertederos y producen metano, un potente gas de efecto invernadero. Comienza un compostero en tu jardín o utiliza un sistema de compostaje en interiores para convertir los restos de comida y otros materiales orgánicos en abono rico en nutrientes para tus plantas.", "\n", "##### 3. Compra consciente: Al realizar compras, elige productos con envases mínimos o envases reciclables. Prefiere productos a granel y compra solo lo que necesitas para reducir el desperdicio de alimentos y otros productos perecederos. Además, considera la posibilidad de apoyar a empresas que adoptan prácticas de embalaje sostenibles y ofrecen opciones de recarga o reutilización.", "\n", "##### 4. Reducción de residuos electrónicos: Los dispositivos electrónicos desechados pueden contaminar el medio ambiente si no se manejan adecuadamente. Recicla tus dispositivos electrónicos viejos o rotos en centros de reciclaje especializados o dona los equipos aún funcionales a organizaciones benéficas. Al comprar dispositivos nuevos, elige opciones de bajo consumo de energía y busca productos que sean fáciles de reparar y actualizar.", "\n", "##### 5. Educación y conciencia: Fomenta una cultura del reciclaje y la reducción de residuos en tu hogar educando a tu familia sobre la importancia de estas prácticas y participando en actividades comunitarias de conservación. A través de la conciencia y la acción colectiva, podemos hacer una diferencia significativa en la reducción de nuestra huella de carbono relacionada con los residuos y contribuir a un futuro más sostenible para todos.", "\n", "##### Al adoptar estas prácticas en casa, puedes desempeñar un papel importante en la reducción de la cantidad de residuos que generamos y en la mitigación de nuestro impacto ambiental. Con pequeños cambios en nuestros hábitos diarios, podemos marcar una gran diferencia en la protección del medio ambiente y la conservación de los recursos naturales para las generaciones futuras.")

            with imagen_columna:
                st.image("https://raw.githubusercontent.com/Vicgutgam/Final-proyect/main/Im%C3%A1genes/reciclaje.jpg")  
                
                
        if organ_sample == 'Energía':
            st.markdown('### Energía para mejorar.')
            
            imagen_columna, texto_columna  = st.columns([1,1])
            with imagen_columna:
                st.image('https://raw.githubusercontent.com/Vicgutgam/Final-proyect/main/Im%C3%A1genes/windmill-6307058_640.jpg')
                st.write("#####  En la era moderna, la electricidad es un recurso vital que utilizamos en casi todos los aspectos de nuestra vida diaria. Sin embargo, la generación de electricidad a menudo implica la quema de combustibles fósiles, lo que contribuye significativamente a las emisiones de gases de efecto invernadero y al cambio climático. Afortunadamente, existen varias formas en las que podemos reducir nuestra huella de carbono en casa al manejar nuestra electricidad de manera más eficiente y adoptar fuentes de energía más limpias. Aquí hay algunas estrategias clave:", "\n", "##### Cambio a fuentes de energía renovable: Una de las formas más efectivas de reducir tu huella de carbono es cambiar a fuentes de energía renovable, como la solar o la eólica. Instalar paneles solares en el techo de tu casa o suscribirte a un proveedor de energía renovable puede reducir drásticamente tus emisiones de carbono asociadas con la electricidad.", "\n", "##### Reduce el consumo de energía: Adopta hábitos que reduzcan tu consumo de electricidad, como apagar las luces y los aparatos electrónicos cuando no estén en uso, utilizar bombillas LED de bajo consumo energético, y mantener los electrodomésticos en buen estado y utilizarlos de manera eficiente.", "\n")
                          
            with texto_columna:
                st.write("\n"  "##### Invierte en electrodomésticos eficientes: Al comprar nuevos electrodomésticos, busca aquellos que tengan una calificación de eficiencia energética alta. Los electrodomésticos modernos están diseñados para ser más eficientes en el uso de energía, lo que puede resultar en ahorros significativos a largo plazo tanto para tu bolsillo como para el medio ambiente.", "\n", "##### Aprovecha la domótica: La domótica, o el uso de tecnología para controlar y automatizar los sistemas del hogar, puede ayudarte a optimizar el uso de la electricidad. Programa termostatos inteligentes para que ajusten la temperatura de tu hogar según tus horarios, utiliza sensores de movimiento para encender y apagar las luces automáticamente, y controla remotamente tus aparatos para evitar el consumo innecesario de energía.", "\n", "##### Participa en programas de eficiencia energética: Muchas compañías eléctricas ofrecen programas de eficiencia energética que pueden ayudarte a identificar y implementar medidas para reducir tu consumo de electricidad. Desde auditorías energéticas hasta incentivos para actualizar tus sistemas de iluminación y HVAC, aprovechar estos programas puede ser beneficioso tanto para ti como para el medio ambiente.", "\n", "##### Al implementar estas estrategias, puedes reducir significativamente tu huella de carbono en casa y contribuir a la lucha contra el cambio climático. Cada pequeño cambio en la forma en que utilizamos la electricidad puede marcar la diferencia, y es fundamental que todos hagamos nuestra parte para crear un futuro más sostenible y saludable para las generaciones venideras.")

            
    

#### SECIÓN DE TRABAJAR JUNTOS          
    
    elif page == 'Trabajemos juntos':
        # Title and logo
        st.markdown("# ¿Dónde puedes colaborar?")
        df = pd.DataFrame({
    'lat': [37.37089785429304,  37.35065576245189, 37.38512609328087],
    'lon': [-5.991058532301121,  -6.0415316764851745, -6.166784796037962],
    'Actividad': ['Acuario de Sevilla', 'Grupo Scout III Aljarafe', 'Granja Escuela Cuna'], 'Donde': ['google maps link','google maps link','google maps link'],
    '¿Qué hacer?' : ['Educación medioambiental','Educación medioambiental','Educación medioambiental'],'Contacto':['tlf/web/email','tlf/web/email','tlf/web/email']})
        st.map(df)
        st.table(df.iloc[:, 2:])
        

        
### CONSEJOS        
        
   

 ## Perfiles de YOUTUBE

        if about_selection == 'Youtube':
            st.markdown("# Los perfiles más verdes")
            columima, columtex = st.columns(2)
            with columima : 
                st.image("https://yt3.googleusercontent.com/ytc/AIdro_ndCLGm2grN-ZpUcvLtyIA9xocM6T6fQNY_bf_p=s176-c-k-c0x00ffffff-no-rj",width=400)
                            
            with columtex :
                st.write("### Si estás buscando la forma de conocer todo lo relacionado con la ecología y el medio ambiente, has encontrado el lugar en el que tendrás toda la información que necesitas. En un solo click, podrás encontrar información sobre el reciclaje, el ahorro energético, el desarrollo sostenible, la contaminación, los animales, las plantas, consejos sobre salud y bienestar y mucho más.")
                st.link_button("Visitar perfil", "https://www.youtube.com/@EcologiaVerde")
            
            columima, columtex = st.columns(2)
            with columima : 
                st.image("https://yt3.googleusercontent.com/ytc/AIdro_kvsydw0ASSAf_vmHQnnYhb3tJPybzkmx-vjfIWew=s176-c-k-c0x00ffffff-no-rj",width=400)
                            
            with columtex :
                st.write("### Canal dedicado a la divulgación científica dirigido por el físico español Jose Luís Crespo. Aprende física, ecología de una manera diferente.")
                st.link_button("Visitar perfil", "https://www.youtube.com/@QuantumFracture")
            
            columima, columtex = st.columns(2)
            with columima : 
                st.image("https://yt3.googleusercontent.com/SiCVAA5geV7vfpVrj8fAt3X73OHAnbxJQbKfzHA129zB9ZmZV1FCF7NZhxoXw8l_mvmlNzb-HQ=s176-c-k-c0x00ffffff-no-rj",width=400)
                            
            with columtex :
                st.write("### Aquí encontrarás inspiración para cultivar una vida más saludable y equilibrada. Sumérgete en consejos prácticos sobre propiedades y beneficios de las plantas, nutrición, ejercicios, técnicas de relajación y más. Su objetivo es brindar información para que tengas una mejor calidad de vida..")
                st.link_button("Visitar perfil", "https://www.youtube.com/@ecovidasaludable")
    
    
## Perfiles de WEBS

        if about_selection == 'Webs de interés':
            st.markdown("# Aprende más navengando en la web:")
            columima, columtex = st.columns(2)
            with columima : 
                st.image("https://youngcapital-uploads-production.s3.amazonaws.com/nl/public/es/Image/lp/greenpeace/Logo.jpg",width=400)
                            
            with columtex :
                st.write("### Hay webs que no necesitan presentación pero aún así aquí está Greenpeace para luchar cada día por un ecosistema más limpio y sostenible. En su web encontrarás proyectos, consejos, noticias y mil formas de participar en esta lucha por un mundo mejor.")
                st.link_button("Visitar perfil","https://es.greenpeace.org/es/")
            
            columima, columtex = st.columns(2)
            with columima : 
                st.image("https://ecocosas.com/wp-content/uploads/cwv-webp-images/2020/07/cropped-cropped-cropped-logo-1-157x49.png.webp",width=400)
                            
            with columtex :
                st.write("### En Ecocasas encontraras toda la información que necesites sobre como convertir tu hogar en un espacio más sostenible para el ecosistema y más cercanoCanal dedicado a la divulgación científica dirigido por el físico español Jose Luís Crespo. Aprende física, ecología de una manera diferente.")
                st.link_button("Visitar perfil", "https://ecocosas.com/")
            
            columima, columtex = st.columns(2)
            with columima : 
                st.image("https://www.ambientum.com/wp-content/uploads/2017/12/logo-ambientum_GrisRojo.png",width=400)
                            
            with columtex :
                st.write("### Ambientum:""\n" "#### ¿Quiéres estar al tanto de las últimas noticias sobre el medio ambiente? En la web de Ambientum podrás leer cada día noticias nuevas sobre todo lo relacionado con el medio ambiente.")
                st.link_button("Visitar perfil", "https://www.ambientum.com/")        
                
                
                
          
        

    elif page == 'Tu huella de carbono':
        
        st.markdown("# Descubre tu huella de carbono")
        option = st.selectbox('## ¿Qué tipo de alimentación llevas?',
    ('Omnívora', 'Vegetariana', 'Vegana'))
        if option == "Omnívora":
            comida = 2700
        if option == "Vegetariana":
            comida = 2250
        if option == "Vegana":
            comida = 1800
        
        restaurante = st.slider( "¿Cuántas veces a la semana comes fuera de casa?", 0, 24, 1)
        rest = restaurante * 1.75
        
        
        number = st.number_input("¿Cuántos km en coche haces a la semana?", value=0)
        coche = number * 0.2 * 52       
       
        ropa = st.slider( "¿Cuántas prendas de vestir compras al año?", value=10)
        ropa_total = ropa * 17
                
        electricidad =  st.number_input( "¿Cuántos kWh de electricidad has consumido en el último mes?", value=0)
        elec_total = electricidad * 0.3 * 12 
        
        gas =  st.number_input( "¿Cuántos kWh de gas has consumido en el último mes?", value=0)
        gas_total = gas * 0.25 * 12
        
        st.write('### Tu huella de carbono es:')
        total_huella = ropa + comida + coche+ gas_total + elec_total +rest
        huella = st.write(f'##',  total_huella,), st.write('### kg de CO2 al año')
        
        if total_huella >= 2000:
            st.write('####  😔 Para llevar a cabo una vida ecológicamente sostenible se cree que tu huella de carbono debería de no ser superior a los 2000 kg. Te invitamos a que leas los consejos o veas proyectos para reducir tu huella de carbono.')
            
        if total_huella <= 2000:
            st.write('#### 🥳 ¡Felicidades!  🥳 Tu huella de carbono está dentro del rango de lo que se condideraría sostenible sigue así y no olvides en ayudar a los demás a reducir su huella de carbono. Entre todos podremos hacer de este mundo un lugar mejor.')
            
            
 


# Enlaces de mis perfiles

github_url = "https://github.com/Vicgutgam"
linkedin_url = "https://www.linkedin.com/in/v%C3%ADctor-guti%C3%A9rrez-gamero-81048b179/"


# Agregar el enlace en la barra lateral

st.sidebar.markdown(f"[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=social&logo=github)]({github_url})")  
        
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=social&logo=linkedin)]({linkedin_url})")