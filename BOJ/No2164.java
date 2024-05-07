import java.util.*;

public class No2164 {
	public static void main(String[] args) {

			Scanner sc = new Scanner(System.in);
			int n = sc.nextInt();
			int flag = 1;

			Deque<Integer> deq = new ArrayDeque<Integer>();
			for (int i = 1; i <= n; i++) {
				deq.addLast(i);
			}

			while (deq.size() >= 1) {
				if (deq.size() == 1) {
					System.out.println(deq.getFirst());
					break;
				}
				if (flag % 2  == 0) {
					int val = deq.removeFirst();
					deq.addLast(val);
				} else {
					deq.removeFirst();
				}
				flag++;
			}
			sc.close();
	}
}

