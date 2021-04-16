from se2020.morse import encode_morse


def test_morse_for_sos():
    assert encode_morse("sos") == "... --- ... "
    # assert 1==1
