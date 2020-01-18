import scrapy

def write_file(file_path, lines_write):
            try:
                file = open(file_path, mode="a")
                file.writelines(lines_write)
                file.close()
            except Exception as error:
                print('Error archivo')


def save_txt(title, prices, img_links):
    path_file = "C:/Users/NICOLE/Documents/GitHub/py-pirca-escobar-nicole-stephanie/04-scrapy/03-arania-basica/arania_basica/info_books.txt"
    books = []

    for x in range(0, len(title)):
        book = "\nTitle: " + title[x] + "\n" 
        + "Prices: " + prices[x] + "\n" ´
        + "Img Links: " + img_links[x] + "\n"
        books.append(book)
    write_file(path_file, books)


class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    urls_category = "http://books.toscrape.com/catalogue/category/books/" 
    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback = self.links_category)
    

    def links_category(self, response):
        books_urls = response.css("div.side_categories > ul > li > ul > li > a::attr(href)").extract()
        def transformBooksToLink(book_link):
            if(book_link != 'index.html'):
                book_link = book_link[3:]
            return self.urls_category + book_link

        books_full_url = list(map(transformBooksToLink, books_urls))
        for url in books_full_url:
            yield scrapy.Request(url=url, callback=self.parse_books)

    def book_info(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css("h3 > a::text").extract()
        precios = etiqueta_contenedora.css("div.product_price > p.price_color::text").extract()
        imagenes = etiqueta_contenedora.css("div.image_container > a > img::attr(src)").extract()

        precios_float = list(map(priceToFloat, precios))
        img_links = list(map(transformImageToLink, imagenes))
        guardar_archivo(titulos, precios, img_links)
        save_txt(title, prices, img_links)
    
    #def parse(self, response):
   #     pass