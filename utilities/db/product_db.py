from interact_with_DB import interact_db

class DBproducts:



    def get_price(self, product):

        get_price = "SELECT Price FROM web_project_g6.products where WHERE ProductID='%s';" % product
        answer = interact_db(query=get_price, query_type='fetch')
        return answer


dbProducts = DBproducts()