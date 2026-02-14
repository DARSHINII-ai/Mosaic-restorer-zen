import tkinter as tk
import random

class MosaicGame:
    def __init__(self, root):
        self.root = root
        self.root.title("The Mosaic Restorer")
        self.root.configure(bg="#2c3e50")

        # Define a peaceful palette
        self.colors = ["#AED6F1", "#A3E4D7", "#F9E79F", "#F5B7B1", "#D7BDE2"]
        self.grid_size = 4
        
        # Create a "Target" pattern the user needs to match
        self.target_pattern = [[random.choice(self.colors) for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        
        self.label = tk.Label(root, text="Restore the Mosaic: Match the grid to the target colors", 
                              fg="white", bg="#2c3e50", font=("Verdana", 10))
        self.label.pack(pady=10)

        # Draw the Target Mini-Map
        self.target_canvas = tk.Canvas(root, width=100, height=100, bg="#2c3e50", highlightthickness=0)
        self.target_canvas.pack(pady=5)
        self.draw_target_map()

        # Main Puzzle Grid
        self.frame = tk.Frame(root, bg="#2c3e50")
        self.frame.pack(pady=10)
        
        self.buttons = []
        for r in range(self.grid_size):
            row_btns = []
            for c in range(self.grid_size):
                # Start everything as Gray
                btn = tk.Button(self.frame, width=8, height=3, bg="#95a5a6", 
                                command=lambda r=r, c=c: self.change_color(r, c))
                btn.grid(row=r, column=c, padx=2, pady=2)
                row_btns.append(btn)
            self.buttons.append(row_btns)

    def draw_target_map(self):
        size = 20
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                self.target_canvas.create_rectangle(c*size, r*size, (c+1)*size, (r+1)*size, 
                                                    fill=self.target_pattern[r][c], outline="white")

    def change_color(self, r, c):
        current_color = self.buttons[r][c].cget("bg")
        # Cycle through colors
        if current_color == "#95a5a6":
            next_idx = 0
        else:
            next_idx = (self.colors.index(current_color) + 1) % len(self.colors)
        
        self.buttons[r][c].config(bg=self.colors[next_idx])
        self.check_win()

    def check_win(self):
        match = True
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                if self.buttons[r][c].cget("bg") != self.target_pattern[r][c]:
                    match = False
        
        if match:
            self.label.config(text="RESTORATION COMPLETE. ZEN ACHIEVED.", fg="#58D68D")
            for r in self.buttons:
                for b in r: b.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = MosaicGame(root)
    root.mainloop()
