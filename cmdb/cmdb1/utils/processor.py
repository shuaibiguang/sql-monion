import pymysql.cursors


class processor():
    @classmethod
    def loop(self, host, port, user, password):
        servers = {}
        servers['myHost'] = host
        servers['myPort'] = port
        try:
            link = pymysql.connect(host=host, user=user, password=password, port=port,
                                   charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            servers['Connect_Error'] = str(e)
            servers['Slave_Healthy'] = 'red'
            return servers
        with link.cursor() as cursors:
            try:
                sql = "SHOW SLAVE STATUS"
                rs = cursors.execute(sql)
                rs = cursors.fetchall()
            except Exception as e:
                servers['Query_Error'] = str(e)
                servers['Slave_Healthy'] = 'red'
                return servers
        row = rs[0]
        if 500 < row['Seconds_Behind_Master'] or 'No' in [row['Slave_IO_Running'], row['Slave_SQL_Running']]:
            row['Slave_Healthy'] = 3
        elif 30 < row['Seconds_Behind_Master'] and row['Seconds_Behind_Master'] <= 500:
            row['Slave_Healthy'] = 2
        elif 5 < row['Seconds_Behind_Master'] and row['Seconds_Behind_Master'] <= 30:
            row['Slave_Healthy'] = 1
        else:
            row['Slave_Healthy'] = 0
        row['myHost'] = host
        row['myPort'] = port
        servers = row
        return servers

    @classmethod
    def master(self, host,port, user, password):
        try:
            link = pymysql.connect(host=host, user=user, password=password, port=port,
                                   charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            return 'err'
        return 'ok'
