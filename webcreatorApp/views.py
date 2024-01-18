from django.shortcuts import render
import requests



def create(request):                                                                                           

  if request.method=='POST':
    pic_keywords= request.POST.get('top5')
    display_keywords = request.POST.get('display')
    reverse =request.POST.get('reverse')
    titlebar = request.POST.get('titlebar')

    user_input ={ "pic_keywords": pic_keywords,"display_keywords": display_keywords,"reverse": reverse,"titlebar": titlebar}


    response =requests.post('http://3.24.216.3/videoapi/createvideo/',data=user_input)
    if response.ok:
      response =response.json()
      video_title = response['title']
      download_link = response['download_link']
      validity = response['Link_Validity']
      print(validity)
      context =  {'title':video_title,'download_link':download_link,'validity':validity}
      return render(request,'received.html',context)
    else:
      response  = response.json()
      error = response['non_field_errors']
      return render(request,'error.html',{'error':error})
      

  return render(request,"index.html")




    







