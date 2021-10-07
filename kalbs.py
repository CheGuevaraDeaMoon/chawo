

import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36',
    'Content-Type': 'text/plain',
    'Origin': 'https://www.premiersports.ie',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.premiersports.ie/index.php?rt=checkout/guest_step_3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cookie': 'language=en; currency=EUR; __utmz=223686490.1633356161.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); AC_SF_570B85B058=iqnt62hm3920m1tjbvg2p4ms47; apbct_checkjs=521c57fd6366ee1c089bd48ea33d5100; __utma=223686490.290451982.1633356161.1633520328.1633621767.3; __utmc=223686490; __utmt=1; apbct_timestamp=1633621967; apbct_cookies_test=c23bc39a27fce3eff2df65b75d927079; apbct_timezone=8; apbct_ps_timestamp=1633621976; apbct_visible_fields=0; apbct_visible_fields_count=0; __utmb=223686490.9.10.1633621767; apbct_fkp_timestamp=1633621980; apbct_pointer_data=%5B%5B1150%2C200%2C4301%5D%2C%5B1223%2C158%2C10924%5D%2C%5B1256%2C106%2C14629%5D%2C%5B1315%2C179%2C16619%5D%5D',
}

data = [
  ('cc_owner', 'Jay+Jay'),
  ('cc_number', '4420620116616706'),
  ('cc_expire_date_month', '02'),
  ('cc_expire_date_year', '2023'),
  ('cc_cvv2', '337'),
  ('', ''),
]

fuc = requests.post('https://www.premiersports.ie/index.php?rt=extension/default_stripe/send', headers = headers, data = data)
print(fuc.status_code)
