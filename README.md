
# Документация API

## 1. Работа с пользователями

### 1.1 Регистрация пользователя

**Endpoint:**
`POST http://localhost/register/`

**Запрос:**
`{   "username": "new_user",   "email": "new_user@example.com",   "password": "secure_password" }`

**Ответ (успех):**
`{   "message": "User registered successfully",   "user": {     "id": 1,     "username": "new_user",     "email": "new_user@example.com"   } }`

**Ответ (ошибка):**
`{   "error": "Invalid registration data. Please check your input." }`

### 1.2 Вход после регистрации

**Endpoint:**
`POST http://localhost/login/`

**Запрос:**
`{   "username": "new_user",   "password": "secure_password" }`

**Ответ (успех):**
`{   "access": "access_token",   "refresh": "refresh_token" }`

**Ответ (ошибка):**
`{   "error": "Invalid login credentials. Please try again." }`

### 2.1 Запрос с токеном

**Endpoint:**
`GET http://localhost/user-data/`

**Запрос (с токеном):**
`// Заголовок Authorization: Bearer some_long_access_token`

**Ответ (успех):**
`{   "id": 1,   "username": "new_user",   "email": "new_user@example.com" }`

**Ответ (ошибка):**
`{   "error": "Unauthorized. Please log in to access this resource." }`

### 3.1 Выход пользователя

**Endpoint:**
`POST http://localhost/logout/`

**Запрос (с токеном):**
`{   "refresh": "refresh_token" }`

**Ответ (успех):**
`{   "message": "User logged out successfully" }`

**Ответ (ошибка):**
`{   "error": "Invalid refresh token. Please log in again." }`

### 4.1 Проверка срока действия токена

**Endpoint:**
`GET http://localhost/check-token/`

**Запрос (с токеном):**
`// Header
`authorization: Bearer access_token`

**Ответ (успех):**
`{   "message": "Token is valid" }`

**Ответ (ошибка):**
`{   "error": "Token expired or invalid. Please log in again." }`

## 2. Работа с объявлениями

### 2.1 Общая информация о объявлении

#### 2.1.1 AdBaseModel 

**Описание:** модель от которой наследуются все объявления

**Модель:**

- `id`: Идентификатор объявления
- `author`: Автор объявления (ID пользователя)
- `city`: Город, в котором размещено объявление
- `publication_date`: Дата публикации объявления
- `price`: Цена объявления

#### 2.1.2 AdImageModel

**Описание:** тк у объявления может быть разное кол-во фото, создана отдельная модель для фото со связью ManyToOne

**Модель:**

- `id`: Идентификатор изображения
- `ad`: Связанное объявление (ID объявления)
- `image`: Изображение объявления

### 2.2 Объявление о продаже автомобиля

**Описание:** модель легковых машин, которая наследуется от AdBaseModel
#### 2.2.1 CarModel

**Модель:**

- `id`: Идентификатор объявления
- `author`: Автор объявления (ID пользователя)
- `city`: Город, в котором размещено объявление
- `publication_date`: Дата публикации объявления
- `price`: Цена объявления
- `brand`: Марка автомобиля
- `model`: Модель автомобиля
- `year`: Год выпуска
- `body`: Тип кузова
- `mileage`: Пробег
- `condition`: Состояние автомобиля
- `color`: Цвет автомобиля
- `engine`: Тип двигателя
- `wheel`: Руль (левый/правый)
- `box`: Тип коробки передач
- `cleared`: Очищен от залогов и арестов (True/False)
- `additionally`: Дополнительные характеристики
- `description`: Описание автомобиля
- `images`: Изображения автомобиля (связанные изображения)

### 2.3 Объявление о продаже грузовика

**Описание:** модель грузовых машин, наследуется от модели легковых машин с добавленными полями: `weight`: Грузоподъемность, `body_volume`: Объем кузова

#### 2.3.1 TruckModel

**Модель:**

- `id`: Идентификатор объявления
- `author`: Автор объявления (ID пользователя)
- `city`: Город, в котором размещено объявление
- `publication_date`: Дата публикации объявления
- `price`: Цена объявления
- `brand`: Марка грузовика
- `model`: Модель грузовика
- `year`: Год выпуска
- `body`: Тип кузова
- `mileage`: Пробег
- `condition`: Состояние грузовика
- `color`: Цвет грузовика
- `engine`: Тип двигателя
- `wheel`: Руль (левый/правый)
- `box`: Тип коробки передач
- `cleared`: Очищен от залогов и арестов (True/False)
- `additionally`: Дополнительные характеристики
- `description`: Описание грузовика
- `weight`: Грузоподъемность
- `body_volume`: Объем кузова
- `images`: Изображения грузовика (связанные изображения)

### 2.4 Объявление о продаже лодки

**Описание:** модель водного транспорта, наследуется от basemodel
#### 2.4.1 BoatModel

**Модель:**

- `id`: Идентификатор объявления
- `author`: Автор объявления (ID пользователя)
- `city`: Город, в котором размещено объявление
- `publication_date`: Дата публикации объявления
- `price`: Цена объявления
- `type`: Тип лодки
- `brand`: Марка лодки
- `model`: Модель лодки
- `year`: Год выпуска
- `mileage`: Пробег (по воде)
- `condition`: Состояние лодки
- `color`: Цвет лодки
- `engine`: Тип двигателя
- `cleared`: Очищен от залогов и арестов (True/False)
- `additionally`: Дополнительные характеристики
- `description`: Описание лодки
- `images`: Изображения лодки (связанные изображения)

### 2.5 Объявление об аренде оборудования

**Описание:** модель инструментов, наследуется от basemodel

#### 2.5.1 EquipmentModel

**Модель:**

- `id`: Идентификатор объявления
- `author`: Автор объявления (ID пользователя)
- `city`: Город, в котором размещено объявление
- `publication_date`: Дата публикации объявления
- `price`: Цена объявления за аренду
- `type`: Тип оборудования
- `name`: Название оборудования
- `additionally`: Дополнительные характеристики
- `description`: Описание оборудования
- `images`: Изображения оборудования (связанные изображения)

### 2.6 Объявление об услуге

**Описание:** модель инструментов, наследуется от basemodel

#### 2.6.1 ServiceModel

**Модель:**

- `id`: Идентификатор объявления
- `author`: Автор объявления (ID пользователя)
- `city`: Город, в котором размещено объявление
- `publication_date`: Дата публикации объявления
- `price`: Цена объявления за услугу
- `type`: Тип услуги
- `name`: Название услуги
- `additionally`: Дополнительные характеристики
- `description`: Описание услуги
- `images`: Изображения услуги (связанные изображения)
### 2.2 работа с api объявлений

#### 2.2.1 Получение списка всех объявлений о продаже автомобилей

**Тип запроса:**
`GET http://localhost/api/cars/`

