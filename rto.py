from tkinter import *
from pylogix import PLC

class PLCInterface:
    def __init__(self, master):
        self.master = master
        master.title("PLC Interface")
        master.attributes('-fullscreen', True)

        self.connection_label = Label(master, text="Connection Status: ")
        self.connection_label.pack()

        self.connect_button = Button(master, text="Connect to PLC", command=self.connect_to_plc)
        self.connect_button.pack()

    def connect_to_plc(self):
        plc_ip = "your_plc_ip_address"
        plc = PLC()
        try:
            plc.IPAddress = plc_ip
            plc.Open()
            self.connection_label.config(text="Connection Status: Successful", fg="green")
            self.show_menu()
        except Exception as e:
            self.connection_label.config(text=f"Connection Status: Failed\nError: {e}", fg="red")

    def show_menu(self):
        self.connect_button.destroy()

        self.diagram_button = Button(self.master, text="Show Diagram", command=self.show_diagram)
        self.diagram_button.pack()

    def show_diagram(self):
        # Add code to read PLC tags and update valve states
        # For now, let's simulate some values
        valve_1_state = True  # Replace with actual PLC tag value
        valve_2_state = False  # Replace with actual PLC tag value
        valve_3_state = True  # Replace with actual PLC tag value
        valve_4_state = False  # Replace with actual PLC tag value

        diagram_window = Toplevel(self.master)
        diagram_window.title("Regenerative Thermal Oxidizer Diagram")

        valves = [valve_1_state, valve_2_state, valve_3_state, valve_4_state]
        valve_labels = []

        for i, state in enumerate(valves):
            label = Label(diagram_window, text=f"Valve {i+1}")
            label.grid(row=i, column=0)
            valve_labels.append(label)

            color = "green" if state else "red"
            valve_labels[i].config(bg=color)

if __name__ == "__main__":
    root = Tk()
    app = PLCInterface(root)
    root.mainloop()