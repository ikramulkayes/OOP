from prettytable import PrettyTable
import prettytable

table = PrettyTable()
table.add_column("Agents",["Jet","Killjoy","Cypher"])
table.add_column("Ultimate",["Blade Storm","Lock Down","Neuro Theft"])
table.align = "l" #change the allignment
print(table)