**Ответ (успех):**
`[   {     "id": 1,     "author": 1,     "city": "City1",     "publication_date": "2024-02-08T12:00:00Z",     "price": 15000,     "brand": "Brand1",     "model": "Model1",     // ...   },   {     "id": 2,     "author": 2,     "city": "City2",     "publication_date": "2024-02-08T13:00:00Z",     "price": 20000,     "brand": "Brand2",     "model": "Model2",     // ...   },   // ... ]`

**Ответ (ошибка):**
`{   "detail": "Authentication credentials were not provided." }`

#### 2.2.2 Создание нового объявления о продаже автомобиля

**Тип запроса:**
`POST http://localhost/api/cars/`

**Запрос:**
`{   "author": 1,   "city": "City3",   "price": 18000,   "brand": "Brand3",   "model": "Model3",   // ... }`

**Ответ (успех):**
`{   "id": 3,   "author": 1,   "city": "City3",   "publication_date": "2024-02-08T14:00:00Z",   "price": 18000,   "brand": "Brand3",   "model": "Model3",   // ... }`

**Ответ (ошибка):**
`{   "error": "Invalid data. Please check your input." }`

#### 2.2.3 Получение деталей конкретного объявления о продаже автомобиля

**Тип запроса:**
`GET http://localhost/api/cars/1/`

**Ответ (успех):**
`{   "id": 1,   "author": 1,   "city": "City1",   "publication_date": "2024-02-08T12:00:00Z",   "price": 15000,   "brand": "Brand1",   "model": "Model1",   // ... }`

**Ответ (ошибка):**
`{   "detail": "Not found." }`

#### 2.2.4 Обновление данных объявления о продаже автомобиля

**Тип запроса:**
`PUT http://localhost/api/cars/1/`

**Запрос:**
`{   "price": 16000,   // ... }`

**Ответ (успех):**
`{   "id": 1,   "author": 1,   "city": "City1",   "publication_date": "2024-02-08T12:00:00Z",   "price": 16000,   "brand": "Brand1",   "model": "Model1",   // ... }`

**Ответ (ошибка):**
`{   "error": "Invalid data. Please check your input." }`

#### 2.2.5 Удаление объявления о продаже автомобиля

**Тип запроса:**
`DELETE http://localhost/api/cars/1/`

**Ответ (успех):**
`{   "detail": "Successfully deleted." }`

**Ответ (ошибка):**
`{   "detail": "Not found." }`

## 3. Работа с чатами и сообщениями

### 3.1 Получение списка пользователей

**Endpoint:**
`GET http://localhost/api/users/`

**Ответ (успех):**
`[   {     "id": 1,     "username": "user1"   },   {     "id": 2,     "username": "user2"   },   // ... ]`

**Ответ (ошибка):**
`{   "detail": "Authentication credentials were not provided." }`

### 3.2 Создание нового чата

**Endpoint:**
`POST http://localhost/api/rooms/`

**Запрос:**
`{   "name": "Room 1",   "users": [1, 2] }`

**Ответ (успех):**
`{   "id": 1,   "name": "Room 1",   "users": [1, 2],   "messages": [] }`

**Ответ (ошибка):**
`{   "name": ["This field is required."] }`

### 3.3 Получение списка чатов

**Endpoint:**
`GET http://localhost/api/rooms/`

**Ответ (успех):**
`[   {     "id": 1,     "name": "Room 1",     "users": [1, 2],     "messages": []   },   {     "id": 2,     "name": "Room 2",     "users": [1, 3],     "messages": []   },   // ... ]`

**Ответ (ошибка):**
`{   "detail": "Authentication credentials were not provided." }`

### 3.4 Получение списка сообщений в чате

**Endpoint:**
`GET http://lcalhost/api/rooms/{room_id}/messages/`

**Ответ (успех):**
`[   {     "id": 1,     "text": "Hello!",     "user": 1,     "room": 1   },   {     "id": 2,     "text": "Hi there!",     "user": 2,     "room": 1   },   // ... ]`

**Ответ (ошибка):**
`{   "detail": "Authentication credentials were not provided." }`

### 3.5 Отправка сообщения в чат

**Endpoint:**
`POST http://localhost/api/rooms/{room_id}/messages/`

**Запрос:**
`{   "text": "New message" }`

**Ответ (успех):**
`{   "id": 3,   "text": "New message",   "user": 1,   "room": 1 }`

**Ответ (ошибка):**
`{   "text": ["This field is required."] }`
