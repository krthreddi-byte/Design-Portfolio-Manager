# ============================================================
#        🎨 DESIGN PORTFOLIO MANAGER 🎨
#        A Professional CLI Portfolio Tool for Designers
# ============================================================

# --- Storage: All projects saved here during runtime ---
projects = []

# ── ASCII Art Display ──────────────────────────────────────

def generate_ascii_art(project_name):
    """Generates simple ASCII art for a project."""
    name = project_name[:10].upper()
    width = max(len(name) + 4, 20)
    border = "+" + "-" * (width) + "+"
    empty  = "|" + " " * (width) + "|"
    title  = "|" + name.center(width) + "|"

    print(f"\n  {border}")
    print(f"  {empty}")
    print(f"  {title}")
    print(f"  |{'🎨 DESIGN PROJECT'.center(width)}|")
    print(f"  {empty}")
    print(f"  {border}")

# ============================================================
#  DISPLAY HELPERS
# ============================================================

def print_banner():
    """Prints a stylish welcome banner."""
    print("\n")
    print("=" * 60)
    print("  🎨  DESIGN PORTFOLIO MANAGER  🎨")
    print("  Your Creative Projects, Beautifully Organized")
    print("=" * 60)
    print()

def print_separator():
    """Prints a visual separator line."""
    print("-" * 60)

def print_stars(rating):
    """Returns star emojis based on rating (1-5)."""
    try:
        rating = int(rating)
        return "⭐" * rating + "☆" * (5 - rating)
    except:
        return "☆☆☆☆☆"

def print_success(message):
    """Prints a success message."""
    print(f"\n  ✅  {message}")

def print_error(message):
    """Prints an error message."""
    print(f"\n  ❌  {message}")

def print_info(message):
    """Prints an info message."""
    print(f"\n  ℹ️   {message}")

# ============================================================
#  DISPLAY A SINGLE PROJECT
# ============================================================

def display_project(project, index=None):
    """Displays a single project in a beautiful formatted style."""
    print_separator()
    if index is not None:
        print(f"  📁  Project #{index + 1}")
    print(f"  🖊️   Project Name     : {project['name']}")
    print(f"  👤  Designer Name    : {project['designer']}")
    print(f"  📝  Description      : {project['description']}")
    print(f"  🎯  Category         : {project['category']}")
    print(f"  🖼️   Image Path       : {project['image_path']}")
    generate_ascii_art(project['name'])
    print(f"  🤝  Client Name      : {project['client']}")
    print(f"  💬  Client Feedback  : {project['feedback']}")
    print(f"  ⭐  Rating           : {print_stars(project['rating'])} ({project['rating']}/5)")
    print(f"  📅  Completion Date  : {project['date']}")
    print_separator()

# ============================================================
#  INPUT HELPER - Prevents Empty Inputs
# ============================================================

def get_input(prompt):
    """Gets user input and prevents empty values."""
    while True:
        value = input(f"  👉  {prompt}: ").strip()
        if value:
            return value
        else:
            print_error("This field cannot be empty. Please enter a value.")

def get_rating():
    """Gets a valid rating between 1 and 5."""
    while True:
        rating = input("  👉  Project Rating (1-5): ").strip()
        if rating in ["1", "2", "3", "4", "5"]:
            return rating
        else:
            print_error("Please enter a valid rating between 1 and 5.")

# ============================================================
#  FEATURE 1: ADD NEW PROJECT
# ============================================================

def add_project():
    """Allows user to add a new design project."""
    print("\n")
    print("=" * 60)
    print("  ➕  ADD NEW PROJECT")
    print("=" * 60)

    # Collect all project details
    name        = get_input("Project Name")
    designer    = get_input("Designer Name")
    description = get_input("Project Description")

    # Category selection
    print("\n  📂  Design Categories:")
    print("      1. Logo Design")
    print("      2. UI/UX Design")
    print("      3. Poster Design")
    print("      4. Branding")
    print("      5. Other")
    category_choice = input("  👉  Choose Category (1-5) or type your own: ").strip()

    categories = {
        "1": "Logo Design",
        "2": "UI/UX Design",
        "3": "Poster Design",
        "4": "Branding",
        "5": "Other"
    }
    category = categories.get(category_choice, category_choice if category_choice else "Other")

    image_path  = get_input("Image File Path (e.g. /images/project1.png)")
    client      = get_input("Client Name")
    feedback    = get_input("Client Feedback")
    rating      = get_rating()
    date        = get_input("Completion Date (e.g. 2024-05-10)")

    # Build the project dictionary
    project = {
        "name"       : name,
        "designer"   : designer,
        "description": description,
        "category"   : category,
        "image_path" : image_path,
        "client"     : client,
        "feedback"   : feedback,
        "rating"     : rating,
        "date"       : date
    }

    # Save to projects list
    projects.append(project)
    print_success(f"Project '{name}' has been added successfully! 🎉")

# ============================================================
#  FEATURE 2: VIEW ALL PROJECTS
# ============================================================

