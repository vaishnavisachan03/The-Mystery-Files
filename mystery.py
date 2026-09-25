# The Mystery 
# : The Stolen Exam Paper
case_title = "The Stolen Exam Paper"
case_description = """At 6:30 PM, a sealed Calculus exam paper was placed
inside a faculty office.
At 7:10 PM, the professor returned and discovered
that the exam paper was missing.
Only four people were known to be in the area that evening.
Your task is to investigate the case, collect evidence,
compare statements, reconstruct the timeline, and identify
the person responsible."""

suspects = {
    1: {"name": "Aarav",
        "role": "Class Representative",
        "statement": "I left the academic block at 6:40 PM "
                     "and went directly to the cafeteria."},

    2: {"name": "Naira",
        "role": "Student Volunteer",
        "statement": "I was organizing documents near the "
                     "faculty office. I left around 6:45 PM."},

    3: {"name": "Kabir",
        "role": "Lab Assistant",
        "statement": "I was working in the computer lab. "
                     "I only came out briefly to collect equipment."},

    4: {"name": "Meera",
        "role": "Faculty Assistant",
        "statement": "I finished my work and left the faculty "
                     "area at around 6:50 PM."}
}

evidence = {
    1: {"name": "Office Key Record",
        "description": "The faculty office was unlocked at 6:47 PM.",
        "related_to": "Unknown"},

    2: {"name": "Printer Record",
        "description": "The office printer was used at 6:49 PM "
                       "to print two pages.",
        "related_to": "Unknown"},

    3: {"name": "Cafeteria Receipt",
        "description": "A receipt shows that Aarav made a "
                       "purchase at 6:43 PM.",
        "related_to": "Aarav"},

    4: {"name": "Torn Paper",
        "description": "A piece of printed paper was found "
                       "near the faculty corridor.",
        "related_to": "Unknown"},

    5: {"name": "Security Log",
        "description": "Someone entered the faculty corridor "
                       "at 6:46 PM.",
        "related_to": "Unknown"},

    6: {"name": "Computer Activity",
        "description": "The faculty computer was accessed "
                       "at 6:48 PM using a staff account.",
        "related_to": "Unknown"},

    7: {"name": "Witness Statement",
        "description": "A witness saw someone leaving the "
                       "faculty corridor at 6:52 PM carrying a folder.",
        "related_to": "Unknown"},

    8: {"name": "Document Folder",
        "description": "A faculty document folder was found "
                       "near the staircase.",
        "related_to": "Unknown"}
}
collected_evidence = []
interviewed_suspects = []
contradictions_found = 0


def view_case():
    print("\nCASE INFORMATION")
    print("\n" + case_title)
    print(case_description)


def view_suspects():
    print("\nSUSPECTS")
    for number, suspect in suspects.items():
        print(f"\n{number}. {suspect['name']}")
        print(f"Role: {suspect['role']}")

def collect_evidence(number):
    if number in collected_evidence:
        print("\nYou have already collected this evidence.")
    else:
        collected_evidence.append(number)
        print(f"\nEvidence collected: {evidence[number]['name']}")

def investigate():
    print("\nINVESTIGATE FACULTY OFFICE")
    print("\n1. Examine the office door")
    print("2. Examine the printer")
    print("3. Search the corridor")
    print("4. Search the staircase")
    print("5. Return")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        print("\nYou examine the office door.")
        print("The key record shows that the office")
        print("was unlocked at 6:47 PM.")
        collect_evidence(1)
        print("\nThe security system also recorded")
        print("someone entering the faculty corridor at 6:46 PM.")
        collect_evidence(5)
    elif choice == "2":
        print("\nYou examine the office printer.")
        print("The printer was used at 6:49 PM")
        print("to print two pages.")
        collect_evidence(2)
    elif choice == "3":
        print("\nYou search the corridor.")
        print("You find a torn piece of printed paper.")
        collect_evidence(4)
        print("\nA witness reports seeing someone")
        print("leave the corridor at 6:52 PM with a folder.")
        collect_evidence(7)
    elif choice == "4":
        print("\nYou search near the staircase.")
        print("You discover a folder similar to those")
        print("used by the faculty department.")
        collect_evidence(8)
    elif choice == "5":
        return
    else:
        print("\nInvalid choice.")

