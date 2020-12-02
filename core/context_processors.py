from resume.models import GitHubButton
from briefcase.models import Type

def global_vars(request):
    context = dict() 
    info_id = request.resolver_match.kwargs.get('info_id')
    github_obj = GitHubButton.objects.filter(user__info_id=info_id).first()
    if github_obj  is not None:
        context.append({
            "github_url": github_obj.url,
            })
    context.update({
        "briefcase": Type.objects.filter(user__info_id=info_id), 
        })
    return context 
