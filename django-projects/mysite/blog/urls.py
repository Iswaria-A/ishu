from django.urls import path
from . import views
urlpatterns = [
path('insert-data',views.insert_blog,name='insert_blog'),
path('select/<int:requested_blog_id>',views.showBlog,name='showBlog'),
path('edit/<int:requested_blog_id>',views.edit_blog,name='edit_blog'),
path('delete/<int:requested_blog_id>',views.delete_entry,name='delete_entry'),
path('pagination',views.listBlogs,name='listBlogs'),
path('signup',views.signup,name='signup'),
path('login',views.logined,name='login'),
path('logout',views.logout_view,name='logouts'),
path('msg',views.index,name='index'),
path('redirect',views.sample_view,name='sample_view'),
path('uploading',views.upload_file,name='upload_file'),
path('image',views.showImage,name='showImage'),
path('mail',views.sendMailToUser,name='sendMailToUser'),
path('view',views.sample_view,name='sample_view'),
path('new',views.some_view,name='some_view'),
path('pdf',views.html_to_pdf_view,name='html_to_pdf_view'),
path('api',views.login,name='login'),
path('sample',views.sample_api,name='sample_api'),
path('data',views.sample_data,name='sample_data'),
path('put/<int:blog_id>',views.sample_put,name='sample_put'),
path('delete1/<int:blog_id>',views.sample_delete,name='sample_delete')
]