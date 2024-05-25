import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class No2161 {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int flag = 1;

		Deque<Integer> deq = new ArrayDeque<Integer>();
		for (int i = 1; i <= n; i++) {
			deq.addLast(i);
		}

		while (deq.size() >= 0) {
			if (deq.size() == 0) {
				break;
			}
			if (flag % 2  == 0) {
				int val = deq.removeFirst();
				deq.addLast(val);
			} else {
				int val = deq.removeFirst();
				System.out.println(val);
			}
			flag++;
		}
		sc.close();
}
}
