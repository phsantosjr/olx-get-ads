# OLX GET ADS
Sistema para capturar anúncios no site da OLX Brasil.

Ele foi criado para analisar os dados dos anúncios de veículos, como preço médio, região com mais anúncios, veículos mais anunciados.

![](https://img.shields.io/badge/Python-3.5%2C%203.6-blue.svg)

## Requirements
Você precisa instalar o Python 3.5.2 para executar OLX GET ADS.


## Virtual Env
Recomendamos o uso de um ambiente virtual para execução do projeto.

```
$ python3 -m pip install -U virtualenv
$ python3 -m virtualenv env
```

## Instalação e uso

```
$ pip install -r requirements.txt
```

Cria uma pasta no mesmo nível da pasta do projeto com nome olx-base e dentro uma pasta capturas.
Os dados capturados no anúncios serão salvos um em cada arquivo.json dentro da pasta capturas.
Nome do arquivo: <id do anúncio>.json


## Link master de captura

* [Carros](http://www.olx.com.br/veiculos-e-acessorios/carros)
* [Motos](http://www.olx.com.br/veiculos-e-pecas/motos)

## JSON de retorno salvo no arquivo

* Carro:

```
{
    "url": "http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/veiculos-e-pecas/carros/mercury-sedan-v-8-1941-para-restauracao-23271492",
    "location": {
        "neighborhood": "Petr\u00f3polis",
        "location": "Porto Alegre",
        "zipcode": "91310-003"
    },
    "price": "32000",
    "id": "23271492",
    "date": "An\u00fancio de Empresa | \n\t\t\n\t\t\t\t 18 Outubro \u00e0s 16:08",
    "typead": "empresa",
    "description": "BANDA BRANCA vende raro Mercury Sedan 4 portas V8\n1941, para restaura\u00e7\u00e3o total.Carroceria muito alinhada, com excelente \u00edndice de\ndetalhes externos e internos, sem problemas graves\nde corros\u00e3o ou ferrugem, apenas pequenas\ncorre\u00e7\u00f5es. Nunca foi batido,Interior original.Mec\u00e2nica V8 flat head, com c\u00e2mbio 3 m, n\u00e3o est\u00e1\nfuncionando mas vira bem. Ve\u00edculo extremamente\noriginal, com exce\u00e7\u00e3o das rodas, est\u00e1 com aro 15.Capuz dianteiro com uma adapta\u00e7\u00e3o f\u00e1cil de\nretirar.Painel com acabamentos em madeira, rel\u00f3gios e\nr\u00e1dio originais em excelente estado.Documento ok com placas amarelas e dut em branco.\nF\u00e1cil regularizar.Estudo proposta a vista, trocas de meu interesse e\nou parcelamento. Transporte documentos por conta\ndo compradorAten\u00e7\u00e3o: valor para troca: R$ 35.000,00Acesse a Loja BANDA BRANCA no OLX e veja nossos\nve\u00edculos.\"Creia no Senhor Jesus e Ele satisfar\u00e1 os desejos\nde teu cora\u00e7\u00e3o\".",
    "title": "Mercury Sedan V 8 1941 para restaura\u00e7\u00e3o",
    "store": "Artur Sperotto",
    "details": {
        "gear": "4 portas",
        "license": "4",
        "categoria": "Carros",
        "model": "HONDA CIVIC SEDAN LXS 1.8/1.8 FLEX 16V AUT. 4P",
        "year": "100.000",
        "doors": "4 portas",
        "km": "Gasolina",
        "fuel": "Manual"
    }
}
```


## Author

* Paulo Henrique (PH)

## Road Map

* 0.0.3:
    * implantação do scrapy

* 0.0.2:
    * captura os links do último nível de região dinamicamente
    * captura link de anúncios de motos das UFs

* 0.0.1:
    * captura link de anúncios de carros das UFs
    * separa os dados de cada link em um arquivo .json

