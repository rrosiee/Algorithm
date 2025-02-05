// N-1 <-> N끼리 차례대로 배정받는다.
// 각 게임에서 이긴 사람은 다시 번호를 부여받는데 1~ N/2 번까지 부여받는다..
// 3~ 4번이 이겼으면 다음 라운드에서는 3번은 2번이 됨.
// A 번과 B번은 몇 번째 라운드에서 만날까?


class Solution {
    public int solution(int n, int a, int b) {
        int answer;
        
        for (answer = 0; a!=b; answer ++) {
            a = (a + 1) / 2;
            b = (b + 1) / 2;
        } // answer 1, a = 2, b = 4 / answer 2, a = 1, b = 2 / answer 3, a = 1, b = 1
        
        return answer;
    }
}