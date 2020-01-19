from Algorhythm import ID3
from data.Collection import Collection
from data.MyAttributes import MyAttributes

myCollection = Collection("../assets/agaricus-lepiota.data")

print(ID3(
    MyAttributes[1:(len(MyAttributes) - 1)],
    MyAttributes[1:(len(MyAttributes) - 1)],
    myCollection
))
