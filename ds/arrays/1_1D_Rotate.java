import java.util.Arrays;
import java.util.stream.IntStream;

class Main {

    public static int gcd(int a, int b) {
        if (a == 0 || b == 0)
            return 0;
        int rem = a % b;
        while (rem != 0) {
            a = b;
            b = rem;
            rem = a % b;
        }
        return b;
    }

    public static void rotate_arr(int[] arr, int d) {
        int partitionSize = gcd(arr.length, d);
        for (int i = 0; i < partitionSize; i++) {
            int j = i;
            int temp = arr[i];
            while (true) {
                int k = j + d;
                if (k >= arr.length)
                    k -= arr.length;
                if (k == i)
                    break;
                arr[j] = arr[k];
                j = k;
            }
            arr[j] = temp;
        }
    }

    public static void main(String... args) {
        int[] testArr = IntStream.range(1, 15).toArray();
        int d = 6;
        rotate_arr(testArr, d);
        System.out.println(Arrays.toString(testArr));
    }
}