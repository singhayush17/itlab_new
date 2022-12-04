
from rest_framework.decorators import APIView
from rest_framework.decorators import api_view
from . import views
from rest_framework.response import Response
from base.models import Room,Topic
from .serializers import RoomSerializer



class StartupAPIView(APIView):
        serializer_class = RoomSerializer


        def get_queryset(self):
                startup = Room.objects.all()
                return startup



        def get(self,request,*args,**kwargs):



         try:
                id = request.query_params["id"]
                print(request.query_params)
                print(id)


                if id!=None:
                                startup=Room.objects.get(id=id)
                                serializer=RoomSerializer(startup)
         except:
                        # print("hello")
                        startups = self.get_queryset()
                        serializer = RoomSerializer(startups,many=True)
                
         return Response(serializer.data)




        


        
        def post(self,request,*args,**kwargs):
                startup_data = request.data
                print(startup_data)
                startups = self.get_queryset()
                # serializer = RoomSerializer(startups,many=True)

                topic_name = "PENDING"
                topic,created = Topic.objects.get_or_create(name=topic_name)  #gets the value or creates a new value
                new_startup=Room.objects.create(
                status="PENDING",
                host = request.user,
                topic = topic,
                name = startup_data['name'],
                description = startup_data['description'],
                )
                new_startup.save()
                serializer=RoomSerializer(new_startup)

                return Response(serializer.data)

        
        def put(self,request,*args,**kwargs):
                startup = Room.objects.get(id = request.query_params["id"])
                print(startup)
                data = request.data
                startup.name = data["name"]
                startup.description = data["description"]
                startup.save()
                serializer = RoomSerializer(startup)
                return Response(serializer.data)


        def patch(self,request,*args,**kwargs):
                startup = Room.objects.get(id = request.query_params["id"])
                data = request.data 
                startup.name = data.get("name", startup.name)
                startup.description = data.get("description", startup.description)
                startup.save()
                serializer = RoomSerializer(startup)
                return Response(serializer.data)

        def delete(self,request,*args,**kwargs):

                startup = Room.objects.get(id = request.query_params["id"])
                # serializer = RoomSerializer(startup)
                # if request.user.is_superuser:

                startup.delete()
                return Response({"message":"Deleted"})
                # else:
                #         return Response({"message":"Action not allowed"})



# @api_view(['GET','POST','PUT','DELETE'])
# def getRoutes(request):
#         if(request=='POST'):
#                 print(1)
#         routes = [
#             'GET /api/startups',
#             'GET /api/startups/:id',
#             'GET /api',
#         ]
#         return Response(routes)

# @api_view(['GET','POST','PUT','DELETE'])
# def getStartups(request):
#         if(request=='POST'):
#                 print(1)
#         rooms = Room.objects.all()
#         serializer = RoomSerializer(rooms,many=True)
#         return Response(serializer.data)

# @api_view(['GET','POST','PUT','DELETE'])
# def getStartup(request,pk):
#     if(request=='POST'):
#         print(1)
#     room = Room.objects.get(id=pk)

#     serializer= RoomSerializer(room,many=False)
#     return Response(serializer.data)