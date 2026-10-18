import json
from pathlib import Path
from json_log import log_json

folder = Path('json_files')

for file in folder.iterdir():
    if file.suffix == '.json':
        try:
            with open(file, encoding='utf-8') as f:
                json.load(f)
        except json.JSONDecodeError:
            log_json(file.name)