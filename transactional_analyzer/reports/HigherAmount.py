from database.MySQLConnector import MySQLConnector


class HigherAmount:
    def __init__(self):
        self.mysql = MySQLConnector()
        self.conn = None
        self.db_cursor = None

    def report(self):
        self.conn = self.mysql.connection
        self.db_cursor = self.conn.cursor()

        sub_query = (
            "SELECT transaction_amount FROM transactionals_data "
            "WHERE has_cbk = 'TRUE' AND transaction_amount > 1000"
        )

        query = (
            "SELECT transaction_id, user_id, transaction_amount, has_cbk "
            "FROM transactionals_data "
            f"WHERE transaction_amount IN ({sub_query}) "
            "ORDER BY transaction_amount DESC"
        )

        self.db_cursor.execute(query)
        results = self.db_cursor.fetchall()

        for transaction_id, user_id, transaction_amount, has_cbk in results:
            print(
                f'Id da transação: {transaction_id}, Id do Usuário: {user_id},'
                f' Valor: R$ {transaction_amount}, Houve Chargeback? {has_cbk}'
            )

        self.db_cursor.close()


if __name__ == '__main__':
    HigherAmount().report()