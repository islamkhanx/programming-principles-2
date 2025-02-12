import json
from typing import List


def output_table(table_data: List[dict]) -> None:
    table_data = [
        x["l1PhysIf"]["attributes"] for x in table_data
    ]
    print("Interface Status")
    print("=" * 80)
    print(f'{"DN":<50} {"Description":<20}',
          f'{"Speed":<7} {"MTU":<5}')

    print(f'{"-" * 49:<50} {"-" * 19:<20}',
          f'{"-" * 8:<7} {"-" * 4:<5}')

    for row in table_data:
        print(f'{row["dn"]:<50} {row["descr"]:<20}',
              f'{row["speed"]:<7} {row["mtu"]:<5}')


def main(path: str) -> None:
    with open(path, 'r') as f:
        data = json.load(f)

    output_table(data["imdata"])


if __name__ == "__main__":
    file_path = "Lab04/sample_data.json"
    main(file_path)
