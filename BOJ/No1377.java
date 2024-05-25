import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No1377 {
	public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(reader.readLine());
		int max = 0;

		Nums[] A = new  Nums[N];
		for (int i = 0; i < N; i++) {
			A[i] = new Nums();
			A[i].index = i;
			A[i].value = Integer.parseInt(reader.readLine());
		}
 
		Arrays.sort(A);

		for (int i = 0; i < N; i++) {
			int dist = A[i].index - i;
			if (dist > max) {
				max = dist;
			}
		}
		System.out.println(max + 1);
	}
}

class Nums implements Comparable<Nums>{
	int value;
	int index;

	@Override
	public int compareTo(Nums n) {
			return this.value - n.value;
	}
}