def view_all_projects():
    """Displays all saved projects."""
    print("\n")
    print("=" * 60)
    print("  📂  ALL PROJECTS")
    print("=" * 60)

    if not projects:
        print_info("No projects found. Please add a project first.")
        return

    print(f"\n  Total Projects: {len(projects)}\n")
    for index, project in enumerate(projects):
        display_project(project, index)

# ============================================================
#  FEATURE 3: SEARCH PROJECT BY NAME
# ============================================================

def search_project():
    """Searches for a project by name."""
    print("\n")
    print("=" * 60)
    print("  🔍  SEARCH PROJECT")
    print("=" * 60)

    if not projects:
        print_info("No projects found. Please add a project first.")
        return

    keyword = get_input("Enter Project Name to Search")
    keyword_lower = keyword.lower()

    # Search through all projects
    results = [p for p in projects if keyword_lower in p["name"].lower()]

    if results:
        print(f"\n  ✅  Found {len(results)} result(s) for '{keyword}':\n")
        for index, project in enumerate(results):
            display_project(project, index)
    else:
        print_error(f"No project found with name '{keyword}'.")

# ============================================================
#  FEATURE 4: DELETE PROJECT
# ============================================================

def delete_project():
    """Deletes a project with confirmation."""
    print("\n")
    print("=" * 60)
    print("  🗑️   DELETE PROJECT")
    print("=" * 60)

    if not projects:
        print_info("No projects found. Please add a project first.")
        return

    # Show all project names
    print("\n  Available Projects:\n")
    for index, project in enumerate(projects):
        print(f"  [{index + 1}] {project['name']}")

    # Get user choice
    choice = input("\n  👉  Enter Project Number to Delete: ").strip()

    try:
        index = int(choice) - 1
        if 0 <= index < len(projects):
            project_name = projects[index]["name"]

            # Confirmation step
            confirm = input(f"\n  ⚠️   Are you sure you want to delete '{project_name}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                projects.pop(index)
                print_success(f"Project '{project_name}' has been deleted successfully!")
            else:
                print_info("Deletion cancelled. Project is safe. 😊")
        else:
            print_error("Invalid project number. Please try again.")
    except ValueError:
        print_error("Invalid input. Please enter a valid number.")

# ============================================================
#  FEATURE 5: UPDATE PROJECT DETAILS
# ============================================================

def update_project():
    """Allows user to update an existing project's details."""
    print("\n")
    print("=" * 60)
    print("  ✏️   UPDATE PROJECT")
    print("=" * 60)

    if not projects:
        print_info("No projects found. Please add a project first.")
        return

    # Show all project names
    print("\n  Available Projects:\n")
    for index, project in enumerate(projects):
        print(f"  [{index + 1}] {project['name']}")

    # Get user choice
    choice = input("\n  👉  Enter Project Number to Update: ").strip()

    try:
        index = int(choice) - 1
        if 0 <= index < len(projects):
            project = projects[index]
            print(f"\n  Updating: '{project['name']}'")
            print_info("Press ENTER to keep the current value.")
            print()

            # Update each field (keep old value if input is empty)
            def update_field(prompt, key):
                new_val = input(f"  👉  {prompt} [{project[key]}]: ").strip()
                if new_val:
                    project[key] = new_val

            update_field("Project Name", "name")
            update_field("Designer Name", "designer")
            update_field("Description", "description")
            update_field("Category", "category")
            update_field("Image Path", "image_path")
            update_field("Client Name", "client")
            update_field("Client Feedback", "feedback")

            # Rating update with validation
            new_rating = input(f"  👉  Rating (1-5) [{project['rating']}]: ").strip()
            if new_rating in ["1", "2", "3", "4", "5"]:
                project["rating"] = new_rating

            update_field("Completion Date", "date")

            print_success(f"Project '{project['name']}' updated successfully! 🎉")
        else:
            print_error("Invalid project number. Please try again.")
    except ValueError:
        print_error("Invalid input. Please enter a valid number.")

# ============================================================
#  MAIN MENU
# ============================================================

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print_banner()
        print("  📋  MAIN MENU\n")
        print("  [1]  ➕  Add New Project")
        print("  [2]  📂  View All Projects")
        print("  [3]  🔍  Search Project by Name")
        print("  [4]  🗑️   Delete Project")
        print("  [5]  ✏️   Update Project Details")
        print("  [6]  🚪  Exit Application")
        print()
        print_separator()

        choice = input("  👉  Enter your choice (1-6): ").strip()
        print()

        if choice == "1":
            add_project()
        elif choice == "2":
            view_all_projects()
        elif choice == "3":
            search_project()
        elif choice == "4":
            delete_project()
        elif choice == "5":
            update_project()
        elif choice == "6":
            print("\n" + "=" * 60)
            print("  👋  Thank you for using Design Portfolio Manager!")
            print("  🎨  Keep Designing, Keep Creating!")
            print("=" * 60 + "\n")
            break
        else:
            print_error("Invalid choice. Please enter a number between 1 and 6.")

        input("\n  🔁  Press ENTER to go back to Main Menu...")

# ============================================================
#  PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main_menu()