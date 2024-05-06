import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        int idx1 = 0;
        int idx2 = 10;
        int flag = 0;
        int totalCnt = 10;

        while (idx1 <= discount.length - 10) {
            String[] checkItem = Arrays.copyOfRange(discount, idx1, idx2);
            Arrays.sort(checkItem);
            int[] checkCnt = Arrays.copyOfRange(number, 0, 10);
            List<String> wantList = new ArrayList<String>(Arrays.asList(want));

            for (int i = 0; i < 10; i++) {
                if (!wantList.contains(checkItem[i])) {
                    break;
                } else {
                    int pos = wantList.indexOf(checkItem[i]);
                    checkCnt[pos]--;
                    totalCnt--;
                    if (checkCnt[pos] < 0) {
                        flag = 1;
                        break;
                    }
                }
            }
            if (flag == 0 && totalCnt == 0) {
                answer++;
            }
            idx1++;
            idx2++;
            flag = 0;
            totalCnt = 10;
        }
        return answer;
    }
}