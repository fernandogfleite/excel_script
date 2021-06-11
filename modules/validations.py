def validate_has_value(value):
    value = value
    if value == "":
        raise ValueError("")
    return value

def validate_has_account(account):
    account = account
    if account == "":
        raise ValueError("Has no account")
    return account
