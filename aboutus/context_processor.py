from .models import CompanyInfo


def get_company(request):
    urls = CompanyInfo.objects.get()
    return locals()
