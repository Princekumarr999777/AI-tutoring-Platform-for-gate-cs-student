from src.core.security import create_access_token, create_refresh_token, decode_token, hash_password, verify_password
def test_password_round_trip():
    hashed = hash_password("strong-passphrase")
    assert hashed != "strong-passphrase"
    assert verify_password("strong-passphrase", hashed)
    assert not verify_password("wrong", hashed)
def test_token_types():
    assert decode_token(create_access_token("1"))["type"] == "access"
    assert decode_token(create_refresh_token("1"))["type"] == "refresh"
