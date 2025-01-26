// 완주하지 못한 선수의 이름을 return
// 동명이인이 있을 수 있음

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // 1. {이름: 참여수} 구조의 HashMap만들기
        HashMap<String, Integer> hashMap = new HashMap<>();
        for (String p: participant) {
            if (hashMap.containsKey(p)) {
                hashMap.put(p, hashMap.get(p) + 1);
            } else {
                hashMap.put(p, 1);
            }
        }
        
        // 2. completion을 순회하며 해당 이름의 참여수를 -1하기
        for (String c: completion) {
            hashMap.put(c, hashMap.get(c) -1);
        }
        
        // 3. HashMap의 참여수가 1보다 큰 값이 있으면 return
        for (String key : hashMap.keySet()) {
            if (hashMap.get(key) == 1) {
                return key;
            }
        }
        return null;
    }
}