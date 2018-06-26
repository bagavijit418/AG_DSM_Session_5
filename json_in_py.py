import json as js
jsonData = '{"name":"Frank","age":38}'
json_to_python = js.loads(jsonData)
print("Json to Python: ",jsonData)

pythondict={"fname":"Avijit","lname":"Bag","age":38}
python_to_json= js.dumps(pythondict)
print("Python to Json: ",python_to_json)

class Employee:
	def __init__(self,p1,p2):
		self.fame=p1
		self.age=p2

e= Employee("Avijit",27)
def jsonDefault(object):
    return object.__dict__
print(js.dumps(e,default=jsonDefault))
