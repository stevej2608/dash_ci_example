

def test_page_nav1(duo, test_app):

    duo.server_url = duo.server_url + "/"

    # Confirm we're on page 1

    result = duo.wait_for_text_to_equal(".display-4", "Welcome to DashSPA", timeout=20)
    assert result
