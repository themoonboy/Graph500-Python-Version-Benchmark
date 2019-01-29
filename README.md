# Graph500-Python-Version-Benchmark
This is a Python implementation on [Graph500 benchmark](https://graph500.org), where there are only C version open-source codes and Octave version provided, you could easily find the official reference code [here](https://graph500.org/?page_id=47) or from their [github](https://github.com/graph500/graph500).

In convenient for private usage, I just mimic the Octave version of original Graph500 benchmark and rewrite into this Python version. I try to tightly follow the data structure and work flow used in Octave reference code, and find closest way to transfer them into Python language, all these corresponding codes located in folder [graph500_reference_code](https://github.com/themoonboy/Graph500-Python-Version-Benchmark/tree/master/graph500_reference_code).

## Folders
Here is a shortly introduction on folder in this repository.
* `graph500_reference_code`: This one include all Python codes tightly imitate originral Octave reference codes.
* `graph500_custom`: This one include modified codes on basis of `graph500_reference_code` but introduce parallelization on BFS section.
* `graph500_custom_memmap`: This one include modified codes on basis `graph500_custom` but call the  `numpy.memmap` to store large-scale matrix on hard disk (files) rather in RAM. This implementation aimed to slove the memory for creating a very large numpy matrix. Note that to run this part of code, you should firstly put an empty folder named "temp" on same directory for storage use.
* `ipython codes`: This contains the ipython-jupyter work sheet for developing all three parts of codes above. Same work located on same name of jupyter notebook, respectively.

## Run the codes
For python folders, simply type
```
python driver.py
```
Or use jupyter notebook to run ipython codes directly. Note to set parameter (SCALE, edgefactor) as you like.

## Customized works
As introduced above, the customize work on this benchmark mainly focus on  `Parallelize BFS` and `call hard disk storage`.

## Incompleteness
Note that, my translation from Octave to Python is incomplete, especially on following parts:
1. Kernels: The original reference codes including driver, edge-generator, kernel_1 (to generate a graph), kernel_2 (top_down BFS), kernel_3 (SSSP), validation and output. But all my works are ingore kernel_3, i.e., the SSSP part, since it is my concentration for enhance the BFS performance only and see what could do if meet inadequate RAM storage.
2. Functions: This is a initail version of my development about Graph500 Python benchmark, therefore, if not totally affect the evaluation of whole codes, I just ignore some technical details and simplify some functions in comparison of original Octave reference codes. These simplification or ingorance mainly located on validation.py and output.py.

## Learning Material
If you are interested of learning Graph500 benchmark, I strongly recommand to firstly learn their development methods from official [tutorial](https://graph500.org/?page_id=12), where the attache codes are wrote in Octave, which looks like MATLAB, but different to some extent. In addition, have some basic knowledge on MPI and bitmap to storge graph may be helpful to understand the C version of their open-source codes, since there are more people play with the C rather Octave benchmarks.
