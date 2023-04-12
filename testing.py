import yaml

with open('ansible/playbook.yaml', 'r') as file:
    try:
        print(yaml.safe_load(file))
    except yaml.YAMLError as exe:
        print(exe)