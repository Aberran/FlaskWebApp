from websie import create_app

def test_home_page():
    '''
    GIVEN a Flask app configured for testing
    When the '/' page is requested (GET)
    THEN check that the response is valid
    '''
    flask_app = create_app()
    
    # Create a test client using the Flask application
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
    
def home_page_post():
    '''
    Given a Flask app configured for testing
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    '''
    flask_app = create_app()
        
    with flask_app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405