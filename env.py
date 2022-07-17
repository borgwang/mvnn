import os

DEBUG = int(os.getenv("DEBUG", "0"))
GRAPH = int(os.getenv("GRAPH", "0"))
LAZY = int(os.getenv("LAZY", "0"))
BACKEND = os.getenv("BACKEND", "opencl")
OPT1 = int(os.getenv("OPT1", "0"))

assert BACKEND in ("numpy", "opencl", "cuda"), f"backend {BACKEND} not supported!"

