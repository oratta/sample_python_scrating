# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

print("start Setting")
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)
load_dotenv()
print("end settings")

SECTION_INFO ={
    'cash' : {
        'name_tr_id': 1,
        'value_tr_id': 2,
        'belongs_tr_id': 3,
        'table_css_selector': '#portfolio_det_depo > section > table'
    },
    'stock' : {
        'name_tr_id': 2,
        'value_tr_id': 6,
        'belongs_tr_id': 10,
        'table_css_selector': '#portfolio_det_eq > table'
    },
    'trust' : {
        'name_tr_id': 1,
        'value_tr_id': 5,
        'belongs_tr_id': 9,
        'table_css_selector': '#portfolio_det_mf > table'
    },
    'recievable' : {
        'name_tr_id': 1,
        'value_tr_id': 5,
        'belongs_tr_id': 9,
        'table_css_selector': '#portfolio_det_bd > table'
    },
    'other' : {
        'name_tr_id': 1,
        'value_tr_id': 3,
        'belongs_tr_id': 7,
        'table_css_selector': '#portfolio_det_oth > table'
    },
    'point' : {
        'name_tr_id': 1,
        'value_tr_id': 5,
        'belongs_tr_id': 7,
        'table_css_selector': '#portfolio_det_po > table'
    },
    'fx' : {
        'table_css_selector': '#portfolio_det_fx > table.table.table-bordered.table-fx'
    },
}
