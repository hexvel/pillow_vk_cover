import asyncio

from cover import CoverImage
from vkbottle.api import API


async def main():
    api = API(token="token")
    user_info = await api.account.get_profile_info()

    cover = CoverImage(api=api, user_id=user_info.id)
    cover.draw_text()
    await cover.upload_image()


if __name__ == '__main__':
    asyncio.run(main())
