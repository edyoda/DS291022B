# xml 

# extension - .xml
# eXtensible markup language

# xml tags are not predefined <>
# we have to create our own tags

"""
<students>
    <student>
        <rno>1</rno>
        <name>Raj</name>
    </student>
    <student>
        <rno>2</rno>
        <name>Ram</name>
    </student>
</students>
"""

students ={
    "student" : [
        {"rno":1,"name":"Raj"},
        {"rno":2,"name":"Ram"}
    ]
}

# Rules
# 1. There should be a root tag
# 2. case sensitive
# 3. if you have started a tag then must end it