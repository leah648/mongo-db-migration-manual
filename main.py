import importlib
import os

MIGRATIONS_PATH = "migrations"

def run_migrations():
    files = sorted(f for f in os.listdir(MIGRATIONS_PATH) if f.endswith(".py"))
    for f in files:
        module_name = f"{MIGRATIONS_PATH}.{f[:-3]}"
        module = importlib.import_module(module_name)
        print(f"Running migration: {f}")
        module.run()

if __name__ == "__main__":
    run_migrations()