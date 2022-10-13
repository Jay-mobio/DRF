from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.emails import send_otp_via_email

from .serializer import *
# Create your views here.

class RegisterAPI(APIView):
    def post (self,request):
        try :
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status':200,
                    'message':'registration successful check email',
                    'data':serializer.data,
                })
            return Response({
                'status':400,
                'message':'something went wrong',
                'data':"dsddfd" 
            })
        
        except Exception as e:
            print(e,'------------------------------')
            return Response('Some thing went wrong')

class VarifyOtp(APIView):
    def post(self,request):
        try :
            data = request.data
            serializer = VarifyAccountSerializer(data = data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email = email)
                if user:
                    if user[0].otp != otp:
                        return Response({
                                        'status':400,
                                        'message':'something went wrong',
                                        'data':"dsddfd" 
                                    })
                    user = user.first()
                    user.is_verified = True
                    user.save()

                    return Response({
                                    'status':200,
                                    'message':'Verification successful',
                                    'data':serializer.data,
                                    })                   
                
                return Response({
                                'status':400,
                                'message':'something went wrong',
                                'data':"dsddfd" 
                            })
            return Response({
                'status':400,
                'message':'something went wrong',
                'data':"dsddfd" 
            })
        
        except Exception as e:
            print(e)
            return Response("Some thing went wrong")

class SocialLogin(APIView):
    template_name = "index.html"

    def get(self,request):
        return render(request,self.template_name)

class Home(APIView):
    template_name = "home.html"
    
    def get(self,request):
        return render(request,self.template_name)