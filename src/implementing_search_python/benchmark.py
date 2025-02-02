import time
from pathlib import Path


class Benchmark:
    def __init__(self, method: str, reads: Path, reference: Path, default_path: Path = Path("python_benchmark.csv"), benchmark_interval: int = 10, mismatches=0):
        self.method = method
        self.reads = reads
        self.reference = reference
        self.benchmark_file = open(default_path, "a")
        if default_path.stat().st_size == 0:
            self.benchmark_file.write("method,mismatches,reference_file,reads_file,time,read_n\n")
        self.start_time = time.time()
        self.interval = benchmark_interval
        self.mismatches = mismatches

    def write(self, read_num: int):
        self.benchmark_file.write(f"{self.method},{self.mismatches},{self.reference},{self.reads},{time.time()-self.start_time},{read_num}\n")

