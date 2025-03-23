import json

def simulate_dfa(dfa):
    current_state = dfa["start_state"]
    path = [current_state]
    
    for symbol in dfa["test_string"]:
        if symbol not in dfa["alphabet"]:
            return f"Invalid symbol '{symbol}' encountered!", "ERROR"
        
        if current_state in dfa["transitions"] and symbol in dfa["transitions"][current_state]:
            current_state = dfa["transitions"][current_state][symbol]
            path.append(current_state)
        else:
            return "Invalid transition detected!", "ERROR"
    
    status = "ACCEPTED" if current_state in dfa["accept_states"] else "REJECTED"
    return "Path: " + " → ".join(path), "Status: " + status

def load_dfa_from_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

file_path = "dfa.json"
dfa = load_dfa_from_file(file_path)
path, result = simulate_dfa(dfa)
print(path)
print(result)