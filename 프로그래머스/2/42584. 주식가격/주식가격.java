class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        // 우선 답 모르겠으니까 for문으로 풀어보기.
        for (int i=0; i < prices.length; i++) {
            for (int j=i+1; j < prices.length; j++) {
                answer[i]++;
                if (prices[i] > prices[j]) {
                    break;
                }
            }
        }
        return answer;
    }
}