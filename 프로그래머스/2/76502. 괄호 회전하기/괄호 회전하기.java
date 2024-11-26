import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        Stack<Character> stack = new Stack<>();
        for (int i=0; i < s.length(); i++) {
            char[] charArray = (s.substring(i) + s.substring(0, i)).toCharArray();
            boolean isCorrect = true;
            stack.clear();
            for (char c : charArray) {
                if (c == '{' || c == '[' || c == '(') {
                    stack.push(c);
                    continue;
                }
                
                if (!stack.isEmpty()) {
                    if (
                        (stack.peek() == '{' && c == '}') ||
                        (stack.peek() == '[' && c == ']') || 
                        (stack.peek() == '(' && c == ')')) {
                        stack.pop();
                        continue;
                    }
                } else {
                    stack.push(c);    
                }
            }
            
            if (stack.isEmpty()) {
                answer ++;
            } 
        }
        
        
        return answer;
    }
}