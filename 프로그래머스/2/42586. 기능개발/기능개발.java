// 앞에 있는 기능이 닫 끝나야 뒤에 있는 기능이 배포될 수 있음
// progresses : 현재 작업의 진도
// speeds : 작업의 속도(하루에 할 수 있는)
// 각 배포(배포는 하루에 한 번)마다 몇 개의 시능이 배포되는가
import java.util.*;


class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // 1. 각 기능별 걸리는 일수를 계산한다.
        int functionCount = progresses.length;
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        for (int i=0; i < functionCount; i++) {
            int leftProgressDay = 100 - progresses[i];
            int totalProgressDays = leftProgressDay % speeds[i] == 0 ? leftProgressDay / speeds[i] : (leftProgressDay / speeds[i]) + 1;
            deque.addLast(totalProgressDays);
        }
        
        // 2. 가장 처음을 pop하고, 그 이후가 만약 처음보다 적다면 pop 하면서 function 을 ++한다.
        ArrayList<Integer> array = new ArrayList<>();
        int first;
        int deployCount;
        while (!deque.isEmpty()) {
            // 가장 처음을 꺼낸다.
            first = deque.pollFirst();
            deployCount = 1;
            
            while (!deque.isEmpty()) {
                int nextFirst = deque.pollFirst();
                if (first >= nextFirst) {
                    deployCount++;
                } else {
                    deque.addFirst(nextFirst);
                    break;
                }
            }
            
            array.add(deployCount);
        }
        
        return array.stream().mapToInt(Integer::intValue).toArray();
    }
}