from PIL import Image

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import redirect
from django.template import Context


from goatfarmapp.models import AnimalType, Breed, City, AnimalData, AnimalPicture
from goatfarmapp.helper import BreedInfo, AnimalInfo
from goatfarm import settings


# Create your views here.


def index(request):
    animaltypes = AnimalType.objects.all()

    animaltypesDictionary = {}

    for animaltype in animaltypes:
        breeds = Breed.objects.filter(AnimalTypeFK=animaltype.TypeID)
        breedsList = []
        for breed in breeds:
            newItem = BreedInfo( breed.BreedID, breed.BreedName, breed.AnimalTypeFK)
            breedsList.append(newItem)

        animaltypesDictionary[animaltype.TypeName] = breedsList

    contextdictionary = {}

    contextdictionary["AnimalTypes"] = animaltypesDictionary

    t = get_template('index.html')
    html = t.render(contextdictionary)
    return HttpResponse(html)


@csrf_protect
def login(request):
    c = {}
    return render(request, "login.html", c)


def performlogin(request):
    username = request.POST['username']
    password = request.POST['passwrd']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request)
        # Redirect to a success page.
        return redirect('openaddbasicinfo/')
    else:
        # Return an 'invalid login' error message.
        return HttpResponse('Unfortunately login denied User authenticated:' + str(request.user.is_authenticated))


# This will open the page animal info page
def openaddbasicinfo(request):
    animaltypes = AnimalType.objects.all()

    cityNames = City.objects.all()

    animaltypesDictionary = {}
    cityNamesDictionary = {}

    for animaltype in animaltypes:
        breeds = Breed.objects.filter(AnimalTypeFK=animaltype.TypeID)
        breedsList = []
        for breed in breeds:
            newItem = BreedInfo( breed.BreedID, breed.BreedName, breed.AnimalTypeFK)
            breedsList.append(newItem)

        animaltypesDictionary[animaltype.TypeName] = breedsList

    for city in cityNames:
        cityNamesDictionary[city.CityID] = city.CityName

    contextdictionary = {}

    contextdictionary["AnimalTypes"] = animaltypesDictionary
    contextdictionary["CityNames"] = cityNamesDictionary

    t = get_template('AddAnimal.html')
    html = t.render(contextdictionary)

    return HttpResponse(html)


def addbasicanimalinfo(request):
    postBreed = request.POST["breedname"]
    tokens = postBreed.split(',')
    breedId = tokens[0]
    animalTypeId = tokens[1]

    cityId = request.POST["cityname"]

    heading = request.POST["heading"]

    description = request.POST["description"]

    price = request.POST["price"]

    height = request.POST["height"]

    length = request.POST["length"]

    neckcircumference = request.POST["neckcircumference"]

    animalId = AnimalData.objects.all().count() + 1

    pAnimalType = AnimalType.objects.get( TypeID = animalTypeId )
    pBreed = Breed.objects.get( BreedID = breedId )
    pCity = City.objects.get( CityID = cityId )

    newrec = AnimalData( AnimalID = animalId,
                         AnimalTypeFK = pAnimalType,
                         BreedFK = pBreed,
                         CityFK = pCity,
                         Heading = heading,
                         Description = description,
                         Price = price,
                         Height = height,
                         Length = length,
                         neckCircumference = neckcircumference)
    newrec.save()

    request.session["AnimalID"] = newrec.AnimalID

    return HttpResponse('')


def uploadImage(request):
    pathToImages = settings.STATIC_URL + 'images/'
    extension = ".jpeg"
    prefixFile = "Image"
    prefixThumbNail = "ThumbNail"

    maxCount = 0

    if AnimalPicture.objects.count() > 0:
        latestObject1 = AnimalPicture.objects.latest('PicID')
        maxCount = int(latestObject1.PicID)

    animalID = int(request.session["AnimalID"])

    message = "No Of file: " + request.FILES['file1'].name
    newFile = request.FILES['file1']

    imageName = prefixFile + str(maxCount) + extension
    thumbNailName = prefixThumbNail + str(maxCount) + extension

    imagePath = pathToImages + imageName
    thumbnailPath = pathToImages + thumbNailName

    newWrite = open(imagePath, 'wb+')
    for chunk in newFile.chunks():
        newWrite.write(chunk)

    newWrite.close()

    size = 80, 80

    out_file = open(thumbnailPath, 'wb')
    im = Image.open(imagePath)
    im.thumbnail(size)
    im.save(out_file, "JPEG")
    out_file.flush()
    out_file.close()

    pAnimal = AnimalData.objects.get(AnimalID=animalID)

    maxCount = maxCount + 1

    pImage = AnimalPicture(AnimalID=pAnimal, PicID=maxCount, PicFileName=imageName, ThumbNailName=thumbNailName)
    pImage.save()

    t = get_template('uploadimage.html')
    contextDictionary = {}
    contextDictionary["RowID"] = str(maxCount)
    contextDictionary["filename"] = thumbNailName

    html = t.render(contextDictionary)

    return HttpResponse(html)


def deleteImage(request):
    imageID = request.POST["ImageID"];

    aPic = AnimalPicture.objects.get(PicID=imageID)
    aPic.delete()

    return HttpResponse()

