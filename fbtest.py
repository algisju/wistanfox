#!/usr/bin/env python 3.9
# -*- coding: utf-8 -*-
#
#  fbtest.py
#  
#  Copyright 2021 geek <geek@KALIBOX>
#  
#  
import Crypto
import requests 
import re
import urllib.parse
from Crypto.Hash import SHA512
email = "adrewx@free.fr"
password = "loulou75"

session = requests.session()
# session.headers.update({
  # 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
# })
# response = session.get('https://wallet.btc.com')
# response = session.post('wallet.btc.com/login.php?', data={
  # '': email,
  # '': password
# }, allow_redirects=False)
h=SHA512.new()
h.update(b'yakyak')
print(h.hexdigest())		#<Response [302]>

