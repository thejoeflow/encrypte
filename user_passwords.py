class UserData:

    def __init__(self, username, password_hash, salt, shared_secret, passwords=[]):
        self._username = username
        self._password_hash = password_hash
        self._salt = salt
        self._shared_secret = shared_secret
        self._passwords = passwords

    @property
    def username(self):
        return self._username

    @property
    def password_hash(self):
        return self._password_hash

    @property
    def salt(self):
        return self._salt

    @property
    def passwords(self):
        return self._passwords

    @property
    def shared_secret(self):
        return self._shared_secret

    @username.setter
    def username(self, val):
        if len(val) < 1:
            raise ValueError("Cannot set a blank username")
        self._username = val

    @password_hash.setter
    def password_hash(self, val):
        if len(val) < 1:
            raise ValueError("Cannot set a blank password")
        self._password_hash = val

    @salt.setter
    def salt(self, val):
        self._salt = val

    @passwords.setter
    def passwords(self, val):
        self._passwords = val

    @shared_secret.setter
    def shared_secret(self, val):
        self._shared_secret = val


class Password:

    def __init__(self, password, service, create_date, expiry_date):
        self._password = password
        self._service = service
        self._create_date = create_date
        self._expiry_date = expiry_date

    @property
    def password(self):
        return self._password

    @property
    def service(self):
        return self._service

    @property
    def create_date(self):
        return self._create_date

    @property
    def expiry_date(self):
        return self._expiry_date

    @password.setter
    def password(self, val):
        self._password = val

    @service.setter
    def service(self, val):
        self._service = val

    @create_date.setter
    def create_date(self, val):
        self._create_date = val

    @expiry_date.setter
    def expiry_date(self, val):
        self._expiry_date = val
