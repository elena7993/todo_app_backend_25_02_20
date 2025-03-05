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


# 요청들어옴 -> 해결 -> 응답해야함함
