from tkinter import *

class PLCInterface:
    def __init__(self, master):
        self.master = master
        master.title("PLC Interface")
        master.attributes('-fullscreen', True)

        self.connection_label = Label(master, text="Connection Status: ")
        self.connection_label.pack()

        self.connect_button = Button(master, text="Connect to PLC", command=self.simulate_connection)
        self.connect_button.pack()

        # Simulated PLC variables
        self.valve_states = [True, False, True, False, True, False]

    def simulate_connection(self):
        # Simulating PLC connection
        self.connection_label.config(text="Connection Status: Successful", fg="green")
        self.show_menu()

    def show_menu(self):
        self.connect_button.destroy()

        self.diagram_button = Button(self.master, text="Show Diagram", command=self.show_diagram)
        self.diagram_button.pack()

    def show_diagram(self):
        diagram_window = Toplevel(self.master)
        diagram_window.title("Piping Layout Diagram")

        self.canvas = Canvas(diagram_window, width=1200, height=800)
        self.canvas.pack(expand=YES, fill=BOTH)

        # Draw lead pipes from machines (Group 1)
        machine_positions = [(200, 50), (400, 50), (600, 50), (800, 50), (1000, 50), (1200, 50)]
        self.draw_machines(machine_positions, "Machine")

        # Draw valves and pipes (Group 1)
        valve_positions = [(200, 80), (400, 80), (600, 80), (800, 80), (1000, 80), (1200, 80)]
        rto_positions = [(200, 150), (400, 150), (600, 150), (800, 150), (1000, 150), (1200, 150)]
        self.draw_valves_and_pipes(valve_positions, rto_positions)

        # Draw lead pipes from machines (Group 2)
        machine_positions_group2 = [(200, 300), (400, 300), (600, 300), (800, 300), (1000, 300), (1200, 300)]
        self.draw_machines(machine_positions_group2, "Machine 2-")

        # Draw valves and pipes (Group 2)
        valve_positions_group2 = [(200, 330), (400, 330), (600, 330), (800, 330), (1000, 330), (1200, 330)]
        rto_positions_group2 = [(200, 400), (400, 400), (600, 400), (800, 400), (1000, 400), (1200, 400)]
        self.draw_valves_and_pipes(valve_positions_group2, rto_positions_group2)

        # Display the alarm label in the diagram screen
        alarm_text = "Active Alarm: Valve 2 is closed"
        self.canvas.create_text(600, 700, text=alarm_text, font=("Helvetica", 16), fill="red")

    def draw_machines(self, machine_positions, label_prefix):
        for i, position in enumerate(machine_positions):
            self.canvas.create_text(position[0] + 15, position[1] - 10, text=f"{label_prefix} {i + 1}")
            self.canvas.create_line(position[0] + 15, position[1], position[0] + 15, position[1] + 30, width=5)

    def draw_valves_and_pipes(self, valve_positions, rto_positions):
        atmosphere_positions = [(valve_position[0] + 45, valve_position[1] + 15) for valve_position in valve_positions]

        for i, (valve_position, rto_position, atmosphere_position) in enumerate(zip(valve_positions, rto_positions, atmosphere_positions)):
            color = "green" if self.valve_states[i] else "red"
            self.canvas.create_oval(valve_position[0], valve_position[1], valve_position[0] + 30,
                                valve_position[1] + 30, outline="black", fill=color)

        # Draw pipes coming off the valve to RTO
            self.canvas.create_line(valve_position[0] + 15, valve_position[1] + 30, rto_position[0] + 15, rto_position[1], width=5)

        # Draw pipes coming off the valve to atmosphere
            self.canvas.create_line(valve_position[0] + 15, valve_position[1] + 15, atmosphere_position[0], atmosphere_position[1], width=5)

        # Label pipes
            self.canvas.create_text(valve_position[0] + 60, rto_position[1] - 15, text=f"RTO Pipe {i + 1}", anchor=W)
        self.canvas.create_text(atmosphere_position[0] + 60, atmosphere_position[1] - 15, text="Atmosphere", anchor=W)

        # Label valve slightly higher and to the left
        self.canvas.create_text(valve_position[0] + 5, valve_position[1] + 30, text=f"Valve {i + 1}", anchor=E)

        # Draw RTO pipes connecting to each other
        if i < len(rto_positions) - 1:
            self.canvas.create_line(rto_positions[i][0] + 15, rto_positions[i][1], rto_positions[i + 1][0] + 15,
                                    rto_positions[i + 1][1], width=5)


if __name__ == "__main__":
    root = Tk()
    app = PLCInterface(root)
    root.mainloop()
