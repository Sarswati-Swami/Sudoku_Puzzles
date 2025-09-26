
import tkinter as tk
from tkinter import messagebox

# ---------------- Sudoku Solver (3x3) ----------------
def is_valid(board, row, col, num):
    """Check if placing num in (row, col) is valid for 3x3 Sudoku."""
    # Check row
    if num in board[row]:
        return False
    # Check column
    for r in range(3):
        if board[r][col] == num:
            return False
    return True

def solve_sudoku(board):
    """Backtracking solver for 3x3 Sudoku."""
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                for num in range(1, 4):  # Numbers 1 to 3
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


# ---------------- Tkinter GUI ----------------
class Sudoku3x3GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("3x3 Sudoku Solver")
        self.entries = []

        # Create a 3x3 grid of Entry widgets
        for r in range(3):
            row_entries = []
            for c in range(3):
                e = tk.Entry(root, width=3, font=("Arial", 18), justify="center", borderwidth=2, relief="ridge")
                e.grid(row=r, column=c, padx=5, pady=5, ipady=5)
                row_entries.append(e)
            self.entries.append(row_entries)

        # Buttons
        tk.Button(root, text="Solve", command=self.solve, bg="lightgreen", font=("Arial", 14)).grid(
            row=3, column=0, columnspan=1, pady=10, sticky="nsew"
        )
        tk.Button(root, text="Clear", command=self.clear_grid, bg="lightcoral", font=("Arial", 14)).grid(
            row=3, column=1, columnspan=2, pady=10, sticky="nsew"
        )

    def get_board(self):
        """Retrieve current board state from Entry widgets."""
        board = []
        for r in range(3):
            row_data = []
            for c in range(3):
                val = self.entries[r][c].get().strip()
                if val.isdigit() and 1 <= int(val) <= 3:
                    row_data.append(int(val))
                else:
                    row_data.append(0)
            board.append(row_data)
        return board

    def display_board(self, board):
        """Display solved board in the grid."""
        for r in range(3):
            for c in range(3):
                self.entries[r][c].delete(0, tk.END)
                if board[r][c] != 0:
                    self.entries[r][c].insert(0, str(board[r][c]))

    def solve(self):
        board = self.get_board()
        if solve_sudoku(board):
            self.display_board(board)
        else:
            messagebox.showerror("Error", "No solution exists for this puzzle!")

    def clear_grid(self):
        for r in range(3):
            for c in range(3):
                self.entries[r][c].delete(0, tk.END)


# ---------------- Run the App ----------------
if __name__ == "__main__":
    root = tk.Tk()
    Sudoku3x3GUI(root)
    root.mainloop()

