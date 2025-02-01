import java.util.*;

class Solution {
    
    private static HashMap<Integer, HashMap<String, Integer>> courseMap;
    
    public String[] solution(String[] orders, int[] course) {
        
        courseMap = new HashMap<>();
        for (int i : course) {
            courseMap.put(i, new HashMap<>());
        }
        
        // 1. 코스를 배열로 만들고 오름차순 정렬해서 가능한 모든 메뉴 구성을 구함
        for (String order: orders) {
            char[] orderArray = order.toCharArray();
            Arrays.sort(orderArray);
            combinations(0, orderArray, "");
        }
        
        
        ArrayList<String> answer = new ArrayList<>();
        // 2. 모든 코스 후보에 대해서
        for (HashMap<String, Integer> count: courseMap.values()) {
            count.values()
                .stream()
                .max(Comparator.comparingInt(o -> o))
                .ifPresent(cnt -> count.entrySet().stream()
                          .filter(entry -> cnt.equals(entry.getValue()) && cnt > 1)
                           .forEach(entry -> answer.add(entry.getKey()))
                          );
        }
        
        Collections.sort(answer);
        return answer.toArray(new String[0]);
    }
    
    
    
    public static void combinations(int idx, char[] order, String result) {
        if (courseMap.containsKey(result.length())) {
            HashMap<String, Integer> map = courseMap.get(result.length());
            map.put(result, map.getOrDefault(result, 0) + 1);
        }    
        
        for (int i=idx; i<order.length; i++) {
            combinations(i + 1, order, result + order[i]);
        }
    }
}