obj = {
    "stuff":'foo',
    "data":{
        "val": {
            "thing":{
                "info":'bar',
                "moreinfo": {
                    "evenmoreInfo":{
                        "wemadeit": 'baz'
                    }
                }
            }
        }
    }
}


def collectStrings(obj):
    # TODO
    arr = []
    for key in obj:
        if type(obj[key]) == str:
            arr.append(obj[key])
        if type(obj[key]) == dict:
            arr.extend(collectStrings(obj[key]))
    return arr

print(collectStrings(obj))