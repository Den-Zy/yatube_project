# posts/views.py
from django.http import HttpResponse

# Main page
def index(request):
    return HttpResponse('Main page of POSTS project')

# Group list
def group_posts(request, sl):
    return HttpResponse(f'''1. post {sl} <p>
                        
                        2. post 2''')