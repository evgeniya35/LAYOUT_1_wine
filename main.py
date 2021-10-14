import argparse
import datetime
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape


FOUNDATION = 1920  # год основания винодельни


def calc_age():
    age = datetime.datetime.today().year - FOUNDATION
    k = age % 10
    if (age > 9) and (age < 20) or (age > 110) or (k > 4) or (k == 0):
        return str(age) + " лет"
    else:
        if k == 1:
            return str(age) + " год"
        else:
            return str(age) + " года"


def main():
    parser = argparse.ArgumentParser(description="Launch parameters")
    parser.add_argument(
        "--wine",
        type=str,
        default="wine.xlsx",
        help="use --wine for path xlsx file (default: wine.xlsx)"
        )
    args = parser.parse_args()
    path = args.wine
    if os.path.exists(path):
        df = pd.read_excel(
            path,
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
            years=calc_age(),
            wines=wines
            )

        with open(file="index.html", mode="w", encoding="utf8") as file:
            file.write(render_page)

        server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
        server.serve_forever()


if __name__ == "__main__":
    main()
