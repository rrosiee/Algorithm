import java.util.*;

class Solution {
    public int solution(String s) {
        // 1. 문자열을 스택에 넣는다.
        // 2. stack.peek()가 같다면 Pop한다.
        char[] charArray = s.toCharArray();
        Stack<Character> stack = new Stack<>();
        
        for (char c : charArray) {
            if (!stack.isEmpty()) {
                if (stack.peek() == c) {
                    stack.pop();
                    continue;
                }
            }
            
            stack.push(c);
        }
        
        int answer;
        if (stack.isEmpty()) {
            answer = 1;
        } else {
            answer = 0;
        }
        return answer;
    }
}