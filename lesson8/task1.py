import re


def email_parse(email):
    VALID_EMAIL = re.compile(r"^[a-zA-z0-9\.!#$%&'*+\-\/=?^_`{|}~]+[@][a-zA-z0-9]+[\.][a-zA-Z]+$")
    if VALID_EMAIL.match(email):
        RE_NAME_DOMEN = re.compile(r"[^@]+")
        name_user = re.findall(RE_NAME_DOMEN, email)[0]
        domen = re.findall(RE_NAME_DOMEN, email)[1]
        dict_email = {name_user: domen}
        return dict_email
    else:
        raise ValueError


if __name__ == "__main__":
    print(email_parse("loginadanil.ru@mail.ru"))
