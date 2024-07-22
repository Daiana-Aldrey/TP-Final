INSERT INTO planes_de_financiacion (id, nombre, cuotas, intereses) VALUES
(1, 'Standar', 0, '0%'),
(2, 'Basic', 6, '15.3%'),
(3, 'Premium', 9, '22.5%'),
(4, 'Elite', 12, '30.8%'),



INSERT INTO Celulares (id, marca, modelo, descripcion, procesador, memoria, camara_delantera, camara_trasera, pantalla, bateria, precio, financiacion, imagen_url) VALUES
(1, 'Samsung', 'Galaxy S21', 'Smartphone con pantalla AMOLED y triple cámara', 'Exynos 2100', '8GB', '10MP', '64MP', '6.2 pulgadas', '4000mAh', 799, 1, 'url_imagen_galaxy_s21.jpg'),
(2, 'Samsung', 'Galaxy Note 20', 'Smartphone con pantalla grande y S-Pen', 'Snapdragon 865+', '8GB', '10MP', '64MP', '6.7 pulgadas', '4300mAh', 950, 2, 'url_imagen_galaxy_note_20.jpg'),
(3, 'Apple', 'iPhone 13', 'Smartphone de última generación', 'A15 Bionic', '6GB', '12MP', '12MP', '6.1 pulgadas', '3095mAh', 999, 3, 'url_imagen_iphone_13.jpg'),
(4, 'Apple', 'iPhone 12', 'Smartphone con diseño renovado y 5G', 'A14 Bionic', '6GB', '12MP', '12MP', '6.1 pulgadas', '2815mAh', 799, 1, 'url_imagen_iphone_12.jpg'),
(5, 'Xiaomi', 'Mi 11', 'Smartphone con pantalla AMOLED y cámara de 108MP', 'Snapdragon 888', '8GB', '20MP', '108MP', '6.81 pulgadas', '4600mAh', 749, 2, 'url_imagen_mi_11.jpg'),
(6, 'Xiaomi', 'Redmi Note 10', 'Smartphone con pantalla AMOLED y batería duradera', 'Snapdragon 678', '4GB', '13MP', '48MP', '6.43 pulgadas', '5000mAh', 299, 3, 'url_imagen_redmi_note_10.jpg');

INSERT INTO tablets (id, marca, modelo, descripcion, procesador, memoria, camara_delantera, camara_trasera, pantalla, bateria, precio, financiacion, imagen_url) VALUES
(1, 'Samsung', 'Galaxy Tab S7', 'Tablet con pantalla AMOLED y S-Pen incluido', 'Snapdragon 865+', '8GB', '8MP', '13MP', '11 pulgadas', '8000mAh', 649, 1, 'url_imagen_galaxy_tab_s7.jpg'),
(2, 'Samsung', 'Galaxy Tab A7', 'Tablet económica con pantalla de 10.4 pulgadas', 'Snapdragon 662', '3GB', '5MP', '8MP', '10.4 pulgadas', '7040mAh', 229, 2, 'url_imagen_galaxy_tab_a7.jpg'),
(3, 'Apple', 'iPad Pro 11', 'Tablet con chip M1 y pantalla Liquid Retina', 'Apple M1', '8GB', '12MP', '12MP', '11 pulgadas', '7538mAh', 799, 3, 'url_imagen_ipad_pro_11.jpg'),
(4, 'Apple', 'iPad Air 4', 'Tablet con chip A14 y diseño delgado', 'A14 Bionic', '4GB', '12MP', '7MP', '10.9 pulgadas', '7606mAh', 599, 1, 'url_imagen_ipad_air_4.jpg'),
(5, 'Xiaomi', 'Mi Pad 5', 'Tablet con pantalla de 120Hz y procesador Snapdragon 860', 'Snapdragon 860', '6GB', '8MP', '13MP', '11 pulgadas', '8720mAh', 399, 2, 'url_imagen_mi_pad_5.jpg'),
(6, 'Xiaomi', 'Redmi Pad', 'Tablet con pantalla de 10.6 pulgadas y buena relación calidad-precio', 'Helio G80', '4GB', '8MP', '8MP', '10.6 pulgadas', '8000mAh', 249, 3, 'url_imagen_redmi_pad.jpg');

-- Insertar datos en la tabla de notebooks
INSERT INTO notebooks (id, marca, modelo, descripcion, procesador, memoria, almacenamiento, sistema_operativo, camara_delantera, pantalla, bateria, precio, financiacion, imagen_url) VALUES
(1, 'Samsung', 'Galaxy Book Pro 360', 'Laptop convertible con pantalla AMOLED', 'Intel Core i7', '16GB', '512GB SSD', 'Windows 10', '720p HD', '13.3 pulgadas', '6000mAh', 1399, 1, 'url_imagen_galaxy_book_pro_360.jpg'),
(2, 'Samsung', 'Notebook 9 Pro', 'Laptop con pantalla táctil y procesador potente', 'Intel Core i5', '8GB', '256GB SSD', 'Windows 10', '720p HD', '13.3 pulgadas', '5000mAh', 999, 2, 'url_imagen_notebook_9_pro.jpg'),
(3, 'Apple', 'MacBook Air M1', 'Laptop ultradelgada con chip M1', 'Apple M1', '8GB', '256GB SSD', '720p HD', '13.3 pulgadas', '5000mAh', 999, 3, 'url_imagen_macbook_air_m1.jpg'),
(4, 'Apple', 'MacBook Pro 16', 'Laptop con pantalla de 16 pulgadas y chip M1 Pro', 'Apple M1 Pro', '16GB', '512GB SSD', '1080p HD', '16 pulgadas', '10000mAh', 2399, 1, 'url_imagen_macbook_pro_16.jpg'),
(5, 'Xiaomi', 'Mi Notebook Pro', 'Laptop con pantalla de 15.6 pulgadas y gran rendimiento', 'Intel Core i7', '16GB', '512GB SSD', 'Windows 10', '720p HD', '15.6 pulgadas', '5500mAh', 1199, 2, 'url_imagen_mi_notebook_pro.jpg'),
(6, 'Xiaomi', 'RedmiBook 15', 'Laptop económica con pantalla grande y buena batería', 'Intel Core i5', '8GB', '256GB SSD', 'Windows 10', '720p HD', '15.6 pulgadas', '5000mAh', 699, 3, 'url_imagen_redmibook_15.jpg');
