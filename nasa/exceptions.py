class NasaSDKError(Exception):
    """Base error for the SDK"""
    pass

class AuthenticationError(NasaSDKError):
    """Raised on 403 Forbidden (Bad API Key)"""
    pass

class ResourceNotFoundError(NasaSDKError):
    """Raised on 404 Not Found"""
    pass