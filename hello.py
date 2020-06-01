import xmltodict
my_xml = {"name":"nandu"}

my_dict = xmltodict.unparse(my_xml)
print(my_dict)