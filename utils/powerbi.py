import csv
from pathlib import Path
import requests
from django.conf import settings


# example_payload = {  # To: test-mostra-stream
#     'nome': 'Elias',
#     'votos1': 10,
#     'votos2': 98.6,
#     'votos3': 150,
#     'votos4': 98.6,
#     'votos5': 105,
# }
example_payload = [{  # To: mostra-stream
    'total_votos': 21,
    'total_genero_masculino': 10,
    'total_genero_feminino': 6,
    'preferred_dispositivo': 'Smartphone',
    'preferred_cor': 'Blue',
    'media_idade': 23.6,
    'media_opiniao': 3.5,

    'grafico': 'Teste',
    'min_media_opiniao': 1,
    'max_media_opiniao': 5,
}]


def push_stream_api(payload: list[dict[str, str | int | float]], endpoint: str = settings.POWERBI_SERVICE_STREAM_ENDPOINT):
    payload[0]['min_media_opiniao'] = 1
    payload[0]['max_media_opiniao'] = 5
    payload[0]['grafico'] = 'Mostra'
    return requests.post(endpoint, json=payload, timeout=5)


def push_stream_csv(payload: dict, csv_path: str | Path = settings.CSV_STREAM_PATH):
    with open(csv_path, 'a+', encoding='utf-8', newline='\n') as csv_file:  # newline='\r\n'
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(payload.values())
