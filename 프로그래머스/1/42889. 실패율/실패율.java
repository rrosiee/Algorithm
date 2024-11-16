import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        // 스테이지별 도전자수 구하기
        int[] challengers = new int[N+2];
        for (int i=0; i < stages.length; i++) {
            challengers[stages[i]] ++;
        }
        
        // 스테이지별 실패율 구하기 -> HashMap에 저장
        double total = stages.length;
        HashMap<Integer, Double> fails = new HashMap<>();
        for (int i=1; i < challengers.length - 1; i++) {
            if (challengers[i] == 0) {
                fails.put(i, 0.);
            } else {
                fails.put(i, challengers[i] / total);
                total -= challengers[i];
            }
        }
        
        // 실패율이 높은 순서대로, idx를 정렬
        return fails.entrySet().stream().sorted((o1, o2) -> Double.compare(o2.getValue(), o1.getValue())).mapToInt(HashMap.Entry::getKey).toArray();
        
    }
}