def interview_suspect():
    global contradictions_found
    view_suspects()
    try:
        choice = int(input("\nChoose a suspect: "))
    except ValueError:
        print("\nPlease enter a valid number.")
        return
    if choice not in suspects:
        print("\nInvalid suspect.")
        return
    suspect = suspects[choice]
    name = suspect["name"]
    print(f"\nInterviewing {name}")
    print(f"\n{name}:")
    print(suspect["statement"])
    if choice not in interviewed_suspects:
        interviewed_suspects.append(choice)
    if name == "Aarav":
        print("\nYou ask Aarav when he reached the cafeteria.")
        print("\nAarav:I reached there shortly after leaving the block.You check the cafeteria records.")
        collect_evidence(3)
        print("\nThe receipt confirms a purchase at 6:43 PM.")
    elif name == "Naira":
        print("\nYou ask Naira what she was organizing.")
        print("\nNaira:I was organizing event forms and attendance sheets.You ask if she entered the faculty office.")
        print("\nNaira:")
        print("No. I stayed outside the office.")
    elif name == "Kabir":
        print("\nYou ask Kabir where he went after leaving the lab.")
        print("\nKabir:")
        print("I went to collect some equipment from storage.")
        print("\nYou ask if he entered the faculty corridor.")
        print("\nKabir:")
        print("No, I did not.")
    elif name == "Meera":
        print("\nYou ask Meera what she was doing around 6:45 PM.")
        print("\nMeera:")
        print("I was finishing some administrative work.")
        print("\nYou ask whether she used the faculty computer.")
        print("\nMeera:")
        print("I don't remember using it after 6:30 PM.")
        collect_evidence(6)
        print("\nThe computer was accessed at 6:48 PM.")
        contradictions_found += 1
        print("\nYou notice a possible contradiction.")
        print("Meera claims she did not use the computer,")
        print("but the computer was accessed while")
        print("she was still in the faculty area.")

def view_evidence():
    print("\nCOLLECTED EVIDENCE")
    if len(collected_evidence) == 0:
        print("\nYou have not collected any evidence yet.")
        return
    for number in collected_evidence:
        item = evidence[number]
        print(f"\n{item['name']}")
        print(f"{item['description']}")
        print(f"Related to: {item['related_to']}")

def reconstruct_timeline():
    print("\nTIMELINE")
    print("\n6:30 PM  - Exam paper placed inside the office.")
    print("6:40 PM  - Aarav claims he leaves.")
    print("6:43 PM  - Aarav makes a cafeteria purchase.")
    print("6:45 PM  - Naira claims she leaves.")
    print("6:46 PM  - Someone enters the faculty corridor.")
    print("6:47 PM  - Faculty office is unlocked.")
    print("6:48 PM  - Faculty computer is accessed.")
    print("6:49 PM  - Printer is used.")
    print("6:52 PM  - Someone leaves carrying a folder.")
    print("7:10 PM  - Missing exam paper is discovered.")
    print("\nStudy the timeline carefully.")
    if len(collected_evidence) >= 4:
        print("\nYou have enough evidence to begin")
        print("connecting the events.")
    else:
        print("\nYou should collect more evidence before")
        print("drawing a conclusion.")

def review_investigation():
    print("\nINVESTIGATION REVIEW")
    print(f"\nEvidence collected: {len(collected_evidence)}/8")
    print(f"Suspects interviewed: {len(interviewed_suspects)}/4")
    print(f"Contradictions found: {contradictions_found}")
    if len(collected_evidence) >= 6:
        print("\nInvestigation status: Strong")
    elif len(collected_evidence) >= 3:
        print("\nInvestigation status: In progress")
    else:
        print("\nInvestigation status: Very early")

def final_accusation():
    print("\nFINAL ACCUSATION")
    print("\nYou should only make an accusation")
    print("after reviewing the evidence.")
    view_suspects()
    try:
        choice = int(input("\nWho do you accuse? "))
    except ValueError:
        print("\nPlease enter a valid number.")
        return
    if choice not in suspects:
        print("\nInvalid choice.")
        return
    accused = suspects[choice]["name"]
    print(f"\nYou accuse {accused}.")
    if accused == "Meera":
        if (1 in collected_evidence
            and 2 in collected_evidence
            and 6 in collected_evidence
            and 7 in collected_evidence
            and contradictions_found >= 1):
            print("\nCASE SOLVED!")
            print("\nYour accusation is supported by")
            print("multiple pieces of evidence.")
            print("\nThe timeline shows that:")
            print("The office was accessed at 6:47 PM.")
            print("The computer was used at 6:48 PM.")
            print("The printer was used at 6:49 PM.")
            print("Someone left with a folder at 6:52 PM.")
            print("\nMeera's statement does not fully")
            print("match the evidence.")
            print("\nYou successfully solved the case.")
        else:
            print("\nYour accusation may be correct,")
            print("but you do not have enough evidence.")
            print("Investigate further before reaching")
            print("a final conclusion.")
    else:
        print("\nWRONG ACCUSATION")
        print("\nThe available evidence does not")
        print("strongly support your accusation.")
        print("The case remains unresolved.")
def main():
    print("\nTHE MYSTERY FILES")
    print("Case #001: The Stolen Exam Paper")
    print("\nYou have been assigned to investigate")
    print("the disappearance of a Calculus exam paper.")
    while True:
        print("\nMain Menu")
        print("\n1. View Case")
        print("2. View Suspects")
        print("3. Investigate Faculty Office")
        print("4. Interview Suspects")
        print("5. Examine Evidence")
        print("6. Reconstruct Timeline")
        print("7. Review Investigation")
        print("8. Make Final Accusation")
        print("9. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            view_case()
        elif choice == "2":
            view_suspects()
        elif choice == "3":
            investigate()
        elif choice == "4":
            interview_suspect()
        elif choice == "5":
            view_evidence()
        elif choice == "6":
            reconstruct_timeline()
        elif choice == "7":
            review_investigation()
        elif choice == "8":
            final_accusation()
        elif choice == "9":
            print("\nThank you for playing The Mystery Files.")
            print("Investigation ended.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 9.")
main()