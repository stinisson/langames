import json
import webbrowser
from pathlib import Path

from src.algorithm import analyze
from src.table_builders import HtmlTableBuilder, CsvTableBuilder, ConsoleTableBuilder


def run():
    json_object = json.loads(Path('data/gamers.json').read_text(encoding='utf8'))
    print(f"Read information about {len(json_object['gamers'])} LAN gamers.")
    ans = input("""I'm ready to analyze that data, but first, what output format do you want?
    1. HTML (will open in browser)
    2. CSV (you may open in Excel e.g)
    3. Console (display it here)
Your choice: """)
    if ans == "1":
        table_builder = HtmlTableBuilder()
        analyze(json_object, table_builder)
        html_content = table_builder.get_html()
        p = Path("data") / "output.html"
        p.write_text(html_content, encoding='utf8')
        print(f"Opening {p} in your default web browser...")
        webbrowser.open(str(p))
    elif ans == "2":
        table_builder = CsvTableBuilder()
        analyze(json_object, table_builder)
        csv_string = table_builder.get_csv_text()
        p = Path("data") / "output.csv"
        p.write_text(csv_string, encoding='utf8')
        print(f"The CSV file has been written to {p}.")
    elif ans == "3":
        table_builder = ConsoleTableBuilder(column_width=20)
        analyze(json_object, table_builder)
        text = table_builder.get_string_output()
        print(text)
    else:
        print("Not a valid option, quitting.")
        return


if __name__ == '__main__':
    run()
