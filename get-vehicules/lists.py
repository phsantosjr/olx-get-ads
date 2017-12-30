import requests
from bs4 import BeautifulSoup


class Lists(object):
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

        # 'http://www.olx.com.br/veiculos-e-acessorios/carros',
        self.url = [
            # 'http://sp.olx.com.br/sao-paulo-e-regiao/centro/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/sao-paulo-e-regiao/zona-leste/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/sao-paulo-e-regiao/zona-norte/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/sao-paulo-e-regiao/zona-oeste/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/sao-paulo-e-regiao/zona-sul/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/sao-paulo-e-regiao/abcd/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/sao-paulo-e-regiao/alphaville-e-tambore/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/sao-paulo-e-regiao/outras-cidades/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/sao-paulo-e-regiao/regiao-de-braganca/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/sao-paulo-e-regiao/regiao-de-jundiai/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/sao-paulo-e-regiao/interior/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/vale-do-paraiba-e-litoral-norte/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/baixada-santista-e-litoral-sul/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/regiao-de-bauru-e-marilia/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/regiao-de-sorocaba/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/regiao-de-ribeirao-preto/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/regiao-de-sao-jose-do-rio-preto/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/regiao-de-presidente-prudente/veiculos-e-acessorios/carros',
            # 'http://sp.olx.com.br/grande-campinas/veiculos-e-acessorios/carros',
            # 'http://rj.olx.com.br/rio-de-janeiro-e-regiao/veiculos-e-acessorios/carros',
            # 'http://rj.olx.com.br/norte-do-estado-do-rio/veiculos-e-acessorios/carros',
            # 'http://rj.olx.com.br/serra-angra-dos-reis-e-regiao/veiculos-e-acessorios/carros',
            # 'http://pr.olx.com.br/regiao-de-curitiba-e-paranagua/bairro-novo/veiculos-e-acessorios/carros',
            # 'http://pr.olx.com.br/regiao-de-curitiba-e-paranagua/boa-vista/veiculos-e-acessorios/carros',
            # 'http://pr.olx.com.br/regiao-de-curitiba-e-paranagua/boqueirao/veiculos-e-acessorios/carros',
            # 'http://pr.olx.com.br/regiao-de-curitiba-e-paranagua/cajuru/veiculos-e-acessorios/carros',
            # 'http://pr.olx.com.br/regiao-de-curitiba-e-paranagua/cidade-industrial/veiculos-e-acessorios/carros',
            # 'http://pr.olx.com.br/regiao-de-curitiba-e-paranagua/fazendinha-portao/veiculos-e-acessorios/carros',
            # 'http://pr.olx.com.br/regiao-de-curitiba-e-paranagua/matriz/veiculos-e-acessorios/carros',
            # 'http://pr.olx.com.br/regiao-de-curitiba-e-paranagua/pinheirinho/veiculos-e-acessorios/carros',
            # 'http://pr.olx.com.br/regiao-de-curitiba-e-paranagua/santa-felicidade/veiculos-e-acessorios/carros',
            # 'http://pr.olx.com.br/regiao-de-curitiba-e-paranagua/grande-curitiba/veiculos-e-acessorios/carros',
            # 'http://pr.olx.com.br/regiao-de-curitiba-e-paranagua/outras-cidades/veiculos-e-acessorios/carros'
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/barreiro/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/pampulha/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/venda-nova/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/zona-centro-sul/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/zona-leste/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/zona-nordeste/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/zona-noroeste/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/zona-norte/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/zona-oeste/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/grande-belo-horizonte/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/zona-da-mata/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/regiao-de-ipatinga/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/ouro-preto-e-cons-lafayete/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/belo-horizonte-e-regiao/regiao-de-sete-lagoas/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-juiz-de-fora/barbacena-e-sao-joao-del-rei/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-juiz-de-fora/regiao-de-muriae-uba-e-vicosa/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-juiz-de-fora/regiao-de-juiz-de-fora/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-governador-valadares-e-teofilo-otoni/vale-do-jequitinhonha/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-governador-valadares-e-teofilo-otoni/manhuacu/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-governador-valadares-e-teofilo-otoni/regiao-de-governador-valadares/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-governador-valadares-e-teofilo-otoni/regiao-de-ipatinga/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-governador-valadares-e-teofilo-otoni/regiao-de-teofilo-otoni/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-uberlandia-e-uberaba/alto-paranaiba/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-uberlandia-e-uberaba/triangulo-mineiro/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-pocos-de-caldas-e-varginha/regiao-de-itajuba/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-pocos-de-caldas-e-varginha/regiao-de-lavras/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-pocos-de-caldas-e-varginha/pocos-de-caldas-e-pouso-alegre/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-pocos-de-caldas-e-varginha/regiao-de-passos/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-pocos-de-caldas-e-varginha/regiao-de-varginha-e-alfenas/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-divinopolis/regiao-central-mineira/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-divinopolis/regiao-de-divinopolis-e-formiga/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-divinopolis/regiao-de-sete-lagoas/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-montes-claros-e-diamantina/vale-do-jequitinhonha/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-montes-claros-e-diamantina/noroeste-de-minas/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-montes-claros-e-diamantina/norte-de-minas/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-montes-claros-e-diamantina/regiao-de-montes-claros/veiculos-e-acessorios/carros',
            # 'http://mg.olx.com.br/regiao-de-montes-claros-e-diamantina/regiao-de-pirapora-e-curvelo/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/norte-de-santa-catarina/regiao-do-vale-do-itajai/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/florianopolis-e-regiao/centro/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/florianopolis-e-regiao/norte/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/florianopolis-e-regiao/sul/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/florianopolis-e-regiao/leste/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/florianopolis-e-regiao/continente/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/florianopolis-e-regiao/grande-florianopolis/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/florianopolis-e-regiao/outras-cidades/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/oeste-de-santa-catarina/regiao-de-chapeco/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/oeste-de-santa-catarina/regiao-de-joacaba/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/oeste-de-santa-catarina/regiao-de-xanxere-e-concordia/veiculos-e-acessorios/carros',
            # 'http://sc.olx.com.br/oeste-de-santa-catarina/regioes-de-curitibanos-e-c-dos-lages/veiculos-e-acessorios/carros',
            # 'http://es.olx.com.br/norte-do-espirito-santo/vitoria/veiculos-e-acessorios/carros',
            # 'http://es.olx.com.br/norte-do-espirito-santo/vila-velha/veiculos-e-acessorios/carros',
            # 'http://es.olx.com.br/norte-do-espirito-santo/outras-cidades/veiculos-e-acessorios/carros',
            # 'http://es.olx.com.br/norte-do-espirito-santo/afonso-claudio-e-regiao/veiculos-e-acessorios/carros',
            # 'http://es.olx.com.br/norte-do-espirito-santo/guarapari-e-regiao/veiculos-e-acessorios/carros',
            # 'http://es.olx.com.br/norte-do-espirito-santo/regiao-de-colatina-e-nova-venecia/veiculos-e-acessorios/carros',
            # 'http://es.olx.com.br/norte-do-espirito-santo/regiao-de-linhares-e-sao-mateus/veiculos-e-acessorios/carros',
            # 'http://es.olx.com.br/norte-do-espirito-santo/santa-teresa-e-regiao/veiculos-e-acessorios/carros',
            # 'http://es.olx.com.br/sul-do-espirito-santo/guarapari-e-regiao/veiculos-e-acessorios/carros',
            # 'http://es.olx.com.br/sul-do-espirito-santo/cachoeiro-de-itapemirim-e-regiao-sul/veiculos-e-acessorios/carros',
            # 'http://es.olx.com.br/sul-do-espirito-santo/afonso-claudio-e-regiao/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/campus-puc/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/centro/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/extremo-sul/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/leste/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/moinhos-de-vento/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/norte/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/praia-de-belas/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/sul/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/ufrgs/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/grande-porto-alegre/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/outras-cidades/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-pelotas-rio-grande-e-bage/regiao-de-bage/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-pelotas-rio-grande-e-bage/sudeste-rio-grandense/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-caxias-do-sul-e-passo-fundo/regiao-de-carazinho/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-caxias-do-sul-e-passo-fundo/regiao-de-caxias-do-sul/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-caxias-do-sul-e-passo-fundo/regiao-de-erechim/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-caxias-do-sul-e-passo-fundo/regiao-de-gramado-e-canela/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-caxias-do-sul-e-passo-fundo/regiao-de-nao-me-toque-e-soledade/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-caxias-do-sul-e-passo-fundo/regiao-de-passo-fundo/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-caxias-do-sul-e-passo-fundo/regiao-de-vacaria/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-santa-maria-uruguaiana-e-cruz-alta/noroeste-do-estado/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-santa-maria-uruguaiana-e-cruz-alta/norte-do-estado/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-santa-maria-uruguaiana-e-cruz-alta/oeste-do-estado/veiculos-e-acessorios/carros',
            # 'http://rs.olx.com.br/regioes-de-santa-maria-uruguaiana-e-cruz-alta/regiao-de-cruz-alta-e-ijui/veiculos-e-acessorios/carros',
            'http://rs.olx.com.br/regioes-de-santa-maria-uruguaiana-e-cruz-alta/regiao-de-santa-maria/veiculos-e-acessorios/carros',
        ]

        self.links = []
        self.max_page_number = 100  # max pagination of OLX is 100

    def get_lists(self):
        for url in self.url:

            page = 1

            while page <= self.max_page_number:
                url_consulta = url + "?o={0}".format(str(page))
                try:
                    r = requests.get(url_consulta, headers=self.headers, timeout=10)
                    html = r.text
                    soup = BeautifulSoup(html, 'lxml')
                    listing_section = soup.findAll('a', {'class': 'OLXad-list-link'})

                    for link in listing_section:
                        if link['href'].strip() not in self.links:
                            self.links.append(link['href'].strip())

                except Exception as ex:
                    print ("## ERROR: " + str(ex))
                    continue

                print(' # Capturando links de : {0}'.format(url_consulta))

                page += 1
