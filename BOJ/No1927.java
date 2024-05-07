import java.util.Scanner;
import java.util.PriorityQueue;

public class No1927 {
	public static void main(String[] args) {
		Scanner scan  = new Scanner(System.in);
		PriorityQueue<Integer> priorityQue = new PriorityQueue<Integer>();

		int n = scan.nextInt();
		for (int i = 0; i < n; i++) {
			int elem = scan.nextInt();
			if (elem == 0) {
				if (priorityQue.isEmpty()) {
					System.out.println("0");
				} else {
					System.out.println(priorityQue.poll());
				}
			} else {
				priorityQue.offer(elem);
			}
		}

		scan.close();
	}
}