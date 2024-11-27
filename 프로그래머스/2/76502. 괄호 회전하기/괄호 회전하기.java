import java.util.*;

class Solution {
    public int solution(String s) {
        int result = 0;        
        Stack<Character> stack = new Stack<>();
        
        for (int i=0; i < s.length(); i++) {
            String rotatedString = s.substring(i) + s.substring(0, i);
            char[] charArray = rotatedString.toCharArray();
            stack.clear();
        
            for (char c : charArray) {
                
                // 여는 괄호면 stack에 넣기
                if (c == '{' || c == '[' || c == '(') {
                    stack.push(c);
                    continue;
                }
                
                // 닫는 괄호면 짝이 맞는지 확인하기
                if (!stack.isEmpty()) {
                    if (
                        (stack.peek() == '{' && c == '}') ||
                        (stack.peek() == '[' && c == ']') ||
                        (stack.peek() == '(' && c == ')')
                    ) {
                        stack.pop();
                        continue;
                    }
                }
                
                // 짝이 안맞는다면 False
                stack.push(c);
            }
            if (stack.isEmpty()) {
                result++;
            }
        }
        return result;
    }
}