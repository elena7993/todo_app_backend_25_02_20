from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framwwork.permissions import IsAuthenticated
from .serializer import UserSerializer


class Me(APIView):
    permission_classes = [IsAuthenticated]
    # Me역시 로그인되어야만 볼 수 있게 해야함

    def get(self, req):
        user = req.user

        serializer = UserSerializer(user)

        return Response(serializer.data)


# 요청들어옴 -> 해결 -> 응답해야함

# req : 요청했을 때 그에 대한 정보들

# serializer : 번역기
# python code -> json으로 응답해야함.
# 브라우저는 python 코드를 모르기 때문에
# =>serializer를 통해 json 형식으로 변환
# =>serializer-> django에 기본적으로 있으나 꾸지기 때문에
# DRF의 serializer를 사용하면 번역도 해주고, 유효성 검사도 해줌
