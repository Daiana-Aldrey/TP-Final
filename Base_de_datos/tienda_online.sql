--
-- PostgreSQL database dump
--

-- Dumped from database version 15.7 (Ubuntu 15.7-1.pgdg23.10+1)
-- Dumped by pg_dump version 16.3 (Ubuntu 16.3-1.pgdg23.10+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: celulares; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.celulares (
    id integer NOT NULL,
    marca character varying NOT NULL,
    modelo character varying NOT NULL,
    descripcion character varying NOT NULL,
    procesador character varying NOT NULL,
    memoria character varying NOT NULL,
    camara_delantera character varying NOT NULL,
    camara_trasera character varying NOT NULL,
    pantalla character varying NOT NULL,
    bateria character varying NOT NULL,
    precio integer NOT NULL,
    financiacion integer,
    imagen_url character varying NOT NULL
);


ALTER TABLE public.celulares OWNER TO postgres;

--
-- Name: celulares_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.celulares_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.celulares_id_seq OWNER TO postgres;

--
-- Name: celulares_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.celulares_id_seq OWNED BY public.celulares.id;


--
-- Name: notebooks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notebooks (
    id integer NOT NULL,
    marca character varying NOT NULL,
    modelo character varying NOT NULL,
    descripcion character varying NOT NULL,
    procesador character varying NOT NULL,
    memoria character varying NOT NULL,
    almacenamiento character varying NOT NULL,
    sistema_operativo character varying NOT NULL,
    camara_delantera character varying NOT NULL,
    pantalla character varying NOT NULL,
    bateria character varying NOT NULL,
    precio integer NOT NULL,
    financiacion integer,
    imagen_url character varying NOT NULL
);


ALTER TABLE public.notebooks OWNER TO postgres;

--
-- Name: notebooks_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.notebooks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.notebooks_id_seq OWNER TO postgres;

--
-- Name: notebooks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.notebooks_id_seq OWNED BY public.notebooks.id;


--
-- Name: planes_de_financiacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.planes_de_financiacion (
    id integer NOT NULL,
    nombre character varying NOT NULL,
    cuotas integer NOT NULL,
    intereses character varying NOT NULL
);


ALTER TABLE public.planes_de_financiacion OWNER TO postgres;

--
-- Name: planes_de_financiacion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.planes_de_financiacion_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.planes_de_financiacion_id_seq OWNER TO postgres;

--
-- Name: planes_de_financiacion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.planes_de_financiacion_id_seq OWNED BY public.planes_de_financiacion.id;


--
-- Name: tablets; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tablets (
    id integer NOT NULL,
    marca character varying NOT NULL,
    modelo character varying NOT NULL,
    descripcion character varying NOT NULL,
    procesador character varying NOT NULL,
    memoria character varying NOT NULL,
    camara_delantera character varying NOT NULL,
    camara_trasera character varying NOT NULL,
    pantalla character varying NOT NULL,
    bateria character varying NOT NULL,
    precio integer NOT NULL,
    financiacion integer,
    imagen_url character varying NOT NULL
);


ALTER TABLE public.tablets OWNER TO postgres;

--
-- Name: tablets_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tablets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tablets_id_seq OWNER TO postgres;

--
-- Name: tablets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tablets_id_seq OWNED BY public.tablets.id;


--
-- Name: celulares id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.celulares ALTER COLUMN id SET DEFAULT nextval('public.celulares_id_seq'::regclass);


--
-- Name: notebooks id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notebooks ALTER COLUMN id SET DEFAULT nextval('public.notebooks_id_seq'::regclass);


--
-- Name: planes_de_financiacion id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.planes_de_financiacion ALTER COLUMN id SET DEFAULT nextval('public.planes_de_financiacion_id_seq'::regclass);


--
-- Name: tablets id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tablets ALTER COLUMN id SET DEFAULT nextval('public.tablets_id_seq'::regclass);


--
-- Data for Name: celulares; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.celulares (id, marca, modelo, descripcion, procesador, memoria, camara_delantera, camara_trasera, pantalla, bateria, precio, financiacion, imagen_url) FROM stdin;
1	Apple	iPhone 13	 El sistema de dos cámaras más avanzado en un iPhone. El superrápido chip A15 Bionic. Un gran salto en duración de bateria,. Un diseño resistente. Y una pantalla Super Retina XDR más brillante.	Apple A15 Bionic	Almacenamiento: 128GB, RAM: 4GB	12 Mpx	12 Mpx/12 Mpx/12 Mpx	6.1 "	3240mAh	1100000	4	https://http2.mlstatic.com/D_NQ_NP_973345-MLA47781591382_102021-O.webp
2	Samsung	Galaxy A54	Smartphone de gama media que ofrece conectividad 5G, una pantalla Super AMOLED de alta definición, un sistema de cámaras versátil y un diseño moderno y delgado. Rendimiento sólido y buena relación calidad-precio dentro de su categoría.	Exynos 1380	Almacenamiento: 256GB, RAM: 8GB	32 Mpx	50 Mpx/12 Mpx/5 Mpx	6.4 "	5000mAh	790000	3	https://http2.mlstatic.com/D_NQ_NP_732057-MLA70868353813_082023-O.webp
3	Xiaomi	Redmi Note 13 Pro+ 5G	Capacidad y eficiencia. Con su potente procesador y memoria RAM de 8GB tu equipo alcanzará un alto rendimiento con gran velocidad de transmisión de contenidos y ejecutará múltiples aplicaciones a la vez sin demoras.	MediaTek Dimensión 7200-Ultra	Almacenamiento: 256GB, RAM: 8GB	16 Mpx	200 Mpx/8 Mpx/2 Mpx	6.67 "	5020mAh	714999	3	https://http2.mlstatic.com/D_NQ_NP_748621-MLA76569863127_052024-O.webp
4	Samsung	Galaxy A14	Smartphone de gama de entrada con una pantalla grande y fluida, bateria, de larga duración, cámara triple decente y precio accesible. Ideal para usuarios que buscan un teléfono confiable para tareas básicas como navegar por internet, redes sociales y mensajería instantánea.	MediaTek MT6572M	Almacenamiento: 128GB, RAM: 4GB	13 Mpx	50 Mpx/5 Mpx/2 Mpx	6.6 "	5000mAh	339999	1	https://http2.mlstatic.com/D_NQ_NP_870142-MLA54920742936_042023-O.webp
5	Apple	iPhone 11	Graba videos 4K y captura retratos espectaculares y paisajes increíbles con el sistema de dos cámaras. Toma grandes fotos con poca luz gracias al modo Noche. Disfruta colores reales en las fotos, videos y juegos con la pantalla Liquid Retina de 6.1 pulgadas. Aprovecha un rendimiento sin precedentes en los juegos, la realidad aumentada y la fotografía con el chip A13 Bionic. Haz mucho más sin necesidad de volver a cargar el teléfono gracias a su bateria, de larga duración. Y no te preocupes si se moja, el iPhone 11 tiene una resistencia al agua de hasta 30 minutos a una profundidad máxima de 2 metros. 	Apple A13 Bionic	Almacenamiento: 64GB, RAM: 4GB	12 Mpx	12 Mpx/12 Mpx	6.1 "	3046mAh	749999	2	https://http2.mlstatic.com/D_NQ_NP_656548-MLA46114829749_052021-O.webp
6	Xiaomi	Redmi 9A	Smartphone de gama baja que ofrece una pantalla grande de 6.53 pulgadas, bateria, de 5000 mAh, procesador MediaTek Helio G25, cámara trasera de 13 MP y cámara delantera de 5 MP. Es una opción económica para usuarios que buscan un teléfono básico para tareas cotidianas como llamadas, mensajes de texto y navegación web.	MediaTek MT6762G Helio G25	Almacenamiento: 32GB, RAM: 2GB	5 Mpx	5 Mpx/13 Mpx	6.53 "	5000mAh	169000	1	https://http2.mlstatic.com/D_NQ_NP_739762-MLA43167718857_082020-O.webp
7	Apple	iPhone 15 Pro	Smartphone excelente con un diseño premium, un procesador potente, un sistema de cámara versátil y una bateria, de larga duración. Es una buena opción para los usuarios que buscan lo mejor que Apple tiene para ofrecer.	Apple A17 Pro	Almacenamiento: 128GB, RAM: 8GB	12 Mpx	48 Mpx/12 Mpx/12 Mpx	6.1 "	3274mAh	1849999	4	https://http2.mlstatic.com/D_NQ_NP_891263-MLA71783089058_092023-O.webp
8	Samsung	Galaxy A34 5G	Smartphone de gama media-alta que se destaca por su pantalla Super AMOLED de 6.6 pulgadas con tasa de refresco de 120Hz, procesador Dimensity 1080, cámara principal de 48MP, bateria, de 5000mAh y conectividad 5G.	Mediatek MT6877V Dimensity 1080	Almacenamiento: 128GB, RAM: 6GB	13 Mpx	48 Mpx/8 Mpx/5 Mpx	6.6 "	5000mAh	559999	2	https://http2.mlstatic.com/D_NQ_NP_651776-MLA54688514315_032023-O.webp
9	Samsung	Galaxy A04	Smartphone de gama baja que se destaca por su pantalla grande de 6.5 pulgadas con resolución HD+, procesador octa-core para un rendimiento fluido, cámara trasera doble de 50MP para capturar fotos nítidas y detalladas, y bateria, de 5000mAh de larga duración.	Unisoc T616	Almacenamiento: 64GB, RAM: 4GB	5 Mpx	50 Mpx/2 Mpx	6.5 "	5000mAh	249999	1	https://http2.mlstatic.com/D_NQ_NP_648782-MLA52416267113_112022-O.webp
10	Apple	iPhone 8 Plus	Se destaca por su pantalla Retina HD de 5.5 pulgadas con True Tone y 3D Touch, ofreciendo una experiencia visual vívida y sensible. Su potente procesador A11 Bionic garantiza un rendimiento fluido en todas las tareas, desde juegos hasta edición de video. El sistema de cámara dual de 12MP en la parte posterior captura fotos y videos con gran detalle, incluso en condiciones de poca luz. Además, la bateria, de larga duración te permite disfrutar de tu teléfono todo el día sin necesidad de recargarlo.	Apple A11 Bionic	Almacenamiento: 64GB, RAM: 3GB	7 Mpx	12 Mpx/12 Mpx	5.5 "	2691mAh	524999	2	https://http2.mlstatic.com/D_NQ_NP_712176-MLA49534079470_032022-O.webp
11	Xiaomi	Redmi 10C	Smartphone de gama de entrada que destaca por su bateria, de 5000mAh, que te ofrece hasta dos días de uso con una sola carga. Cuenta con una pantalla grande de 6.71 pulgadas para una experiencia visual inmersiva, y una cámara principal de 50MP para capturar fotos nítidas. El procesador Snapdragon 680 garantiza un rendimiento fluido para las tareas diarias. Incluye una cámara selfie de 5MP, Android 11, conectividad 4G LTE y soporte para expansión de memoria microSD. Una opción ideal para quienes buscan un teléfono accesible con buena bateria,, pantalla y cámara.	Snapdragon 680	Almacenamiento: 128GB, RAM: 4GB	5Mpx	50 Mpx/2 Mpx	6.71" 	5000mAh	235000	1	https://http2.mlstatic.com/D_NQ_NP_649323-MLU70029610391_062023-O.webp
12	Xiaomi	Pocophone Poco X6 5G	Smartphone de gama media que ofrece una excelente relación calidad-precio. Destaca por su potente procesador Snapdragon Serie 7 de 8 núcleos, su bateria, de 5100mAh con carga rápida de 67W, y su pantalla AMOLED de 6.67 pulgadas con tasa de refresco de 120Hz.	Snapdragon 7S Gen 2	Almacenamiento: 256GB, RAM: 8GB	16Mpx	64 Mpx/8 Mpx/2 Mpx	6.67" 	5100mAh	549999	2	https://http2.mlstatic.com/D_NQ_NP_830275-MLA73967764697_012024-O.webp
13	Apple	iPhone 14	El iPhone 14 viene con el sistema de dos cámaras más impresionante, para que tomes fotos espectaculares con mucha o poca luz. Y te da más tranquilidad gracias a una funcionalidad de seguridad que salva vidas.	Apple A15 Bionic	Almacenamiento: 128GB, RAM: 6GB	12 Mpx	12 Mpx/12 Mpx	6.1 "	3279mAh	1299999	4	https://http2.mlstatic.com/D_NQ_NP_786356-MLM51559385272_092022-O.webp
14	Samsung	Galaxy S24 5G	Smartphone de gama alta; su pantalla AMOLED de 6.2 pulgadas y 120Hz ofrece una experiencia visual fluida, mientras que el procesador Exynos 2400 garantiza un rendimiento sólido para las tareas del día a día. El sistema de cámara trasera triple, con un sensor principal de 50 megapíxeles, captura imágenes de alta calidad, y la bateria, de 3880 mAh con carga rápida de 45W asegura una buena autonomía. Su diseño elegante y compacto lo hace cómodo de usar	Exynos 2400	Almacenamiento: 256GB, RAM: 12GB	12 Mpx	50 Mpx/12 Mpx/10 Mpx	6.2 "	3880mAh	1499999	4	https://http2.mlstatic.com/D_NQ_NP_649997-MLU76728912841_052024-O.webp
15	Xiaomi	Redmi Note 11	Smartphone con pantalla AMOLED de 6.4 pulgadas a 90Hz, el procesador Snapdragon 680 que solventa tareas básicas, un sistema de cámara cuádruple con sensor principal de 50 megapíxeles y una bateria, de 5000mAh con carga rápida, que garantiza una larga duración. Su diseño elegante y precio accesible lo convierten en una excelente opción para usuarios que buscan un buen smartphone sin gastar demasiado.	Snapdragon 680	Almacenamiento: 64GB, RAM: 4GB	13Mpx	50 Mpx/8 Mpx/2 Mpx/2 Mpx	6.43 "	5000mAh	299999	1	https://http2.mlstatic.com/D_NQ_NP_951771-MLA52132712156_102022-O.webp
\.


--
-- Data for Name: notebooks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notebooks (id, marca, modelo, descripcion, procesador, memoria, almacenamiento, sistema_operativo, camara_delantera, pantalla, bateria, precio, financiacion, imagen_url) FROM stdin;
1	Apple	Macbook Air	La notebook más delgada y ligera de Apple viene con los superpoderes del chip M1. Termina todos tus proyectos mucho más rápido con el CPU de 8 núcleos y disfruta como nunca antes de apps y juegos con gráficos avanzados gracias al GPU de hasta 8 núcleos. Además, el Neural Engine de 16 núcleos se encarga de acelerar todos los procesos de aprendizaje automático. Todo en un diseño silencioso sin ventilador que te ofrece la mayor duración de batería en una MacBook Air: hasta 18 horas.  Portátil como siempre, más poderosa que nunca.	Apple M1	8GB	256GB SSD	macOS	720p	2560 px x 1600 px LED	50.9 Wh	1299999	4	https://http2.mlstatic.com/D_NQ_NP_801112-MLA46516512347_062021-O.webp
2	Apple	Macbook Pro	Equipada con un chip M1 que ofrece un rendimiento y gráficos excepcionales, una pantalla Liquid Retina XDR de impresionante belleza, una batería de larga duración que te acompaña todo el día y un diseño elegante y liviano, la MacBook Pro es la herramienta perfecta para profesionales que exigen lo mejor. Su intuitivo sistema operativo macOS te permite trabajar con fluidez y seguridad, mientras que su amplia gama de aplicaciones te brinda las herramientas que necesitas para llevar a cabo tus tareas de manera eficiente. No importa si eres editor de video, desarrollador de software, diseñador gráfico, científico de datos, profesional de negocios o estudiante, la MacBook Pro es la computadora ideal para ti. ¡No te pierdas la oportunidad de tener lo mejor en tecnología!	Apple M1	8GB	256GB SSD, 256GB Disco Rígido	macOS	720p	3456 px x 2234 px	100 Wh	2699999	4	https://http2.mlstatic.com/D_NQ_NP_970913-MLA51804671567_102022-O.webp
\.


--
-- Data for Name: planes_de_financiacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.planes_de_financiacion (id, nombre, cuotas, intereses) FROM stdin;
1	Standard	0	0%
2	Basic	6	15,3%
3	Premium	9	22,5%
4	Elite	12	30,8%
\.


--
-- Data for Name: tablets; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tablets (id, marca, modelo, descripcion, procesador, memoria, camara_delantera, camara_trasera, pantalla, bateria, precio, financiacion, imagen_url) FROM stdin;
1	Samsung	Galaxy Tab A7 Lite	Disfruta de películas y juegos en una amplia pantalla de 8.7 pulgadas. Los biseles reducidos ofrecen una mayor relación pantalla-cuerpo sin aumentar el tamaño de la tableta. Además, el factor de forma cómodamente compacto ayuda a que no se te cansen las manos, incluso cuando llevas horas jugando.\nLa Galaxy Tab A7 Lite combina estilo y comodidad en un formato delgado. Esta tableta superportátil, que mide 8.0 mm y pesa 366 g, cabe fácilmente en tu bolso y es cómoda de llevar.	Octa-core Cortex-A53	Almacenamiento: 32GB, RAM: 3GB	2 Mpx	8 Mpx	8.7 "	5100mAh	349999	2	https://http2.mlstatic.com/D_NQ_NP_643152-MLU72561065958_112023-O.webp
2	Apple	iPad 9th generation	Lleno de potencia, muy fácil de usar y versátil. El nuevo iPad viene con una espectacular pantalla Retina de 10.2 pulgadas, el potente chip A13 Bionic y una cámara frontal ultra gran angular con Encuadre Centrado. Además, es compatible con el Apple Pencil y el Smart Keyboard.\nCon el iPad, harás de todo como si nada. Y por menos de lo que imaginas.	Apple a13 Bionic	Almacenamiento: 64GB, RAM: 3GB	12 Mpx	8 Mpx	10.2 "	8557mAh	629999	3	https://http2.mlstatic.com/D_NQ_NP_991281-MLA47871333051_102021-O.webp
3	Xiaomi	Redmi Pad 11	Esta tablet es la combinación perfecta de rendimiento y versatilidad, ideal para acompañar cada una de tus actividades.\nTransferir, sincronizar y acceder a tus dispositivos las veces que quieras ahora es posible. Sus conexiones bluetooth,usb-c,wi-fi te permiten potenciar sus funciones al máximo. Gracias a sus cámaras, con resoluciones de 8 Mpx y 8 Mpx, podrás hacer videollamadas o sacarte fotos en cualquier momento y lugar, con una excelente calidad de imagen. Nitidez, brillo y colores vibrantes harán que tus experiencias se reflejen de manera óptima.	Snapdragon 680	Almacenamiento: 128GB, RAM: 6GB	8 Mpx	8 Mpx	11 "	8000mAh	599999	3	https://http2.mlstatic.com/D_NQ_NP_898746-MLU71748789909_092023-O.webp
4	Apple	iPad 10th generation	Este producto combina la potencia y la capacidad de una computadora con la versatilidad y facilidad de uso que solo un iPad puede brindar. Realizar varias tareas a la vez, como editar documentos mientras buscás información en internet o sacarte una selfie, es sumamente sencillo. Como si esto fuera poco, también ofrece la posibilidad de descargar desde la App Store cientos de aplicaciones creadas para pintar, dibujar, escuchar música y ¡mucho más!	Apple A14 Bionic	Almacenamiento: 256GB, RAM: 4GB	12 Mpx	12 Mpx	10.9 "	7606mAh	1199999	4	https://http2.mlstatic.com/D_NQ_NP_803992-MLA52988770428_122022-O.webp
5	Samsung	Galaxy Tab S6 Lite	Esta tablet Samsung es la compañera ideal, con capacidad de sobra para cada una de tus actividades. El diseño delgado, compacto y portátil, con facilidad para sostener en una mano, lo convierte en una combinación perfecta de rendimiento y versatilidad.	Snapdragon 720G	Almacenamiento: 64GB, RAM: 4GB	5 Mpx	8 Mpx	10.4 "	7040mAh	679999	3	https://http2.mlstatic.com/D_NQ_NP_777339-MLU51046177368_082022-O.webp
6	Xiaomi	Redmi Pad SE	La Tablet Redmi Pad SE es la elección perfecta para aquellos que buscan un dispositivo potente y versátil. Con una capacidad de batería de 8000 mAh, podrás disfrutar de largas horas de uso sin preocuparte por quedarte sin energía. Su procesador Mediatek Helio G99 de 8 núcleos y su procesador gráfico Mali-G57 MC2 garantizan un rendimiento excepcional, permitiéndote realizar múltiples tareas sin problemas. Además, su pantalla de máxima resolución de 1200 px x 2000 px te brindará una experiencia visual inmersiva y de alta calidad. Con su sistema operativo Android y la capa de personalización MIUI 13, tendrás acceso a una amplia variedad de aplicaciones y funciones personalizadas. Su cámara frontal de 8 Mpx te permitirá capturar selfies y realizar videollamadas con una excelente calidad de imagen. Y gracias a su lector de tarjetas de memoria Micro-SDXC, podrás expandir fácilmente el almacenamiento de tu tablet. La Tablet Redmi Pad SE es el compañero perfecto para el entretenimiento, el trabajo y mucho más.	Snapdragon 680	Almacenamiento: 256GB, RAM: 8GB	8 Mpx	8 Mpx	11 "	8000mAh	679999	3	https://http2.mlstatic.com/D_NQ_NP_795195-MLA74337075970_022024-O.webp
\.


--
-- Name: celulares_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.celulares_id_seq', 1, false);


--
-- Name: notebooks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.notebooks_id_seq', 1, false);


--
-- Name: planes_de_financiacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.planes_de_financiacion_id_seq', 1, false);


--
-- Name: tablets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tablets_id_seq', 1, false);


--
-- Name: celulares celulares_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.celulares
    ADD CONSTRAINT celulares_pkey PRIMARY KEY (id);


--
-- Name: notebooks notebooks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notebooks
    ADD CONSTRAINT notebooks_pkey PRIMARY KEY (id);


--
-- Name: planes_de_financiacion planes_de_financiacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.planes_de_financiacion
    ADD CONSTRAINT planes_de_financiacion_pkey PRIMARY KEY (id);


--
-- Name: tablets tablets_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tablets
    ADD CONSTRAINT tablets_pkey PRIMARY KEY (id);


--
-- Name: celulares celulares_financiacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.celulares
    ADD CONSTRAINT celulares_financiacion_fkey FOREIGN KEY (financiacion) REFERENCES public.planes_de_financiacion(id);


--
-- Name: notebooks notebooks_financiacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notebooks
    ADD CONSTRAINT notebooks_financiacion_fkey FOREIGN KEY (financiacion) REFERENCES public.planes_de_financiacion(id);


--
-- Name: tablets tablets_financiacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tablets
    ADD CONSTRAINT tablets_financiacion_fkey FOREIGN KEY (financiacion) REFERENCES public.planes_de_financiacion(id);


--
-- PostgreSQL database dump complete
--

