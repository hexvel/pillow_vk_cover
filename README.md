# Код для создания и обновления обложки VK

## Установка зависимостей
Для установки необходимых зависимостей, установите и разархивируйте данный репозиторий.


## Использование
1. Импортируйте необходимые модули:
```py
from cover import CoverImage
from vkbottle.api import API
```

3. Создайте экземпляр класса CoverImage:
```py
cover = CoverImage()
```

4. Создайте шаблон обложки с помощью метода draw():
```py
cover.draw()
```

5. Обновите обложку на странице VK с помощью метода upload() и объекта api с user_id:
```py
api = API(token="token")
user_info = await api.account.get_profile_info()

await cover.upload(api=api, user_id=user_info.id)
```

## Примечание
Не забудьте заменить "token" на ваш собственный токен VK API.


## P.S
### Поставьте пожалуйста звёздочку)
