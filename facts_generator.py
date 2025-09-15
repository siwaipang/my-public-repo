#-----------------------------------------------------------------------------

def class_contributions():

    """
    Each student should add their name and a fun fact or a short fact in the 'contributions' list below.
    Example: ("Alice", "I love Python!")
    """
    contributions = [

        # Teacher contribution
        ("Ruud", "Ik ben getrouwd, maar woon niet samen."),
        ("Josey", "Ik ben 35 jaar oud, getrouwd, woon in een losstaand huis én ik heb 3 kinderen.")
        
        # 👇 Students, add your entries here:
        ("Si Wai", "hello world."),

        ("Ahmed", "Hoi"),

    ]

    return contributions

#-----------------------------------------------------------------------------

def main():

    print("💻 GitHub Collaboration Workshop")

    print("=" * 40)
    
    print("Contributions:\n")

    for name, fact in class_contributions():

        print(f"- {name}: {fact}")

#-----------------------------------------------------------------------------

if __name__ == "__main__":

    main()

#-----------------------------------------------------------------------------