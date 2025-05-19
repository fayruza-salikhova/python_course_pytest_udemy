from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.core.mail import send_mail
from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


@api_view(http_method_names=["POST"])
def send_company_email(request: Request) -> Response:
    """
    sends email with request payload
    sender: biruzka@gmail.com
    receiver: biruzka@gmail.com
    :param request:
    :return:
    """
    send_mail(
        subject=request.data.get("subject"),
        message=request.data.get("message"),
        from_email=None,
        recipient_list=["test@example.com"],
    )
    return Response(
        {"status": "success", "email": "email sent successfully"}, status=200
    )
