from rdflib import Graph, Namespace, RDF, OWL
from owlrl import DeductiveClosure, OWLRL_Semantics

# Ініціалізація онтології
STALKER = Namespace("http://example.org/stalker_game#")

# Створення графу онтології
stalker_ontology = Graph()
stalker_ontology.parse("Stalker.owl", format="xml")  # Завантаження вашої онтології
stalker_ontology.bind("stalker", STALKER)

# Аналіз онтології
def analyze_ontology(graph):
    print("Аналіз онтології:")

    # Підрахунок класів
    class_count = len(list(graph.subjects(RDF.type, OWL.Class)))
    print(f"Кількість класів: {class_count}")

    # Підрахунок об'єктних властивостей
    object_property_count = len(list(graph.subjects(RDF.type, OWL.ObjectProperty)))
    print(f"Кількість об'єктних властивостей: {object_property_count}")

    # Підрахунок властивостей типів даних
    datatype_property_count = len(list(graph.subjects(RDF.type, OWL.DatatypeProperty)))
    print(f"Кількість властивостей типів даних: {datatype_property_count}")

    # Підрахунок екземплярів
    individual_count = len(list(graph.subjects(RDF.type, OWL.NamedIndividual)))
    print(f"Кількість екземплярів: {individual_count}")

# Пошук класів, які мають конкретну властивість
def find_classes_with_property(graph, property_name):
    print(f"\nКласи, що мають властивість '{property_name}':")
    found_classes = set()

    for subject, predicate, obj in graph:
        if str(predicate).endswith(property_name):
            found_classes.add(subject)

    if found_classes:
        for cls in found_classes:
            print(f"Клас: {cls}")
    else:
        print(f"Властивість {property_name} не знайдено в онтології.")

# Додавання обмежень в онтологію
def add_restrictions(graph):
    print("\nДодавання обмежень:")
    new_restriction = (STALKER.MainCharacter, RDF.type, OWL.Restriction)
    graph.add(new_restriction)
    print(f"Додано обмеження: {new_restriction}")

# Перевірка консистентності онтології
def check_consistency(graph):
    print("\nПеревірка консистентності онтології:")
    try:
        DeductiveClosure(OWLRL_Semantics).expand(graph)
        print("Онтологія узгоджена (consistent).")
    except Exception as e:
        print(f"Онтологія неузгоджена: {e}")

# Головна функція
def main():
    analyze_ontology(stalker_ontology)
    find_classes_with_property(stalker_ontology, "usesEquipment")  # Використання властивості usesEquipment
    add_restrictions(stalker_ontology)
    check_consistency(stalker_ontology)

if __name__ == "__main__":
    main()
