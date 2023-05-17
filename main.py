import sys 
import pprint

sys.path.append('/home/roborobo/HundredFinanceDetector/python-solidity-parser/')

from solidity_parser import parser

sourceUnit = parser.parse_file(sys.argv[1], loc=True)
sourceUnit = parser.objectify(sourceUnit)
# divisions = []
# mods = []
def traverseExpression(exp, divisions, mods):
    if exp == None: return
    if 'operator' in exp:
        if exp.operator == '/':
            divisions.append(exp)
        if exp.operator == '%':
            mods.append(exp)

    if 'left' in exp:
        traverseExpression(exp.left, divisions, mods)

    if 'right' in exp:
        traverseExpression(exp.right, divisions, mods)

def findCriticalIdentifiers(exp, identifiers):
    if exp == None: return
    if exp.type == "Identifier" and "rate" in exp.name.lower():
        if exp.name not in identifiers:
            identifiers.append(exp.name)
    if 'left' in exp:
        findCriticalIdentifiers(exp.left, identifiers)

    if 'right' in exp:
        findCriticalIdentifiers(exp.right, identifiers)


def checkContract(contract):
    for func_name in contract.functions.keys():
        divisions, mods = [], []
        div_identifiers = []
        mod_identifiers = []


        for statement in contract.functions[func_name]._node.body.statements:
            
            if statement.type == "ExpressionStatement":
                if statement.expression.type == "BinaryOperation":
                    traverseExpression(statement.expression, divisions, mods)
                    for div in divisions: 
                        findCriticalIdentifiers(div, div_identifiers)
                    for mod in mods:
                        findCriticalIdentifiers(mod, mod_identifiers)
                    
        for div_id in div_identifiers:
            if div_id not in mod_identifiers:
                print(f"[Warning]Do not use the division operation on rate-like quantities without modding them first to prevent rounding errors: variable: {div_id}, line: {statement.loc}")


contract_names = sourceUnit.contracts.keys()

for name in contract_names:
    checkContract(sourceUnit.contracts[name])
