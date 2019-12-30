import requests
import time
from concurrent import futures


class TiebaSpider(object):
    def __init__(self):
        self.url = 'http://xidong.net/List000/Catalog_{}_T1.html'

    def parse_url(self, url):
        print('pend to send')
        response = requests.get(url)
        return response

    def run(self):
        url_li = [
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
            67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185
        ]
        url_list = [self.url.format(i) for i in url_li]

        # with futures.ThreadPoolExecutor(5) as executor:
        #     responses = executor.map(self.parse_url, url_list)
        #     for response in responses:
        #         if response.status_code == 200:
        #             print('get')
        #         else:
        #             print('not get')

        for i in url_list:
            response = self.parse_url(i)
            if response.status_code == 200:
                print('get')
            else:
                print('not get')

        print(len(url_li))


if __name__ == "__main__":
    start = time.perf_counter()
    liyi = TiebaSpider()
    liyi.run()
    end = time.perf_counter()
    print(f'用时: {end - start}')
    # 330 用时42
    # 960 105
    # 5 个线程 83
