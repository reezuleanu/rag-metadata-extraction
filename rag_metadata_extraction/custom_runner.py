import time

from rich.panel import Panel
from docetl.runner import DSLRunner


class CustomRunner(DSLRunner):
    def load_run(self, serialize_output: bool = False) -> tuple[float, any]:
        """Load and run the pipeline, return the output directly

        Returns:
            tuple[float, dict]: the cost and the output
        """
        output_path = self.get_output_path(require=True)

        # Print the query plan
        self.print_query_plan()

        start_time = time.time()

        if self.last_op_container:
            self.load()
            self.console.rule("[bold]Pipeline Execution[/bold]")
            output, _, _ = self.last_op_container.next()
            if serialize_output:
                self.save(output)

        execution_time = time.time() - start_time

        # Print execution summary
        summary = (
            f"Cost: [green]${self.total_cost:.2f}[/green]\n"
            f"Time: {execution_time:.2f}s\n"
            + (
                f"Cache: [dim]{self.intermediate_dir}[/dim]\n"
                if self.intermediate_dir
                else ""
            )
            + f"Output: [dim]{output_path}[/dim]"
        )
        self.console.log(Panel(summary, title="Execution Summary"))

        return self.total_cost, output
