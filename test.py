# import sys
# with open("./test.txt","r") as file:
#     content=file.read()
#     print(content)

# with open("./test.txt","r") as file:
#     content=file.read()
#     print(content)

# filename=sys.argv[2]
# print(filename)
# with open(filename,"r") as file:
#     content=file.read()
#     print(content)

type_dict={"<class 'list'>":'[]',"<class 'set'>":'{}',"<class 'dict'>":"{}","<class 'tuple'>":"()"}
dit={1:"a",2:"b",3:{1,2},4:[1,2]}
# base="json"
# print(f"{base}={{}}")
# for key,value in dict.items():
#     if isinstance(value, (int, float, str, bool)):
#         base=f"{base}.{key}"
#         print(f"{base}:{value}")
#     else:
#         base=f"{base}.{key}"
#         print(f"{base}:{type_dict.get(str(type(value)))}")

def flatten(my_dict,last_key):
 if isinstance(my_dict, (int, float, str, bool)):
    print(f"{last_key}={my_dict}")
 elif isinstance(my_dict,list):
     for idx,value in enumerate(my_dict):
         print(f"{last_key}[{idx}]={value}")
 elif isinstance(my_dict,dict):
    for key, value in my_dict.items():
        if isinstance(value, (list,dict)):
            print(f"{last_key}.{key}={type_dict.get(str(type(value)))}")
            flatten(value,last_key={key})
        else:
           flatten(value,last_key={key})

flatten(dit,last_key="json")

import re
import json
test="json = {};\njson.menu = {};\njson.menu.id = file;\njson.menu.id.value = File;\njson.menu.id.value.popup.menuitem[2].value.onclick.test.value.onclick.test.value.onclick.test[0] = 1;\njson.menu.id.value.popup.menuitem[0] = {};"
tet='{"a":1,"b":2}'
test2='json={}'
# print(json.loads(test2))
# 层级关系，key和value
# 层级关系：通过list的index来取
# key和value简单.

# 当前问题：如何解决update导致的覆盖问题，如何解决结构识别问题
# 解决list的读取访问问题

def getExpress(s):
   if "[" in s:
      return eval(s)
   else:
      return s

def getKV(string):
      string=string[:-1]
      pattern=r"(\w+)(\[\d\])?(\s*=\s*)(.*)"
      match=re.search(pattern,string)
      if match.group(2):
         key=f"{match.group(1)}{match.group(2)}"
      else:
        key=match.group(1)
      value=match.group(4)
      return key,value

def getObject(s):
   if(s=='{}'):
      return {}
   if(s=='[]'):
      return []
   else:
      return s

def ungron(string):
   lines=string.split("\n")
   res={}
   for line in lines:
      test=line.split(".")[::-1]
      cur_res={}
      for idx,item in enumerate(test):
         if idx==0:
            key,value=getKV(item)
            # print(type(key),key)
            cur_res={getExpress(key):getObject(value)}
         else:
            key=item
            # print(type(key),key)
            cur_res={key:cur_res}
            print(f"{idx} round: {cur_res}")
      res.update(cur_res)
   print(res)

    #   if match:
    #     key,_,value=match.group()
    #     print(match)

a=ungron(test)
# print(a)


test={
   "me":[1,2,3],
   "you":[2,5,6],
   "he":{"a":[1,2,3]}
}
# print(test["you"][1])
# print(1,"you"[1])
# print(test.get("he").get("a"))
# print(test)

# container=test.get("me")
# container[0]=10000
# print(test)
# test2={"me":container}
# test2["me"][0]=-1
# print(test)

# container={"k":[]}
# test.update(container)
# container={1:2}
# test.update(container)
# container.update({1:[1,2]})
# test.update(container)
# print(test)