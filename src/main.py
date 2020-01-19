from Algorhythm import ID3
from data.MushroomCollection import MushroomCollection
from data.MyAttributes import MyAttributes

myCollection = MushroomCollection("../assets/agaricus-lepiota.data")

print(ID3(
    MyAttributes[1:(len(MyAttributes) - 1)],
    MyAttributes[1:(len(MyAttributes) - 1)],
    myCollection
).dump())
