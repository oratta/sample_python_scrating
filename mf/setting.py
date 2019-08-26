# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

print("start Setting")
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)
load_dotenv()
print("end settings")

BS_TAG = 'bs_detail'
SECTION_INFO ={}
SECTION_INFO[BS_TAG] = {}
SECTION_INFO[BS_TAG]['name_tr_id'] = 1
SECTION_INFO[BS_TAG]['value_tr_id'] = 2
SECTION_INFO[BS_TAG]['belongs_tr_id'] = 3
section_tag = 'bs_detail'
