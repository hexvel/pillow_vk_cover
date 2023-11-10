from test import CoverImage
from vkbottle.api import API


async def main():
    api = API(token="token")
    cover = CoverImage() # Создание экземпляра класса
  
    cover.draw_text() # Создание всего шаблона обложки
  
    cover.save_cover_image(123456789) # Сохранение обложки
    await cover.upload_image(api, 123456789) # Обновление вашей обложки на странице
