class AutoUnitTelegramMessage:
    def __init__(self, auto_unit_list):
        self.auto_unit_list = auto_unit_list
        self.parse_mode = "HTML"

    def createParamsRequest(self, chat_id):
        text = ""
        if len(self.auto_unit_list) == 0:
            text = 'No new items found'
        else:
            for num, unit in enumerate(self.auto_unit_list, start=1):
                text += f'<a href="{unit.url}">{num}. {unit.title}, {unit.race} | {unit.year}  | {unit.price_usd}$</a' \
                        f'>%0A '

        return f"chat_id={chat_id}&parse_mode={self.parse_mode}&disable_web_page_preview=true&text={text}"

    def createPhotoParamsRequest(self, chat_id):
        return f"chat_id={chat_id}&parse_mode={self.parse_mode}&disable_web_page_preview=true"

    def createList(self):
        text = ""
        for num, unit in enumerate(self.auto_unit_list, start=1):
            text = ''.join((text,
                            f'<a href="{unit.url}">{num}. {unit.title} | {unit.year} | ${unit.price_usd}</a>'))
        return text

    @classmethod
    def photo_params(cls, chat_id: int):
        return {
            'chat_id': chat_id,
            'parse_mode': 'HTML'
        }

    # files = {'photo': open(collage_path, 'rb')}
    # params = {
    #     'chat_id': chat_id,
    #     'parse_mode': 'HTML'
    # }
