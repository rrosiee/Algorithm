// 1. move에 따라 board에 원소가 있는지 확인
// 2. board에 원소가 있으면 0으로, 아니면 다음 move로
// 2-1. board에 원소가 있는 경우 -> stack에 push하기 전 맨 위의 원소와 같다면 맨 위의 원소를 Pop하기
// 만약 pop했다면 result + 1

import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        
        int boardLength = board.length;
        int result = 0;
        Stack<Integer> stack = new Stack<>();
        
        for (int move : moves) {
            for (int i=0; i< board.length; i++) {
                int toy = board[i][move-1];
                if (toy == 0) {
                    // 인형이 없다면 다음 인형으로
                    continue;
                } 
                
                board[i][move-1] = 0;
                if (!stack.isEmpty() && stack.peek() == toy) {
                    // 같은 인형일 경우
                    stack.pop();
                    result += 2;
                } else {
                    // 다른 인형일 경우
                    stack.push(toy);
                }
                break;
            }    
        }
        return result;
    }
}