import json

JSON_FILE = "payloads.json"

def rename_payloads():
    with open(JSON_FILE, "r") as f:
        payloads = json.load(f)

    print("Edit Payload Display Names and Min FW")
    print("Press Enter to keep the current value.\n")

    changed = False
    for item in payloads:
        current_name = item.get("name", "")
        current_fw = item.get("min_fw") or ""
        source = item.get("source", "")
        print(f"  Source : {source}")

        new_name = input(f"  Name   [{current_name}]: ").strip()
        if new_name and new_name != current_name:
            item["name"] = new_name
            changed = True
            print(f"  -> Name set to '{new_name}'")

        new_fw = input(f"  Min FW [{current_fw or 'not set'}]: ").strip()
        if new_fw and new_fw != current_fw:
            item["min_fw"] = new_fw
            changed = True
            print(f"  -> Min FW set to '{new_fw}'")
        elif not new_fw and current_fw:
            pass  # keep existing if user just pressed Enter
        print()

    if changed:
        with open(JSON_FILE, "w") as f:
            json.dump(payloads, f, indent=2)
        print("Saved changes to payloads.json")
    else:
        print("No changes made.")

if __name__ == "__main__":
    rename_payloads()
