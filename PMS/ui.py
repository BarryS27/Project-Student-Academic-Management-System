import numpy as np

class ConsoleUI:
    def __init__(self, manager):
        self.manager = manager

    def _get_input(self, prompt, is_float=False):
        val = input(prompt).strip()
        if val == '':
            return np.nan
        if is_float:
            try:
                return float(val)
            except ValueError:
                print("Invalid number, using NaN.")
                return np.nan
        return val

    def page_add(self):
        print("\n--- [ Add Info ] ---")
        grade = input('Target Grade (G9/G10/G11/G12): ').strip()
        
        if not self.manager.get_data(grade) is not None:
            print(f"Error: Grade '{grade}' not found.")
            return

        print(f"Adding to {grade}...")
        row_data = {
            'Sem': input('Semester: '),
            'Level': input('Level: '),
            'Code': input('Code: '),
            'Course': input('Course: '),
            'Weight': self._get_input('Weight: ', True),
            'Q1_Points': self._get_input('Q1 Pts: ', True),
            'Q2_Points': self._get_input('Q2 Pts: ', True),
            'Q3_Points': self._get_input('Q3 Pts: ', True),
            'Q4_Points': self._get_input('Q4 Pts: ', True),
        }

        if input('Save this row? (y/n): ') == 'y':
            self.manager.add_row(grade, row_data)
            self.manager.save_all()
            print("Saved.")
        else:
            print("Cancelled.")

    def page_edit(self):
        print("\n--- [ Edit Info ] ---")
        grade = input('Target Grade: ').strip()
        df = self.manager.get_data(grade)
        
        if df is None or df.empty:
            print("No data available.")
            return

        print(df.to_string())
        
        try:
            r_idx = int(input('Row Index: '))
            col = input('Column Name: ')
            val = input('New Value: ')
            
            if input('Confirm update? (y/n): ') == 'y':
                success = self.manager.update_cell(grade, r_idx, col, val)
                if success:
                    self.manager.save_all()
                    print("Updated.")
                else:
                    print("Failed. Check index or column name.")
        except ValueError:
            print("Invalid input format.")

    def start_loop(self):
        while True:
            print("\n=== My System ===")
            print("1. Add Info")
            print("2. Edit Info")
            print("3. Exit")
            
            choice = input("Select: ").strip()
            
            if choice == '1':
                self.page_add()
            elif choice == '2':
                self.page_edit()
            elif choice == '3':
                print("Bye!")
                break
            else:
                print("Invalid choice.")