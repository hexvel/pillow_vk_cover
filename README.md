# Код для создания и обновления обложки VK

Этот код позволяет создавать и обновлять обложку на странице VK. Для работы кода необходимо иметь установленные модули `cover` и `vkbottle`.

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

4. Создайте шаблон обложки с помощью метода draw_text():
```py
cover.draw()
```

5. Сохраните обложку на диск с помощью метода save_cover_image():
```py
cover.save_cover_image(123456789)  # Здесь 123456789 - идентификатор пользователя
```

6. Обновите обложку на странице VK с помощью метода upload() и объекта api с user_id:
```py
api = API(token="token")
user_info = await api.account.get_profile_info()

await cover.upload(api=api, user_id=user_info.id)
```

## Примечание
Не забудьте заменить "token" на ваш собственный токен VK API и указать правильный идентификатор пользователя в методах save_cover_image() и upload_image().
