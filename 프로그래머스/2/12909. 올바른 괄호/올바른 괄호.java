import java.util.*;

class Solution {
    boolean solution(String s) {
        // HINT : 짝지어졌다 -> 가장 최근의 괄호 쌍이 짝지어졌다.
        // HINT : 가장 최근 -> 스택을 이용하라는 것
        
        ArrayDeque<Character> stack = new ArrayDeque<>();
        char[] sCharacters = s.toCharArray();
        
        for (char sCharacter: sCharacters) {
            if (sCharacter == '(') {
                stack.push(sCharacter);
            } else if (stack.isEmpty() || stack.pop() == sCharacter) {
                return false;
            }
            
        }
        return stack.isEmpty();
    }
}