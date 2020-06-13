#include "common.h"

// If you are writing in C++, you need to use extern "C" so that the compiler does not mangle the namespace. 
extern "C" EXPORT void inplace_accumulate(double *arr, int n);
extern "C" EXPORT double sum(const double *arr, int n);

double sum(const double *arr, int n){
    double x = 0.0;
    for (int i=0;i<n;i++){
        x += arr[i];
    }
    return x;
}

void inplace_accumulate(double *arr, int n){
    for (int i=1;i<n;i++)
        arr[i] = arr[i-1] + arr[i];
}

