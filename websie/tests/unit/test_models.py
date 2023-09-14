from websie.models import User

def test_new_user():
    '''
    GIVEN User model
    When a new User is created
    THEN check the mail and password_hashed fields are defined correctly
    '''
    user = User('vlado@gmail.com', 'FlaskIsAwesom')
    assert user.email == 'vlado@gmail.com'
    assert user.password != 'FlaskIsAwesom'