#!_*_coding:utf-8_*_
#__author__:"Alex Li"



import os
import sys
import logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = "%s/db/account" % BASE_DIR


LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}
LOG_PATH = os.path.join(BASE_DIR,'logs')

LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},

}