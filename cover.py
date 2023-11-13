from datetime import datetime
from aiohttp import ClientSession, FormData
from io import BytesIO

from vkbottle import API
from PIL import Image, ImageDraw, ImageFont


class CoverImage:
    def __init__(self, api: API, user_id: int,
                 font_size_time=100, font_size_date=60,
                 font_color="white",
                 font_path="assets/fonts/cover.ttf",
                 bg_path="assets/images/cover_bg.jpg") -> None:
        self._api = api
        self.user_id =  user_id

        self.font_size_time = font_size_time
        self.font_size_date = font_size_date
        self.font_color = font_color
        self.font_path = font_path

        self.bg_path = bg_path

        self.bytes_image = None

    def draw(self):
        weekdays = {
            0: "Понедельник", 
            1: "Вторник", 
            2: "Среда",
            3: "Четверг", 
            4: "Пятница", 
            5: "Суббота",
            6: "Воскресенье"
        }

        months = {
            1: "января", 
            2: "февраля", 
            3: "марта",
            4: "апреля", 
            5: "мая", 
            6: "июнья",
            7: "июля", 
            8: "августа", 
            9: "сентября",
            10: "октября",
            11: "ноября", 
            12: "декабря"
        }

        image = Image.open(self.bg_path).resize((1920, 768))
        draw = ImageDraw.Draw(image)

        font_time = ImageFont.truetype(self.font_path, self.font_size_time)
        font_date = ImageFont.truetype(self.font_path, self.font_size_date)

        date = datetime.now()
        time = date.strftime("%H:%M")
        date = f"{date.day} {months[date.month]}, {weekdays[date.weekday()]}"

        x, y = image.size

        draw.text((x / 2, y / 2), time, self.font_color, font_time, "ms")
        draw.text((x / 2, y / 2 + 100), date, self.font_color, font_date, "ms")

        self.bytes_image = BytesIO()
        image.save(self.bytes_image, "PNG")
        self.bytes_image.seek(0)
    
    async def upload(self):
        upload = await self._api.request(
            'photos.getOwnerCoverPhotoUploadServer',
             dict(user_id=self.user_id, crop_width=1920, crop_height=768)
        )

        upload_url = upload['response']['upload_url']
        data = FormData()
        data.add_field("photo", self.bytes_image)

        async with ClientSession() as session:
            async with session.post(upload_url, data=data) as response:
                response_data = await response.json()

                await self._api.photos.save_owner_cover_photo(
                    hash=response_data['hash'],
                    photo=response_data['photo']
                )
