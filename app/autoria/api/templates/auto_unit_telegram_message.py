# chat_id	Integer or String	Yes	Unique identifier for the target chat or username of the target channel (in the format @channelusername)
# text	String	Yes	Text of the message to be sent, 1-4096 characters after entities parsing
# parse_mode	String	Optional	Mode for parsing entities in the message text. See formatting options for more details.
# disable_web_page_preview	Boolean	Optional	Disables link previews for links in this message
# disable_notification	Boolean	Optional	Sends the message silently. Users will receive a notification with no sound.
# reply_to_message_id	Integer	Optional	If the message is a reply, ID of the original message
# reply_markup	InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply	Optional	Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

class AutoUnitTelegramMessage:
    def __init__(self, auto_unit_list):
        self.auto_unit_list = auto_unit_list
        self.parse_mode = "HTML"

    def createParamsRequest(self, chat_id):
        text = ""
        for num, unit in enumerate(self.auto_unit_list, start=1):
            text += f'<a href="{unit.url}">{num}. {unit.title}</a>%0A'

        return f"chat_id={chat_id}&parse_mode={self.parse_mode}&text={text}"
