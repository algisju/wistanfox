
#include <stdio.h>
#include <cuda.h>

#define SIZE	4096

__global__ void VectorAdd(int *a, int *b, int *c, int n)
{
	int i = threadIdx.x;
	if (i < n)
		c[i] = a[i] + b[i];
}

int main()
{

	int nDevices;

	cudaGetDeviceCount(&nDevices);
	for (int i = 0; i < nDevices; i++) {
		cudaDeviceProp prop;
		cudaGetDeviceProperties(&prop, i);
		printf("Device Number: %d\n", i);
		printf("  Device name: %s\n", prop.name);
		printf("  Memory Clock Rate (KHz): %d\n",
			prop.memoryClockRate);
		printf("  Memory Bus Width (bits): %d\n",
			prop.memoryBusWidth);
		printf("  Peak Memory Bandwidth (GB/s): %f\n\n",
			2.0*prop.memoryClockRate*(prop.memoryBusWidth/8)/1.0e6);
	}


	int *a, *b, *c;
	int *d_a, *d_b, *d_c;

	a = (int *)malloc(SIZE*sizeof(int));
	b = (int *)malloc(SIZE*sizeof(int));
	c = (int *)malloc(SIZE*sizeof(int));

	cudaMalloc( &d_a, SIZE*sizeof(int));
	cudaMalloc( &d_b, SIZE*sizeof(int));
	cudaMalloc( &d_c, SIZE*sizeof(int));

	for( int i = 0; i < SIZE; ++i )
	{
		a[i] = i;
		b[i] = i;
		c[i] = i;
	}

	cudaMemcpy( d_a, a, SIZE*sizeof(int), cudaMemcpyHostToDevice );
	cudaMemcpy( d_b, b, SIZE*sizeof(int), cudaMemcpyHostToDevice );
	cudaMemcpy( d_c, c, SIZE*sizeof(int), cudaMemcpyHostToDevice );

	VectorAdd<<< 1, SIZE >>>(d_a, d_b, d_c, SIZE);
	
	cudaMemcpy( c, d_c, SIZE*sizeof(int), cudaMemcpyDeviceToHost );

	for( int i = 0; i < 10; ++i)
		printf("c[%d] = %d\n", i, c[i]);

	free(a);
	free(b);
	free(c);

	cudaFree(d_a);
	cudaFree(d_b);
	cudaFree(d_c);

	return 0;
}
