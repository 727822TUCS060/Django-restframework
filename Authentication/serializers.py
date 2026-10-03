from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
class CustomToken_Serializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        #return super().validate(attrs) #only send access and refresh tokens
        data = super().validate(attrs) #custom data
        data.update({
            'username':self.user.username, #to return username for the particular login
            'first_name':self.user.first_name

        })
        return data

    