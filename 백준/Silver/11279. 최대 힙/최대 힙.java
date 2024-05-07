import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan  = new Scanner(System.in);
		PriorityQueue<Integer> priorityQue = new PriorityQueue<Integer>(Collections.reverseOrder());

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