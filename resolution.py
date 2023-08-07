from to_cnf import to_cnf

# taking input from user 

numFor = int(input("Number of closed formulae : "))
forList = []
for_cnf = []

for x in range(numFor):
    inp = input()
    forList.append(inp)
    cnf = to_cnf(inp,"f")
    for_cnf.append(cnf)

print("Formulae List")
print(forList)

print("Formulae converted to clause list")
print(for_cnf)

query = input("Enter Query : ")
query_cnf = to_cnf(query,"q")

print("Before")
print(for_cnf)
print(query_cnf) 

to_remove = []
for x in for_cnf: 
    if "&" in x : 
        temp = x.split("&")
        to_remove.append(x)
        for y in temp : 
            for_cnf.append(y)
for x in to_remove: 
    for_cnf.remove(x)

if "&" in query_cnf:
    temp = query_cnf.split("&")
    for x in temp[1:]:
        for_cnf.append(x)
    query_cnf = temp[0]

print("After")
print(for_cnf)
print(query_cnf) 

solution = query_cnf
solution = solution.split("|")
solution = [x.strip() for x in solution]
solution = "|".join(solution)

while True:
    print("solution : ", solution)
    
    if (solution == ""):
        print("True")
        break

    cmd = input("")
    if (cmd == "q"):
        break

    else : 
        get_target = solution.split("|")
        target = {}
        for x in  get_target:
            if x[0] == "~":
                target[x[1]] = x
            else :
                target["~" + x[0]] = x
            
            # target = "~" + solution[0]
        for x in for_cnf:
            print(target , x)
            form = x
            change = False
            for lit in target : 
                if lit in form and ("~"+lit) not in form and target[lit] in solution:  

                    change = True
                    
                    form = form.split("|")
                    form = [x.strip() for x in form]
                    print("Lit : ", lit)
                    form.remove(lit)
                    form = "|".join(form)

                    solution = solution.split("|")
                    solution.remove(target[lit])
                    solution = "|".join(solution)
                    print("Form", form)

            if change :
                if len(solution) == 0 : 
                        solution = form
                elif len(form) == 0:
                    pass
                else :
                    solution = solution + "|" + form

            print("Iteration ended : ", solution)
print("Broken, lol")

