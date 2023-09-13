from rest_framework.response import Response

class crud():
    def __init__(self, request, model, srl_model, key):
        self.m = model
        self.r = request
        self.s = srl_model
        self.k = key
        
    
    def create(self):
        content = self.s(data = self.r.data)
        if content.is_valid():
            content.save()
            return Response(200)
        else: 
            return Response(f"new data failed : {content.errors}")
    
    def read(self):
        
        get_content = self.m.objects.all()
        content = self.s(get_content, many=True)
        return Response(content.data)
    
    def update(self):
        try:
            get_content = self.m.objects.get(id=self.k)
        except:
            return Response(f"This {self.k} don't exist")
            
        content = self.s(get_content, data = self.r.data)
        if content.is_valid():
            content.save()
            return Response(200)
        else:
            get_content.save()
            return Response(f"update failed : {content.errors}") 
    
    def delete(self):
        try:
            get_content = self.m.objects.get(id=self.k)
        except:
            return Response(f"This {self.k} don't exist")
        get_content.delete()
        return Response(200)