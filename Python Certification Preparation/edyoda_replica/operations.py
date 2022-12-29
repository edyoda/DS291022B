import json
import os

def register(filename,name,mobile_no,email_ID,password):
    details = {
        "Full Name":name,
        "Mobile Number":mobile_no,
        "Email ID":email_ID,
        "Password":password
    }

    file = open(filename,"r+")

    try:
        data = json.load(file)
        if details not in data:
            data.append(details)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    except json.decoder.JSONDecodeError:
        lst = []
        lst.append(details)
        json.dump(lst,file)
        file.close()
        return True
    return False

def login(filename,email_ID,password):
    file = open(filename,"r")
    try:
        data = json.load(file)
        for i in data:
            if i["Email ID"] == email_ID and i["Password"] == password:
                return True
            else:
                return False
    except json.decoder.JSONDecodeError:
        return False
    finally:
        file.close()
    return False
        
def create_module(filename,module_ID,module_name,start_date,end_date):
    details = {
        "Module ID":module_ID,
        "Module Name":module_name,
        "Start Date":start_date,
        "End Date":end_date
    }

    if os.path.exists(filename) == False:
        file = open(filename,"x")
        print("File got created!")
    else:
        print("File already exist")
        file = open(filename,"r+")

    try:
        data = json.load(file)
        if details not in data:
            data.append(details)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    except json.decoder.JSONDecodeError:
        lst = []
        lst.append(details)
        json.dump(lst,file)
        file.close()
        return True
    return False

def view_module(filename):
    file_data = None
    with open(filename) as file:
        file_data=json.load(file)
    return file_data

def delete_module(filename,module_ID):
    with open(filename,"r+") as file:
        file_data=json.load(file)
       
        for i in range(len(file_data)):
            if file_data[i]["Module ID"]==module_ID:
                file_data.pop(i)

                file.seek(0)
                file.truncate()
                json.dump(file_data,file)
                file.close()
                return True    
    return False

def update_module(filename,module_ID,module_name,start_date,end_date):
    with open(filename,"r+") as file:
        file_data=json.load(file)
        for i in range(len(file_data)):            
            if file_data[i]["Module ID"]==module_ID:
                file_data[i]["Module Name"]=module_name
                file_data[i]["Start Date"]=start_date
                file_data[i]["End Date"]=end_date

                file.seek(0)
                file.truncate()
                json.dump(file_data,file)
                file.close()
                return True

    return False

