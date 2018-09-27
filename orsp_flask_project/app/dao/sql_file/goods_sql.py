do_goods_sql={
    ##sql模版# "addUser":"insert into user(telephone,password,regist_date) values('{0}','{1}',CURDATE())",
    "get_product_type_one":"SELECT * from product_type",
    "get_product_type_two":"SELECT * from product_type_two WHERE product_type_one_id={}",
    "get_product_type_three":"SELECT * from product_type_three WHERE product_type_two_id={}",

}