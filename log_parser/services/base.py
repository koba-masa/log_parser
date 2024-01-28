import os


class Base:
    def output_result(
        self, output_dir: str, filename: str, headers: list[str], rows: list[list[str]]
    ) -> None:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(f"{output_dir}/{filename}", "w") as f:
            f.write(f"{'\t'.join(headers)}\n")
            for row in rows:
                f.write(f"{'\t'.join(row)}\n")
