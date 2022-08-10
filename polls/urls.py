from django.urls import include, path

# from .views import polls_detail, polls_list
# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail")
# ]

from .apiviews import ChoiceList, CreateVote, LoginView, PollViewSet, UserCreate #, PollList, PollDetail, 

# urlpatterns = [
#     path("polls/", PollList.as_view(), name="polls_list"),
#     path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
#     path("choices/", ChoiceList.as_view(), name="choice_list"),
#     path("vote/", CreateVote.as_view(), name="create_vote"),
# ]

urlpatterns = [
    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]

# os dois primeiros views usam o mesmo modelo e serializer.
# usando routers, podemos agrupar:

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')
urlpatterns.append(path('', include(router.urls)))

# usando swagger para documentação
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Polls API')
urlpatterns.append(path(r'swagger-docs/', schema_view))
