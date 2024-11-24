# THIS SOLUTION WAS PROVIDED FROM CHATGPT - replace with programmer solution when obtained

from collections import deque

def find_erdos_number(collaborations, target_researcher):
    # Create a graph of collaborations
    graph = {}
    for researcher1, researcher2 in collaborations:
        if researcher1 not in graph:
            graph[researcher1] = []
        if researcher2 not in graph:
            graph[researcher2] = []
        graph[researcher1].append(researcher2)
        graph[researcher2].append(researcher1)

    # Initialize BFS variables
    queue = deque([("Paul Erdős", 0, "P")])  # (current researcher, Erdős number, path)
    visited = set()

    while queue:
        current_researcher, erdos_number, path = queue.popleft()

        if current_researcher in visited:
            continue

        visited.add(current_researcher)

        # Check if we've found the target researcher
        if current_researcher == target_researcher:
            return f"{erdos_number}{path}"

        # Add neighbors to the queue
        for neighbor in graph[current_researcher]:
            if neighbor not in visited:
                queue.append((neighbor, erdos_number + 1, path + neighbor[0]))

    # If the target researcher is not connected to Paul Erdős
    return "Not connected"

# Example usage
collaborations = [
    ("Paul Erdős", "Alice"),
    ("Derek", "Nolan"),
    ("Bob", "Homse"),
    ("Charlie", "David"),
    ("George", "Bobby"),
    ("Alice", "Bob"),
    ("Bobby", "Charlie"),
    ("Caroline", "David"),
    ("Arthur", "Alfred"),
    ("Paul", "Steven"),
    ("Bob", "Bruce"),
    ("Charlie", "David"),
    ("Harry", "Matthieu"),
    ("Jiji", "Alice"),
    ("David", "Hank"),
    ("Bruce", "Frank"),
    ("Alfred", "George"),
    ("Bob", "Homse"),
    ("Carolyn", "Davies"),
    ("George", "Bobby"),
    ("Nolon", "John"),
    ("Kay", "Charlie"),
    ("Matthew", "Frank"),
    ("Lula", "Robert"),
    ("Charlie", "Jiji"),
    ("Alice", "George"),
    ("Serena", "Frank"),
    ("Timothy", "Jacob"),
    ("Richard", "Rob"),
    ("Eda", "Raymond"),
    ("George", "Bobby"),
    ("Nolon", "John"),
    ("Kay", "Charlie"),
    ("Roy", "Eda"),
    ("Lula", "Robert"),
    ("Charlie", "Jiji"),
    ("Alice", "George"),
    ("Serena", "Frank"),
    ("Timothy", "Jacob"),
    ("Richard", "Rob"),
    ("Edmund", "Arthur"),
    ("Coco", "Alfred"),
    ("Luna", "Noel"),
    ("Kay", "Nolan"),
    ("Luna", "Homse"),
    ("Mike", "Bob"),
    ("Carol", "Serena"),
    ("Peter", "Kimberly"),
    ("Nolan", "Luna"),
    ("Alice", "Derek"),
    ("David", "Kim"),
    ("Susan", "John"),
    ("Susan", "Geoff"),
    ("Bob", "Frank"),
    ("Rene", "Carolyn"),
    ("Lucy", "Alfred"),
    ("Luna", "Noel"),
    ("Kay", "Derek"),
    ("Olympia", "Eve"),
    ("Aiden", "Rob"),
    ("Homse", "Bruce"),
    ("Peter", "Luna"),
    ("Derek", "Luna"),
    ("Peter", "Susan"),
    ("Kimberly", "Bob"),
    ("Homse", "Serena"),
    ("Rob", "Paul"),
    ("Nolan", "Luna"),
    ("Alice", "Derek"),
    ("Grace", "Aiden"),
    ("Bob", "Bruce"),
    ("Grace", "Geoff"),
    ("Winona", "Brook"),
    ("Jiji", "Homse"),
    ("David", "Hank"),
    ("Bruce", "Frank"),
    ("Brook", "Alicia"),
    ("George", "Frank"),
    ("Bobby", "Charlie"),
    ("Richard", "Frank"),
    ("Frank", "Coco"),
    ("Charlie", "Matt"),
    ("Alice", "George"),
    ("Mattie", "Matt"),
    ("Kiki", "Jacob"),
    ("David", "Hank"),
    ("Martha", "Raymond"),
    ("Shirley", "Raymond"),
    ("George", "Frank"),
    ("Bobby", "Charlie"),
    ("Charles", "Roy"),
    ("Frank", "Coco"),
    ("Charlie", "Matt"),
    ("Alice", "George"),
    ("Mattie", "Matt"),
    ("Kiki", "Jacob"),
    ("Shirley", "Llyod"),
    ("Edmund", "Mattie"),
    ("Coco", "Alfred"),
    ("Luna", "Matthieu"),
    ("Kay", "Nolan"),
    ("Kiki", "Homse"),
    ("John", "Bob"),
    ("Nolan", "Bob"),
    ("Bobby", "Charlie"),
    ("Caroline", "David"),
    ("Chad", "Nolon"),
    ("Paul", "Steven"),
    ("Nolan", "Bruce"),
    ("Charles", "Cookie"),
    ("Caroline", "David"),
    ("Arthur", "Alfred"),
    ("Paul", "Steven"),
    ("Bob", "Bruce"),
    ("Cynthia", "Clayton"),
    ("Harry", "Matthieu"),
    ("Jiji", "Alice"),
    ("Andres", "Kayden"),
    ("Nolan", "Frank"),
    ("Alfred", "George"),
    ("Nolon", "Kayden"),
    ("Timothy", "David"),
    ("Abigail", "Bobby"),
    ("Cathy", "Clayton"),
    ("Richard", "Frank"),
    ("Frank", "Coco"),
    ("Charlie", "Matt"),
    ("Alice", "George"),
    ("Mattie", "Matt"),
    ("Abigail", "Brook"),
    ("Richard", "Rob"),
    ("Edmund", "Mattie"),
    ("Coco", "Alfred"),
    ("Luna", "Matthieu"),
    ("Kay", "Nolan"),
    ("Kiki", "Homse"),
    ("Brock", "Bob"),
    ("Nolan", "Bob"),
    ("Bobby", "Charlie"),
    ("Brook", "Rosita"),
    ("Chad", "Brock"),
    ("Abigail", "Rene"),
    ("Nolan", "Bruce"),
    ("Bobby", "Charlie"),
    ("Rosita", "Davies"),
    ("George", "Bobby"),
    ("Lula", "Barbara"),
    ("Bobby", "Charlie"),
    ("Caroline", "David"),
    ("Arthur", "Alfred"),
    ("Paul", "Steven"),
    ("Bob", "Bruce"),
    ("Rosita", "Jose"),
    ("Harry", "Matthieu"),
    ("Jiji", "Alice"),
    ("Ricky", "Jose"),
    ("Bruce", "Frank"),
    ("Alfred", "George"),
    ("Rick", "Homse"),
    ("Cathy", "Jose"),
    ("Cynthia", "Aida"),
    ("Edmund", "Mattie"),
    ("Coco", "Alfred"),
    ("Luna", "Matthieu"),
    ("Kay", "Nolan"),
    ("Kiki", "Homse"),
    ("Brock", "Bob"),
    ("Raymond", "Nelson"),
    ("Nelson", "Irma"),
    ("Brook", "Rosita"),
    ("Aida", "Lula"),
    ("Abigail", "Rene"),
    ("Nolan", "Bruce"),
    ("Bobby", "Charlie"),
    ("Rosita", "Davies"),
    ("George", "Bobby"),
    ("Barbara", "Raymond"),
    ('Bodhi', 'Tulip'),
    ('Clair', 'Drayden'),
    ('Jasmine', 'Gordie'),
    ('Wally', 'Cookie'),
    ('Ryme', 'Lana'),
    ('Katy', 'Clay'),
    ('Rowan', 'Tate'),
    ('Brycen', 'Fantina'),
    ('Ryme', 'Bodhi'),
    ('Morty', 'Clara'),
    ('Erika', 'Lisa'),
    ('Chuck', 'Ramos'),
    ('Chili', 'Ernest'),
    ('Flannery', 'Melony'),
    ('Blaine', 'Viola'),
    ('Gordie', 'Lenora'),
    ('Falkner', 'Nathan'),
    ('Sabrina', 'Bryon'),
    ('Grusha', 'Raleigh'),
    ('Bryon', 'Blaine'),
    ('Norman', 'Clemont'),
    ('Ryme', 'Olympia'),
    ('Pryce', 'Drayden'),
    ('Skyla', 'Poppy'),
    ('Jack', 'Drayden'),
    ('Bodhi', 'Reed'),
    ('Tate', 'Gilbert'),
    ('Ernest', 'Grusha'),
    ('Shane', 'Maisie'),
    ('Ember', 'Kahili'),
    ('Allister', 'Wally'),
    ('Iona', 'Brawly'),
    ('Grusha', 'Ember'),
    ('Sophocles', 'Sophocles'),
    ('Melony', 'Ilima'),
    ('Kabu', 'Shane'),
    ('William', 'Lisa'),
    ('Landon', 'Giovanni'),
    ('Sophocles', 'Tulip'),
    ('Avery', 'Olympia'),
    ('Viola', 'Bea'),
    ('Flannery', 'Betsy'),
    ('Hala', 'Milo'),
    ('Reed', 'Giovanni'),
    ('Clemont', 'Brycen'),
    ('Drayden', 'Ramos'),
    ('Falkner', 'Wattson'),
    ('Wallace', 'Allister'),
    ('Candice', 'Grusha'),
    ('Bugsy', 'Melony'),
    ('Blaine', 'Sophocles'),
    ('Landon', 'Ilima'),
    ('Koga', 'Bea'),
    ('Olympia', 'Viola'),
    ('Avery', 'Wallace'),
    ('Sophocles', 'Skyla'),
    ('Sophocles', 'Opal'),
    ('Geeta', 'Gardenia'),
    ('Lisa', 'Misty'),
    ('Ernest', 'Cress'),
    ('Jasmine', 'Volkner'),
    ('Tulip', 'Drayden'),
    ('Brawly', 'Lt. Surge'),
    ('Bryon', 'Fantina'),
    ('Wulfric', 'Elesa'),
    ('Sophocles', 'Kiawe'),
    ('Candice', 'Brassius'),
    ('Brycen', 'Roark'),
    ('Kiawe', 'Geeta'),
    ('Viola', 'Blaine'),
    ('Bugsy', 'Ernest'),
    ('Candice', 'Kabu'),
    ('Fantina', 'Zephyr'),
    ('Maisie', 'Bryon'),
    ('Grant', 'Jasmine'),
    ('Chuck', 'Viola'),
    ('Viola', 'Hassel'),
    ('Clair', 'Drayden'),
    ('Landon', 'Avery'),
    ('Poppy', 'Landon'),
    ('Rory', 'Poppy'),
    ('Saffron', 'Evander'),
    ('Gardenia', 'Elesa'),
    ('Elesa', 'Jasmine'),
    ('Betsy', 'Cilan'),
    ('Brawly', 'Hala'),
    ('Lana', 'Blaine'),
    ('Jack', 'Chuck'),
    ('Viola', 'Valerie'),
    ('Ramos', 'Wulfric'),
    ('Evander', 'Grusha'),
    ('Jasmine', 'Hazel'),
    ('Flannery', 'Kabu'),
    ('Cress', 'Brycen'),
    ('Kiawe', 'Billy'),
    ('Skyla', 'Giovanni'),
    ('Zephyr', 'Rowan'),
    ('Wattson', 'William'),
    ('Ryme', 'Rory'),
    ('Acerola', 'Shane'),
    ('Sophocles', 'Blaine'),
    ('Bugsy', 'Ramos'),
    ('Zephyr', 'Ryme'),
    ('Misty', 'Sophocles'),
    ('Morty', 'Roxanne'),
    ('Opal', 'Nathan'),
    ('Kofu', 'Gilbert'),
    ('Chili', 'Cilan'),
    ('Bodhi', 'Wattson'),
    ('Brassius', 'Brawly'),
    ('Flannery', 'Grusha'),
    ('Saffron', 'Lisa'),
    ('Skyla', 'Valerie'),
    ('Cress', 'Gilbert'),
    ('Brawly', 'Gardenia'),
    ('Chili', 'Roark'),
    ('Ember', 'Zephyr'),
    ('Melony', 'Bodhi'),
    ('Brassius', 'Candice'),
    ('Gordie', 'Tulip'),
    ('Jack', 'Lt. Surge'),
    ('Clay', 'Rowan'),
    ('William', 'Cilan'),
    ('Bea', 'Lenora'),
    ('Viola', 'Fantina'),
    ('Brassius', 'Milo'),
    ('Erika', 'Kabu'),
    ('William', 'Wattson'),
    ('Elesa', 'Elesa'),
    ('Kiawe', 'Brawly'),
    ('Sophocles', 'Wattson'),
    ('Erika', 'Ember'),
    ('Gardenia', 'Chuck'),
    ('Roxanne', 'Skyla'),
    ('Hazel', 'Melony'),
    ('Lana', 'Grusha'),
    ('Raleigh', 'Falkner'),
    ('Viola', 'Roxanne'),
    ('Candice', 'Norman'),
    ('Roxanne', 'Jack'),
    ('Olympia', 'Brycen'),
    ('Hazel', 'Hassel'),
    ('Brassius', 'Wattson'),
    ('Misty', 'Gordie'),
    ('Bryon', 'Gilbert'),
    ('Gardenia', 'Burgh'),
    ('Reed', 'Pryce'),
    ('Roark', 'William'),
    ('Pryce', 'William'),
    ('Burgh', 'Ramos'),
    ('Raleigh', 'Brycen'),
    ('Grusha', 'Katy'),
    ('Ramos', 'Olympia'),
    ('Misty', 'Milo'),
    ('Sophocles', 'Korrina'),
    ('Fantina', 'Viola'),
    ('Blaine', 'Milo'),
    ('Iona', 'Nathan'),
    ('Tulip', 'Kofu'),
    ('Morty', 'Sabrina'),
    ('Drayden', 'Nathan'),
    ('Bodhi', 'Ilima'),
    ('Gilbert', 'Milo'),
    ('Chili', 'Viola'),
    ('Milo', 'Kabu'),
    ('Korrina', 'Brycen'),
    ('Koga', 'Chuck'),
    ('Hala', 'Grusha'),
    ('Cress', 'Reed'),
    ('Lisa', 'Korrina'),
    ('Saffron', 'Kahili'),
    ('Hala', 'Gardenia'),
    ('Jack', 'Brassius'),
    ('Roxanne', 'Kiawe'),
    ('Opal', 'Brassius'),
    ('Olympia', 'Gilbert'),
    ('Sabrina', 'Viola'),
    ('Sophocles', 'Larry'),
    ('Bodhi', 'Clay'),
    ('Roark', 'Norman'),
    ('Nessa', 'Clair'),
    ('Hazel', 'Saffron'),
    ('Clemont', 'Cilan'),
    ('Cress', 'Rowan'),
    ('Jack', 'Sophocles'),
    ('Kahili', 'Erika'),
    ('Roxanne', 'Korrina'),
    ('Kofu', 'Cilan'),
    ('Brassius', 'Grant'),
    ('Roxanne', 'Hazel'),
    ('Tulip', 'Clemont'),
    ('Morty', 'Kahili'),
    ('Evander', 'Fantina'),
    ('Ilima', 'Evander'),
    ('Tate', 'Elesa'),
    ('Viola', 'Nathan'),
    ('Korrina', 'Lisa'),
    ('Hassel', 'Evander'),
    ('Olympia', 'Elesa'),
    ('Geeta', 'Viola'),
    ('Brycen', 'Nathan'),
    ('Koga', 'Bryon'),
    ('Candice', 'Clemont'),
    ('Clemont', 'Kabu'),
    ('Giovanni', 'Roark'),
    ('Grusha', 'Hala'),
    ('Clay', 'Grusha'),
    ('Lt. Surge', 'Roxanne'),
    ('Giovanni', 'Pryce'),
    ('Korrina', 'Roxanne'),
    ('Elesa', 'Morty'),
    ('Jasmine', 'Hala'),
    ('Ilima', 'Elesa'),
    ('Opal', 'Misty'),
    ('Maisie', 'Sabrina'),
    ('Viola', 'Milo'),
    ('Gilbert', 'Hazel'),
    ('Reed', 'Hazel'),
    ('Drayden', 'Hala'),
    ('Sabrina', 'Gardenia'),
    ('Flannery', 'Milo'),
    ('Falkner', 'Grant'),
    ('Nessa', 'Wattson'),
    ('Pryce', 'Korrina'),
    ('Billy', 'Roxanne'),
    ('Brycen', 'Acerola'),
    ('Hazel', 'Melony'),
    ('Blaine', 'Clair'),
    ('Kofu', 'Grant'),
    ('Milo', 'Gordie'),
    ('Korrina', 'Kofu'),
    ('Acerola', 'Hala'),
    ('Acerola', 'Gilbert'),
    ('Koga', 'Roark'),
    ('Pryce', 'Olympia'),
    ('Olympia', 'Tate'),
    ('Volkner', 'Acerola'),
    ('Jack', 'Viola'),
    ('William', 'Kiawe'),
    ('Pryce', 'Olympia'),
    ('Bodhi', 'Wattson'),
    ('Bugsy', 'Bugsy'),
    ('Nessa', 'Tate'),
    ('William', 'Raleigh'),
    ('Olympia', 'Saffron'),
    ('Ernest', 'Bodhi'),
    ('Acerola', 'Olympia'),
    ('Reed', 'Evander'),
    ('Reed', 'Evander'),
    ('Bea', 'Reed'),
    ('Raleigh', 'Hala'),
    ('Candice', 'Kabu'),
    ('Rowan', 'Opal'),
    ('Nathan', 'Roxanne'),
    ('Geeta', 'Bryon'),
    ('Sophocles', 'Pryce'),
    ('Clay', 'William'),
    ('Katy', 'Nathan'),
    ('Gordie', 'Chuck'),
    ('Betsy', 'Burgh'),
    ('Katy', 'Clair'),
    ('Bea', 'Roark'),
    ('Lana', 'Cress'),
    ('Roxanne', 'Kabu'),
    ('Jasmine', 'Ilima'),
    ('Wulfric', 'Jasmine'),
    ('Nathan', 'Olympia'),
    ('Betsy', 'Viola'),
    ('Grant', 'Olympia'),
    ('Raleigh', 'Clay'),
    ('Larry', 'Geeta'),
    ('Lenora', 'Valerie'),
    ('Kiawe', 'Cilan'),
    ('Korrina', 'Kabu'),
    ('Larry', 'Billy'),
    ('Hazel', 'Viola'),
    ('Brawly', 'Milo'),
    ('Ernest', 'Volkner'),
    ('Misty', 'Viola'),
    ('Gardenia', 'Clemont'),
    ('Melony', 'Misty'),
    ('Skyla', 'Bea'),
    ('Grant', 'Geeta'),
    ('Volkner', 'Blaine'),
    ('Brycen', 'Bea'),
    ('Kofu', 'Evander'),
    ('Milo', 'Cress'),
    ('Misty', 'Brassius'),
    ('Olympia', 'Reed'),
    ('Hassel', 'Ramos'),
    ('Roxanne', 'Candice'),
    ('Viola', 'Clemont'),
    ('Gardenia', 'Raleigh'),
    ('Hazel', 'Larry'),
    ('Clair', 'Nathan'),
    ('Chili', 'Brassius'),
    ('Grant', 'Larry'),
    ('Betsy', 'Rowan'),
    ('Clair', 'Roxanne'),
    ('Gordie', 'Pryce'),
    ('Sabrina', 'Ernest'),
    ('Opal', 'Raleigh'),
    ('Viola', 'Bodhi'),
    ('Volkner', 'Brassius'),
    ('Betsy', 'Clara'),
    ('Lana', 'Lana'),
    ('Hala', 'Roxanne'),
    ('Tate', 'Falkner'),
    ('Billy', 'Tulip'),
    ('Giovanni', 'Wulfric'),
    ('Brawly', 'Chili'),
    ('Burgh', 'Brycen'),
    ('Burgh', 'Nessa'),
    ('Iona', 'Hazel'),
    ('Cress', 'Nessa'),
    ('Acerola', 'Hala'),
    ('Skyla', 'William'),
    ('Roark', 'Clair'),
    ('Lana', 'Wattson'),
    ('Iona', 'Katy'),
    ('Tate', 'Kiawe'),
    ('Volkner', 'Jack'),
    ('Blaine', 'Bodhi'),
    ('William', 'Roark'),
    ('Nathan', 'Gordie'),
    ('Katy', 'Iona'),
    ('Lana', 'Bodhi'),
    ('Mallow', 'Milo'),
    ('Brassius', 'Hassel'),
    ('Misty', 'Volkner'),
    ('Larry', 'Roxanne'),
    ('Betsy', 'Jack'),
    ('Falkner', 'Nessa'),
    ('Lt. Surge', 'Viola'),
    ('Korrina', 'Chuck'),
    ('Geeta', 'Bodhi'),
    ('Kofu', 'Wattson'),
    ('Korrina', 'Hala'),
    ('Acerola', 'Billy'),
    ('Chili', 'Tate'),
    ('Bea', 'Misty'),
    ('Ramos', 'Nathan'),
    ('Brassius', 'Tulip'),
    ('Bugsy', 'William'),
    ('Cress', 'Sophocles'),
    ('Olympia', 'Viola'),
    ('Reed', 'Betsy'),
    ('Gardenia', 'Tulip'),
    ('Sophocles', 'Hassel'),
    ('Pryce', 'Acerola'),
    ('Nathan', 'Giovanni'),
    ('Kiawe', 'Grant'),
    ('Lana', 'Nathan'),
    ('Ernest', 'Milo'),
    ('Kofu', 'Acerola'),
    ('Wattson', 'Koga'),
    ('Blaine', 'Blaine'),
    ('Blaine', 'Maisie'),
    ('Bodhi', 'Lana'),
    ('Sabrina', 'Volkner'),
    ('Sophocles', 'Kofu'),
    ('Viola', 'Korrina'),
    ('Mallow', 'Ernest'),
    ('Gardenia', 'Iona'),
    ('Blaine', 'Billy'),
    ('Drayden', 'Gardenia'),
    ('Larry', 'Pryce'),
    ('Viola', 'Melony'),
    ('Shane', 'Hazel'),
    ('Norman', 'Kiawe'),
    ('Hala', 'Bugsy'),
    ('Gardenia', 'Chuck'),
    ('Fantina', 'Brassius'),
    ('Flannery', 'Norman'),
    ('Wattson', 'Viola'),
    ('Flannery', 'Melony'),
    ('Hazel', 'Volkner'),
    ('Grant', 'Hala'),
    ('Melony', 'Iona'),
    ('Maisie', 'Ernest'),
    ('Grant', 'Betsy'),
    ('Larry', 'Hazel'),
    ('Drayden', 'Drayden'),
    ('Hala', 'Mallow'),
    ('Gardenia', 'Katy'),
    ('Misty', 'Clair'),
    ('Skyla', 'Volkner'),
    ('Gardenia', 'Lenora'),
    ('Maisie', 'William'),
    ('Norman', 'Roark'),
    ('Misty', 'Hassel'),
    ('Brawly', 'Iona'),
    ('Wattson', 'Chili'),
    ('Gilbert', 'Clara'),
    ('Norman', 'Wattson'),
    ('Kiawe', 'Evander'),
    ('Roxanne', 'Kofu'),
    ('Bugsy', 'Blaine'),
    ('Flannery', 'Iona'),
    ('Clay', 'Chuck'),
    ('Hala', 'Melony'),
    ('Melony', 'Hazel'),
    ('Gilbert', 'Pryce'),
    ('Mallow', 'Lisa'),
    ('Reed', 'Roxanne'),
    ('Candice', 'Ernest'),
    ('Kabu', 'Hala'),
    ('Drayden', 'Ernest'),
    ('Chili', 'Billy'),
    ('Skyla', 'Bodhi'),
    ('Ramos', 'Hala'),
    ('Viola', 'Gardenia'),
    ('Olympia', 'Maisie'),
    ('Drayden', 'Evander'),
    ('Ernest', 'Evander'),
    ('Koga', 'Betsy'),
    ('Sophocles', 'Clemont'),
    ('Hassel', 'Hala'),
    ('Tate', 'Chuck'),
    ('Kiawe', 'Candice'),
    ('Jack', 'Ernest'),
    ('Fantina', 'Larry'),
    ('Gilbert', 'Geeta'),
    ('Chuck', 'Hassel'),
    ('Chili', 'Acerola'),
    ('Valerie', 'Brassius'),
    ('Volkner', 'Gordie'),
    ('Rowan', 'Larry'),
    ('Kofu', 'Bea'),
    ('Norman', 'Hassel'),
    ('Burgh', 'Katy'),
    ('Valerie', 'Tate'),
    ('Candice', 'Kiawe'),
    ('Clara', 'Clair'),
    ('Drayden', 'Volkner'),
    ('Opal', 'Evander'),
    ('Flannery', 'Rowan'),
    ('Hala', 'Gardenia'),
    ('Ernest', 'Olympia'),
    ('Shane', 'Ernest'),
    ('William', 'Blaine'),
    ('Fantina', 'Burgh'),
    ('Lt. Surge', 'Grant'),
    ('Hassel', 'Clemont'),
    ('Flannery', 'Chili'),
    ('Tate', 'Kabu'),
    ('Lisa', 'Hala'),
    ('Gardenia', 'Rowan'),
    ('Falkner', 'Roark'),
    ('Candice', 'Skyla'),
    ('Grusha', 'Candice'),
    ('Hala', 'Nessa'),
    ('Larry', 'Billy'),
    ('Tate', 'William'),
    ('Wattson', 'Grusha'),
    ('Pryce', 'Gordie'),
    ('Clara', 'Lt. Surge'),
    ('Roark', 'Opal'),
    ('Katy', 'Korrina'),
    ('Roxanne', 'Viola'),
    ('Gilbert', 'Drayden'),
    ('Katy', 'Lt. Surge'),
    ('Ernest', 'Roxanne'),
    ('Grant', 'Bea'),
    ('Sophocles', 'Cilan'),
    ('William', 'Burgh'),
    ('Hala', 'Hazel'),
    ('Jack', 'Katy'),
    ('Kiawe', 'Ernest'),
    ('Larry', 'Wattson'),
    ('Jack', 'Brassius'),
    ('Betsy', 'Viola'),
    ('Gordie', 'Cress'),
    ('Valerie', 'Gilbert'),
    ('Bea', 'Brawly'),
    ('Tulip', 'Shane'),
    ('Evander', 'Drayden'),
    ('Jack', 'Pryce'),
    ('Viola', 'Hassel'),
    ('Acerola', 'Milo'),
    ('Bea', 'Evander'),
    ('Acerola', 'Bugsy'),
    ('Fantina', 'Blaine'),
    ('William', 'Grant'),
    ('Roark', 'Bugsy'),
    ('Sabrina', 'Roxanne'),
    ('Roxanne', 'Flannery'),
    ('Viola', 'Bugsy'),
    ('Bugsy', 'Milo'),
    ('Koga', 'Sophocles'),
    ('Milo', 'Saffron'),
    ('Clair', 'Volkner'),
    ('Tate', 'Raleigh'),
    ('Cress', 'Korrina'),
    ('Reed', 'Clair'),
    ('Tate', 'Billy'),
    ('Milo', 'Larry'),
    ('Mallow', 'Gordie'),
    ('Chuck', 'Milo'),
    ('Fantina', 'William'),
    ('Hala', 'Hala'),
    ('Lenora', 'Clara'),
    ('Gardenia', 'Brawly'),
    ('Clemont', 'Clair'),
    ('Brycen', 'Lenora'),
    ('Sabrina', 'Shane'),
    ('Fantina', 'Kiawe'),
    ('Gardenia', 'Brawly'),
    ('Ernest', 'Tulip'),
    ('Misty', 'Betsy'),
    ('Brycen', 'Reed'),
    ('Brassius', 'Kofu'),
    ('Brawly', 'Maisie'),
    ('Bryon', 'Shane'),
    ('Drayden', 'Hala'),
    ('Olympia', 'Volkner'),
    ('Lenora', 'Drayden'),
    ('Clemont', 'Norman'),
    ('Korrina', 'Drayden'),
    ('Roark', 'Clemont'),
    ('Korrina', 'Chuck'),
    ('Tate', 'Misty'),
    ('Hazel', 'Iona'),
    ('William', 'Bea'),
    ('Cress', 'Lenora'),
    ('Bugsy', 'Clay'),
    ('Gardenia', 'Cress'),
    ('Misty', 'Olympia'),
    ('Jack', 'Cress'),
    ('Clara', 'Nessa'),
    ('Sophocles', 'Fantina'),
    ('Evander', 'Maisie'),
    ('Shane', 'Ernest'),
    ('Hassel', 'Hassel'),
    ('Koga', 'Katy'),
    ('Betsy', 'Saffron'),
    ('Clair', 'Valerie'),
    ('William', 'Kofu'),
    ('Lisa', 'Grant'),
    ('Gordie', 'Evander'),
    ('Blaine', 'Maisie'),
    ('Volkner', 'Kiawe'),
    ('Clemont', 'Kabu'),
    ('Hazel', 'Iona'),
    ('Hazel', 'Katy'),
    ('Brassius', 'Falkner'),
    ('Reed', 'Shane'),
    ('Norman', 'Brawly'),
    ('Viola', 'Blaine'),
    ('Ernest', 'Ramos'),
    ('Cress', 'Hala'),
    ('William', 'Sabrina'),
    ('Viola', 'Clay'),
    ('Koga', 'Blaine'),
    ('Roark', 'Volkner'),
    ('Gordie', 'Clara'),
    ('Lt. Surge', 'Bugsy'),
    ('Katy', 'Korrina'),
    ('Falkner', 'Raleigh'),
    ('Nessa', 'Norman'),
    ('Bea', 'Rowan'),
    ('Kabu', 'Reed'),
    ('Gilbert', 'Chili'),
    ('Gardenia', 'Shane'),
    ('Geeta', 'Tate'),
    ('Misty', 'Pryce'),
    ('Bea', 'Valerie'),
    ('Betsy', 'Jack'),
    ('Fantina', 'Gilbert'),
    ('Koga', 'Jack'),
    ('Billy', 'Geeta'),
    ('Opal', 'Blaine'),
    ('Betsy', 'Flannery'),
    ('Nessa', 'Hazel'),
    ('Jack', 'Pryce'),
    ('Betsy', 'Ernest'),
    ('Gardenia', 'Viola'),
    ('Geeta', 'Bryon'),
    ('Tate', 'Roxanne'),
    ('Melony', 'Bea'),
    ('Pryce', 'Kofu'),
    ('Bugsy', 'Viola'),
    ('Saffron', 'Brawly'),
    ('Lenora', 'Flannery'),
    ('Hazel', 'Betsy'),
    ('Reed', 'Maisie'),
    ('Volkner', 'Volkner'),
    ('Shane', 'Maisie'),
    ('Brawly', 'Hala'),
    ('Blaine', 'Katy'),
    ('Mallow', 'Cilan'),
    ('Koga', 'Kabu'),
    ('Clemont', 'Viola'),
    ('Norman', 'Pryce'),
    ('Fantina', 'Blaine'),
    ('Lisa', 'Bryon'),
    ('Melony', 'Volkner'),
    ('Gilbert', 'Fantina'),
    ('Clemont', 'Viola'),
    ('Iona', 'Roxanne'),
    ('Kiawe', 'Lenora'),
    ('Olympia', 'Bea'),
    ('Ernest', 'Ramos'),
    ('Falkner', 'Gordie'),
    ('Hala', 'Valerie'),
    ('Bugsy', 'Cilan'),
    ('Clemont', 'Drayden'),
    ('Lenora', 'Falkner'),
    ('Cress', 'Hassel'),
    ('Cilan', 'Gilbert'),
    ('Evander', 'Betsy'),
    ('William', 'Cilan'),
    ('Norman', 'Betsy'),
    ('Burgh', 'Norman'),
    ('Viola', 'Tulip'),
    ('Olympia', 'Flannery'),
    ('Burgh', 'Grant'),
    ('Pryce', 'Clay'),
    ('Kabu', 'Lisa'),
    ('Geeta', 'Clay'),
    ('Clara', 'Bea'),
    ('Flannery', 'Drayden'),
    ('Hazel', 'Shane'),
    ('Gardenia', 'Clay'),
    ('Clara', 'Chili'),
    ('Billy', 'Hassel'),
    ('Grant', 'Gardenia'),
    ('Lenora', 'Acerola'),
    ('Cress', 'Viola'),
    ('Clay', 'Billy'),
    ('Geeta', 'Hassel'),
    ('Cress', 'William'),
    ('Betsy', 'Saffron'),
    ('Gordie', 'Chili'),
    ('Gardenia', 'Lenora'),
    ('Bugsy', 'Viola'),
    ('Olympia', 'Nessa'),
    ('Lenora', 'Jack'),
    ('Olympia', 'Kiawe'),
    ('Hassel', 'Brycen'),
    ('Gordie', 'Ernest'),
    ('Lt. Surge', 'Hala'),
    ('Reed', 'Tate'),
    ('Rowan', 'Pryce'),
    ('Kabu', 'Hala'),
    ('Tate', 'Clara'),
    ('Geeta', 'Kabu'),
    ('Iona', 'Chili'),
    ('Raleigh', 'Bugsy'),
    ('Ernest', 'Clair'),
    ('Tate', 'Kofu'),
    ('Mallow', 'Flannery'),
    ('Gardenia', 'Iona'),
    ('Saffron', 'Opal'),
    ('Drayden', 'Evander'),
    ('Brassius', 'Grant'),
    ('Melony', 'Ramos'),
    ('Flannery', 'Kabu'),
    ('Kabu', 'Mallow'),
    ('Bryon', 'Chili'),
    ('Olympia', 'Viola'),
    ('Brycen', 'Olympia'),
    ('Clay', 'Gardenia'),
    ('Hassel', 'Reed'),
    ('Brycen', 'Cress'),
    ('Billy', 'Roark'),
    ('Iona', 'Brycen'),
    ('Mallow', 'Grant'),
    ('Grant', 'Ramos'),
    ('Bea', 'Bugsy'),
    ('Rowan', 'Lisa'),
    ('Viola', 'Ernest'),
    ('Kofu', 'Clay'),
    ('Kabu', 'Falkner'),
    ('Lt. Surge', 'Mallow'),
    ('Viola', 'Kofu'),
    ('Saffron', 'Kiawe'),
    ('Falkner', 'Burgh'),
    ('Tulip', 'Bryon'),
    ('Misty', 'Sabrina'),
    ('Billy', 'Clemont'),
    ('Flannery', 'Norman'),
    ('Hazel', 'Falkner'),
    ('Lt. Surge', 'Viola'),
    ('Clay', 'Roark'),
    ('Shane', 'Hala'),
    ('Olympia', 'Tate'),
    ('Rowan', 'Kabu'),
    ('Bryon', 'Volkner'),
    ('Gordie', 'Tate'),
    ('Ramos', 'Bugsy'),
    ('Grant', 'Geeta'),
    ('Lisa', 'Ernest'),
    ('Kabu', 'Volkner'),
    ('Reed', 'Kabu'),
    ('Rowan', 'Chili'),
    ('Chili', 'Gordie'),
    ('Falkner', 'Iona'),
    ('Bea', 'Norman'),
    ('Viola', 'Jack'),
    ('Sophocles', 'Lt. Surge'),
    ('Maisie', 'Gordie'),
    ('Billy', 'Brawly'),
    ('Nessa', 'Saffron'),
    ('Evander', 'Sophocles'),
    ('Jack', 'Opal'),
    ('Tate', 'Maisie'),
    ('Misty', 'Lenora'),
    ('Burgh', 'Ernest'),
    ('Volkner', 'Billy'),
    ('Jack', 'Clemont'),
    ('Kiawe', 'Norman'),
    ('Lenora', 'Jack'),
    ('Sophocles', 'Betsy'),
    ('Gordie', 'Misty'),
    ('Rowan', 'Kabu'),
    ('Hazel', 'Norman'),
    ('Billy', 'Brawly'),
    ('Roark', 'Ernest'),
    ('Saffron', 'Viola'),
    ('Acerola', 'Kiawe'),
    ('Maisie', 'Gardenia'),
    ('Viola', 'Kofu'),
    ('Olympia', 'Tate'),
    ('Tulip', 'Maisie'),
    ('Brassius', 'Billy'),
    ('Hala', 'Tulip'),
    ('Geeta', 'Drayden'),
    ('Evander', 'Tate'),
    ('Clair', 'Jack'),
    ('Lisa', 'Gardenia'),
    ('Bryon', 'Nessa'),
    ('Ernest', 'Falkner'),
    ('Melony', 'Bea'),
    ('Rowan', 'Lenora'),
    ('Bryon', 'Roxanne'),
    ('Acerola', 'Kabu'),
    ('Roark', 'Billy'),
    ('Raleigh', 'Tate'),
    ('Clay', 'Volkner'),
    ('Drayden', 'Brawly'),
    ('Roark', 'Norman'),
    ('Flannery', 'Drayden'),
    ('Burgh', 'Gordie'),
    ('Hala', 'Betsy'),
    ('Evander', 'Clemont'),
    ('Saffron', 'Mallow'),
    ('Maisie', 'Tate'),
    ('Olympia', 'Shane'),
    ('Flannery', 'Clara'),
    ('Bryon', 'Clara'),
    ('Flannery', 'Roxanne'),
    ('Raleigh', 'Geeta'),
    ('Misty', 'Sophocles'),
    ('Chili', 'Ramos'),
    ('Mallow', 'Melony'),
    ('Norman', 'Geeta'),
    ('Clemont', 'Flannery'),
    ('Hala', 'Clay'),
    ('Sophocles', 'Acerola'),
    ('Sophocles', 'Hala'),
    ('Misty', 'Lisa'),
    ('Ramos', 'Jack'),
    ('Flannery', 'Sophocles'),
    ('Clair', 'Maisie'),
    ('Misty', 'Bryon'),
    ('Misty', 'Bea'),
    ('Hassel', 'Kiawe'),
    ('Valerie', 'Lenora'),
    ('Raleigh', 'Kofu'),
    ('Kabu', 'Burgh'),
    ('Lisa', 'Maisie'),
    ('Lisa', 'Hazel'),
    ('Billy', 'Clair'),
    ('Pryce', 'Lt. Surge'),
    ('Volkner', 'Tate'),
    ('Viola', 'Nessa'),
    ('Hazel', 'Clay'),
    ('Reed', 'Acerola'),
    ('Betsy', 'Betsy'),
    ('Viola', 'Opal'),
    ('Valerie', 'Koga'),
    ('Gardenia', 'Misty'),
    ('Gardenia', 'Ernest'),
    ('Clair', 'Acerola'),
    ('Reed', 'Misty'),
    ('Clay', 'Olympia'),
    ('Viola', 'Lt. Surge'),
    ('Lenora', 'Gardenia'),
    ('Olympia', 'Pryce'),
    ('Geeta', 'Lt. Surge'),
    ('Shane', 'Tulip'),
    ('Sophocles', 'Kofu'),
    ('Clair', 'Chili'),
    ('Bugsy', 'Valerie'),
    ('Evander', 'Lt. Surge'),
    ('Tulip', 'Nessa'),
    ('Burgh', 'Lenora'),
    ('Brawly', 'Kiawe'),
    ('Sabrina', 'Burgh'),
    ('Lt. Surge', 'Lisa'),
    ('Billy', 'Olympia'),
    ('Acerola', 'Lt. Surge'),
    ('Clara', 'Ramos'),
    ('Billy', 'Geeta'),
    ('Rowan', 'Hassel'),
    ('Sophocles', 'Koga'),
    ('Viola', 'Sabrina'),
    ('Sophocles', 'Brawly'),
    ('Volkner', 'Betsy'),
    ('Saffron', 'Saffron'),
    ('Tate', 'Viola'),
    ('Melony', 'Jack'),
    ('Brassius', 'Bea'),
    ('Volkner', 'Koga'),
    ('Volkner', 'Betsy'),
    ('Clara', 'Reed'),
    ('Kiawe', 'Kiawe'),
    ('Shane', 'Clara'),
    ('Hazel', 'Sophocles'),
    ('Clemont', 'Chili'),
    ('Bryon', 'Clay'),
    ('Misty', 'Sophocles'),
    ('Evander', 'Valerie'),
    ('Koga', 'Kabu'),
    ('Acerola', 'Chili'),
    ('Nessa', 'Chili'),
    ('Brassius', 'Bugsy'),
    ('Raleigh', 'Misty'),
    ('Billy', 'Gordie'),
    ('Clay', 'Kiawe'),
    ('Bea', 'Pryce'),
    ('Kabu', 'Tulip'),
    ('Reed', 'Billy'),
    ('Reed', 'Mallow'),
    ('Evander', 'Olympia'),
    ('Hala', 'Norman'),
    ('Saffron', 'Roxanne'),
    ('Clemont', 'Kofu'),
    ('Chili', 'Kofu'),
    ('Pryce', 'Mallow'),
    ('Drayden', 'Pryce'),
    ('Roark', 'Brawly'),
    ('Brassius', 'Bea'),
    ('Hazel', 'Lisa'),
    ('Raleigh', 'Kabu'),
    ('Volkner', 'Reed'),
    ('Bea', 'Bryon'),
    ('Acerola', 'Kofu'),
    ('Roark', 'Nessa'),
    ('Viola', 'Misty'),
    ('Rowan', 'Hassel'),
    ('Bugsy', 'Sophocles'),
    ('Sophocles', 'Koga'),
    ('Clay', 'Lt. Surge'),
    ('Reed', 'Tate'),
    ('Hala', 'Flannery'),
    ('Acerola', 'Tulip'),
    ('Valerie', 'Reed'),
    ('Rowan', 'Shane'),
    ('Bea', 'Lisa'),
    ('Roxanne', 'Valerie'),
    ('Billy', 'Bea'),
    ('Volkner', 'Grant'),
    ('Jack', 'Evander'),
    ('Viola', 'Clay'),
    ('Viola', 'Volkner'),
    ('Bugsy', 'Bugsy'),
    ('Gordie', 'Clay'),
    ('Hazel', 'Koga'),
    ('Shane', 'Mallow'),
    ('Rowan', 'Clair'),
    ('Jack', 'Lt. Surge'),
    ('Clara', 'Nessa'),
    ('Lt. Surge', 'Olympia'),
    ('Norman', 'Brassius'),
    ('Grant', 'Clay'),
    ('Tulip', 'Kabu'),
    ('Saffron', 'Acerola'),
    ('Lt. Surge', 'Olympia'),
    ('Rowan', 'Pryce'),
    ('Betsy', 'Acerola'),
    ('Clara', 'Drayden'),
    ('Jack', 'Melony'),
    ('Sophocles', 'Shane'),
    ('Roark', 'Lt. Surge'),
    ('Mallow', 'Drayden'),
    ('Kiawe', 'Lisa'),
    ('Raleigh', 'Clara'),
    ('Pryce', 'Grant'),
    ('Mallow', 'Opal'),
    ('Roark', 'Billy'),
    ('Shane', 'Nessa'),
    ('Kabu', 'Roxanne'),
    ('Pryce', 'Koga'),
    ('Olympia', 'Drayden'),
    ('Saffron', 'Kabu'),
    ('Shane', 'Grant'),
    ('Jack', 'Koga'),
    ('Nessa', 'Tulip'),
    ('Brassius', 'Opal'),
    ('Hassel', 'Evander'),
    ('Clara', 'Mallow'),
    ('Ramos', 'Geeta'),
    ('Ramos', 'Clara'),
    ('Clara', 'Mallow'),
    ('Olympia', 'Hazel'),
    ('Clara', 'Saffron'),
    ('Kofu', 'Maisie'),
    ('Opal', 'Sophocles'),
    ('Rowan', 'Hazel'),
    ('Hazel', 'Bugsy'),
    ('Grant', 'Grant'),
    ('Lt. Surge', 'Roark'),
    ('Evander', 'Volkner'),
    ('Kofu', 'Flannery'),
    ('Lt. Surge', 'Misty'),
    ('Brassius', 'Roark'),
    ('Geeta', 'Hala'),
    ('Mallow', 'Hazel'),
    ('Lisa', 'Jack'),
    ('Clemont', 'Hazel'),
    ('Olympia', 'Clara'),
    ('Roark', 'Shane'),
    ('Clair', 'Hala'),
    ('Jack', 'Lt. Surge'),
    ('Clair', 'Koga'),
    ('Ramos', 'Betsy'),
    ('Flannery', 'Volkner'),
    ('Koga', 'Bryon'),
    ('Geeta', 'Kiawe'),
    ('Norman', 'Jack'),
    ('Shane', 'Ramos'),
    ('Bryon', 'Kofu'),
    ('Opal', 'Bea'),
    ('Melony', 'Hala'),
    ('Clair', 'Geeta'),
    ('Shane', 'Tulip'),
    ('Volkner', 'Betsy'),
    ('Tulip', 'Opal'),
    ('Pryce', 'Brassius'),
    ('Mallow', 'Bugsy'),
    ('Clair', 'Mallow'),
    ('Melony', 'Betsy'),
    ('Rowan', 'Evander'),
    ('Kiawe', 'Shane'),
    ('Lt. Surge', 'Sophocles'),
    ('Kiawe', 'Drayden'),
    ('Norman', 'Jack'),
    ('Grant', 'Flannery'),
    ('Gordie', 'Ramos'),
    ('Acerola', 'Billy'),
    ('Ramos', 'Melony'),
    ('Brassius', 'Brassius'),
    ('Geeta', 'Flannery'),
    ('Flannery', 'Shane'),
    ('Chili', 'Misty'),
    ('Tulip', 'Maisie'),
    ('Chili', 'Rowan'),
    ('Drayden', 'Pryce'),
    ('Evander', 'Lisa'),
    ('Lt. Surge', 'Bryon'),
    ('Bea', 'Lisa'),
    ('Bea', 'Flannery'),
    ('Geeta', 'Lt. Surge'),
    ('Drayden', 'Mallow'),
    ('Sophocles', 'Drayden'),
    ('Ramos', 'Pryce'),
    ('Clemont', 'Clemont'),
    ('Volkner', 'Bryon'),
    ('Ramos', 'Norman'),
    ('Maisie', 'Kofu'),
    ('Jack', 'Pryce'),
    ('Rowan', 'Clay'),
    ('Clemont', 'Mallow'),
    ('Clemont', 'Misty'),
    ('Hazel', 'Opal'),
    ('Tulip', 'Shane'),
    ('Hala', 'Bugsy'),
    ('Drayden', 'Sophocles'),
    ('Sophocles', 'Kiawe'),
    ('Clair', 'Jack'),
    ('Brawly', 'Rowan'),
    ('Brassius', 'Roark'),
    ('Drayden', 'Flannery'),
    ('Brassius', 'Brawly'),
    ('Bugsy', 'Bugsy'),
    ('Bea', 'Norman'),
    ('Grant', 'Jack'),
    ('Flannery', 'Brassius'),
    ('Melony', 'Hala'),
    ('Sophocles', 'Hazel'),
    ('Hazel', 'Roark'),
    ('Viola', 'Ramos'),
    ('Chili', 'Hala'),
    ('Betsy', 'Grant'),
    ('Hala', 'Melony'),
    ('Brawly', 'Maisie'),
    ('Billy', 'Nessa'),
    ('Shane', 'Volkner'),
]


target_researcher = "Eve"
print(find_erdos_number(collaborations, target_researcher))
