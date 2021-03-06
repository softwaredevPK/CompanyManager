import unittest
from orm import DataAccessLayer


class MyTestCase(unittest.TestCase):

    def setUp(self):
        dal = DataAccessLayer()
        dal.conn_string = r"sqlite:///my_test_db.db"
        dal.echo = True
        dal.connect()
        self.session = dal.session_maker()

    def tearDown(self):
        self.session.close()


class TestCheckConstraintMethods(MyTestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_1(self):
        print('Works')




if __name__ == '__main__':
    unittest.main()

