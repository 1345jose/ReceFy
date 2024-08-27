document.addEventListener('DOMContentLoaded', () => {
    const consejos = [
        { 
            titulo: 'Afilado de Cuchillos', 
            descripcion: `
            <p>El afilado de cuchillos es una de las prácticas más importantes en la cocina. Un cuchillo afilado no solo facilita el proceso de cortar y picar alimentos, sino que también aumenta la seguridad en la cocina. Un cuchillo desafilado requiere más presión al cortar, lo que puede provocar que el cuchillo resbale y cause accidentes. Además, un cuchillo bien afilado realiza cortes más precisos, permitiendo un manejo más eficiente de los ingredientes y un acabado más profesional en tus preparaciones culinarias.</p>
            <p>Para mantener tus cuchillos en óptimas condiciones, es esencial afilarlos regularmente. Existen varias técnicas y herramientas para afilar cuchillos, desde piedras de afilar hasta afiladores manuales o eléctricos. La elección del método depende de tu nivel de experiencia y de la frecuencia con la que utilizas tus cuchillos. Independientemente del método que elijas, asegúrate de seguir las instrucciones cuidadosamente para obtener el mejor resultado y prolongar la vida útil de tus herramientas de cocina.</p>
            <p>Además del afilado regular, es importante aprender a utilizar y mantener correctamente los cuchillos. Siempre corta sobre superficies adecuadas y evita golpear el cuchillo contra objetos duros que puedan dañar el filo. Al limpiar tus cuchillos, hazlo a mano con cuidado y evita sumergirlos en agua durante largos periodos para prevenir el deterioro del filo. Un buen mantenimiento garantiza que tus cuchillos sigan siendo una extensión eficiente de tus habilidades culinarias y te permitan disfrutar del proceso de cocinar.</p>`,
    
            imagen: "https://images.pexels.com/photos/2291591/pexels-photo-2291591.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Uso de Hierbas Frescas', 
            descripcion: `
            <p>Las hierbas frescas son una adición fantástica a tus platos, pero es importante saber cuándo y cómo usarlas para obtener el máximo sabor y aroma. Añadir hierbas frescas al final de la cocción ayuda a preservar sus sabores delicados y sus aceites esenciales.</p>
            <p>El perejil, la albahaca y el cilantro son excelentes opciones para añadir frescura a tus platos. El perejil puede complementar casi cualquier plato, mientras que la albahaca es ideal para platos italianos y el cilantro para preparaciones mexicanas y asiáticas. Siempre recuerda añadir las hierbas frescas justo antes de servir para disfrutar de su sabor completo y evitar que se marchiten.</p>
            <p>Además, no todas las hierbas necesitan cocinarse. Algunas, como el cilantro y la albahaca, se deben añadir al final para mantener su frescura. También es útil almacenar las hierbas frescas en un lugar fresco y seco o en el refrigerador para prolongar su vida útil.</p>`,
            imagen: "https://images.pexels.com/photos/357737/pexels-photo-357737.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Control de Temperatura', 
            descripcion: `
            <p>El control de la temperatura es crucial en la cocina para garantizar que los alimentos se cocinen correctamente y sean seguros para comer. Utilizar un termómetro de cocina es una manera efectiva de asegurarte de que tus carnes estén cocidas a la perfección y no queden crudas en el centro.</p>
            <p>Para la carne de res, cerdo y pollo, el uso de un termómetro puede ayudarte a alcanzar las temperaturas internas recomendadas para evitar enfermedades transmitidas por alimentos. Por ejemplo, la carne de res se debe cocinar a una temperatura mínima de 63°C, mientras que el pollo debe alcanzar los 74°C.</p>
            <p>Además del control de la temperatura interna, es importante ajustar la temperatura de cocción en tu estufa o horno según la receta. Cocinar a temperaturas muy altas puede quemar los alimentos por fuera mientras permanecen crudos por dentro, mientras que temperaturas demasiado bajas pueden resultar en una cocción desigual.</p>`,
            imagen: "https://images.pexels.com/photos/376464/pexels-photo-376464.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Mantenimiento de Utensilios', 
            descripcion: `
            <p>El mantenimiento adecuado de tus utensilios de cocina es esencial para prolongar su vida útil y asegurar un entorno de cocina higiénico. Limpia y desinfecta tus utensilios regularmente para prevenir la acumulación de bacterias y evitar la contaminación cruzada.</p>
            <p>Para utensilios de acero inoxidable, usa esponjas suaves y detergentes no abrasivos para evitar rayaduras. Los utensilios de madera deben lavarse a mano y secarse completamente para evitar la absorción de agua, lo cual puede llevar a deformaciones o grietas.</p>
            <p>Almacena tus utensilios de manera organizada para prevenir daños. Utiliza organizadores o soportes para mantenerlos en su lugar y evitar que se desgasten prematuramente. Un buen cuidado y mantenimiento contribuyen a una experiencia de cocina más segura y agradable.</p>`,
            imagen: "https://images.pexels.com/photos/6956739/pexels-photo-6956739.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Uso Correcto de Aceites', 
            descripcion: `
            <p>Cada tipo de aceite tiene un punto de humo diferente, lo que afecta cómo se comporta durante la cocción. Utiliza aceites adecuados para cada tipo de cocción para evitar sabores amargos y humo excesivo. Por ejemplo, el aceite de oliva es ideal para saltear a fuego medio, mientras que los aceites con puntos de humo más altos, como el aceite de aguacate, son mejores para freír a altas temperaturas.</p>
            <p>Es importante también almacenar los aceites correctamente para evitar que se enrancien. Guarda los aceites en un lugar fresco y oscuro, y asegúrate de cerrar bien el envase después de cada uso.</p>
            <p>El uso adecuado de aceites no solo mejora el sabor de tus platos, sino que también puede impactar la textura y la presentación de los mismos. Experimenta con diferentes tipos de aceites para encontrar cuáles complementan mejor tus recetas.</p>`,
            imagen: "https://images.pexels.com/photos/26605561/pexels-photo-26605561/free-photo-of-mujer-sentado-sujetando-tenedor.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Conservación de Alimentos', 
            descripcion: `
            <p>Almacenar los alimentos de manera adecuada es clave para mantener su frescura y evitar la contaminación. Utiliza envases herméticos para proteger los alimentos de la humedad y el aire, lo que puede prolongar su vida útil y prevenir la proliferación de bacterias.</p>
            <p>Etiqueta los envases con la fecha de almacenamiento para asegurarte de utilizar los alimentos dentro de su período de frescura. También es útil organizar tu despensa y refrigerador para que los alimentos más antiguos se utilicen primero.</p>
            <p>Además, asegúrate de seguir las recomendaciones de almacenamiento específicas para cada tipo de alimento, ya que algunos deben refrigerarse mientras que otros pueden almacenarse a temperatura ambiente.</p>`,
            imagen: "https://images.pexels.com/photos/26466932/pexels-photo-26466932/free-photo-of-comida-apple-manzana-frutas.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Preparación de Ingredientes', 
            descripcion: `
            <p>La preparación de ingredientes es una parte esencial de la cocina que puede afectar la eficiencia y el resultado final de tus platos. Prepara todos tus ingredientes antes de comenzar a cocinar para tener todo a mano y evitar olvidos.</p>
            <p>Esto incluye medir y cortar los ingredientes según sea necesario, así como tener todos los utensilios y equipos listos para su uso. Tener todos los ingredientes preparados de antemano te permitirá cocinar de manera más fluida y disfrutar del proceso sin interrupciones.</p>
            <p>Además, la preparación previa puede ayudar a reducir el tiempo de cocción y permitirte concentrarte en técnicas más avanzadas o en la presentación de los platos.</p>`,
            imagen: "https://images.pexels.com/photos/106877/pexels-photo-106877.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Uso de Especias', 
            descripcion: `
            <p>Las especias son un componente clave para añadir sabor y profundidad a tus platos. Sin embargo, el momento en que añades las especias puede afectar el sabor final del plato. Algunas especias liberan más sabor cuando se tuestan ligeramente antes de añadirlas a tus recetas.</p>
            <p>Experimenta con la cantidad y el tipo de especias que usas para encontrar el equilibrio perfecto para cada plato. También es útil conocer la diferencia entre especias enteras y molidas, ya que las especias enteras a menudo tienen un sabor más intenso y duradero.</p>
            <p>Recuerda que el almacenamiento adecuado de las especias es esencial para mantener su frescura y sabor. Guarda las especias en recipientes herméticos en un lugar fresco y oscuro.</p>`,
            imagen: "https://images.pexels.com/photos/1340116/pexels-photo-1340116.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Higiene en la Cocina', 
            descripcion: `
            <p>La higiene en la cocina es fundamental para prevenir enfermedades y mantener un ambiente de cocina seguro. Lávate las manos frecuentemente, especialmente después de manejar alimentos crudos o tocar superficies sucias.</p>
            <p>Limpia las superficies de trabajo, los utensilios y los equipos con regularidad para evitar la proliferación de bacterias y otros patógenos. Utiliza desinfectantes y asegúrate de que los productos de limpieza sean seguros para el contacto con alimentos.</p>
            <p>Un ambiente de cocina ordenado y limpio no solo mejora la seguridad alimentaria, sino que también hace que cocinar sea una experiencia más agradable y eficiente.</p>`,
            imagen: "https://images.pexels.com/photos/2062426/pexels-photo-2062426.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Evaluación de Textura', 
            descripcion: `
            <p>La evaluación de la textura de los alimentos es crucial para determinar si están cocidos correctamente. No te fíes únicamente del tiempo de cocción, ya que este puede variar según el equipo de cocina y el tamaño de los ingredientes.</p>
            <p>Para alimentos como carnes y pasteles, prueba la textura con un tenedor o un termómetro para asegurarte de que estén cocidos a fondo. La textura puede darte pistas sobre si un alimento necesita más tiempo de cocción o si está listo para servir.</p>
            <p>Aprender a evaluar la textura correctamente puede mejorar significativamente la calidad de tus platos y ayudarte a evitar errores comunes en la cocina.</p>`,
            imagen: "https://images.pexels.com/photos/672046/pexels-photo-672046.jpeg?auto=compress&cs=tinysrgb&w=600"
        },

        { 
            titulo: 'Uso Adecuado del Horno',
            descripcion: `
            <p>El horno es una herramienta esencial en la cocina, pero es crucial usarlo correctamente para obtener los mejores resultados. Precalienta siempre el horno antes de colocar los alimentos, ya que esto asegura una cocción uniforme y un mejor acabado. El tiempo de precalentamiento puede variar según el modelo de horno, así que sigue las recomendaciones de tu manual.</p>
            <p>Utiliza las rejillas del horno de manera adecuada para obtener una cocción óptima. La colocación de los alimentos en la rejilla central suele ser la mejor opción para una cocción uniforme. Además, evita abrir la puerta del horno con frecuencia para mantener la temperatura constante y prevenir cambios en el tiempo de cocción.</p>
            <p>Siempre revisa los alimentos hacia el final del tiempo de cocción recomendado para evitar que se quemen. Usa un temporizador para no olvidarte de los platos y considera utilizar un termómetro de horno para verificar la temperatura exacta. Esto garantiza que tus platos se cocinen a la perfección.</p>`,
            imagen: "https://images.pexels.com/photos/3082785/pexels-photo-3082785.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Preparación de Masa',
            descripcion: `
            <p>La preparación de masa es un arte que requiere precisión y paciencia. Asegúrate de medir todos los ingredientes con precisión para obtener la consistencia correcta. Utiliza ingredientes a temperatura ambiente, especialmente la mantequilla y los huevos, para facilitar su mezcla y obtener una masa más suave.</p>
            <p>Amasar la masa adecuadamente es crucial para desarrollar el gluten, lo que da estructura a los productos horneados. Amasa hasta que la masa esté suave y elástica, pero evita amasar en exceso, ya que esto puede hacer que la textura sea dura.</p>
            <p>Deja reposar la masa según las indicaciones de la receta para permitir que el gluten se relaje y para que la levadura haga su trabajo. Un buen reposo ayuda a mejorar la textura y el sabor de la masa. Cubre la masa con un paño húmedo para evitar que se seque durante el reposo.</p>`,
            imagen: "https://images.pexels.com/photos/9095/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Uso de Plancha de Cocción',
            descripcion: `
            <p>Las planchas de cocción son ideales para lograr un dorado perfecto y un sabor ahumado en los alimentos. Precalienta la plancha antes de comenzar a cocinar para obtener una superficie caliente que sella rápidamente los alimentos, reteniendo sus jugos y sabores.</p>
            <p>Asegúrate de aplicar una capa ligera de aceite en la plancha para evitar que los alimentos se peguen. Utiliza utensilios de cocina adecuados para evitar dañar la superficie de la plancha, como espátulas de silicona o madera.</p>
            <p>Después de cocinar, limpia la plancha mientras aún esté tibia para eliminar los restos de alimentos. Usa un raspador adecuado para evitar rayaduras y asegúrate de secarla bien para prevenir la oxidación. Un buen mantenimiento prolongará la vida útil de tu plancha de cocción.</p>`,
            imagen: "https://images.pexels.com/photos/4552980/pexels-photo-4552980.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Uso de Sartenes de Hierro Fundido',
            descripcion: `
            <p>Las sartenes de hierro fundido son conocidas por su durabilidad y capacidad para retener el calor. Antes de usarlas, asegúrate de que estén bien sazonadas para evitar que los alimentos se peguen. Sazonar una sartén implica cubrirla con una capa delgada de aceite y calentarlo para formar una capa antiadherente.</p>
            <p>Cuando cocines con sartenes de hierro fundido, evita usar utensilios metálicos que puedan rayar la superficie. Opta por utensilios de madera, silicona o plástico para mantener la capa de sazón en buen estado.</p>
            <p>Después de usar, limpia la sartén con agua caliente y un cepillo de cerdas suaves. Evita usar detergentes agresivos y asegúrate de secarla completamente antes de guardarla para prevenir la oxidación. Un buen mantenimiento garantiza que la sartén siga funcionando durante muchos años.</p>`,
            imagen: "https://images.pexels.com/photos/26651105/pexels-photo-26651105/free-photo-of-casas-casa-mesa-cocina.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Preparación de Salsa Base',
            descripcion: `
            <p>Preparar una salsa base es el primer paso para crear una variedad de salsas y aderezos. Comienza por saltear cebollas, ajo o especias en aceite caliente para desarrollar una base de sabor. Una vez que los ingredientes estén dorados y fragantes, añade líquidos como caldo o vino para crear la base de la salsa.</p>
            <p>Deja que la salsa base hierva a fuego lento para que los sabores se mezclen y la salsa se reduzca a la consistencia deseada. Ajusta el sabor con sal, pimienta y otras especias según tu preferencia. La reducción ayuda a intensificar el sabor y a conseguir una textura más rica.</p>
            <p>Una vez que la salsa base esté lista, puedes personalizarla añadiendo ingredientes como hierbas frescas, crema o queso. La salsa base se puede guardar en el refrigerador durante unos días o congelarse para su uso posterior. Prepárala con anticipación para ahorrar tiempo en la cocina.</p>`,
            imagen: "https://images.pexels.com/photos/5907859/pexels-photo-5907859.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Cocción de Pasta',
            descripcion: `
            <p>Cocer pasta correctamente es esencial para obtener una textura perfecta. Utiliza abundante agua con sal para hervir la pasta; la sal ayuda a sazonar la pasta durante la cocción. No agregues aceite al agua, ya que esto puede evitar que las salsas se adhieran a la pasta.</p>
            <p>Sigue las instrucciones del paquete para el tiempo de cocción, y prueba la pasta unos minutos antes de que finalice el tiempo recomendado para asegurarte de que esté al dente, es decir, cocida pero firme al morder. Escurre la pasta y mézclala inmediatamente con la salsa para evitar que se pegue.</p>
            <p>Si preparas la pasta con anticipación, enjuágala con agua fría después de escurrirla para detener el proceso de cocción y evitar que se pegue. Guarda la pasta en un recipiente hermético en el refrigerador y mézclala con un poco de salsa o aceite antes de recalentarla.</p>`,
            imagen: "https://images.pexels.com/photos/5907896/pexels-photo-5907896.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Uso de Limón en la Cocina',
            descripcion: `
            <p>El limón es un ingrediente versátil que puede realzar el sabor de muchos platos. Añade jugo de limón a tus recetas para aportar acidez y frescura. También puedes usar ralladura de limón para dar un toque cítrico y aromático a tus preparaciones.</p>
            <p>Cuando exprimas un limón, utiliza un exprimidor para obtener la mayor cantidad de jugo posible y evitar las semillas. La ralladura de limón se debe tomar solo de la capa externa de la piel, ya que la parte blanca es amarga.</p>
            <p>El limón también es útil para prevenir la oxidación de frutas y verduras cortadas. Rocía un poco de jugo de limón sobre las superficies expuestas para mantener los alimentos frescos y evitar que se pongan marrones.</p>`,
            imagen: "https://images.pexels.com/photos/26098725/pexels-photo-26098725/free-photo-of-naturaleza-planta-arbol-follaje.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Preparación de Brotes y Germinados',
            descripcion: `
            <p>Los brotes y germinados son una excelente adición a ensaladas y sándwiches. Puedes prepararlos en casa utilizando un frasco de vidrio y semillas de brotes. Enjuaga las semillas y déjalas en remojo durante la noche, luego enjuágalas nuevamente y colócalas en un frasco cubierto con una gasa o tela fina.</p>
            <p>Enjuaga los brotes dos veces al día con agua fresca y asegúrate de mantener el frasco en un lugar cálido y oscuro. Después de unos días, verás cómo los brotes comienzan a crecer. Una vez que alcancen el tamaño deseado, enjuágalos bien y guárdalos en el refrigerador.</p>
            <p>Los brotes y germinados se pueden almacenar en un recipiente hermético en el refrigerador durante una semana. Úsalos en tus comidas para agregar un toque fresco y crujiente. Asegúrate de lavarlos bien antes de consumirlos para eliminar cualquier posible contaminante.</p>`,
            imagen: "https://images.pexels.com/photos/99548/water-lilies-bud-pond-green-99548.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Uso de Ingredientes Frescos',
            descripcion: `
            <p>Utilizar ingredientes frescos es clave para obtener el mejor sabor y calidad en tus platos. Compra frutas y verduras de temporada, ya que suelen estar más frescas y tener un mejor sabor. Al seleccionar ingredientes frescos, busca aquellos que tengan colores vivos y texturas firmes.</p>
            <p>Almacena los ingredientes frescos correctamente para prolongar su vida útil. Las frutas y verduras deben guardarse en lugares frescos y secos, o en el refrigerador si es necesario. Asegúrate de revisar los productos regularmente para eliminar cualquier parte dañada o en descomposición.</p>
            <p>Antes de cocinar, limpia y prepara los ingredientes frescos adecuadamente. Lava bien las frutas y verduras para eliminar residuos y pesticidas. Para asegurar la frescura, utiliza los ingredientes frescos lo antes posible después de comprarlos.</p>`,
            imagen: "https://images.pexels.com/photos/1414651/pexels-photo-1414651.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Uso de Aceites en Cocina',
            descripcion: `
            <p>Los aceites juegan un papel importante en la cocina, proporcionando sabor y ayudando en la cocción. Elige el aceite adecuado según el método de cocción; por ejemplo, el aceite de oliva es ideal para saltear y aderezar, mientras que los aceites con alto punto de humo, como el de canola, son mejores para freír.</p>
            <p>Al almacenar aceite, guárdalo en un lugar fresco y oscuro para evitar que se oxide y se vuelva rancio. Usa envases opacos o ámbar para proteger el aceite de la luz, lo que ayuda a mantener su calidad y sabor durante más tiempo.</p>
            <p>Evita reutilizar el aceite para cocinar varias veces, ya que esto puede afectar su sabor y calidad. Después de freír o saltear, permite que el aceite se enfríe antes de desecharlo adecuadamente. Recuerda que un buen aceite es fundamental para una cocina saludable y sabrosa.</p>`,
            imagen: "https://images.pexels.com/photos/1022385/pexels-photo-1022385.jpeg?auto=compress&cs=tinysrgb&w=600"
        },
        { 
            titulo: 'Conservación de Hierbas Aromáticas',
            descripcion: `
            <p>Las hierbas aromáticas frescas pueden agregar sabores excepcionales a tus platos, pero es importante conservarlas adecuadamente para mantener su frescura. Puedes almacenar las hierbas frescas en el refrigerador en una bolsa perforada o en un recipiente cerrado para evitar que se marchiten.</p>
            <p>Para conservar hierbas a largo plazo, considera secarlas o congelarlas. Para secarlas, cuelga las hierbas en un lugar seco y oscuro hasta que estén completamente secas, luego guárdalas en frascos herméticos. Para congelarlas, pica las hierbas y colócalas en bandejas de hielo con agua o aceite.</p>
            <p>Usa las hierbas secas en tus recetas de manera similar a las frescas, pero recuerda que su sabor puede ser más concentrado. Al almacenar hierbas secas, mantén los frascos en un lugar fresco y oscuro para preservar su aroma y sabor.</p>`,
            imagen: "https://images.pexels.com/photos/6387848/pexels-photo-6387848.jpeg?auto=compress&cs=tinysrgb&w=600"
        }

        
    ];

    const itemsPorPagina = 10;
    let paginaActual = 1;

    function mostrarConsejos(pagina) {
        const container = document.getElementById('consejos-container');
        container.innerHTML = '';
        
        const inicio = (pagina - 1) * itemsPorPagina;
        const fin = inicio + itemsPorPagina;
        const consejosPagina = consejos.slice(inicio, fin);
        
        consejosPagina.forEach(consejo => {
            const consejoHTML = `
                <div class="consejo-container mb-4">
                    <div class="row">
                        <div class="col-md-4">
                            <img src="${consejo.imagen}" alt="${consejo.titulo}" class="img-fluid">
                        </div>
                        <div class="col-md-8">
                            <h5 class="consejo-titulo">${consejo.titulo}</h5>
                            <p class="consejo-descripcion">${consejo.descripcion}</p>
                        </div>
                    </div>
                </div>
            `;
            container.innerHTML += consejoHTML;
        });
    }

    function mostrarPaginacion() {
        const paginationContainer = document.querySelector('.pagination');
        paginationContainer.innerHTML = '';

        const totalPaginas = Math.ceil(consejos.length / itemsPorPagina);

        const crearBoton = (texto, pagina) => {
            const boton = document.createElement('li');
            boton.classList.add('page-item');
            if (pagina === paginaActual) {
                boton.classList.add('active');
            }
            boton.innerHTML = `<a class="page-link" href="#">${texto}</a>`;
            boton.addEventListener('click', (event) => {
                event.preventDefault();
                paginaActual = pagina;
                mostrarConsejos(paginaActual);
                mostrarPaginacion();
                window.scrollTo({ top: 0, behavior: 'smooth' }); // Desplazar hacia arriba
            });
            return boton;
        };

        paginationContainer.appendChild(crearBoton('&laquo;', paginaActual - 1));
        for (let i = 1; i <= totalPaginas; i++) {
            paginationContainer.appendChild(crearBoton(i, i));
        }
        paginationContainer.appendChild(crearBoton('&raquo;', paginaActual + 1));
    }

    mostrarConsejos(paginaActual);
    mostrarPaginacion();
});

