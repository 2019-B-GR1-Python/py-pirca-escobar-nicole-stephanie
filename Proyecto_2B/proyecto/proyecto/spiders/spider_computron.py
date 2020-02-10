import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from proyecto.items import ProductoLapto
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaProductosPoint(CrawlSpider):
    name = 'crawl_computron'
    allowed_domains = [
        'computron.com.ec'
    ]
    start_urls = [
        'https://computron.com.ec/categories/laptops/1839',
        'https://computron.com.ec/categories/de_escritorio_y_all_in_one/1817',
        'https://computron.com.ec/categories/televisores/1825'
    ]
    
    url_segmento_permitido = (
        '#[0-9]+'
    )
    
    rules = (
        Rule(
            LinkExtractor(
                allow= (url_segmento_permitido,)
            ), callback = 'parse'
        ),
    )
    
    

    def parse(self, response):
        categoria=response.css('div.product-gallery>h2.title::text').extract_first()
       ## productos1 = response.css('li>div.productVitrine')
        productos = response.css('div.product-gallery__gallery u-margin-bottom-medium')
       ## precio = response.css('div.product-card')


        for producto in productos:
            existe_producto = producto.css('div.product-card__item__countdown--empty')

            if(len(existe_producto) > 0):
                producto_loader=ItemLoader(
                    item=ProductoLapto(),
                    selector=producto
                )
                producto_loader.add_css(
                    'nombre',
                    'div.product-card>h3.product-card__Text>a::text'
                )
                producto_loader.add_css(
                    'precio_regular',
                    'div.product-card>div.product-card__discount-price>p::text'
                )
                producto_loader.add_css(
                    'precio_oferta',
                    'div.product-card>div.product-card__discount-label>p::text'
                )
                producto_loader.add_value(
                    'categoria',
                    categoria
                )
                producto_loader.add_value(
                    'empresa',
                    'Computron'
                )

                yield producto_loader.load_item()

