import java.util.*;

public class MaximumPairwiseProduct {

	public long findProduct(int num, int[] list) {
		Queue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
		for(int n : list) {
			pq.offer(n);
		}
		int max_first = pq.poll();
		int max_second = pq.poll();
		return (long)max_first * max_second;
	}

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int[] list = new int[num];
		for(int i = 0; i < num; ++ i) {
			list[i] = sc.nextInt();
		}

		MaximumPairwiseProduct m = new MaximumPairwiseProduct();
		System.out.println(m.findProduct(num, list));
	}
}