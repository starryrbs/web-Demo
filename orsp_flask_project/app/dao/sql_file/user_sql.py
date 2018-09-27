do_user_sql={
    ##sql模版#"addUser":"insert into user(telephone,password,regist_date) values('{0}','{1}',CURDATE())",
    "registerUser":"INSERT INTO `user` (`telephone`, `password`,`username`) VALUES ('{}', '{}','{}')",
    "isExist":"SELECT * FROM `user` WHERE telephone='{}'",
}