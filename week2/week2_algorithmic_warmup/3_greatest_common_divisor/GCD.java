import java.util.*;

public class GCD {
  private static int gcd_naive(int a, int b) {
    if (a == b)
      return a;

    int big = a > b ? a : b;
    int small = a < b ? a : b;

    while (small != 0) {
      int tem_big = big;
      big = small;
      small = tem_big % small;
      if (small == 1)
        return small;
    }

    return big;
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();

    System.out.println(gcd_naive(a, b));
  }
}
