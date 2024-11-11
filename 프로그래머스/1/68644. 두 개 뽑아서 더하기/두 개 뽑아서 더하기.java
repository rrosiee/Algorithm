import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        // 1. 두 개의 수를 뽑아 더할 수 있는 모든 수 구하기 -> 시간복잡도 O(N^2) -> 3000개 데이터까지 가능하다.
        Set<Integer> numsSet = new HashSet<Integer>();
        for (int i = 0; i - 1 < numbers.length; i++) {
            for (int k = i + 1; k < numbers.length; k++) {
                numsSet.add(numbers[i] + numbers[k]);
            }
        }
        
        
        // 2. 배열에 오름차순으로 담아 return
        int[] answer = numsSet.stream().sorted().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}