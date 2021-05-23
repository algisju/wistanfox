#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  get2.py
#  
#  Copyright 2021 geek <geek@KALIBOX>
#  
from pyisemail import is_email

address = "1q2w3e4r5t6y7u8i@hotmail.com"
bool_result_with_check = is_email(address,check_dns=True)
detailed_result_with_check = is_email(address, diagnose=True)

print(bool_result_with_check)
print(detailed_result_with_check)
