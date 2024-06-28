import java.util.Arrays;
import java.util.Collections;

public class Solution {
    public long solution(long n) {
        // 정수를 문자열로 변환
        String str = Long.toString(n);
        
        // 문자열을 문자 배열로 변환
        Character[] chars = new Character[str.length()];
        for (int i = 0; i < str.length(); i++) {
            chars[i] = str.charAt(i);
        }
        
        // 문자 배열을 내림차순으로 정렬
        Arrays.sort(chars, Collections.reverseOrder());
        
        // 정렬된 문자 배열을 다시 문자열로 변환
        StringBuilder sb = new StringBuilder();
        for (char c : chars) {
            sb.append(c);
        }
        
        // 문자열을 정수로 변환하여 반환
        return Long.parseLong(sb.toString());
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(118372));  // 873211
    }
}
