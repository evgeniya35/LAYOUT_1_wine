import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape



def age_winery(start_wine=None):  # костыль...
    if start_wine is None:
        start_wine = datetime.datetime(year=1920, month=1, day=1)
    duration = datetime.datetime.today() - start_wine
    age = duration.days // 365
    k = age % 10
    if (age > 9) and (age < 20) or (age > 110) or (k > 4) or (k == 0):
        return str(age) + " лет"
    else:
        if k == 1:
            return str(age) + " год"
        else:
            return str(age) + " года"

df = pd.read_excel(
    "wine3.xlsx",
    sheet_name="Лист1",
    header=0,
    na_values="NaN",
    keep_default_na=False
    )

wines = {}
for category in df["Категория"].unique():
    wines[category] = df[df["Категория"] == category].to_dict("records")

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape(["html", "xml"])
)

template = env.get_template("template.html")
render_page = template.render(
    years=age_winery(),
    wines=wines
    )

with open(file="index.html", mode="w", encoding="utf8") as file:
    file.write(render_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
