import os


class Base:
    def output_result(
        self, output_dir: str, filename: str, rows: list[list[str]]
    ) -> None:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(f"{output_dir}/{filename}", "w") as f:
            for row in rows:
                f.write(f"{'\t'.join(row)}\n")
