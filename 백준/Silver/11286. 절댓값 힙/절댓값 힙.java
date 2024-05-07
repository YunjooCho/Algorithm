import java.util.PriorityQueue;
import java.util.Scanner;

class InputValues implements Comparable<InputValues> {
	int inputVal;
	int absVal;

	InputValues(int intputVal, int absVal) {
		this.inputVal = intputVal;
		this.absVal = absVal;
	}

	@Override
	public int compareTo(InputValues value) {
		if (this.absVal > value.absVal)
		{
			return 1;
		} else if (this.absVal == value.absVal) {
			if (this.inputVal > value.inputVal) {
				return 1;
			}
		}
		return -1;
	}
}

public class Main {

	public static void main(String[] args) {
		Scanner scan  = new Scanner(System.in);
		PriorityQueue<InputValues> priorityQue = new PriorityQueue<InputValues>();

		int n = scan.nextInt();
		for (int i = 0; i < n; i++) {
			int elem = scan.nextInt();
			if (elem == 0) {
				if (priorityQue.isEmpty()) {
					System.out.println("0");
				} else {
					System.out.println(priorityQue.poll().inputVal);
				}
			} else {
				int tmp = elem;
				if (elem < 0) {
					tmp *= -1;
				}
				priorityQue.offer(new InputValues(elem, tmp));
			}
		}
		scan.close();
	}
}
