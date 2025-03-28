#include <stdio.h>

int countZeroSumSubarrays(int arr[], int n) {
    int count = 0;

    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += arr[j];
            if (sum == 0) {
                count++;
            }
        }
    }

    return count;
}

int main() {
    int arr[] = {1, -1, 2, -2, 3, -3, 4, -4}; 
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Total subarrays with sum 0: %d\n", countZeroSumSubarrays(arr, n));
    return 0;
}
