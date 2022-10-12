from rest_framework.authentication import TokenAuthentication as BasetokenAuth

class TokenAuthentication(BasetokenAuth):
    keyword = 'Token'