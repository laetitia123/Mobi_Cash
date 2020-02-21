from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    url(r'newsToday',views.news_today,name='newsToday'),
    url(r'register/',views.register,name = 'register'),
    url(r'^$',views.login_view,name='login'),
    url(r'logout/',views.logout_view,name='logout'),
    url(r'^new/article$', views.add_customer, name='add-customer'),

    url(r'^update/(?P<pk>\d+)$',views.update,name="update"),
    url(r'^view_customer/$',views.view_customer,name = 'view-customer'),
    url(r'^edit_customer/$',views.edit_customer,name = 'edit'),
    url(r'^delete_customer/$',views.delete_customer,name = 'delete'),
    url(r'^deleted/(?P<pk>\d+)$',views.deleted,name="deleted"),
    
    url(r'render/pdf/', views.gen_pdf,name='pdf'),
    url(r'^xls/$', views.export_xls, name='export_xls'),


    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'^api/merchpro/$', views.MerchListpro.as_view())
    # url(r'^page/(\d+)', views.page,name=('pa')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)