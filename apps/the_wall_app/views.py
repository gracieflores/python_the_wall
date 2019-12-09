from django.shortcuts import render, HttpResponse, redirect
from .models import Message, Comment
from apps.login_app.models import User

def index2(request):
    if (request.session.has_key('id')):
        context = {
            'user' : User.objects.get( id = request.session['id']),
            'all_messages': Message.objects.all().select_related('users'),
            'all_comments': Comment.objects.all().select_related('messages')
        }
        return render(request, "the_wall_app/index2.html", context)
    return redirect('/')

def messageToPost(request):
    if request.method == "POST":
        message = request.POST['message']
        user = User.objects.get(id = request.session['id'])
        context = {
            'messages' : Message.objects.create(message = message, users_id= user.id),
            'all_messages': Message.objects.all()
        }
        print(message)
    return redirect('/wall', context)

def commentToPost(request):
    if request.method == "POST":
        comment = request.POST['comment']
        user = User.objects.get(id = request.session['id'])
        context = {
            'comments' : Comment.objects.create(comment = comment, messages_id = request.POST['message_id'] , users_id = user.id)
        }
        print(comment)
        return redirect('/wall', context)

def deleteMessage(request):
    if request.method == "POST":
        this_message = Message.objects.get(id = request.POST['message_id'])
        print(request.POST['message_users_id'] == request.session['id'])
        if int(request.POST['message_users_id']) == request.session['id']:
            print(request.session['id'])
            
            this_message.delete()
            print(this_message)
        else:
            return redirect('/wall')
    return redirect('/wall')


def logoff(request):
    try:
        del request.session['email']
        del request.session['id']
    except KeyError:
        pass
    return redirect('/')