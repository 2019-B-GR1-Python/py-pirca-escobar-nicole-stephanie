import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from proyecto.items import ProductoLapto
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaProductosPoint(CrawlSpider):
    name = 'crawl_point'
    allowed_domains = [
        'point.com.ec'
    ]
    start_urls = [
        'https://point.com.ec/categories/laptops',
        'https://point.com.ec/categories/de_escritorio_y_all_in_one',
        'https://point.com.ec/categories/televisores'
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

