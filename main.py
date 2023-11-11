import asyncio

from cover import CoverImage
from vkbottle.api import API


async def main():
    api = API(token="vk1.a.8dx5gt94y4hqf2AYf5VIcnNl-avTciJeVuakRkHFcuRGYz0G-7AH-PQ1aA3rSMSjWqovw_adqc7fRfTqxz1ECI1o-xZfkkotu5Gw7IH42Xa49BcpLsbcWZBi04O9V7C0kEG5qjSOBwmg_ooTkArpUQBtP7sAuIeNZM6Ht_e9ZSTceFBdZ3L42lpH1TJXIP6Ev3LdwhH5mWuVmF8wXeJyxw")
    user_info = await api.account.get_profile_info()

    cover = CoverImage(api=api, user_id=user_info.id)
    cover.draw_text()
    await cover.upload_image()


if __name__ == '__main__':
    asyncio.run(main())
