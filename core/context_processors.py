from django.db.utils import OperationalError
from .models import SiteSettings


def site_settings_context(request):
    try:
        settings_obj = SiteSettings.get_solo()
    except OperationalError:
        settings_obj = None
    return {"site_settings": settings_obj}
