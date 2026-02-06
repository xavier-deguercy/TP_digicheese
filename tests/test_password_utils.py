from src.utils.password import hash_password, verify_password


def test_hash_and_verify_password_roundtrip():
    password = "super-secret"
    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed) is True


def test_verify_password_rejects_wrong_password():
    password = "super-secret"
    hashed = hash_password(password)

    assert verify_password("wrong-password", hashed) is False
