import pycuda.autoinit
import pycuda.driver as drv
import numpy
from pycuda.compiler import SourceModule
import time


mod = SourceModule("""
__global__ void multiply_them(float *dest, float *a, float *b)
{
  const int i = threadIdx.x;
  dest[i] = a[i] * b[i];
}
""")

multiply_them = mod.get_function("multiply_them")

a = numpy.random.randn(400).astype(numpy.float32)
b = numpy.random.randn(400).astype(numpy.float32)

dest = numpy.zeros_like(a)
start = time.time()
multiply_them(
        drv.Out(dest), drv.In(a), drv.In(b),
        block=(400,1,1), grid=(1,1)
        )

end = time.time()
print(dest)

parallel = end-start
print(parallel)


mul = numpy.zeros_like(a)
start = time.time()
for i in range(len(a)):
    mul[i]=a[i]*b[i]
end = time.time()
print(mul)


serial =end-start
if(mul.all()==dest.all()):
    print('EQUAL')
print(serial)
if(parallel>serial):
    print('Wtf man')
else:
    print('Works man')
