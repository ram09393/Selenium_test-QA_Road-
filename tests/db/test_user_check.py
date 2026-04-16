from sqlalchemy import text


def test_user_create_in_db(db_connection):
    test_email = "esaveleva@qmail.com"

    result = db_connection.execute(
        text("select*from users_user where email = :email"),
        {"email": test_email}
    )
    user = result.fetchone()
    #fetchall
    #fetchmany(5)

    assert user is not None, "Пользователь не найден"
    assert user.email == test_email
    print(user.email)


def test_user_field(db_connection):
    test_email = "test2@gmail.com"

    result = db_connection.execute(
        text("select*from users_user where email = :email"),
        {"email": test_email}
    )
    user = result.fetchone()
    user_dict = user._mapping

    assert "id" in user_dict
    print(user.id)
    print(user_dict["id"])
    assert "email" in user_dict
    assert "username" in user_dict
