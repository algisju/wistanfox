#include <memory>
#include <iostream>
#include <cuda_runtime.h>
#include <string>
// Main Program
using namespace std;
int main(void)
{
int device_Count = 0;
cudaGetDeviceCount(&device_Count);
if (device_Count == 0)
	{
	printf("There are no available device(s) that support CUDA\n");
	}
else
	{
	printf("Detected %d CUDA Capable device(s)\n", device_Count);
	}
int device=0;int driver_Version=0;int runtime_Version=0;
cudaDeviceProp device_Property;
cudaGetDeviceProperties(&device_Property, device);
printf("\nDevice %d: \"%s\"\n", device, device_Property.name);
cudaDriverGetVersion(&driver_Version);
cudaRuntimeGetVersion(&runtime_Version);
printf(" CUDA Driver Version / Runtime Version %d.%d / %d.%d\n", driver_Version / 1000, (driver_Version% 100) / 10, runtime_Version / 1000, (runtime_Version % 100) / 10);
printf(" Total amount of global memory: %.0f MBytes (%llu bytes)\n",(float)device_Property.totalGlobalMem / 1048576.0f, (unsigned long long) device_Property.totalGlobalMem);
printf(" (%2d) Multiprocessors", device_Property.multiProcessorCount );
printf(" GPU Max Clock rate: %.0f MHz (%0.2f GHz)\n", device_Property.clockRate * 1e-3f,device_Property.clockRate * 1e-6f);
printf(" Maximum number of threads per multiprocessor: %d\n",device_Property.maxThreadsPerMultiProcessor);
printf(" Maximum number of threads per block: %d\n", device_Property.maxThreadsPerBlock);
printf(" Max dimension size of a thread block (x,y,z): (%d, %d, %d)\n",
	device_Property.maxThreadsDim[0],
	device_Property.maxThreadsDim[1],
	device_Property.maxThreadsDim[2]);
printf(" Max dimension size of a grid size (x,y,z): (%d, %d, %d)\n",
	device_Property.maxGridSize[0],
	device_Property.maxGridSize[1],
	device_Property.maxGridSize[2]);
printf( " Total amount of global memory: %.0f MBytes (%llu bytes)\n",
	(float)device_Property.totalGlobalMem / 1048576.0f, 
	(unsigned long long)device_Property.totalGlobalMem);
printf(" Memory Clock rate: %.0f Mhz\n", device_Property.memoryClockRate * 1e-3f);
printf(" Memory Bus Width: %d-bit\n", device_Property.memoryBusWidth);
if (device_Property.l2CacheSize)
	{
	printf(" L2 Cache Size: %d bytes\n", device_Property.l2CacheSize);
	}	
printf(" Total amount of constant memory: %lu bytes\n", device_Property.totalConstMem);
printf(" Total amount of shared memory per block: %lu bytes\n", device_Property.sharedMemPerBlock);
printf(" Total number of registers available per block: %d\n", device_Property.regsPerBlock);
}
