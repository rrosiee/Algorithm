// 관리자창

// "Enter uid1234 Muzi" -> "Muzi님이 들어왔습니다."
// "Leave uid1234" -> "Muzi님이 나갔습니다."

import java.util.*;


class Solution {
    public String[] solution(String[] record) {
        
        // 1. {uid : 닉네임} 으로 구성된 hashMap 만들기
        HashMap<String, String> nicknameHashMap = new HashMap<>();
        for (String r:record) {
            String[] splitedRecord = r.split(" ");
            if (splitedRecord[0].equals("Enter") | splitedRecord[0].equals("Change")) {
                nicknameHashMap.put(splitedRecord[1], splitedRecord[2]);    
            }
        }
        
        // 2. result 배열 만들기
        ArrayList<String> result = new ArrayList<>();
        for (String r:record) {
            String[] splitedRecord = r.split(" ");
            if (splitedRecord[0].equals("Enter")) {
                result.add(nicknameHashMap.get(splitedRecord[1]) + "님이 들어왔습니다.");
            } else if (splitedRecord[0].equals("Leave")) {
                result.add(nicknameHashMap.get(splitedRecord[1]) + "님이 나갔습니다.");
            }
        }
        
        return result.toArray(new String[0]);
    }
}