//GLOSARIO

document.addEventListener("DOMContentLoaded", function() {
    const glossary = {
        A: [
            { term: "Abrillantar", definition: "Dar brillo con gelatina o grasa a un preparado." },
            { term: "Aclarar", definition: "Formar canales o estrías en el exterior de un género crudo, antes de utilizarlo." },
            { term: "Acaramelar", definition: "Bañar con caramelo un pastel u otro preparado." },
            { term: "Aderezar", definition: "Sazonar." },
            { term: "Adobar", definition: "Poner un género crudo con un preparado llamado adobo, con el objeto de conservarlo, ablandarlo o darle un aroma especial." },
            { term: "Agarrarse", definition: "Pegarse por efecto del calor al fondo del recipiente un género, dándole mal sabor y color." },
            { term: "Agitar", definition: "Remover con frecuencia una salsa mediante una espátula o similares para recuperar la homogeneidad." },
            { term: "Albardar", definition: "Envolver en una lámina delgada de tocino un género para evitar que éste se seque al cocinarlo." },
            { term: "Aliñar", definition: "Aderezar o sazonar." },
            { term: "Almíbar", definition: "Azúcar disuelto en agua a fuego muy lento hasta que adquiera una cierta consistencia. Se utiliza para tortitas, caramelizar moldes, glaseados, entre otros." },
            { term: "Al Dente", definition: "Comida que se cocina para que esté firme al morderla." },
            { term: "Amasar", definition: "Trabajar una masa con las manos." },
            { term: "Aplastar", definition: "Reducir el grosor de un producto a mano o mediante algún utensilio." },
            { term: "Aprovechar", definition: "1. Utilizar restos de comida para otros preparados. 2. Recoger totalmente restos de pastas, cremas, etc." },
            { term: "Aromatizar", definition: "Agregar especias o hierbas a preparados para darles un cierto sabor u olor." },
            { term: "Arreglar o aviar", definition: "Preparar de forma completa un ave para su cocción o asado, etc." },
            { term: "Arropar", definition: "Tratar con un paño un preparado de levadura para facilitar su estufado o fermentación. Sinónimo: estofar y fermentar." },
            { term: "Asar", definition: "Cocinar un alimento a altas temperaturas en un horno, parrilla o similares." },
            { term: "Asustar", definition: "Añadir un líquido frío a un preparado que está en ebullición, para que de forma momentánea deje de cocer." },
            { term: "Atemperar", definition: "Proceso que se lleva a cabo en algunos alimentos como el chocolate. Se funde al baño maría y luego se enfría para que se vuelva más estable." },
            { term: "A punto de nieve", definition: "Se obtiene batiendo únicamente las claras hasta que adquieran una consistencia espumosa." }
            // Añade aquí más términos de la sección A...
        ],
        B: [
            { term: "Bañar", definition: "Cubrir totalmente un género con una materia líquida para alcanzar la densidad o grado de amalgamiento deseado." },
            { term: 'Batir', definition: 'Agitar los ingredientes mediante una varilla o una batidora, hasta adquirir la consistencia deseada.' },
            { term: 'Blanquear', definition: 'Dar un hervor o cocer a medias, para quitar el mal gusto, mal sabor o mal color a ciertos géneros.' },
            { term: 'Bolear', definition: 'Trabajar una masa hasta darle forma redondeada. Obtenemos así panes redondos, albóndigas, trufas de chocolate, entre otros.' },
            { term: 'Brasear o Bresear', definition: 'Cocinar un género (generalmente carnes duras y de gran tamaño), lentamente, durante largo tiempo en compañía de elementos de condimentación, hortalizas, vino, caldo, especias.' },
            { term: 'Bridar', definition: 'Atar aves, carnes o pescado mediante un cordel (bramante) para evitar que pierdan su forma durante la cocción.' },
            { term: 'Bouquet-garni', definition: 'Consiste en atar en un ramillete hierbas aromáticas. Se utiliza para que no queden restos de hierbas en el preparado.' }
        ],

        C: [
            { term: 'Caramelizar', definition: 'Derretir el azúcar hasta adquirir un color dorado para luego untar en un preparado o molde.' },
            { term: 'Clarificar', definition: 'Dar limpieza o transparencia a una salsa, caldo o gelatina, ya sea espumándola durante su cocción lenta o por la adición de clarificantes.' },
            { term: 'Confitar', definition: 'Cocinar un alimento a baja temperatura (entre 60 y 90ºC) sumergiéndolo en un medio graso.' },
            { term: 'Camisar', definition: 'Untar un molde con mantequilla, glucosa u otros productos para evitar que el producto del interior se pegue en la cocción.' },
            { term: 'Cincelar', definition: 'Hacer incisiones sobre un pescado para facilitar su cocción.' },
            { term: 'Clavetear', definition: 'Introducir, pinchándolos, clavos (especias muy olorosas) en una cebolla o similar.' },
            { term: 'Cocer', definition: `<ol>
                <li>Transformar por la acción de calor el gusto y propiedades de un género.</li>
                <li>Ablandar y hacer digeribles los artículos.</li>
                <li>Hacer entrar en ebullición un líquido.</li>
                <li>Cocinar o guisar.</li>
            </ol>` },
            { term: 'Cocer al baño-maría', definition: 'Cocer lentamente un preparado poniéndole en un recipiente, que a su vez, debe introducirse en otro mayor con agua, poniéndose el todo para su cocción al horno o fogón.' },
            { term: 'Cocer al vapor', definition: 'Cocinar un alimento mediante vapor de agua. Los alimentos se introducen en un recipiente para que no entren en contacto con el medio líquido.' },
            { term: 'Cocer a la inglesa', definition: 'Técnica utilizada normalmente en vegetales, que consiste en hervirlos en agua con abundante sal.' },
            { term: 'Cocer en blanco', definition: 'Cocinar al horno en moldes de pasta sin aderezos sustituyendo estos por legumbres secas, que se han de retirar antes de completar la cocción.' },
            { term: 'Cocer en papillote', definition: 'Cocinar un alimento recubriéndolo con papel de aluminio o papel de horno para conservar todo su sabor y mantener todos sus jugos.' },
            { term: 'Colar', definition: 'Filtrar por un colador o estameña un líquido para privarle de impurezas.' },
            { term: 'Condimentar o sazonar', definition: 'Añadir condimentos a un género para darle sabor.' },
            { term: 'Cortar en cubos', definition: 'Cortar la comida en pequeños cubos.' },
            { term: 'Cortar en juliana', definition: 'Cortar alimentos en tiras finas y parejas.' },
            { term: 'Coulis', definition: 'Salsa de consistencia similar al jarabe obtenida a partir del triturado de alimentos y la concentración de su sabor.' }
        ],

        D:[
            { term: 'Decorar', definition: 'Embellecer con adornos un género, para su presentación.' },
            { term: 'Desalar', definition: 'Sumergir un género salado en agua, fría generalmente, para que pierda la sal.' },
            { term: 'Desangrar', definition: 'Sumergir en agua fría una carne o pescado para que pierda la sangre. También se dice desangrar a la operación de despojar a una langosta o similar, de la materia que en crudo tiene en su cabeza, para su posterior empleo.' },
            { term: 'Desecar', definition: 'Secar por evaporación un preparado, poniéndolo con su cacerola al fuego y moviendo con la espátula de madera o similar, para que no se pegue al utensilio. Sinónimo: Reducción.' },
            { term: 'Desembarazar o desbarasar', definition: 'Desocupar el lugar donde se ha trabajado, colocar cada cosa en su lugar habitual.' },
            { term: 'Desescamar', definition: 'Quitar las escamas de un pescado.' },
            { term: 'Desglasar', definition: 'Añadir vino a una asadura recién utilizada para recuperar la grasa o jugo que contenga.' },
            { term: 'Desgrasar', definition: 'Retirar la grasa de un preparado.' },
            { term: 'Deshuesar', definition: 'Separar los huesos de una carne.' },
            { term: 'Desmoldear', definition: 'Sacar un preparado del molde, del que conservará la forma.' },
            { term: 'Desollar', definition: 'Desposeer a una res sacrificada de su piel.' },
            { term: 'Desplumar', definition: 'Despojar de las plumas a los animales sacrificados.' },
            { term: 'Dorar', definition: 'Dar un golpe de calor a un alimento para que adquiera un color dorado en su superficie.' }
        ],

        E: [
            { term: 'Emborrachar', definition: 'Empapar de almíbar y licor o vino un postre.' },
            { term: 'Embridar o Bridar', definition: 'Sujetar con un bramante ave, carne o pescados, para apretar su carne y que conserven su forma después de cocinadas.' },
            { term: 'Empanar', definition: 'Pasar por harina, huevo batido y pan rallado un género que resultará cubierto por una especie de costra.' },
            { term: 'Emplatar', definition: 'Poner los preparados terminados en la fuente en que han de servirse.' },
            { term: 'Encamisar, camisar o forrar', definition: 'Cubrir las paredes interiores de un molde con un género, dejando un hueco central para rellenar con otro preparado distinto.' },
            { term: 'Encolar', definition: 'Adicionar gelatina o un preparado líquido para que, al enfriarse, tome cuerpo y brillo.' },
            { term: 'Enfriar con hielo', definition: 'Poner un recipiente dentro de otro recipiente que contenga hielo y sal o agua.' },
            { term: 'Engrasar', definition: 'Embadurnar el interior de un molde con aceite u otra grasa.' },
            { term: 'Enharinar', definition: '1. Espolvorear. 2. Cubrir de harina la superficie de un género.' },
            { term: 'Envejecer', definition: 'Dar tiempo a una carne (generalmente caza) para que logre cierto punto de maduración.' },
            { term: 'Emulsión', definition: 'Una mezcla de dos líquidos que normalmente no se unen, como aceite y vinagre. Para emulsionar, bata los dos líquidos juntos hasta que formen una mezcla cremosa.' },
            { term: 'Escabechar', definition: 'Poner un género cociendo en un preparado líquido llamado escabeche para su conservación y toma de sabor característico.' },
            { term: 'Escaldar', definition: 'Sumergir en agua hirviendo un género, manteniéndolo poco tiempo.' },
            { term: 'Escalfar', definition: 'Sumergir y cocinar el alimento (normalmente huevos) en agua a unos 90ºC con un chorrito de vinagre.' },
            { term: 'Escalonar', definition: 'Cortar en láminas gruesas y sesgadas un género.' },
            { term: 'Escamar o desescamar', definition: 'Despojar de las escamas a un pescado.' },
            { term: 'Escarchar', definition: 'Cocer fruta en azúcar. Cuando se seca la fruta queda recubierta por una fina capa brillante parecida a la escarcha.' },
            { term: 'Escudillar', definition: 'Hacer dibujos o trabajar con la manga pastelera.' },
            { term: 'Espalmar', definition: 'Adelgazar un género mediante golpes suaves con la aplastadora o espalmadera.' },
            { term: 'Espolvorear', definition: 'Repartir en forma de lluvia por la superficie de un preparado un género en polvo.' },
            { term: 'Espumar o desespumar', definition: 'Retirar de un preparado, con la espumadera, las impurezas que en forma de espuma floten en él.' },
            { term: 'Esquinar', definition: 'Cortar una res en dos, siguiendo su espina dorsal.' },
            { term: 'Estirar', definition: '1. Presionar con el rodillo sobre una pasta para adelgazarla. 2. Conseguir mayor rendimiento del normal en un género al racionarlo.' },
            { term: 'Estofar', definition: 'Cocinar lentamente, con su propio jugo y el que posean los elementos de condimentación o guarnición que acompañan al género principal.' },
            { term: 'Estufar', definition: 'Poner en la estufa o lugar tibio una pasta de levadura bien tapada, para que fermente y desarrolle.' }
        ],

        F:[
            { term: 'Faisandé', definition: 'Sabor parecido al del faisán que toma algunas especies de caza cuando se dejan envejecer.' },
            { term: 'Fermentar', definition: 'Propiciar el crecimiento de microorganismos como mohos, bacterias o levaduras, para la obtención de alimentos como yogures, miso, kimchi, entre otros.' },
            { term: 'Filetear', definition: 'Cortar un género en lonchas delgadas y alargadas.' },
            { term: 'Flamear o llamear', definition: '1. Pasar por una llama, sin humo, un género para quemarle las plumas o pelos que hayan quedado al desplumar o limpiar. 2. Hacer arder un líquido espirituoso en un preparado (flambear).' },
            { term: 'Fondearse', definition: 'Agarrarse ligeramente.' },
            { term: 'Fondear', definition: 'Adaptar una masa a un molde con ayuda de una porción de masa o con las propias manos.' },
            { term: 'Freír', definition: 'Introducir en una sartén con grasa caliente un género para su cocinado, debiendo formar costra dorada.' }
        ],

        G: [
            { term: 'Gelificar', definition: 'Convertir un líquido en gelatina.' },
            { term: 'Glacear', definition: '1. Cubrir un género con un almíbar reducido a la mitad de su cantidad inicial, con el objetivo de darle brillo y consistencia. 2. Pasar por una gelatina fundida un género.' },
            { term: 'Glaseado', definition: 'Cubrir con una capa brillante un género, a menudo dulce.' },
            { term: 'Grano', definition: 'Punto y grano de lo cocido.' },
            { term: 'Grasa', definition: 'Cubrir un género con una grasa líquida o untuosa.' },
            { term: 'Gratinar', definition: 'Hacer tostar a horno fuerte o gratinadora las capas superiores granulosas de un preparado (dorar).' },
            { term: 'Gratinar', definition: '1. Dar vueltas al arroz con un tenedor, esparciéndolo y mezclándolo con otros ingredientes. 2. Trabajar con una espátula el hojaldre, para conservarlo seco y que no se pegue.' },
            { term: 'Guarnición', definition: 'Adorno que sirve para acompañar el platillo principal.' }
        ],
        H: [
            { term: 'Helar', definition: 'Coagular por medio de temperaturas de menos de 0º una mezcla de repostería llamada helado.' },
            { term: 'Heñir', definition: 'Tratar una masa para la elaboración de pan u otros bollos con los puños.' },
            { term: 'Hermosear', definition: 'Suprimir los elementos inútiles a la presentación de un manjar. Ejemplo: suprimir los huesos superfluos de las chuletas.' },
            { term: 'Hervir', definition: '1. Cocer un género por inmersión en un líquido en ebullición. 2. Hacer que un líquido entre en ebullición por la acción del calor.' },
            { term: 'Hornear', definition: 'Cocinar alimentos con calor seco dentro del horno.' }
        ],
        L: [
            { term: 'Levantar', definition: 'Hervir de nuevo un preparado para evitar una posible fermentación o deterioro.' },
            { term: 'Ligar', definition: 'Espesar un preparado por la acción de un elemento de ligazón, fécula, harina,….' },
            { term: 'Lustrar', definition: 'Espolvorear de azúcar llamado glas o lustre un preparado dulce.' }
        ],
        M: [
            { term: 'Macerar', definition: 'Poner frutas peladas y generalmente cortadas en compañía de azúcar, vino, licores, para que tome el sabor de éstos. Por extensión se aplica también a las carnes en adobo o en marinada.' },
            { term: 'Majar', definition: 'Quebrar de forma grosera: machacar de forma imperfecta, generalmente con ayuda del mortero.' },
            { term: 'Marcar', definition: 'Preparar un plato a falta de su cocción.' },
            { term: 'Marchar', definition: 'Empezar la cocción de un plato, previamente preparado o marcado.' },
            { term: 'Marinar o enmarinar', definition: 'Poner géneros, generalmente carnes, en compañía de vino, hierbas aromáticas, etc., para conservar, aromatizar o ablandarlos.' },
            { term: 'Masa madre', definition: 'Masa formada por harina y agua. En la propia harina se encuentran las levaduras y bacterias necesarias para la fermentación de las masas. Gracias a la masa madre se obtiene un sabor y olor muy específico en los alimentos elaborados con esta masa madre.' },
            { term: 'Mechar', definition: 'Introducir a una carne cruda, con ayuda de una mechadora, tiras de tocino en forma de mecha.' },
            { term: 'Moldear', definition: 'Poner un preparado dentro de un molde para que tome las forma de este.' },
            { term: 'Mojar', definition: 'Añadir a un preparado el líquido necesario para su cocción.' },
            { term: 'Montar', definition: '1. Colocar los géneros, después de guisados, sobre un zócalo, castrón o simplemente emplatar. 2. Sinónimo de batir y emulsionar.' },
            { term: 'Mortificar', definition: 'Dejar envejecer una carne para que se ablande. (faisande)' }
        ],
        N: [
            { term: 'Napar', definition: 'Cubrir totalmente un preparado con un líquido espeso que permanezca.' },
            { term: 'Neutralizar', definition: 'Contrarrestar el sabor ácido o amargo de un alimento mediante la adición de un ingrediente neutral.' },
            { term: 'Nitrurar', definition: 'Proceso por el cual se conserva un género crudo, añadiéndole nitrato o salitres.' },
            { term: 'Nacarar', definition: 'Dar brillo a una preparación por medio de un barniz transparente, el cual se hace con clara de huevo batida y colada con miga de pan.' }
        ],
        P:[
            { term: 'Pasado', definition: '1. Punto de los géneros crudos que no están frescos y bordean el punto de descomposición, sin llegar a él. 2. Excesivamente crudo. 3. Colado (triturar).' },
            { term: 'Pasar o colar', definition: 'Despojar un preparado de sustancias innecesarias por medio de colador o estameña. 2. Tamizar.' },
            { term: 'Picar', definition: '1. Mechar superficialmente un preparado. 2. Cortar finamente un género.' },
            { term: 'Pinchar', definition: 'Dar pequeñas punzadas a una masa para evitar que se hinche o se encoja.' },
            { term: 'Pochar', definition: 'Cocinar un alimento en poco aceite y baja temperatura, de esta manera conseguimos que el alimento se cocine en su propio jugo.' },
            { term: 'Prensar', definition: 'Poner un preparado dentro de un molde-prensa para su enfriamiento dentro de ella o, a falta de este utensilio, poner unos pesos apropiados encima del preparado con el objeto de comprimirlo.' },
            { term: 'Puesta a Punto', definition: 'Preparación y acercamiento de todo lo necesario para empezar a trabajar.' },
            { term: 'Punto', definition: 'Cuando un artículo alcanza un grado justo de cocción o razonamiento, se dice que está a punto para su utilización.' }
        ],
        R:[
            { term: 'Racionar', definition: 'Dividir un género en porciones o fracciones para su distribución.' },
            { term: 'Rallar', definition: 'Desmenuzar un determinado género empleando un rallador u otro utensilio similar.' },
            { term: 'Rebozar', definition: 'Cubrir un alimento con harina o pan rallado y huevo, para freírlo posteriormente.' },
            { term: 'Rectificar', definition: 'Poner a punto el razonamiento o color de un preparado.' },
            { term: 'Reducir', definition: 'Disminuir el volumen de un preparado líquido por evaporación al hervir, para que resulte más sustancioso o espeso.' },
            { term: 'Reforzar', definition: 'Añadir a una salsa, sopa o similar, un preparado que intensifique su sabor o color natural.' },
            { term: 'Refrescar', definition: '1. Poner en agua fría un género inmediatamente después de cocido o blanqueado, para cortar la cocción de forma rápida. 2. Añadir pasta nueva a una ya trabajada.' },
            { term: 'Rehogar', definition: 'Cocinar total o parcialmente un género, poniéndolo a fuego lento con poca grasa.' },
            { term: 'Remojar', definition: 'Poner un género desecado, para que recupere la humedad, dentro de un líquido frío.' },
            { term: 'Risolar', definition: 'Dorar a fuego vivo, con grasa, un género que resultará totalmente cocinado.' }
        ],
        S:[
            { term: 'Salar', definition: 'Poner en salmuera un género crudo para su conservación, toma de sabor o color característico.' },
            { term: 'Salsear', definition: 'Cubrir de salsa un género, generalmente al servicio.' },
            { term: 'Saltear', definition: 'Cocinar totalmente o parcialmente, con grasa y a fuego violento para que no pierda su jugo un preparado que debe salir dorado.' },
            { term: 'Sazonar', definition: '1. Añadir condimentos a un género para darle olor o sabor. 2. Añadir sal a un género.' },
            { term: 'Sofreír', definition: 'Rehogar.' },
            { term: 'Sudar', definition: 'Dejar que un alimento expulse su jugo mediante la cocción lenta del mismo.' },
            { term: 'Sufratar', definition: 'Napar una pieza de carne o pescado con una salsa, que al enfriarse, permanece sobre el género.' }
        ],
        V:[
            { term: 'Volcán', definition: 'Recopilar una montaña de harina haciendo un agujero en el centro para derramar los diferentes alimentos necesarios y proceder al amasado.' },
            { term: 'Vinagreta', definition: 'Un aderezo para ensalada hecho con un ácido, aceite y condimentos.' },
            { term: 'Volver a cocer', definition: 'Cocinar nuevamente un alimento que ya ha sido cocido previamente.' },
            { term: 'Volver al fuego', definition: 'Continuar la cocción de un preparado después de un reposo o pausa.' }
        ]
    };

    function createGlossarySection(letter, terms) {
        const section = document.createElement('div');
        section.id = letter;
        section.className = 'glossary-section';

        const header = document.createElement('h3');
        header.textContent = letter;
        header.className = 'letter-header'; // Common class for all letters
        section.appendChild(header);

        terms.forEach(term => {
            const paragraph = document.createElement('p');

            const strong = document.createElement('strong');
            strong.textContent = term.term + ':';
            paragraph.appendChild(strong);

            paragraph.appendChild(document.createTextNode(' ' + term.definition));
            section.appendChild(paragraph);
        });

        return section;
    }

    const glossaryContainer = document.getElementById('glossary-container');
    for (const [letter, terms] of Object.entries(glossary)) {
        const section = createGlossarySection(letter, terms);
        glossaryContainer.appendChild(section);
    }
});