import aiohttp

from io import BytesIO
from datetime import datetime

from aiohttp import FormData

from vkbottle.user import Message
from PIL import Image, ImageDraw, ImageFont


class CoverImage:
    def __init__(self):
        self.fill = "#ffffff"

        self.img = Image.open('assets/images/cover_bg.jpg')
        self.x, self.y = self.img.size

        self.draw = ImageDraw.Draw(self.img)
        self.font = ImageFont.truetype('assets/fonts/cover.ttf', 100)

    def draw_text(self):
        self.draw.text((self.x / 2, self.y / 2), datetime.now().strftime("%H:%M"),
                       font=self.font, anchor="ms", fill=self.fill)

        weekdays = {
            1: "Понедельник", 2: "Вторник", 3: "Среда",
            4: "Четверг", 5: "Пятница", 6: "Суббота",
            7: "Воскресенье"
        }

        months = {
            1: "января", 2: "февраля", 3: "марта",
            4: "апреля", 5: "мая", 6: "июнья",
            7: "июля", 8: "августа", 9: "сентября",
            10: "октября", 11: "ноября", 12: "декабря"
        }

        date = f"{datetime.now().day} {months[datetime.now().month]}, {weekdays[datetime.now().weekday()]}"
        self.font = ImageFont.truetype('assets/fonts/cover.ttf', 60)
        self.draw.text((self.x / 2, self.y / 2 + 100), date,
                       font=self.font, anchor="ms", fill=self.fill)

    def save_cover_image(self, user_id: int):
        self.img.save(f'assets/images/cover_{user_id}_bg.jpg', format="JPEG")

    @staticmethod
    async def get_upload_server(_api: Message.ctx_api, user_id: int):
        upload = await _api.request(
            'photos.getOwnerCoverPhotoUploadServer',
            dict(user_id=user_id, crop_width=1920, crop_height=768)
        )
        return upload["response"]["upload_url"]

    async def upload_image(self, _api: Message.ctx_api, user_id: int):
        form_data = FormData()
        form_data.add_field('photo', open(f'assets/images/cover_{user_id}_bg.jpg', 'rb'))
        upload_server = await self.get_upload_server(_api, user_id)

        async with aiohttp.ClientSession() as session:
            async with session.post(upload_server, data=form_data) as response:
                upload_url = await response.json()
                data = dict(photo=upload_url["photo"], hash=upload_url["hash"])

                await _api.request('photos.saveOwnerCoverPhoto', data)
