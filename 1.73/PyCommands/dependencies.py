"""pycmd example"""

DESC="""Find a exported function on the loaded dll"""

import immlib
def usage(imm):
    imm.Log("!dependencies   Find an exported function on the loaded dll")
    imm.Log("!dependencies   module.function")
    imm.Log("ex: !dependencies  rpcrt4.rpcserveruseprotseqw")

def main(args):
    imm=immlib.Debugger()
    if len(args) !=1:
        usage(imm)
        return "Error: Wrong arguments"
        
    result = imm.findDependecies( [ args[0] ] )
    ret = 0
    for modname in result.keys():
        for mod in result[modname]:
            imm.Log("Found: %20s on %s" % (modname, mod.name), address = mod.address)
            ret +=1
    return "Found %d dependencies" % ret