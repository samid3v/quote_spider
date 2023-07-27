import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    
    start_urls = [
        "https://quotes.toscrape.com/"
        ]         
            
    def parse(self, resp):
        quotes = resp.css('div.quote')
        for qoute in quotes:
            yield {
                'text': qoute.css('span.text::text').get().replace('“','').replace('”',''),
                'tags': qoute.css('div.tags a.tag::text').getall(),
                'author': qoute.css('small.author::text').get()
            }
            
            next_page = resp.css('li.next a::attr("href")').get()
            
            if next_page is not None:
                next_page = resp.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)