import json

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
        
