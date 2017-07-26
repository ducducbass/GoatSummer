# coding=utf-8

# GOAT Summer Entry Bot by @edzart/@573supreme

import requests
from time import sleep, time


GOATUSER = 'fake@gmail.com'  # GOAT email here
GOATPASS = 'password123'  # GOAT password here


class Goat:
    def __init__(self):
        self.start = time()
        self.s = requests.Session()
        self.headers = {
            'Host': 'www.goat.com',
            'Accept-Encoding': 'gzip,deflate',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'Accept-Language': 'en-US;q=1',
            'User-Agent': 'GOAT/1.11 (iPhone; iOS 10.3.2; Scale/2.00)',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.auth_token = ''
        self.products = []
        print '='*50
        print '\n #GOATSUMMER ENTRY JIG \n BY @EDZART/@573SUPREME \n http://github.com/alxgmpr/goatsummer \n'
        print '='*50

    def login(self, username, password):
        url = 'https://www.goat.com/api/v1/users/sign_in'
        data = {
            'user[login]': username,
            'user[password]': password
        }
        try:
            print 'logging in w/ {}:{}'.format(username, password)
            r = self.s.post(
                url,
                data=data,
                headers=self.headers,
                timeout=5
            )
            if r.status_code == 200:
                print 'getting user token'
                try:
                    r = r.json()
                    self.auth_token = r['authToken']
                    print 'using auth token {}'.format(self.auth_token)
                    self.headers['Authorization'] = 'Token token="{}"'.format(self.auth_token)
                    return True
                except KeyError:
                    print 'couldnt find auth token'
                    return False
            else:
                print 'got bad status code {} from login'.format(r.status_code)
                return False
        except requests.exceptions.Timeout:
            print 'timeout from login request'
            return False

    def get_products(self, page):
        url = 'https://www.goat.com/api/v1/contests/2?page={}'.format(page)
        try:
            print 'scraping up product template ids (page {})'.format(page)
            r = self.s.get(
                url,
                headers=self.headers,
                timeout=5
            )
            if r.status_code == 200:
                try:
                    r = r.json()
                    for prod in r['productTemplates']:
                        self.products.append(prod['id'])
                        print '{} \t|| {}'.format(prod['id'], prod['name'].encode('utf-8'))
                    print 'scraped {} ids'.format(len(self.products))
                    return True
                except KeyError:
                    print 'couldnt find product ids'
                    return False
            else:
                print 'got bad status code {} from pid scrape'.format(r.status_code)
                return False
        except requests.exceptions.Timeout:
            print 'timeout from product scrape'
            return False

    def share_product(self, pid, network):
        url = 'https://www.goat.com/api/v1/contests/2/shared'
        data = {
            'productTemplateId': pid,
            'socialMediaType': network
        }
        try:
            print 'submitting share for prod {}'.format(pid)
            r = self.s.post(
                url,
                headers=self.headers,
                data=data,
                timeout=5
            )
            if r.status_code == 200:
                print 'successfully submitted {}'.format(pid)
            else:
                print 'got bad status code {} from share'.format(r.status_code)
        except requests.exceptions.Timeout:
            print 'timeout from product share {}'.format(pid)
            return False
g = Goat()
if g.login(GOATUSER, GOATPASS):
    print '=' * 50
    for i in range(0, 16):
        g.get_products(i)
        print '='*50
    for p in g.products:
        g.share_product(p, 'twitter')
        sleep(1)
        g.share_product(p, 'facebook')
        sleep(1)
        g.share_product(p, 'instagram')
        sleep(1)
print '='*50
print 'time to run: {} sec'.format(abs(g.start-time()))