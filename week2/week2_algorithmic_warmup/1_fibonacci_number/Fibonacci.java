import java.util.Scanner;

public class Fibonacci {
  private static long calc_fib(int n) {
    if (n == 0)
      return 0;
    if (n <= 2)
      return 1;
    long[] res = new long[n];
    res[0] = 1;
    res[1] = 1;
    for (int i = 2; i < n; ++i) {
      res[i] = res[i - 1] + res[i - 2];
    }
    return res[n - 1];
  }

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    System.out.println(calc_fib(n));
  }
}
