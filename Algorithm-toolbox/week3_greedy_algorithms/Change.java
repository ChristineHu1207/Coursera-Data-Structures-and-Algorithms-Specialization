import java.util.Scanner;

public class Change {
    private static int getChange(int m) {
        // write your code here
        // corner case
        if (m < 1)
            return 0;

        int[] change = { 10, 5, 1 };
        int counter = 0;
        for (int i = 0; i < 3; ++i) {
            while (m - change[i] >= 0) {
                m -= change[i];
                ++counter;
            }
        }

        return counter;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        System.out.println(getChange(m));
    }
}
