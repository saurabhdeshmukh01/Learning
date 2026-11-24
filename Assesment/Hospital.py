class Node:
    def __init__(self, patient_id, name, priority):
        self.patient_id = patient_id
        self.name = name
        self.priority = priority
        self.next = None


head = None
priority_names = {1: "Critical", 2: "Serious", 3: "Normal"}


def enqueue(patient_id, name, priority):
    global head
    if priority not in [1, 2, 3]:
        print("Invalid priority Enter 1, 2, or 3.")
        return

    new_node = Node(patient_id, name, priority)

    if head is None or priority < head.priority:
        new_node.next = head
        head = new_node
    else:
        temp = head
        while temp.next is not None and temp.next.priority <= priority:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    print(f"Added: {name} (ID: {patient_id}) - {priority_names[priority]}")


def display_next():
    if head is None:
        print("No patients waiting.")
        return
    print(f"\nNext Patient -> ID: {head.patient_id} | Name: {head.name} | Condition: {priority_names[head.priority]}")


def dequeue():
    global head
    if head is None:
        print("No patients to treat.")
        return
    removed = head
    head = head.next
    print(f"\nTreated & Removed -> ID: {removed.patient_id} | Name: {removed.name} ({priority_names[removed.priority]})")


def display_all():
    if head is None:
        print("\nWaiting list is empty.")
        return
    print("\n--- All Waiting Patients ---")
    temp = head
    while temp is not None:
        print(f"ID: {temp.patient_id} | Name: {temp.name} | Priority: {temp.priority} ({priority_names[temp.priority]})")
        temp = temp.next
    print("----------------------------")


while True:
    print("\n=== Hospital Emergency System ===")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Treat Next Patient (Remove)")
    print("4. Display All Waiting Patients")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '1':
        p_id = input("Enter Patient ID: ")
        p_name = input("Enter Patient Name: ")
        p_prio = int(input("Enter Priority (1=Critical, 2=Serious, 3=Normal): "))
        enqueue(p_id, p_name, p_prio)

    elif choice == '2':
        display_next()

    elif choice == '3':
        dequeue()

    elif choice == '4':
        display_all()

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice.")