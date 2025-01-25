// 카드 뭉치 2개(1번 카드 뭉치 -> 2번 카드 뭉치) -> 단어 배열을 만들 것이다.
import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        // Set Cards1 Deque
        ArrayDeque<String> cards1Deque = new ArrayDeque<>();
        for (String card1 : cards1) {
            cards1Deque.addLast(card1);
        }
        
        // Set Cards2 Deque
        ArrayDeque<String> cards2Deque = new ArrayDeque<>();
        for (String card2 : cards2) {
            cards2Deque.addLast(card2);
        }
        
        String card1Word;
        String card2Word;
        
        // 1. goal의 배열을 순회
        for (String g:goal) {    
            // 2. cards1과 일치하는지 확인, cards2와 일치하는지 확인
            card1Word = cards1Deque.isEmpty() ? null : cards1Deque.pollFirst();
            card2Word = cards2Deque.isEmpty() ? null : cards2Deque.pollFirst();
            
            // 3. cards1과 일치한다면 cards2에 다시 push 하기
            if (g.equals(card1Word)) {
                if (card2Word != null) {
                    cards2Deque.addFirst(card2Word);
                }
            } 
            // 4. cards2와 일치한다면, card1에 다시 push 하기    
            else if (g.equals(card2Word)) {
                if (card1Word != null) {
                    cards1Deque.addFirst(card1Word);
                }
            } 
            // 5. card1, card2의 첫 번째 원소와 일치하지 않는다면 No 반환    
            else {
                System.out.println("g: [" + g + "]");
                System.out.println("card1Word: [" + card1Word + "]");
                System.out.println("card2Word: [" + card2Word + "]");

                return "No";
            }
        }
        
        // 6. 배열을 모두 성공적으로 마쳤다면 Yes 반환
        return "Yes";
    }
}