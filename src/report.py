import json
from pathlib import Path

def generate_summary():
    base_dir = Path(__file__).resolve().parent.parent
    data_path = base_dir / "data" / "processed" / "verified_events.json"
    
    if not data_path.exists():
        print(" Data file not found!")
        return

    with open(data_path, "r") as f:
        events = json.load(f)

    print("\n" + "="*90)
    print(f"{'REBEL GROUP':<30} | {'WEAPON SYSTEM':<25} | {'STATUS'}")
    print("-" * 90)
    
    for event in events:
        nlp = event.get('nlp_analysis', {})
        
        # Handle cases where the model returns a dict instead of a string
        group = nlp.get('rebel_group', 'N/A')
        if isinstance(group, dict):
            group = group.get('name', group.get('group', 'Unknown'))
            
        weapon = nlp.get('weapon', 'N/A')
        status = nlp.get('verification_status', 'N/A')
        
        # Clean up 'None' or 'null' values for display
        group = "Unknown Group" if group is None or group == "null" else group
        weapon = "Not Specified" if weapon is None or weapon == "null" else weapon
        
        print(f"{str(group)[:29]:<30} | {str(weapon)[:24]:<25} | {status}")
    print("="*90 + "\n")

if __name__ == "__main__":
    generate_summary()