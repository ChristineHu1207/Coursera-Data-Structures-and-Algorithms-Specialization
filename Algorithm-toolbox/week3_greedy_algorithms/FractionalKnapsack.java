import java.text.DecimalFormat;
import java.util.*;

public class FractionalKnapsack {
    private static double getOptimalValue(int capacity, int[] values, int[] weights) {
        // corner case
        if (capacity <= 0)
            return 0;

        int len = values.length;
        double[][] valuePerWeight = new double[len][2];
        for (int i = 0; i < len; ++i) {
            valuePerWeight[i][0] = (double) values[i] / weights[i];
            valuePerWeight[i][1] = (double) weights[i];
        }
        Arrays.sort(valuePerWeight, new Comparator<double[]>() {
            public int compare(double[] a, double[] b) {
                return Double.compare(b[0], a[0]);
            }
        });

        double value = 0;
        int currentWeight = 0;
        // write your code here
        int i = 0;
        while (currentWeight < capacity && i < len) {
            int currentCapacity = capacity - currentWeight;
            if (currentCapacity >= valuePerWeight[i][1]) {
                value += valuePerWeight[i][0] * valuePerWeight[i][1];
                currentWeight += valuePerWeight[i][1];
            } else {
                value += valuePerWeight[i][0] * currentCapacity;
                currentWeight += currentCapacity;
            }
            ++i;
        }

        return value;
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int capacity = scanner.nextInt();
        int[] values = new int[n];
        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
            weights[i] = scanner.nextInt();
        }
        double result = getOptimalValue(capacity, values, weights);
        System.out.println(String.format("%.4f", result));
        scanner.close();
    }
}
