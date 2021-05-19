import java.util.*;
import java.io.*;

public class CarFueling {
    static int computeMinRefills(int dist, int tank, int[] stops) {
        // Build a new array to indicate the whole road
        int len = stops.length;
        int[] road = new int[len + 2];
        road[0] = 0;
        for (int i = 1; i < len + 1; ++i) {
            road[i] = stops[i - 1];
        }
        road[len + 1] = dist;

        int i = 0;
        int currentLoc = road[0];
        int refuel = 0;

        while (i < road.length) {
            if (road[i] - currentLoc <= tank) {
                ++i;
            } else {
                currentLoc = road[i - 1];
                if (road[i] - currentLoc <= tank) {
                    ++refuel;
                } else {
                    return -1;
                }
            }
        }
        return refuel;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int dist = scanner.nextInt();
        int tank = scanner.nextInt();
        int n = scanner.nextInt();
        int stops[] = new int[n];
        for (int i = 0; i < n; i++) {
            stops[i] = scanner.nextInt();
        }

        System.out.println(computeMinRefills(dist, tank, stops));
    }
}
