import json

JSON_FILE = "payloads.json"

def rename_payloads():
    with open(JSON_FILE, "r") as f:
        payloads = json.load(f)

    print("Edit Payload Display Names, Categories, and Min Firmware")
    print("Press Enter to keep the current value.\n")

    changed = False
    for item in payloads:
        current_name = item.get("name", "")
        current_cat = item.get("category") or ""
        current_fw = item.get("min_fw") or ""
        source = item.get("source", "")
        print(f"  Source   : {source}")

        new_name = input(f"  Name     [{current_name}]: ").strip()
        if new_name and new_name != current_name:
            item["name"] = new_name
            changed = True
            print(f"  -> Name set to '{new_name}'")

        new_cat = input(f"  Category [{current_cat or 'Uncategorized'}]: ").strip()
        if new_cat and new_cat != current_cat:
            item["category"] = new_cat
            changed = True
            print(f"  -> Category set to '{new_cat}'")

        new_fw = input(f"  Min FW   [{current_fw or 'none'}]: ").strip()
        if new_fw and new_fw != current_fw:
            item["min_fw"] = new_fw
            changed = True
            print(f"  -> Min FW set to '{new_fw}'")
        print()

    if changed:
        with open(JSON_FILE, "w") as f:
            json.dump(payloads, f, indent=2)
        print("Saved changes to payloads.json")
    else:
        print("No changes made.")

if __name__ == "__main__":
    rename_payloads()
