#include <iostream>
#include <cuda.h>
#include <cuda_runtime.h>
__global__ void gpuAdd(int d_a, int d_b, int *d_c)
{
	//execute in gpu
	*d_c = d_a + d_b;
}

int main(void)
{
	int h_c;
	int *d_c;
	cudaMalloc((void**)&d_c, sizeof(int));
	gpuAdd << <1, 1 >> > (8, 1, d_c);
	cudaMemcpy(&h_c, d_c, sizeof(int), cudaMemcpyDeviceToHost);
	printf("Yayaya 8 + 3 = %d\n", h_c);
	cudaFree(d_c);
	return 0;
}
