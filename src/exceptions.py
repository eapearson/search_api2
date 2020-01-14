

class InvalidParameters(Exception):
    """Invalid request parameters."""

    def __init__(self, msg): self.msg = msg

    def __str__(self): return self.msg


class UnknownMethod(Exception):
    """Unrecognized RPC method."""

    def __init__(self, msg): self.msg = msg

    def __str__(self): return self.msg


class MissingHeader(Exception):
    """Missing required header in a request."""

    def __init__(self, header_name):
        self.header_name = header_name

    def __str__(self):
        return "Missing header: " + self.header_name


class UnauthorizedAccess(Exception):
    "Authentication failed for an authorization header."""

    def __init__(self, auth_url, response):
        self.auth_url = auth_url
        self.response = response
