from tkinter import *
import random
import os

print(os)

class PLCInterface:
    def __init__(self, master):
        self.master = master
        master.title("PLC Interface")
        master.attributes('-fullscreen', True)

        self.connection_label = Label(master, text="Connection Status: ")
        self.connection_label.pack()

        self.connect_button = Button(master, text="Connect to PLC", command=self.simulate_connection)
        self.connect_button.pack()

        self.main_menu_button = Button(master, text="Main Menu", command=self.main_menu)
        self.main_menu_button.pack()

        self.diagram_button = Button(master, text="test", command=self.show_menu)
        self.diagram_button.pack()

        self.active_alarm_label = Label(master, text="", font=("Helvetica", 16), fg="red")
        self.active_alarm_label.pack()

        # Canvas for diagram
        self.canvas = Canvas(master, width=1200, height=800)
        self.canvas.pack(expand=YES, fill=BOTH)
    def main_menu(self):
        self.title("Main Menu")

    def simulate_connection(self):
        # Simulating PLC connection
        self.connection_label.config(text="Connection Status: Successful", fg="green")
        

    def show_menu(self):
        self.connect_button.destroy()

        self.diagram_button = Button(self.master, text="Show Diagram", command=self.show_diagram)
        self.diagram_button.pack()

        # Simulate initial state of valves
        self.valve_states = [random.choice([True, False]) for _ in range(12)]

        # Check for alarms and update label
        self.check_alarms()

        # Schedule valve state updates
        self.master.after(5000, self.update_valve_states)

    def show_diagram(self):
        # Clear canvas
        self.canvas.delete("all")

        # Draw lead pipes from machines
        machine_positions = [(200, 50), (400, 50), (600, 50), (800, 50), (1000, 50), (1200, 50),
                             (200, 300), (400, 300), (600, 300), (800, 300), (1000, 300), (1200, 300)]
        self.draw_machines(machine_positions)

        # Draw valves and pipes
        valve_positions = [(200, 80), (400, 80), (600, 80), (800, 80), (1000, 80), (1200, 80),
                           (200, 330), (400, 330), (600, 330), (800, 330), (1000, 330), (1200, 330)]
        self.draw_valves_and_pipes(valve_positions)

        # Display the alarm label
        self.display_alarm_label()

    def draw_machines(self, machine_positions):
        for i, position in enumerate(machine_positions):
            self.canvas.create_text(position[0] + 15, position[1] - 10, text=f"Machine {i + 1}")
            self.canvas.create_line(position[0] + 15, position[1], position[0] + 15, position[1] + 30, width=5)

    def draw_valves_and_pipes(self, valve_positions):
        for i, valve_position in enumerate(valve_positions):
            color = "green" if self.valve_states[i] else "red"
            self.canvas.create_oval(valve_position[0], valve_position[1], valve_position[0] + 30,
                                    valve_position[1] + 30, outline="black", fill=color)

            # Draw pipes coming off the valve
            self.canvas.create_line(valve_position[0] + 15, valve_position[1] + 30, valve_position[0] + 15, valve_position[1] + 80, width=5)
            self.canvas.create_line(valve_position[0] + 30, valve_position[1] + 10, valve_position[0] + 50, valve_position[1] + 10, width=5)

            # Label pipes
            self.canvas.create_text(valve_position[0] + 60, valve_position[1] + 30, text="Atmosphere", anchor=W)
            self.canvas.create_text(valve_position[0] + 60, valve_position[1] + 80, text="RTO", anchor=W)

            # Label valve slightly higher and to the left
            self.canvas.create_text(valve_position[0] + 5, valve_position[1] + 30, text=f"Valve {i + 1}", anchor=E)

    def update_valve_states(self):
        # Simulate valve states changing randomly
        self.valve_states = [random.choice([True, False]) for _ in range(12)]

        # Check for alarms and update label
        self.check_alarms()

        # Redraw valves and pipes
        self.show_diagram()

        # Schedule the next valve state update
        self.master.after(5000, self.update_valve_states)

    def check_alarms(self):
        # Check if any valves are closed (red)
        closed_valves = [i + 1 for i, state in enumerate(self.valve_states) if not state]

        # Update alarm label
        if closed_valves:
            self.active_alarm_label.config(text=f"Active Alarm: Valve(s) {', '.join(map(str, closed_valves))}")
        else:
            self.active_alarm_label.config(text="")

    def display_alarm_label(self):
        # Display the alarm label in the diagram screen
        alarm_text = self.active_alarm_label.cget("text")
        if alarm_text:
            self.canvas.create_text(600, 700, text=alarm_text, font=("Helvetica", 16), fill="red")

if __name__ == "__main__":
    root = Tk()
    app = PLCInterface(root)
    root.mainloop()
