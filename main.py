import os
import requests
import textwrap
from datetime import datetime, timedelta, timezone

pre_ids = {
    "北海道": 2130037,
    "青森県": 2130658,
    "岩手県": 2112518,
    "宮城県": 2111888,
    "秋田県": 2113126,
    "山形県": 2110556,
    "福島県": 2112923,
    "茨城県": 1862033,
    "栃木県": 1850311,
    "群馬県": 1863501,
    "埼玉県": 6940394,
    "千葉県": 2113015,
    "東京都": 1850147,
    "神奈川県": 1860291,
    "新潟県": 1855431,
    "富山県": 1849876,
    "石川県": 1861393,
    "福井県": 1863983,
    "山梨県": 1848649,
    "長野県": 1856215,
    "岐阜県": 1863640,
    "静岡県": 1851717,
    "愛知県": 1865694,
    "三重県": 1857357,
    "滋賀県": 1852553,
    "京都府": 1857910,
    "大阪府": 1853908,
    "兵庫県": 1862047,
    "奈良県": 1855612,
    "和歌山県": 1926004,
    "鳥取県": 1849890,
    "島根県": 1852442,
    "岡山県": 1854383,
    "広島県": 1862415,
    "山口県": 1848689,
    "徳島県": 1850158,
    "香川県": 1860834,
    "愛媛県": 1864226,
    "高知県": 1859146,
    "福岡県": 1863967,
    "佐賀県": 1853303,
    "長崎県": 1856177,
    "熊本県": 1858421,
    "大分県": 1854487,
    "宮崎県": 1856717,
    "鹿児島県": 1860827,
    "沖縄県": 1894616
}

icons = {
    200: "⚡",
    201: "⚡",
    202: "⚡",
    210: "⚡",
    211: "⚡",
    212: "⚡",
    221: "⚡",
    230: "⚡",
    231: "⚡",
    232: "⚡",
    300: "🌧",
    301: "🌧",
    302: "🌧",
    310: "🌧",
    311: "🌧",
    312: "🌧",
    313: "🌧",
    314: "🌧",
    321: "🌧",
    500: "🌦",
    501: "🌦",
    502: "🌦",
    503: "🌦",
    504: "🌦",
    511: "❄️",
    520: "🌧",
    521: "🌧",
    522: "🌧",
    531: "🌧",
    600: "❄️",
    601: "❄️",
    602: "❄️",
    611: "❄️",
    612: "❄️",
    613: "❄️",
    615: "❄️",
    616: "❄️",
    620: "❄️",
    621: "❄️",
    622: "❄️",
    701: "🌫",
    711: "🌫",
    721: "🌫",
    731: "🌫",
    741: "🌫",
    751: "🌫",
    761: "🌫",
    771: "🌫",
    781: "🌫",
    800: "☀️",
    801: "🌤",
    802: "⛅️",
    803: "☁️",
    804: "☁️"

}


def get_weather_data(name, pre_id):
    url = "http://api.openweathermap.org/data/2.5/weather"
    query = {
        "APPID": os.environ.get("APPID"),
        "units": "metric",
        "id": pre_id,
        "mode": "json"
    }
    r = requests.get(url, params=query)
    data = r.json()
    print(data)
    weather = icons[data["weather"][0]["id"]]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    temp_max = data["main"]["temp_max"]
    temp_min = data["main"]["temp_min"]
    return "|{}|{}|{}|{}|{}|{}|".format(name, weather, description, humidity, temp_max, temp_min)


if __name__ == "__main__":
    jst = timezone(timedelta(hours=+9), "JST")
    today = datetime.now(jst).strftime("%Y-%m-%d")

    md = textwrap.dedent("""
        ![workflow](https://github.com/0x0u/auto_open_weather_map/workflows/workflow/badge.svg?branch=master)
        ## Auto Open Weather Map
        update: {}
        
        |prefectures|weather|description|humidity(%)|temp_max(℃)|temp_min(℃)|
        |:-----------:|:------------:|:------------:|:-----------:|:------------:|:-----------:|
    """).format(today).strip() + "\n"

    for i in pre_ids:
        data = get_weather_data(i, pre_ids[i])
        md += data + "\n"

    with open("README.md", "w") as f:
        f.write(md)
