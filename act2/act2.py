class Route:
    def __init__(self, name, stops):
        self.name = name
        self.stops = stops

class Rule:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

def match(rule, fact):
    for a in rule.antecedent.split():
        if a not in fact:
            return False
    return True

def deduce(rules, facts):
    new_facts = []
    for rule in rules:
        if match(rule, facts):
            new_facts.append(rule.consequent)
    return new_facts

def resolve(facts, rules):
    new_facts = facts
    while new_facts:
        new_facts = deduce(rules, new_facts)
        facts += new_facts
    return facts

def find_best_route(rules, facts):
    resolved_facts = resolve(facts, rules)
    for fact in resolved_facts:
        if "best_route" in fact:
            return fact.replace("best_route(", "").replace(")", "")

# Define las reglas logicas
rules = [
    Rule("A B", "route_ab"),
    Rule("route_ab route_bc", "best_route(route_ac)"),
    Rule("route_ab route_cd", "best_route(route_ad)"),
]

# Definir las paradas o punto de paradas en el sistema de transporte colectivo
facts = ["A", "B", "C", "D"]

# Encontrar la mejor ruta entre el punto A y el punto D
print(find_best_route(rules, facts))