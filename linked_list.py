'''
En vanlig klass för en ända nod i länkade listan 
Anledning inte @dataclass eftersom next-fältet pekar på en annan Node, skulle en auto-genererad __repr__/__eq__ bli rekursiv och oanvändbar
'''
class Node:
    def __init__(self, session):
        self.session = session
        self.next = None


class MonthList:
    def __init__(self):
        self.head = None

    # INFOGA NY SESSION
    def insert(self, session):
        new_node = Node(session) # skapar instans av klassen

        # infoga allra först, använder session dataklassens date attribut
        if self.head is None or session.date < self.head.session.date: 
            new_node.next = self.head # nya noden pekar på gamla head 
            self.head = new_node # head pekar nu på nya noden
            return

        # infogning i mitten eller på slutet
        current = self.head #håll koll på varje nod i listan
        while current.next is not None and current.next.session.date <= session.date:
            current = current.next
        new_node.next = current.next # nya noden pekar på det som current pekade på
        current.next = new_node # current pekar nu på nya noden 

    # TA BORT SESSION
    def remove(self, session):
        # tom lista, inget att ta bort
        if self.head is None:
            return False  

        # specialfall ta bort FÖRSTA noden
        if self.head.session == session:  
            self.head = self.head.next
            return True

        # leta i resten av listan
        current = self.head 
        while current.next is not None:
            if current.next.session == session:
                current.next = current.next.next  # hoppa över den bort tagna noden
                return True
            current = current.next

        return False  # sessionen hittades inte

    # DENNA Functionen gör länkade listan MonthList TRAVERSERBAR, eg så man inte behöver skriva ut hela traverseringen manuellt varje gång
    def __iter__(self): # specialmetoden __iter__
        current = self.head # Skapar en temporär pekare som startar vid första noden 
        while current is not None: # ortsätt så länge vi inte är i slutet
            yield current.session # yield "ger tillbaka", datan som finns lagrad i den aktuella noden
            current = current.next