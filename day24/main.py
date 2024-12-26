file = open("day24/data.txt")
initial_values, gates = file.read().split("\n\n")
initial_values = initial_values.split("\n")
gates = gates.split("\n")

wires = {}
for value in initial_values:
    name, value = value.split(": ")
    wires[name] = int(value)


queue = []
gates_new = []
for gate in gates:
    in1, op, in2, out = gate.replace("->", "").split()
    queue.append([in1, op, in2, out])
    gates_new.append([in1, op, in2, out])
    wires[out] = None

gates = gates_new

while queue:
    in1, op, in2, out = queue.pop(0)
    if wires[in1] == None or wires[in2] == None:
        queue.append([in1, op, in2, out])
        continue
    if op == "AND":
        wires[out] = wires[in1] & wires[in2]
    elif op == "OR":
        wires[out] = wires[in1] | wires[in2]
    elif op == "XOR":
        wires[out] = wires[in1] ^ wires[in2]

z_wires = []
for key, value in list(wires.items()):
    if key[0] == "z":
        z_wires.append((key, value))

z_wires = sorted(z_wires, key=lambda x: x[0], reverse=True)

out = int("".join([str(value) for wire, value in z_wires]), 2)

print(f"part 1: {out}")

def find_gates_by_output(out_target):
    result = []
    for gate in gates:
        in1, op, in2, out = gate
        if out == out_target:
            result.append(gate)
    return result

def find_gates_by_input(in_target):
    result = []
    for gate in gates:
        in1, op, in2, out = gate
        if in1 == in_target or in2 == in_target:
            result.append(gate)
    return result

# idea here is to check each wire is going to the right gates,
# if they are not going to the write gates, they are sus.
wire_labels = {}
errors = []
for wire in wires.keys():
    wire_labels[wire] = None
    outs = {}
    ins = {}
    outputs = find_gates_by_output(wire)
    inputs = find_gates_by_input(wire)
    
    for output in outputs:
        in1, op, in2, out = output
        if op not in outs:
            outs[op] = 0
        outs[op] += 1
    
    for input in inputs:
        in1, op, in2, out = input
        if op not in ins:
            ins[op] = 0
        ins[op] += 1

    # check that ALL input wires, x or y, go into an AND and XOR gate
    if wire[0] == 'x' or wire[0] == 'y':
        if len(outs) == 0 and len(ins) == 2 and ins.get('XOR', None) == 1 and ins.get('AND', None) == 1:
            wire_labels[wire] = 'in'
        else:
            errors.append(wire)
        continue
    
    # check that ALL output wires, z, come out of an XOR gate
    # EXCEPT if it is the last bit, it must come out of an OR gate
    elif wire[0] == 'z':
        if len(ins) == 0 and len(outs) == 1 and outs.get('XOR', None) == 1:
            wire_labels[wire] = 'out'
        elif wire == "z45" and len(outs) == 1 and outs.get('OR', None) == 1 and len(ins) == 0:
            wire_labels[wire] = 'out'
        else:
            errors.append(wire)
        continue

    # Checking the wires that feed into the OR gate that produces the 
    # carry output for the full adder.
    elif len(ins) == 1 and ins.get('OR', None) == 1 and len(outs) == 1 and outs.get('AND', None) == 1:
        and_gate = find_gates_by_output(wire)
        in1, op, in2, out = and_gate[0]
        if in1[0] == 'x' and in2[0] == 'y' or in1[0] == 'y' and in2[0] == 'x':
            wire_labels[wire] = 'd'
        else:
            wire_labels[wire] = 'c'
        continue
    
    # checking that the wire outputing from XOR gate with the inputs wires
    # and inputing into the XOR gate that produces the output wire is correct.
    elif len(outs) == 1 and outs.get('XOR', None) == 1 and len(ins) == 2 and ins.get('XOR', None) == 1 and ins.get('AND', None) == 1:
        xor_gate = find_gates_by_output(wire)
        in1, op, in2, out = xor_gate[0]
        if in1[0] == 'x' and in2[0] == 'y' or in1[0] == 'y' and in2[0] == 'x':
            wire_labels[wire] = 'a'
        else:
            errors.append(wire) 
        continue
    
    # check that ALL wires carrying the "carry" between full adders is coming out of an OR gate
    # and is going into an AND gate and XOR gate.
    elif len(outs) == 1 and outs.get('OR', None) == 1 and len(ins) == 2 and ins.get('AND', None) == 1 and ins.get('XOR', None) == 1:
        wire_labels[wire] = 'carry'
        continue

    # check the carry wire coming out of the half adder is coming out of an AND gate
    # and is going into an AND gate and XOR gate.
    elif len(outs) == 1 and  outs.get('AND', None) == 1 and len(ins) == 2 and ins.get('AND', None) == 1 and ins.get('XOR', None) == 1:
        and_gate = find_gates_by_output(wire)
        in1, op, in2, out = and_gate[0]
        if in1 == 'x00' and in2 == 'y00' or in1 == 'y00' and in2 == 'x00':
            wire_labels[wire] = 'carry'
        else:
            errors.append(wire)
        continue

    else:
        errors.append(wire)

errors.sort()
ans = ",".join(errors)

print(f"part 2: {ans}")