class AutoData:
    def __init__(self, auto_id, description, version, year, gear_box_name, mark_name, race):
        self.auto_id = auto_id
        self.description = description
        self.version = version,
        self.year = year
        self.gearboxName = gear_box_name
        self.markName = mark_name
        self.race = race

    @classmethod
    def parseJson(cls, json, mark_name):
        return cls(
            json["autoId"],
            json["description"],
            json["version"],
            json["year"],
            json["gearboxName"],
            mark_name,
            json["race"]
        )


class AutoUnit:
    def __init__(self, title, url, auto_data, location_city_name, price_usd, price_uah, price_eur, photo_data, add_date,
                 update_date, expire_date):
        # self.auto_data = auto_data
        self.title = title
        self.url = url
        self.photo_data = photo_data
        self.location_city_name = location_city_name

        self.price_usd = price_usd
        self.price_uah = price_uah
        self.price_eur = price_eur

        self.add_date = add_date
        self.update_date = update_date
        self.expire_date = expire_date

        self.auto_id = auto_data.auto_id
        self.year = auto_data.year
        self.race = auto_data.race

    @classmethod
    def parseJson(cls, json):
        return cls(
            json["title"],
            f'https://auto.ria.com{json["linkToView"]}',
            AutoData.parseJson(json["autoData"], json["markName"]),
            json["locationCityName"],
            json["USD"],
            json["UAH"],
            json["EUR"],
            json["photoData"]["seoLinkF"],
            json["addDate"],
            json["updateDate"],
            json["expireDate"],
        )

    def toJson(self):
        return {
            "title": self.title,
            "usd": self.price_usd,
            "year": self.year,
        }
