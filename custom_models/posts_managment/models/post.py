from odoo import api, models,fields,_
from bs4 import BeautifulSoup
import requests
import logging



_logger = logging.getLogger(__name__)


class Post(models.Model):
    _name = 'post.publication'
    _description = 'Post Publications'

    name = fields.Char(string="Nom",required=True)
    link = fields.Char(string="Lien")
    publisher = fields.Char(string='Publicateur')
    description = fields.Text(string='Description')
    publication_date = fields.Date(string='Date de publication')

    @api.model
    def scrape_and_add_posts(self):
        response = requests.get('https://techcrunch.com/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            divs = soup.find_all('div', class_='wp-block-tc23-post-picker')
            for div in divs:
                try:
                    name = div.find('h2').text
                    description = div.find('p', class_='wp-block-post-excerpt__excerpt').text
                    publication_date = div.find('time').get('datetime')
                    publisher = div.find('div', class_='wp-block-tc23-author-card-name').find('a').text
                    link = div.find('h2').find('a').get('href')
                    self.create({
                        'name': name,
                        'link': link,
                        'publisher': publisher,
                        'description': description,
                        'publication_date': publication_date
                    })
                except Exception as e:
                    _logger.error(f"Error while scraping: {e}")
        else:
            print("No posts found")
            _logger.error(f"Failed to retrieve job postings. Status code: {response.status_code}")
