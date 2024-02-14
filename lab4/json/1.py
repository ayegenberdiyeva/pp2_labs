import json

# Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.
# Interface Status
# ================================================================================
# DN                                                 Description           Speed    MTU  
# -------------------------------------------------- --------------------  ------  ------
# topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 

f = open("/Users/aminayegenberdiyeva/Projects/pp2/pp2_labs/lab4/json/sample-data.json")

my_dict = json.load(f)

interf = """
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
"""
print(interf, end="")
n = 0

for i in my_dict["imdata"]:

    print(
        i["l1PhysIf"]["attributes"]["dn"],
        "\t\t\t\t",
        i["l1PhysIf"]["attributes"]["descr"],
        i["l1PhysIf"]["attributes"]["speed"],
        i["l1PhysIf"]["attributes"]["mtu"]
        )
    n += 1
    if n == 3:
        break

f.close()

