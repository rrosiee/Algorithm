// want 는 10 이하
// discount 10만 이하



import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        // 1. want를 가진 hashMap을 만든다.
        HashMap<String, Integer> wantHashMap = new HashMap<>();
        for (int i=0; i < want.length; i++) {
            wantHashMap.put(want[i], number[i]);
        }
        
        // 2. 1째 날부터 10일간의 hashMap을 만든다.
        int okDayCount = 0;
        boolean isSame;
        HashMap<String, Integer> discountHashMap = new HashMap<>();
        for (int i=0; i<=(discount.length - 10); i++){
            discountHashMap.clear();
            for (int k=i; k < i + 10; k++) {
                discountHashMap.put(discount[k], discountHashMap.getOrDefault(discount[k], 0) + 1);
            }
            // 3. hashMap의 모든 원소가 같다면 +1
            isSame = true;
            for (String key: wantHashMap.keySet()) {
                if (wantHashMap.get(key) != discountHashMap.getOrDefault(key, 0)) {
                    isSame = false;
                    break;
                }
            }
            if(isSame) {
                okDayCount += 1;
            } 
            
        }
        
        // 4. 가능한 날짜 return
        return okDayCount;
    }
}