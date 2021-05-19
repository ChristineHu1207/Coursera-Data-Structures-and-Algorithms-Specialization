import java.util.*;
import java.io.*;

public class MajorityElement {

    private static int getMajorityElement(int[] a, int left, int right) {
        int majorElement = getMajorityElementHelper(a, left, right);
        int count = count(a, majorElement, left, right);
        return (a.length / 2) < count ? 1 : 0;
    }

    private static int getMajorityElementHelper(int[] a, int left, int right) {

        // write your code here
        if (left == right) {
            return a[left];
        }
        int mid = left + (right - left) / 2;
        int leftMajor = getMajorityElementHelper(a, left, mid);
        int rightMajor = getMajorityElementHelper(a, mid + 1, right);
        if (leftMajor == rightMajor)
            return leftMajor;
        int leftCount = count(a, leftMajor, left, right);
        int rightCount = count(a, rightMajor, left, right);

        return leftCount > rightCount ? leftMajor : rightMajor;
    }

    private static int count(int[] a, int num, int left, int right) {
        int count = 0;
        for (int i = left; i <= right; ++i) {
            if (a[i] == num)
                count++;
        }
        return count;
    }

    public static void main(String[] args) {
        FastScanner scanner = new FastScanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }
        System.out.println(getMajorityElement(a, 0, a.length - 1));
    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream) {
            try {
                br = new BufferedReader(new InputStreamReader(stream));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}
