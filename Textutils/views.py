
from django.http import HttpResponse
from django.shortcuts import render #   This  is use for templates


def index(request):
  
  return render(request, 'index.html')


def ana_lyze(request):

  # Get the text

  djtext=request.POST.get('text','default')        # ye ham ny 'text' jo name hy textarea ka us ky data ko removep my access kia hy 

  # Check checkbox values

  removepunc=request.POST.get('removepunc','off')
  fullcaps=request.POST.get('fullcaps','off')
  newlineremove=request.POST.get('newlineremove','off')
  extraspaceremove=request.POST.get('extraspaceremove','off')
  chareactercount=request.POST.get('chareactercount','off')
  
  #======================  Check which checkbox is on=============================

# check removepunc checkbox

  if removepunc == "on":

#   Ab yam yaha par ik for loop chaly gy jo agar djtext ky andar punctions ho gi unhy remove kar dy ga


    punctions = '''#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''

    analyzed=""

    for i in djtext:
      if i not in punctions:
        analyzed= analyzed + i
      

    params = {'purpose': 'REMOVE PUNCTIONS' , 'analyzed_text' : analyzed }
    djtext = analyzed

      

  # check fullcaps checkbox

  if(fullcaps == "on"):

    analyzed=""
    for i in djtext:
      analyzed= analyzed + i.upper()

    params = {'purpose': ' Changed to Upper case letters' , 'analyzed_text' : analyzed }
    djtext = analyzed
   


  # Check new line remove checkbox

  if(newlineremove == "on"):

    analyzed=""
    for i in djtext:
      if i !="\n" and i!="\r":
        analyzed= analyzed + i

    params = {'purpose': ' Remove new line' , 'analyzed_text' : analyzed }

    djtext = analyzed
   


  # Check Extra space remove checkbox

  if(extraspaceremove == "on"):

    analyzed=""
    for index, i in enumerate(djtext):
      if not(djtext[index] == " " and djtext[index+1]== " "):
        analyzed= analyzed + i

    params = {'purpose': ' Extra Space Remove' , 'analyzed_text' : analyzed }
    djtext = analyzed


  # Check CHaracter count checkbox

  if(chareactercount == "on"):

    analyzed={}
    for i in djtext:
      if i not in analyzed:
        analyzed[i] = 0
      analyzed[i]+=1

      
    params = {'purpose': ' Count Characters' , 'analyzed_text' : analyzed }
   


  if(chareactercount != "on" and extraspaceremove != "on" and newlineremove != "on" and fullcaps != "on" and removepunc != "on"):
    return HttpResponse("Please Select any operation")

  return render(request,'analyze.html',params)
 








