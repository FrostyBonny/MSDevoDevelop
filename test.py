#
# INSERT INTO `ClassTest`.`m_user`(`password`, `username`, `name`, `phone`, `role`, `class`) 
# VALUES ('202cb962ac59075b964b07152d234b70', 'user2', '用户2', '13120184444', 'student', 12)
from random import choice,randint
userInedx = 3
index2 = 20
classIndex = [1,8,9,10,12,13,14,15,16]
for i in range(7):
    # print("INSERT INTO `ClassTest`.`m_user`(`password`, `username`, `name`, `phone`, `role`, `class`)" +  
    #     "VALUES (\'202cb962ac59075b964b07152d234b70\', \'user%s\', \'用户%s\', \'13120184444\', \'student\', %s);"%(\
    #         userInedx,userInedx,choice(classIndex)))
    # print("INSERT INTO `ClassTest`.`sc`(`score`, `student`, `course`) VALUES (%s, %s, %s);"%(
    #     randint(70,101),randint(27,45),randint(1,13)))
    print("UPDATE `ClassTest`.`m_user` SET `name` = '班主任%s' WHERE `id` = %s;"%(userInedx,index2))
    userInedx = userInedx + 1
    index2 = index2 + 1
# sql = "INSERT INTO %s%s VALUES %s"%(table,\
            # create_insert_sql_column(values),create_insert_sql_values(values))

# INSERT INTO `ClassTest`.`sc`(`score`, `student`, `course`) VALUES (88, 1, 1)