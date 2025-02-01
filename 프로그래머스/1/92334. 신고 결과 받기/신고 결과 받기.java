// 각 유저는 한 번에 한 명의 유저를 신고할 수 있다. -> 한 유저를 여러 번 신고하면 1번으로 처리
// k번 이상 신고된 유저는 게시판 이용이 정지, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
// id_list : 전체 유저의 목록(1000)
// report : report 목록(200000)
// k : 정지 기준 number
// return : 각 유저별로 메일을 받은 횟수

import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] reports, int k) {
        // 1. reports를 순회하며 reportedUserHashMap에 당한사람: {한 사람} 으로 저장한다. O(N)
        HashMap<String, HashSet<String>> reportedUserHashMap = new HashMap<>();
        for (String report : reports) {
            String[] splitedReport = report.split(" ");
            String reportedUser = splitedReport[1];
            String reportUser = splitedReport[0];
            if (reportedUserHashMap.getOrDefault(reportedUser, null) == null) {
                HashSet<String> reportUserHashSet = new HashSet<>();
                reportUserHashSet.add(reportUser);
                reportedUserHashMap.put(reportedUser, reportUserHashSet);
            } else {
                reportedUserHashMap.get(reportedUser).add(reportUser);
            }
        }
        
        // 2. reportedUserHashMap을 모두 순회하며, 신고 한 사람의 수가 k개가 넘으면 mailedUserCountHashMap 에 count+1
        HashMap<String, Integer> mailedUserCountHashMap = new HashMap<>();
        for (String reportedUser: reportedUserHashMap.keySet()) {
            if (reportedUserHashMap.get(reportedUser).size() >= k) {
                for (String reportUser : reportedUserHashMap.get(reportedUser)) {
                    mailedUserCountHashMap.put(reportUser, mailedUserCountHashMap.getOrDefault(reportUser, 0) + 1);
                }
            }
        }
        
        // 3. id_list를 순회하며 결과값을 반환한다.
        int[] answer = new int[id_list.length];
        for (int i=0; i < id_list.length; i++) {
            answer[i] = mailedUserCountHashMap.getOrDefault(id_list[i], 0);
        }
        return answer;
    }
}