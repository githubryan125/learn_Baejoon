class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;

        for (int i = 1; i <= number; i++) {
            int cnt = 0;
            
            // 약수 계산
            for (int j = 1; j * j <= i; j++) {
                if (i % j == 0) {
                    cnt++; // 작은 약수
                    if (j * j != i) {
                        cnt++; // 큰 약수 (중복 제외)
                    }
                }
            }

            // limit 초과 시 power 추가
            if (cnt > limit) {
                answer += power;
            } else {
                answer += cnt;
            }
        }

        return answer;
    }
}
