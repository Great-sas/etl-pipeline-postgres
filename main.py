from src.extract import extract
from src.transform import transform
from src.load import load

if __name__ == "__main__":
    print("=== EXTRACT ===")
    extract()
    print()
    print("=== TRANSFORM ===")
    transform()
    print()
    print("=== LOAD ===")
    load()