from .models import Message
from .serializers import MessageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def new_message(request):

    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def message_detail(request, id):

    try:
        message = Message.objects.get(pk=id)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def messages_for_spesific_receiver(request, receiver):
    try:
        messages = Message.objects.filter(receiver__exact=receiver)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)