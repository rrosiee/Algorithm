import java.util.*;

class Solution {
    public String solution(int n, int k, String[] cmd) {
        
        // 1. 삭제된 행의 인덱스를 저장하는 스택
        Stack<Integer> deleted = new Stack<>();
        
        // 2. 각 행을 기준으로 연산에 따른 위치를 표시하기 위한 배열
        int[] up = new int[n+2];
        int[] down = new int[n+2];
        
        for (int i=0; i < n+2; i++) {
            up[i] = i-1;
            down[i] = i+1;
        } 
        
        // 3. 현재 위치를 나타내는 인덱스
        k++;
        
        // 4. 주어진 명령어 배열을 하나씩 처리
        for (String c: cmd) {
            // 5. 현재 위치를 삭제하고 그 다음 위치로 이동
            if (c.startsWith("C")) {
                deleted.push(k);
                up[down[k]] = up[k];
                down[up[k]] = down[k];
                k = n < down[k] ? up[k] : down[k];
            } 
            // 6. 가장 최근에 삭제된 행을 복원
            else if (c.startsWith("Z")) {
                int restore = deleted.pop();
                up[down[restore]] = restore;
                down[up[restore]] = restore;
            }
            // 7. U또는 D일 경우
            else {
                String[] s = c.split(" ");
                int x = Integer.parseInt(s[1]);
                
                for (int i=0; i < x; i ++) {
                    k = s[0].equals("U") ? up[k] : down[k];
                }
            }
        }
        
        // 8. 삭제된 행의 위치에 X를, 그렇지 않으면 O를
        char[] answer = new char[n];
        Arrays.fill(answer, 'O');
        
        for (int i: deleted) {
            answer[i - 1] = 'X';
        }
        
        return new String(answer);
    }
}