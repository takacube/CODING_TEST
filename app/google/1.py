blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    }
]

reqs = ["gym", "school", "store", "office"]

gymdist=0
schooldist=0
store=0
for index, block in enumerate(blocks):
    if(block["gym"]):
        gymdist
