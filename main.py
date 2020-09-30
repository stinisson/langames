import json
import webbrowser
from pathlib import Path

from src.algorithm import analyse2

if __name__ == '__main__':
    json_object = json.loads(Path('data/gamers.json').read_text(encoding='utf8'))
    html_table = analyse2(json_object)
    Path('output.html').write_text(html_table, encoding='utf8')
    webbrowser.open('output.html')

