from Algorhythm import ID3, C45
from data.MushroomCollection import MushroomCollection
from data.MyAttributes import MyAttributes

myCollection = MushroomCollection("../assets/agaricus-lepiota.data")

print(C45(
    MyAttributes[0],
    MyAttributes[1:(len(MyAttributes) - 1)],
    myCollection
).dump())
