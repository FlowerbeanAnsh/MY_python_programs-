def fun(nestedDict,Dic,currentKey):
    for Key in nestedDict,Key():
        if type(nestedDict[Key])==int:
            Dic[(currentKey+"."+Key).strip(".")]=nestedDict[Key]
        else:
            dic=fun(nestedDict[Key],Dic(currentKey+"."+Key).strip("."))
    return Dic
def func_dic(nestedDic):
    return fun(nestesdDic,duc(),"")
def main():
    nestesdDictionary=  {
        "Key":3,
        "foo":  {
            "a":5,
            "bar":  {
                "bar":8
                }
            }
        }
    dicten=func_dic(nestesdDictionary)
    print(dicten)
