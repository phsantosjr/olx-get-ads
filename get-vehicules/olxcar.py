#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import json
import os
from detail import *
from lists import *
import requests

ANUNCIOS = Lists()
DETALHE = Detail()
ANUNCIOS.max_page_number = 100


def execute_scrap():
    DIR_SAVE_JSON = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'olx-base/capturas/')
    ANUNCIOS.get_lists()

    print ("    # {0} Links Capturados".format(str(len(ANUNCIOS.links))))

    for link in ANUNCIOS.links:
        try:
            DETALHE.url = link
            DETALHE.get_detail_info()

            if DETALHE.listid == 0:
                continue

            file = str(DETALHE.listid) + '.json'
            file_path = os.path.join(DIR_SAVE_JSON, file)
            print ("    ## - Salvando arquivo : " + file)

            with open(file_path, 'w') as f:

                valores = {
                    "id": DETALHE.listid,
                    "store": DETALHE.store,
                    "typead": DETALHE.anuncio,
                    "title": DETALHE.title,
                    "price": DETALHE.price,
                    "location": {
                        "location": DETALHE.location,
                        "neighborhood": DETALHE.neighborhood,
                        "zipcode": DETALHE.zipcode
                    },
                    "description": DETALHE.description,
                    "date": DETALHE.date,
                    "details": DETALHE.veiculedetails,
                    "url": link
                }

                json.dump(valores, f, indent=4)

        except requests.ConnectionError:
            continue
        except requests.exceptions.MissingSchema:
            continue


if __name__ == '__main__':
    execute_scrap()
