from resume.models import UrlButton
from briefcase.models import Type


def global_vars(request):
    context = dict()
    info_id = request.resolver_match.kwargs.get("info_id")
    url_buttons = UrlButton.objects.filter(user__info_id=info_id)
    if url_buttons is not None:
        context.update(
            {
                "url_buttons": url_buttons,
            }
        )
    context.update(
        {
            "briefcase": Type.objects.filter(user__info_id=info_id),
        }
    )
    return context
