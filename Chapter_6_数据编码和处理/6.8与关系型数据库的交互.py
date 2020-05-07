'''
@Time    :   2020/05/07 22:32:13
@Author  :   Zhang Hui
'''

# 问题：想在关系型数据库中查询、增加和删除记录

import os
from os import path
import sqlite3

if __name__ == '__main__':

    stocks = [
        ('GOOG', 100, 490.1),
        ('AAPL', 50, 545.75),
        ('FB', 150, 7.45),
        ('HPQ', 75, 33.2),
    ]

    portfolio_db = path.join(path.dirname(__file__), 'database.db')

    if path.exists(portfolio_db):
        os.remove(portfolio_db)

    db = sqlite3.connect(portfolio_db)
    c = db.cursor()
    c.execute('create table portfolio (symbol text, shares integer, price real)')
    db.commit()
    c.executemany('insert into portfolio values (?, ?, ?)', stocks)
    db.commit()

    for row in db.execute('select * from portfolio'):
        print(row)

    print('price >= 100')
    min_price = 100
    for row in db.execute('select * from portfolio where price >= ?', (min_price,)):
        print(row)
