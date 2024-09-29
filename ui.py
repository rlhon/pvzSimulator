import tkinter as tk
import pvzsim as pvz

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(pady = 15, padx = (15, 15))

frameButton = tk.Frame(root)
frameButton.pack(pady = 10, padx = (10, 10))

frameInputs = tk.Frame(root)
frameInputs.pack(pady = 10, padx = (10, 10))

frameState = tk.Frame(root)
frameState.pack(pady = 15, padx = (15, 15))

option_vars = []
option_menus = []

currMap = [["Brain", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],
           ["Brain", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],
           ["Brain", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],
           ["Brain", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],
           ["Brain", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"]]

BrainOption = [
    "Brain \t",
    "Brain Eaten"
]

plantOptions = [
    "Brain  \t",
    "Empty  \t",
    "Sunflower  ",
    "Peashooter ",
    "Wallnut  \t",
    "Potato Mine", 
    "Snow Pea   ",
    "Chomper",
    "Repeater\t",
    "Puff shroom",
    "Fume shroom",
    "Scaredy shroom",
    "Squash\t",
    "Threepeater",
    "Spikeweed",
    "Torchwood",
    "Split Pea",
    "Starfruit",
    "Magnet shroom",
    "Kernel Pult",
    "Umbrella Leaf",    
]

zombieOptions = [
    "Imp",
    "Conehead",
    "Buckethead",
    "Pole Vaulter",
    "Football",
    "Digger",
    "Bungee",
    "Ladder"
]

rowOptions = [
    "1",
    "2",
    "3",
    "4",
    "5"
]
         
def option_change(row, col):
    currMap[row][col] = op.get()
    
def hello():
    print("hello")

# Frame
for i in range(5):
    for j in range(7):
        if j == 0:
            
            #label = tk.Label(frame, text ="Brain")
            #label.grid(row = i, column = j, pady = (10,10))
            variableB = tk.StringVar(frame)
            variableB.set(BrainOption[0])
            opB = tk.OptionMenu(frame, variableB, *BrainOption)
            opB.grid(row = i, column = j)
            
            option_vars.append(variableB)
            option_menus.append(opB)
        else:
            variable00 = tk.StringVar(frame)
            variable00.set(plantOptions[1])
            op = tk.OptionMenu(frame, variable00, *plantOptions)
            op.grid(row = i, column = j)
            
            option_vars.append(variable00)
            option_menus.append(op) 
            
            #variable00.trace_add("write", option_change(i,j))
            #op.trace("w", hello)
            #op.trace("w", option_change(i,j))
    

#define reset button
def reset():
    for widget in frame.winfo_children():
        widget.destroy()
    option_vars.clear()
    option_menus.clear()
    for i in range(5):
        for j in range(7):
            if j == 0:
                #label = tk.Label(frame, text ="Brain")
                #label.grid(row = i, column = j, pady  = (10,10))
                variableB = tk.StringVar(frame)
                variableB.set(BrainOption[0])
                opB = tk.OptionMenu(frame, variableB, *BrainOption)
                opB.grid(row = i, column = j)
                
                option_vars.append(variableB)
                option_menus.append(opB)
            else:
                variable00 = tk.StringVar(frame)
                variable00.set(plantOptions[1])
                op = tk.OptionMenu(frame, variable00, *plantOptions)
                op.grid(row = i, column = j)
                
                
                option_vars.append(variable00)
                option_menus.append(op)
                #op.trace("w", simulate)        
                #op.trace("w", option_change(i,j))
   
def simulate():
    x = pvz.simulate(currMap)
    for i in range(5):
        for j in range(7):
            starts = 0
            for k in range(0, len(plantOptions)):
                if plantOptions[k].startswith(x[i][j]):
                    starts = k #index
            if j == 0:
                if(starts == 0):
                    label = tk.Label(frameState, text ="Brain", fg = "red")
                    label.grid(row = i, column = j, pady = (10,10))
                else:
                    label = tk.Label(frameState, text ="Eaten", fg = "green")
                    label.grid(row = i, column = j, pady = (10,10))
            else:
                if (starts == 1):
                    label2 = tk.Label(frameState, text = "Empty", fg = "green")
                    label2.grid(row= i, column = j, pady = (10,10))
                else:
                    label2 = tk.Label(frameState, text = plantOptions[starts], fg = "green")
                    label2.grid(row= i, column = j, pady = (10,10))
                
    #update Frame Results
    
def simulateStep():
    x, status = pvz.simulateStep(currMap, zombieTypeName.get(), zombRow.get(), 6) # return simulated map
    print(x)
    
    for widget in frameState.winfo_children():
                widget.destroy()

    
    for i in range(5):
        for j in range(7):
            starts = 0
            for k in range(0, len(plantOptions)):
                if plantOptions[k].lower().startswith(x[i][j]):
                    starts = k  #index
            if j == 0:
                if(starts == 0):
                    label = tk.Label(frameState, text ="Brain", fg = "red")
                    label.grid(row = i, column = j, pady = (10,10))
                else:
                    label = tk.Label(frameState, text ="Eaten", fg = "green")
                    label.grid(row = i, column = j, pady = (10,10))
            else:
                if (starts == 1):
                    label2 = tk.Label(frameState, text = "Empty", fg = "green")
                    label2.grid(row= i, column = j, pady = (10,10))
                else:
                    label2 = tk.Label(frameState, text = plantOptions[starts], fg = "green")
                    label2.grid(row= i, column = j, pady = (10,10))
    
    #update Frame Results
         
# Frame Buttons
resetButton = tk.Button(frameButton, text = "Reset", command = reset)
resetButton.pack(side = "left", padx = (10,10))
simulateButton = tk.Button(frameButton, text = "Simulate", command = simulate) #remember your parameters
simulateButton.pack(side = "left", padx = (10,10))
simulateStepButton = tk.Button(frameButton, text = "Simulate Step", command = simulateStep)
simulateStepButton.pack(side = "left", padx = (10,10))


#Frame Inputs
LabelChooseZomb = tk.Label(frameInputs, text = "Choose Zombie: ")
LabelChooseZomb.pack(side = "left", padx = (10, 0))
zombieTypeName = tk.StringVar(frameInputs)
zombieTypeName.set(zombieOptions[0]) #zombieOptions[0]
zombOp = tk.OptionMenu(frameInputs, zombieTypeName, *zombieOptions) #*zombieOptions
zombOp.pack(side = "left", padx = (10,10))

LabelChooseRow = tk.Label(frameInputs, text = "Choose Row: ")
LabelChooseRow.pack(side = "left", padx = (10, 0))
zombRow = tk.StringVar(frameInputs)
zombRow.set(rowOptions[0]) #rowOptions[0]
zombRowOp = tk.OptionMenu(frameInputs, zombRow, *rowOptions)
zombRowOp.pack(side = "left", padx = (10,10))


# Frame Results
#default display of results
for i in range(5):
    for j in range(7):
        if j == 0:
            label = tk.Label(frameState, text ="Brain", fg = "green")
            label.grid(row = i, column = j, pady = (10,10))
        else:
            label2 = tk.Label(frameState, text = "Empty", fg = "green")
            label2.grid(row= i, column = j, pady = (10,10))
            
root.mainloop()


