import java.util.*;

class Solution {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        
        // 1. 판매원의 부모를 매핑하는 HashMap을 만든다.
        HashMap<String, String> parents = new HashMap<>();
        HashMap<String, Integer> points = new HashMap<>();

        for (int i = 0; i < enroll.length; i++) { // O(2N)
            parents.put(enroll[i], referral[i]);
            points.put(enroll[i], 0);
        }
        
        // 2. seller를 순회한다.
        for (int i = 0; i < seller.length; i++) { // O(2N) : 최대 10만개
            String name = seller[i];
            int point = amount[i] * 100;
            // 2-1. 만약 부모가 "-"이라면 다음 seller로 넘어간다.
            while (!name.equals("-") && point != 0) { // O(N)
                // 2-2. seller의 name에 해당하는 부모를 찾고, point를 추가한다.
                points.put(name, points.get(name) + point - (point / 10));
                point = point/10;
                name = parents.get(name);
            }
        }
        
        // 3. enroll의 순서에 맞게 point와 비교하면서 result를 반환한다.
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i=0; i < enroll.length; i++) {
            answer.add(points.get(enroll[i]));
        }
        return answer.stream().mapToInt(Integer::intValue).toArray(); // O(N)
    }
}