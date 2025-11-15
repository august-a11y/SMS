from typing import Optional, Callable


class Menu:
    def __init__(self, title: str):
        self.title = title
        self.options: list[tuple[str, str, Callable]] = []
    
    def add_option(self, key: str, description: str, handler: Callable):
        self.options.append((key, description, handler))
    
    def display(self):
        print("\n" + "=" * 60)
        print(self.title.center(60))
        print("=" * 60)
        for key, description, _ in self.options:
            print(f"{key}. {description}")
        print("=" * 60)
    
    def get_choice(self) -> Optional[str]:
        choice = input("\nChoice: ").strip()
        return choice
    
    def run(self):
        while True:
            self.display()
            choice = self.get_choice()
            
            handler = None
            for key, _, h in self.options:
                if key == choice:
                    handler = h
                    break
            
            if handler:
                try:
                    result = handler()
                    if result is False:
                        break
                except Exception as e:
                    print(f"\n✗ Error: {e}")
                    input("\nPress Enter to continue...")
            else:
                print("\n✗ Error: Invalid choice. Please try again.")
                input("Press Enter to continue...")


class AdminMenu(Menu):
    def __init__(self):
        super().__init__("MENU ADMIN")
        self.setup_options()
    
    def setup_options(self):
        pass


class StudentMenu(Menu):
    def __init__(self):
        super().__init__("MENU STUDENT")
        self.setup_options()
    
    def setup_options(self):
        pass


class LecturerMenu(Menu):
    def __init__(self):
        super().__init__("MENU LECTURER")
        self.setup_options()
    
    def setup_options(self):
        pass

