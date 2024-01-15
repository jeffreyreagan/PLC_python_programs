from tkinter import *
import random

class PLCInterface:
    def __init__(self, master):
        self.master = master
        master.title("PLC Interface")
        master.attributes('-fullscreen', True)

        self.connection_label = Label(master, text="Connection Status: ")
        self.connection_label.pack()

        self.connect_button = Button(master, text="Connect to PLC", command=self.simulate_connection)
        self.connect_button.pack()

        self.valve_states = [random.choice([0, 1]) for _ in range(12)]
        self.update_interval = 2000
        self.alarm_label = Label(master, text="", fg="red")
        self.alarm_label.pack()

    def simulate_connection(self):
        self.connection_label.config(text="Connection Status: Successful", fg="green")
        self.show_menu()

    def show_menu(self):
        self.connect_button.destroy()

        self.diagram_button = Button(self.master, text="Show Diagram", command=self.show_diagram)
        self.diagram_button.pack()

        self.master.after(self.update_interval, self.update_valve_states)

    def update_valve_states(self):
        self.valve_states = [random.choice([0, 1]) for _ in range(12)]
        print("Valve States:", self.valve_states)
        self.check_closed_valves()
        self.master.after(self.update_interval, self.update_valve_states)

    def check_closed_valves(self):
        closed_valves = [i + 1 for i, state in enumerate(self.valve_states) if state == 0]
        if closed_valves:
            self.alarm_label.config(text=f"Active Alarm: Valves {', '.join(map(str, closed_valves))} closed")
        else:
            self.alarm_label.config(text="")

    def show_diagram(self):
        if hasattr(self, 'diagram_window'):
            self.diagram_window.destroy()

        self.diagram_window = Toplevel(self.master)
        self.diagram_window.title("Piping Layout Diagram")

        canvas = Canvas(self.diagram_window, width=1200, height=800)
        canvas.pack(expand=YES, fill=BOTH)

        # Draw lead pipes from machines (Group 1)
        machine_positions = [(200, 50), (400, 50), (600, 50), (800, 50), (1000, 50), (1200, 50)]
        self.draw_machines(canvas, machine_positions, "Machine")

        # Draw valves and pipes (Group 1)
        valve_positions = [(200, 80), (400, 80), (600, 80), (800, 80), (1000, 80), (1200, 80)]
        rto_positions = [(200, 150), (400, 150), (600, 150), (800, 150), (1000, 150), (1200, 150)]
        atmosphere_positions = [(valve_positions[i][0] + 30, valve_positions[i][1] + 15) for i in range(6)]
        self.draw_valves_and_pipes(canvas, valve_positions, rto_positions, atmosphere_positions)

        # Draw lead pipes from machines (Group 2)
        machine_positions_group2 = [(200, 300), (400, 300), (600, 300), (800, 300), (1000, 300), (1200, 300)]
        self.draw_machines(canvas, machine_positions_group2, "Machine 2-")

        # Draw valves and pipes (Group 2)
        valve_positions_group2 = [(200, 330), (400, 330), (600, 330), (800, 330), (1000, 330), (1200, 330)]
        rto_positions_group2 = [(200, 400), (400, 400), (600, 400), (800, 400), (1000, 400), (1200, 400)]
        atmosphere_positions_group2 = [(valve_positions_group2[i][0] + 30, valve_positions_group2[i][1] + 15) for i in range(6)]
        self.draw_valves_and_pipes(canvas, valve_positions_group2, rto_positions_group2, atmosphere_positions_group2)

    def draw_machines(self, canvas, machine_positions, label_prefix):
        for i, position in enumerate(machine_positions):
            canvas.create_text(position[0] + 15, position[1] - 10, text=f"{label_prefix} {i + 1}")
            canvas.create_line(position[0] + 15, position[1], position[0] + 15, position[1] + 30, width=5)

    def draw_valves_and_pipes(self, canvas, valve_positions, rto_positions, atmosphere_positions):
        for i, (valve_position, rto_position, atmosphere_position) in enumerate(zip(valve_positions, rto_positions, atmosphere_positions)):
            color = "green" if self.valve_states[i] == 0 else "red"
            canvas.create_oval(valve_position[0], valve_position[1], valve_position[0] + 30, valve_position[1] + 30, outline="black", fill=color)

            # Draw pipes coming off the valve
            canvas.create_line(valve_position[0] + 15, valve_position[1] + 30, rto_position[0] + 15, rto_position[1], width=5)
            canvas.create_line(valve_position[0] + 30, valve_position[1] + 15, atmosphere_position[0], atmosphere_position[1], width=5)

            # Label pipes
            canvas.create_text(rto_position[0] + 60, rto_position[1] - 15, text=f"RTO Pipe {i + 1}", anchor=W)
            canvas.create_text(atmosphere_position[0] + 15, atmosphere_position[1], text="Atmosphere", anchor=W)

            # Label valve slightly higher and to the left
            canvas.create_text(valve_position[0] + 5, valve_position[1] + 30, text=f"Valve {i + 1}", anchor=E)

        # Draw RTO pipes connecting to each other
        for i in range(len(rto_positions) - 1):
            canvas.create_line(rto_positions[i][0] + 15, rto_positions[i][1], rto_positions[i + 1][0] + 15, rto_positions[i + 1][1], width=5)

if __name__ == "__main__":
    root = Tk()
    app = PLCInterface(root)
    root.mainloop()
