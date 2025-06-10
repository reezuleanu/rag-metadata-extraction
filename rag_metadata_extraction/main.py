from custom_runner import CustomRunner

YAML_PATH = "dev/inputs/Determine and extract metadatas.yaml"


runner = CustomRunner.from_yaml(YAML_PATH)

cost, output = runner.load_run()

print(f"Cost: ${cost}")
print("=" * 25)
print("Output: ")
for item in output:
    for metadata in item.get("metadatas", []):
        print("=" * 5)
        for k, v in metadata.items():
            print(f"{k}: {v}")
