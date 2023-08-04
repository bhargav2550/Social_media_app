from rest_framework.decorators import api_view,permission_classes
from social_media_app.models import Post,User
from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer,UserSerializer
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

@permission_classes((IsAuthenticated, ))
@api_view(["POST","GET"])
def posts(request):
    if request.method == "POST":
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            Post.objects.create(**serializer.data)
            return JsonResponse(data =serializer.data,status = 201)
        return Response(serializer.errors,status = 400 )
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
       
@permission_classes((IsAuthenticated, ))
@api_view(["DELETE",'GET'])
def postsdetails(request,pk):
    if request.method == "GET":
        post = Post.objects.get(id = pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
        #return JsonResponse({"message": "Invalid post"})
    if request.method=='DELETE':
        post = Post.objects.get(pk = pk)
        post.delete()
@permission_classes((IsAuthenticated, ))
@api_view(['GET'])
def like(request,pk): 
    post = Post.objects.get(pk=pk)
    post.likes+=1
    post.save()
    return JsonResponse({
        "id":post.id,
        "likes":post.likes
    })

@permission_classes((IsAuthenticated, ))
@api_view(["POST"])
def unlike(request,pk):
    post = Post.objects.get(pk=pk)
    post.likes-=1
    post.save()
    return JsonResponse({"message": "Unliked the post"})

@permission_classes((IsAuthenticated, ))
@api_view(['GET'])
def comment(request,pk):
    post = Post.objects.get(pk=pk)
    post.comments+=1
    post.save()
    return JsonResponse({"id":post.id})

@permission_classes((IsAuthenticated, ))
@api_view(['GET'])
def users(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return JsonResponse({
            "UserName": user.name,
            "followers":user.followers,
            "following":user.following
        })
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=404)

@permission_classes((IsAuthenticated, ))
@api_view(['POST','GET'])
def follow(request,user_id):
    if request.method == "GET":
        curr_user = request.user
        curr_user_id = curr_user.id 
        user = User.objects.get(id = user_id)
        user.followers+=1
        user.save()
        curr = User.objects.get(id = curr_user_id)
        curr.following+=1
        curr.save()
        return Response({"message": "Followed "+user.name})


