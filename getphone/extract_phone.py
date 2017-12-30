#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import re
import os
import json

caminho = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'capturas')
phonePattern = re.compile(r'(\d{2})\D*(\d{5})\D*(\d{4})\D*(\d*)$')
# phonePattern = re.compile(r'^(\(11\) [9][0-9]{4}-[0-9]{4})|(\(1[2-9]\) [5-9][0-9]{3}-[0-9]{4})|(\([2-9][1-9]\) [5-9][0-9]{3}-[0-9]{4})$')


def extract_phone():
    arquivo_tratado = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tratado', 'olx-20171129.txt')

    for root, dirs, filenames in os.walk(caminho):
        for f in filenames:
            file = os.path.join(caminho, f)
            with open(file, 'r') as data_file:
                data = json.load(data_file)

                if data['typead'] == 'empresa':
                    for i in re.findall(phonePattern, data['description']):
                        linha = ''.join(i) + '|' + data['store'] + '|' + data['location']['location'] + '\n'
                        file_open = open(arquivo_tratado, 'a')
                        file_open.write(linha)
                        file_open.close()
                        print ("    # Salvando : {0}".format(i))


if __name__ == '__main__':
    print(" Starting ...")
    extract_phone()
    print(" Finished ...")
