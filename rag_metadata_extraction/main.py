from docetl.runner import DSLRunner

YAML_PATH = "dev/inputs/Determine and extract metadatas.yaml"

runner = DSLRunner.from_yaml(YAML_PATH)

cost = runner.load_run_save()

print(f"Cost: ${cost}")
