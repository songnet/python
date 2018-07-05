import mysql.connector
import sys

class TransferMoney(object):
    def __init__(self,db):
        self.db = db

    def transfer(self, source, target, money):
        try:
            self.checkid(source)
            self.checkid(target)
            self.check_money(source, money)
            self.reduce(source, money)
            self.add(target, money)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def checkid(self, source):
        try:
            cursor = self.db.cursor()
            sql = "select * from bank where id = %s" % source
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("%s not exist" % source)
        finally:
            cursor.close()

    def check_money(self, source, money):
        try:
            cursor = self.db.cursor()
            sql = "select * from bank where id = %s and mondy > %s" % (source,money)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("%s not money" % source)
        finally:
            cursor.close()

    def reduce(self, source, money):
        try:
            cursor = self.db.cursor()

            sql = "update bank set mondy = mondy-%s where id = %s" %(money, source)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception("%s not money" % source)
        finally:
            cursor.close()

    def add(self, target, money):
        try:
            cursor = self.db.cursor()
            sql = "update bank set mondy = mondy+%s where id = %s" % (money, target)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception("%s not money" % target)
        finally:
            cursor.close()

