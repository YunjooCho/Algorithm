import java.util.*;

public class Main {
	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);

		int n = scan.nextInt();
		int[] arr = new int[n];
		int sum = 0;
		int result = 0;

		for (int i = 0; i < n; i++) {
			arr[i] = scan.nextInt();
		}
		Arrays.sort(arr);

		for (int i = 0; i < n; i++) {
			sum += arr[i];
			result += sum;
		}

		System.out.println(result);
		scan.close();
	}
}
