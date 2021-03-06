class RiaParamsBuilder:
    def __init__(self, price_ot=8000, price_do=12000, year_from=2017):
        self.category_id = 1
        self.currency = 1
        self.abroad = 2
        self.custom = 1
        self.with_photo = 1

        self.price_ot = price_ot
        self.price_do = price_do

        self.gearbox_1 = 2

        self.type_0 = 1
        self.type_1 = 2

        self.s_yers_1 = year_from
        # self.s_yers_2 = year_to

    def build(self, count_page: int):
        return f"category_id={self.category_id}&" \
               f"price_ot={self.price_ot}&" \
               f"price_do={self.price_do}&" \
               f"currency={self.currency}&" \
               f"countpage={count_page}&" \
               f"abroad={self.abroad}&" \
               f"custom{self.custom}&" \
               f"gearbox[1]=2&" \
               f"type[0]{self.type_0}&" \
               f"type[1]{self.type_1}&" \
               f"with_photo={self.with_photo}&" \
               f"s_yers[1]={self.s_yers_1}&" \
               f"bodystyle[0]=3&" \
               f"bodystyle[1]=5&" \
               f"bodystyle[3]=4&" \
               f"credit=0&" \
               f"confiscated=0&" \
               f"auto_repairs=2&" \
               f"engineVolumeTo=1.7&" \
               f"raceTo=75&" \
               f"damage=1"
