
class BreedInfo:

    BreedId = 0
    Name = ""
    AnimalType = 0

    def __init__(self, breedid, name, animaltype):
        self.BreedId = breedid
        self.Name = name
        self.AnimalType = animaltype


class AnimalInfo:
    AnimalID = 0
    AnimalTypeFK = 0
    BreedFK = 0
    CityFK = 0
    CityID = 0
    CityName = ""
    Description = ""
    Price = 0
    Height = 0
    Length = 0
    NeckCircumference = 0

    def __init__(self, animalid, animaltypeid, breedid, cityid, cityname, description, price, height, length, neckcircumference):
        self.AnimalID = animalid
        self.AnimalTypeFK = animaltypeid
        self.BreedFK = breedid
        self.CityID = cityid
        self.CityName = cityname
        self.Description = description
        self.Price = price
        self.Height = height
        self.Length = length
        self.NeckCircumference = neckcircumference

