# torch\_mr
NVIDIA GPU Memory Reporting for PyTorch in IPython

This tool is built for visually profiling the GPU usage from PyTorch.

[](images/VRAM_monitoring.png)

# Installation
Clone the repo and install the module using pip install -e .

# Usage
Within a script, call one of the following:
- TorchMemoryReport.print\_vram() - Print bar graph of total VRAM available
- TorchMemoryReport.print\_reserved() - Prints bar graph of VRAM reserved by PyTorch
- TorchMemoryReport.print\_allocated() - Prints bar graph of VRAM allocated to current Tensors
- TorchMemoryReport.print\_all() - Prints all of the above.
- TorchMemoryReport.save\_snapshot(filename) - Saves a pickle object for profiling by [PyTorch Memory Viz](https://pytorch.org/memory\_viz)
- TorchMemoryReport.clear\_torch\_cache() - Clears unused cache (VRAM that is non-allocated but still reserved)
