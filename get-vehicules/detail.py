#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class Detail(object):
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

        self.url = 'https://www.olx.com.pk/item/civic-87gl-a-cng-cleared-IDUIaEZ.html#8dc446e009'
        self.listid = 0
        self.store = ''
        self.title = ''
        self.price = ''
        self.location = ''
        self.zipcode = ''
        self.neighborhood = ''
        self.description = ''
        self.date = ''
        self.anuncio = 'particular'
        self.veiculedetails = {}
        self.categoria = ''
        self.fuel = ''
        self.year = ''
        self.license = ''
        self.doors = ''
        self.gear = ''
        self.km = ''
        self.model = ''

    def get_detail_info(self):
        r = requests.get(self.url, headers=self.headers)

        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, 'lxml')

            self.listid = self.url.rsplit('-', 1)[1]

            name = soup.findAll('li', {'class', 'item owner mb10px '})
            if name:
                texto = name[0].find('p', class_='text')
                if texto:
                    self.store = texto.text.strip()

            title = soup.find('h1')
            if title is not None:
                self.title = title.text.strip()

            location = soup.findAll('div', {'class': 'OLXad-location mb20px'})
            if location:
                dados = location[0].findAll('ul', {'class': 'list square-gray'})

                for litag in dados[0].findAll('li'):
                    texto = litag.find('span', class_='term')
                    if texto and texto.text == 'Município:':
                        a = dados[0].find('a', class_='link')
                        if a:
                            self.location = a.text.strip()
                    if texto and texto.text == 'CEP:':
                        try:
                            self.zipcode = dados[0].findAll('strong', {'class': 'description'})[1].text.strip()
                        except IndexError as ex:
                            pass
                    if texto and texto.text == 'Bairro:':
                        self.neighborhood = dados[0].findAll('strong', {'class': 'description'})[2].text.strip()

            price = soup.findAll('span', {'class': 'OLXad-price'})
            if price:
                self.price = price[0].text.replace('.', '').replace('R$', '').strip()

            description = soup.findAll('div', {'class': 'OLXad-description mb30px'})
            if description:
                self.description = description[0].text.strip()

            self.anuncio = 'particular'
            date = soup.find('div', {'class': 'OLXad-date mb5px'})
            if date:
                if date.text.__contains__('Anúncio de Empresa'):
                    self.anuncio = 'empresa'
                    try:
                        self.date = date.text.split('|')[:1].replace('Inserido em:', '').strip()
                    except AttributeError as ex:
                        self.date = date.text.replace('Inserido em:', '').strip()
                else:
                    self.date = date.text.replace('Inserido em:', '').strip()

            # veichle details
            details = soup.findAll('div', {'class': 'OLXad-details mb30px'})
            if details:
                dados = details[0].findAll('ul', {'class': 'list square-gray'})
                for litag in dados[0].findAll('li'):
                    texto = litag.find('span', class_='term')
                    if texto and texto.text == 'Categoria:':
                        self.categoria = dados[0].findAll('strong', {'class': 'description'})[0].text.strip()
                    if texto and texto.text == 'Modelo:':
                        self.model = dados[0].findAll('strong', {'class': 'description'})[1].text.strip()
                    if texto and texto.text == 'Ano:':
                        try:
                            self.year = dados[0].findAll('strong', {'class': 'description'})[2].text.strip()
                        except IndexError as ex:
                            continue
                    if texto and texto.text == 'Quilometragem:':
                        try:
                            self.km = dados[0].findAll('strong', {'class': 'description'})[3].text.strip().replace('.', '')
                        except IndexError as ex:
                            continue
                    if texto and texto.text == 'Combustível:':
                        try:
                            self.fuel = dados[0].findAll('strong', {'class': 'description'})[4].text.strip()
                        except IndexError as ex:
                            continue
                    if texto and texto.text == 'Câmbio:':
                        try:
                            self.gear = dados[0].findAll('strong', {'class': 'description'})[5].text.strip()
                        except IndexError as ex:
                            continue
                    if texto and texto.text == 'Portas:':
                        try:
                            self.doors = dados[0].findAll('strong', {'class': 'description'})[6].text.strip()
                        except IndexError as ex:
                            continue
                    if texto and texto.text == 'Final de placa:':
                        try:
                            self.license = dados[0].findAll('strong', {'class': 'description'})[7].text.strip()
                        except IndexError as ex:
                            continue

                self.veiculedetails = {
                    'categoria': self.categoria,
                    'model': self.model,
                    'year': self.year,
                    'km': self.km,
                    'fuel': self.fuel,
                    'gear': self.gear,
                    'doors': self.doors,
                    'license': self.license
                }

        else:
            print (" ERROR")