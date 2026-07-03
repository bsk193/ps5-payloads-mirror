import json

JSON_FILE = "payloads.json"

def rename_payloads():
    with open(JSON_FILE, "r") as f:
        payloads = json.load(f)

    print("Rename Payload Display Names")
    print("Press Enter to keep the current name.\n")

    changed = False
    for item in payloads:
        current_name = item.get("name", "")
        source = item.get("source", "")
        print(f"  Source : {source}")
        new_name = input(f"  Name   [{current_name}]: ").strip()
        if new_name and new_name != current_name:
            item["name"] = new_name
            changed = True
            print(f"  -> Renamed to '{new_name}'")
        print()

    if changed:
        with open(JSON_FILE, "w") as f:
            json.dump(payloads, f, indent=2)
        print("Saved changes to payloads.json")
    else:
        print("No changes made.")

if __name__ == "__main__":
    rename_payloads()
