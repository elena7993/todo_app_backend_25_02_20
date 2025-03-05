from rest_framework.views import APIView
from rest_framework.response import Response


class Me(APIView):
    def get(self, req):
        user = req.user

        return Response(
            {
                "ok": "잘됨!",
            }
        )
