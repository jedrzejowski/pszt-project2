from data.Attribute import Attribute

"""
Lista atrybutów grzybów
"""
MyAttributes = [
    Attribute("edible", ["edible=e", "poisonous=p"]),
    Attribute("cap-shape", ["bell=b", "conical=c", "convex=x", "flat=f", "knobbed=k", "sunken=s"]),
    Attribute("cap-surface", ["fibrous=f", "grooves=g", "scaly=y", "smooth=s"]),
    Attribute("cap-color", ["brown=n", "buff=b", "cinnamon=c", "gray=g", "green=r", "pink=p",
                            "purple=u", "red=e", "white=w", "yellow=y"]),
    Attribute("bruises", ["bruises=t", "no=f"]),
    Attribute("odor", ["almond=a", "anise=l", "creosote=c", "fishy=y", "foul=f",
                       "musty=m", "none=n", "pungent=p", "spicy=s"]),
    Attribute("gill-attachment", ["attached=a", "descending=d", "free=f", "notched=n"]),
    Attribute("gill-spacing", ["close=c", "crowded=w", "distant=d"]),
    Attribute("gill-size", ["broad=b", "narrow=n"]),
    Attribute("gill-color", ["black=k", "brown=n", "buff=b", "chocolate=h", "gray=g",
                             "green=r", "orange=o", "pink=p", "purple=u", "red=e",
                             "white=w", "yellow=y"]),
    Attribute("stalk-shape", ["enlarging=e", "tapering=t"]),
    Attribute("stalk-root", ["bulbous=b", "club=c", "cup=u", "equal=e",
                             "rhizomorphs=z", "rooted=r", "missing=?"]),
    Attribute("stalk-surface-above-ring", ["fibrous=f", "scaly=y", "silky=k", "smooth=s"]),
    Attribute("stalk-surface-below-ring", ["fibrous=f", "scaly=y", "silky=k", "smooth=s"]),
    Attribute("stalk-color-above-ring", ["brown=n", "buff=b", "cinnamon=c", "gray=g", "orange=o",
                                         "pink=p", "red=e", "white=w", "yellow=y"]),
    Attribute("stalk-color-below-ring", ["brown=n", "buff=b", "cinnamon=c", "gray=g", "orange=o",
                                         "pink=p", "red=e", "white=w", "yellow=y"]),
    Attribute("veil-type", ["partial=p", "universal=u"]),
    Attribute("veil-color", ["brown=n", "orange=o", "white=w", "yellow=y"]),
    Attribute("ring-number", ["none=n", "one=o", "two=t"]),
    Attribute("ring-type", ["cobwebby=c", "evanescent=e", "flaring=f", "large=l",
                            "none=n", "pendant=p", "sheathing=s", "zone=z"]),
    Attribute("spore-print-color", ["black=k", "brown=n", "buff=b", "chocolate=h", "green=r",
                                    "orange=o", "purple=u", "white=w", "yellow=y"]),
    Attribute("population", ["abundant=a", "clustered=c", "numerous=n",
                             "scattered=s", "several=v", "solitary=y"]),
    Attribute("habitat", ["grasses=g", "leaves=l", "meadows=m", "paths=p",
                          "urban=u", "waste=w", "woods=d"])
]
