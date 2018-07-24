#include <vector>
#include <iostream>
#include <algorithm>

int gcd(int a, int b)
{
    if (b == 0 || b == 0)
        return 0;
    int rem = a % b;
    while (rem != 0)
    {
        a = b;
        b = rem;
        rem = a % b;
    }
    return b;
}

void rotate_arr(std::vector<int> &arr, int d)
{
    int len = arr.size();
    d = d % len;
    int partition_size = gcd(len, d);
    for (int i = 0; i < partition_size; i++)
    { // i - genertic index over all partitions
        int temp = arr[i];
        int j = i; // j - index to be replaced

        // Loop until we reach the end of cycle so that we can move to the next generic index of first partiton and traverse it's cycle etc.,
        while (true)
        {                  // can use `k % len != i` by keeping `k` outside, adding `d` to it at the end & remove the break condition inside
            int k = j + d; // k - index with which j has to be replaced
            if (k >= len)
                k -= len;
            if (k == i)
                break;
            arr[j] = arr[k];
            j = k;
        }

        arr[j] = temp;
    }
}

void reverse_arr(std::vector<int> &arr, int startInclusive, int endExclusive)
{
    std::reverse(std::begin(arr) + startInclusive, std::begin(arr) + endExclusive);
}

void rotate_arr_by_reversal(std::vector<int> &arr, int d)
{
    int length = arr.size();
    d = d % length;
    reverse_arr(arr, 0, length);
    reverse_arr(arr, 0, length - d);
    reverse_arr(arr, length - d, length);
}

int main()
{
    std::vector<int> test_arr{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14};
    std::vector<int> test_arr2{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14};
    int d = 8;
    rotate_arr(test_arr, d);
    std::for_each(std::begin(test_arr), std::end(test_arr), [](auto x) { std::cout << x << std::endl; });
    std::cout << "Test for Array rotation by Reversal" << std::endl;
    rotate_arr(test_arr2, d);
    std::for_each(std::begin(test_arr2), std::end(test_arr2), [](auto x) { std::cout << x << std::endl; });
    return 0;
}