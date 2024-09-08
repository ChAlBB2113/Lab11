from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def ottieniDDfromDB():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct(Product_color) as c
                   from go_sales.go_products gp 

                             """
        cursor.execute(query, ())
        for row in cursor:
            result.append(row["c"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def ottieniNodi(colore):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct(Product_number) as n
from go_sales.go_products gp 
where Product_color =%s
                                 """
        cursor.execute(query, (colore, ))
        for row in cursor:
            result.append(row["n"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def ottieniArchi(colore, anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select t.p1 as pp1, t.p2 as pp2,  count(*) as c
from	(select g1.Product_number as p1, g2.Product_number as p2, g2.`Date` as d
		from go_daily_sales g1 , go_daily_sales g2
		where   g1.Product_number<g2.Product_number  and g1.Product_number 
				in (select Product_number 
					from go_products gp 
					where Product_color=%s)	
				and g2.Product_number 
				in (select Product_number 
					from go_products gp 
					where Product_color=%s)
					and g1.Retailer_code=g2.Retailer_code
				and year(g1.`Date`)=%s and year(g2.`Date`)=%s
				and g1.`Date`=g2.`Date`
		group by p1, p2, d) as t
group by pp1, pp2

 """
        cursor.execute(query, (colore, colore, anno, anno))
        for row in cursor:
            result.append((row["pp1"], row["pp2"], row["c"]))


        cursor.close()
        conn.close()
        return result
'''
    @staticmethod
    def ottieniList():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select Retailer_code as r, Product_number  as p, year(Date) as y, Date as d
            from go_sales.go_daily_sales gds 
 """
        cursor.execute(query, ())
        for row in cursor:
            result.append((row["r"], row["p"], row["y"], row["d"]))

        cursor.close()
        conn.close()
        return result
'''