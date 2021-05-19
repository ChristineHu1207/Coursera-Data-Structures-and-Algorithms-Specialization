import java.util.*;

public class Inversions {

    private static long numberOfInversions;

    private static long getNumberOfInversions(int[] a, int[] b, int left, int right) {
        numberOfInversions = 0;
        if (right <= left + 1) {
            return numberOfInversions;
        }
        mergeSort(a, b, left, right);

        return numberOfInversions;
    }

    private static void mergeSort(int arr[], int[] b, int low, int high) {
        int mid = low + (high - low) / 2;
        if (low < high) {
            mergeSort(arr, b, low, mid);
            mergeSort(arr, b, mid + 1, high);
            merge(arr, b, low, mid, high);
        }
        for (int num : b) {
            System.out.println(num + " ");
        }
    }

    private static void merge(int arr[], int[] b, int low, int mid, int high) {
        int[] temp = new int[high - low + 1];
        int i = low;
        int j = mid + 1;
        int k = 0;

        while (i <= mid && j <= high) {
            if (arr[i] <= arr[j]) {
                temp[k] = arr[i];
                ++i;
            } else {
                temp[k] = arr[j];
                ++j;
                ++numberOfInversions;
            }
            ++k;
        }
        // 接下来两个while循环是为了将剩余的（比另一边多出来的个数）放到temp数组中
        while (i <= mid)
            temp[k++] = arr[i++];

        while (j <= high)
            temp[k++] = arr[j++];
        for (int l = 0; l < temp.length; l++)
            b[low + l] = temp[l];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }
        int[] b = new int[n];
        System.out.println(getNumberOfInversions(a, b, 0, a.length));
    }
}
