# Создать таблицу Car: марка, год выпуска, страна выпуска, объём двигателя,
# цена, цвет.
# Добавить 10 записей одним запросом (некоторые поля должны быть NULL).
# Написать запрос для вывода списка машин в виде модели автомобиля,
# страны производителя и цвета машины для машин, у которых год выпуска
# моложе, чем 2000.
# Написать запрос, который выводит количество автомобилей определённой марки.
# Добавить там, где возможно, к каждому запросу сортировку
# относительно фирмы по убыванию.

CREATE DATABASE mycars;

USE mycars;

CREATE TABLE Car
(
id int PRIMARY KEY auto_increment,
car_brand VARCHAR(25) NOT NULL,
year_prod YEAR NOT NULL,
country_prod VARCHAR(20) NULL,
volume_engine FLOAT NULL,
price FLOAT NOT NULL,
color VARCHAR(15) NULL
);

INSERT INTO Car (car_brand, year_prod, country_prod, volume_engine, price, color)
VALUES
('AUDI', 2021, 'Germany', 2.8, 25000, 'Black'),
('BMW', 2013, 'Germany', 3.2, 30000, 'Black'),
('Mercedes', 2020, 'Germany', 3.0, 28000, NULL),
('Volvo', 2015, 'Sweden', 2.5, 31000, 'White'),
('Renault', 1999, 'France', NULL, 15000, NULL),
('Citroen', 1998, NULL, 2.0, 16000, NULL),
('Fiat', 2000, 'Italy', 1.9, 14000, 'Red'),
('Skoda', 1997, 'Czech', NULL, 17000, 'Brown'),
('KIA', 2022, NULL, 2.0, 19000, NULL),
('HYNDAI', 1999, 'Korea', NULL, 18000, NULL);

SELECT * FROM Car;


# Написать запрос для вывода списка машин в виде модели автомобиля,
# страны производителя и цвета машины для машин, у которых год выпуска
# моложе, чем 2000.

SELECT car_brand, year_prod, color
FROM Car
WHERE year_prod < 2000
ORDER BY car_brand desc;


# Написать запрос, который выводит количество автомобилей определённой марки.

SELECT count(car_brand) as quantity_auto
FROM Car
where car_brand = 'AUDI';
