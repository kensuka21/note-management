from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class QueryParamJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Try header-based authentication first (default behavior)
        header_auth = super().authenticate(request)
        if header_auth is not None:
            return header_auth

        # Fallback to query parameter authentication
        token = request.query_params.get('token')
        if not token:
            return None  # No token provided in query params

        try:
            validated_token = self.get_validated_token(token)
            user = self.get_user(validated_token)
        except AuthenticationFailed:
            raise AuthenticationFailed("Invalid or expired token.")

        return (user, validated_token)