import java.util.*;

public class Main {
	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		int idx = 1;
		int cnt = scan.nextInt();
		int dis = 0;

		for (int i = 0; i < cnt; i++) {
			int num = Integer.parseInt(scan.next());
			List<Integer> numList = new ArrayList<Integer>();
			for (int j = 0; j < num; j++) {
				int elem = Integer.parseInt(scan.next());
				numList.add(elem);
			}
			Collections.sort(numList);
			for (int j = 0; j < num - 1; j++) {
				int cal = numList.get(j + 1) - numList.get(j);
				if (numList.get(j + 1) - numList.get(j) > dis) {
					dis = cal;
				}
			}
			System.out.println("Class " + idx);
			int maxNum = numList.get(numList.size() - 1);
			int minNum = numList.get(0);
			System.out.println("Max " + maxNum + ", Min " + minNum + ", Largest gap " + dis);
			
			idx++;
			dis = 0;
		}
		scan.close();
	}
}